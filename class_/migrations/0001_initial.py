# Generated by Django 2.2.4 on 2019-10-20 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('section', models.CharField(blank=True, max_length=3, null=True)),
                ('subject', models.CharField(blank=True, max_length=5, null=True)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teacher.Teacher')),
            ],
        ),
    ]
