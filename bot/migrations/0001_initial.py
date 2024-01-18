# Generated by Django 4.2.5 on 2023-09-15 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('ism', models.CharField(max_length=1278, null=True)),
                ('familiya', models.CharField(max_length=1278, null=True)),
                ('username', models.CharField(max_length=56, null=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('lang', models.CharField(default='uz', max_length=2)),
                ('log', models.JSONField(default={'state': 0})),
            ],
        ),
    ]
