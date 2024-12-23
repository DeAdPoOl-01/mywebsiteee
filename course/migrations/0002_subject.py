# Generated by Django 5.1.4 on 2024-12-20 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subject_tutor', models.CharField(max_length=250)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
                ('price', models.CharField(max_length=150)),
                ('detail', models.CharField(max_length=300)),
                ('slug', models.SlugField(unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
    ]