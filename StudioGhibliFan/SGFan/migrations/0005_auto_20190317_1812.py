# Generated by Django 2.1.7 on 2019-03-17 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SGFan', '0004_auto_20190317_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sgmovies',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
