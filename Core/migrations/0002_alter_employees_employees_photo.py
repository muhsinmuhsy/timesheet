# Generated by Django 4.1.5 on 2023-05-23 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='employees_photo',
            field=models.ImageField(default='static/img/profile/user.png', upload_to='employees_photo'),
        ),
    ]