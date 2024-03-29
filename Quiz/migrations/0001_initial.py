# Generated by Django 4.1.7 on 2023-03-14 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_statement', models.TextField()),
                ('optionA', models.CharField(max_length=250)),
                ('optionB', models.CharField(max_length=250)),
                ('optionC', models.CharField(max_length=250)),
                ('optionD', models.CharField(max_length=250)),
                ('correct_ans', models.CharField(choices=[('a', 'optionA'), ('b', 'optionB'), ('c', 'optionC'), ('d', 'optionD')], max_length=20)),
            ],
        ),
    ]
