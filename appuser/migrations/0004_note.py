# Generated by Django 2.0.1 on 2018-03-30 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appuser', '0003_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.FileField(upload_to='./files')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appuser.User')),
            ],
            options={
                'db_table': 'note',
                'ordering': ['nid'],
            },
        ),
    ]
