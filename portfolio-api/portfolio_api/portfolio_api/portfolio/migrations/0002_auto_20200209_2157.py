# Generated by Django 3.0.3 on 2020-02-09 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=10000)),
                ('logo', models.CharField(max_length=1000)),
                ('inserted_at', models.DateTimeField(auto_now_add=True)),
                ('used_on_this_page', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
