# Generated by Django 2.0.7 on 2019-03-02 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_book_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.CharField(default='NULL', max_length=1000),
            preserve_default=False,
        ),
    ]
