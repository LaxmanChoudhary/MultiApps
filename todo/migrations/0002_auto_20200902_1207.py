# Generated by Django 3.1 on 2020-09-02 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['created_on', 'title']},
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]