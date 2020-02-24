# Generated by Django 2.2 on 2020-02-24 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0002_remove_question_qtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='question',
            name='areas',
            field=models.ManyToManyField(to='interview.Area'),
        ),
    ]
