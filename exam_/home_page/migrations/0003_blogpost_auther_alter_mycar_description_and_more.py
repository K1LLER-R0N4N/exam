# Generated by Django 4.2.4 on 2023-08-31 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_mycar'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='auther',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mycar',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='mycar',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]