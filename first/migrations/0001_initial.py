# Generated by Django 2.2.9 on 2019-12-23 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.IntegerField()),
                ('first', models.IntegerField()),
                ('second', models.IntegerField()),
                ('log_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
