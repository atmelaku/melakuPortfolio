# Generated by Django 4.2 on 2023-09-19 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(default='default', upload_to='media/images'),
        ),
    ]
