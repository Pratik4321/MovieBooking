# Generated by Django 4.1 on 2022-08-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seats', '0003_alter_hall_movie_date_alter_hall_movie_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='hall',
            name='title',
            field=models.CharField(default='enter hall name here', max_length=20),
        ),
    ]
