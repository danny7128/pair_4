# Generated by Django 3.2.13 on 2022-10-28 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
