# Generated by Django 5.0 on 2024-04-11 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='englishBody',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='englishTitle',
        ),
        migrations.AddField(
            model_name='post',
            name='arabicBody',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='arabicTitle',
            field=models.CharField(default='no', max_length=500),
            preserve_default=False,
        ),
    ]
