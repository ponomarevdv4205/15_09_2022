# Generated by Django 4.1.1 on 2022-10-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_todo_project"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="todo",
            name="is_active",
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name="todo",
            name="modified",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
