# Generated by Django 3.2.4 on 2022-07-20 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoListApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtask',
            name='taskImg',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
