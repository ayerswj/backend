# Generated by Django 3.0.3 on 2020-04-13 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, default='empty', max_length=200)),
                ('correct', models.CharField(default='correct', max_length=200)),
                ('incorrect', models.CharField(default='incorrect', max_length=200)),
                ('category', models.CharField(choices=[('1', 'Sports'), ('2', 'Music'), ('3', 'Movies'), ('4', 'Pop Culture')], default='Pick one', max_length=50)),
                ('type', models.CharField(choices=[('1', 'Multiple Choice'), ('2', 'True/False')], default='Pick one', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('joinable', models.BooleanField(default=True)),
                ('title', models.CharField(default='Title of Game', max_length=200)),
                ('category', models.CharField(choices=[('1', 'Sports'), ('2', 'Music'), ('3', 'Movies'), ('4', 'Pop Culture')], default='Pick one', max_length=50)),
                ('type', models.CharField(choices=[('1', 'Multiple Choice'), ('2', 'True/False')], default='Pick one', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('score', models.IntegerField(default=0)),
                ('rank', models.TextField(default='none')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]