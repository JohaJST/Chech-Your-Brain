# Generated by Django 4.2.5 on 2023-09-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='tguser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tguser',
            name='menu',
            field=models.SmallIntegerField(default=1),
        ),
    ]
