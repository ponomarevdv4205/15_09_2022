# Generated by Django 4.1.1 on 2022-11-04 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0009_remove_todo_project_remove_todo_user_todo_project_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="todo",
            name="project",
        ),
        migrations.AddField(
            model_name="todo",
            name="project",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.project",
            ),
        ),
    ]
