# Generated by Django 4.1.7 on 2023-05-14 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='featured',
            field=models.ImageField(blank=True, null=True, upload_to='blogs/'),
        ),
    ]
