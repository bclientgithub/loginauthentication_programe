# Generated by Django 4.0.6 on 2022-09-30 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('fname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('mob', models.BigIntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]