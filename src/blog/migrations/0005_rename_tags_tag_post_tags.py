# Generated by Django 4.1.7 on 2023-05-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_tags'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='blog.tag'),
        ),
    ]