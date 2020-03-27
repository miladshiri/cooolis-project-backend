import xlrd 

from django.core.management.base import BaseCommand, CommandError

from interview.models import Area, Question, Option, Category, Questionnaire

class Command(BaseCommand):
    help = 'Add data from an excel file to the database'

    def add_arguments(self, parser):
        parser.add_argument('file_path')

    def handle(self, *args, **options):

        def add_new_category(text):
            obj, created = Category.objects.get_or_create(text=text)
            return obj

        def add_new_area(text):
            obj, created = Area.objects.get_or_create(text=text)
            return obj

        def add_new_question(question, area):
            obj, created = Question.objects.get_or_create(text=question)
            obj.areas.add(area)
            obj.save()
            return obj
            
        def add_new_option(option, is_ans, question):
            obj, created = Option.objects.get_or_create(text=option, question=question, is_answer=is_ans)
            

        def add_questions_from_sheet(sheet, area):
            for i in range(sheet.nrows):
                row = sheet.row_values(i)
                        
                question = row[0]
                answers = row[1:]
                
                if question == "":
                    continue
                question_obj = add_new_question(question, area)
                
                
                c = 0

                while(1):
                    try:
                        ans = answers[c]
                        is_ans = answers[c+1]
                    except:
                        break
                    
                    if (ans == "" or is_ans == "") or (is_ans not in [0, 1]):
                        break
                    
                    add_new_option(ans, int(is_ans), question_obj)          
                    c += 2
                
        def add_new_questionnaire(title, description, areas, max_number, category):
            category_obj, _ = Category.objects.get_or_create(text=category)
            questionnaire, _ = Questionnaire.objects.get_or_create(
                title=title, 
                description=description,
                max_number=max_number,
                category=category_obj
                )
            for area in areas:
                area_obj = Area.objects.filter(text=area).first()
                questionnaire.target_areas.add(area_obj)
            questionnaire.save()
        

        # loc = "questions.xlsx"
        wb = xlrd.open_workbook(options['file_path'])
        
        ## Add categories
        sheet = wb.sheet_by_name("categories")
        for i in range(sheet.nrows):
            category_farsi = sheet.cell_value(i, 0)
            add_new_category(category_farsi)

        ## Add areas and questions
        sheet = wb.sheet_by_name("areas")
        for i in range(sheet.nrows):
            area_farsi = sheet.cell_value(i, 0)
            area_obj = add_new_area(area_farsi)

            area_english = sheet.cell_value(i, 1)
            sheet_area = wb.sheet_by_name(area_english)
            add_questions_from_sheet(sheet_area, area_obj)

        ## Add questionnaires
        sheet = wb.sheet_by_name("questionnaire")
        for i in range(sheet.nrows):
            title = sheet.cell_value(i, 0)
            description = sheet.cell_value(i, 1)
            areas = sheet.cell_value(i, 2).split('-')
            max_number = int(sheet.cell_value(i, 3))
            category = sheet.cell_value(i, 4)
            
            add_new_questionnaire(title, description, areas, max_number, category)

