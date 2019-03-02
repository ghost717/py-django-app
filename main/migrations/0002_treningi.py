# Generated by Django 2.1.5 on 2019-03-02 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treningi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('ex01', models.CharField(max_length=128)),
                ('ex02', models.CharField(max_length=128)),
                ('ex03', models.CharField(max_length=128)),
                ('ex04', models.CharField(max_length=128)),
                ('ex05', models.CharField(max_length=128)),
                ('ex06', models.CharField(max_length=128)),
                ('ex07', models.CharField(max_length=128)),
                ('ex08', models.CharField(max_length=128)),
                ('ex09', models.CharField(max_length=128)),
                ('ex10', models.CharField(max_length=128)),
            ],
        ),
    ]
