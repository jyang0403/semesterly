# Generated by Django 3.2.7 on 2021-12-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0034_auto_20210920_1851"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="jhed",
            field=models.CharField(default="", max_length=255, null=True),
        ),
    ]
