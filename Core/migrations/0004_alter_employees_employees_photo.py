# Generated by Django 4.1.5 on 2023-05-23 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_alter_employees_employees_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='employees_photo',
            field=models.ImageField(default='media/employees_photo/user.png', upload_to='employees_photo'),
        ),
    ]
