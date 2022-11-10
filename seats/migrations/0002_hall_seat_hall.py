# Generated by Django 4.1 on 2022-08-15 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
        ('seats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_time', models.TimeField()),
                ('movie_date', models.DateField()),
                ('movie_showing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
        migrations.AddField(
            model_name='seat',
            name='hall',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seats.hall'),
        ),
    ]