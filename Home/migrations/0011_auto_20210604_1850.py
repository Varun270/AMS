# Generated by Django 3.1.7 on 2021-06-04 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_auto_20210604_1847'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'ordering': ['-date']},
        ),
    ]