# Generated by Django 4.1 on 2022-09-01 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_article_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='update_date',
            field=models.DateTimeField(blank=True),
        ),
    ]