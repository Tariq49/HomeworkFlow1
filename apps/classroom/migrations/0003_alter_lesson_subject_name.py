# Generated by Django 5.1.1 on 2024-09-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("classroom", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lesson",
            name="subject_name",
            field=models.CharField(
                choices=[
                    ("Math", "Math"),
                    ("German", "German"),
                    ("Eng", "English"),
                    ("Bio", "Biology"),
                    ("Chem", "Chemistry"),
                    ("PE", "Physical Education"),
                    ("HST", "History"),
                    ("Art", "Art"),
                    ("Geo", "Geography"),
                    ("Phi", "Philosophy"),
                    ("Eth", "Ethics"),
                    ("Rel", "Religion"),
                    ("Spa", "Spanish"),
                    ("Fre", "French"),
                    ("Lat", "Latin"),
                ],
                max_length=30,
            ),
        ),
    ]
