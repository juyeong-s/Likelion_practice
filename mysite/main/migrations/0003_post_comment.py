# Generated by Django 3.2 on 2021-06-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
