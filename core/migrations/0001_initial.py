# Generated by Django 2.2.13 on 2021-02-25 20:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('mensaje', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Error404',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error404', models.ImageField(upload_to='error404')),
            ],
        ),
        migrations.CreateModel(
            name='My_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=150)),
                ('contenido', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('img', models.ImageField(upload_to='project')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('descripcion', models.CharField(max_length=150)),
                ('contenido', ckeditor.fields.RichTextField(verbose_name='Contenido')),
                ('img', models.ImageField(upload_to='skill')),
                ('icon', models.CharField(choices=[('icon solid major fa-lock', 'icon solid major fa-lock'), ('icon solid major fa-link', 'icon solid major fa-link'), ('icon solid major fa-cog', 'icon solid major fa-cog'), ('icon solid major fa-desktop', 'icon solid major fa-desktop'), ('icon major fa-gem', 'icon major fa-gem'), ('icon solid major fa-code', 'icon solid major fa-code')], max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Social_network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=150)),
                ('youtube', models.CharField(max_length=150)),
                ('git', models.CharField(max_length=150)),
                ('Linkedin', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encabezado', models.CharField(max_length=150)),
                ('biografia', models.CharField(max_length=3000)),
                ('contenido', ckeditor.fields.RichTextField(verbose_name='Contenido')),
            ],
        ),
    ]
