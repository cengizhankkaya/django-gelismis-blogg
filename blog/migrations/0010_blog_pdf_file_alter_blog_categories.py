# Generated by Django 4.2.1 on 2023-06-19 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_blog_category_blog_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdfs'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.category'),
        ),
    ]
