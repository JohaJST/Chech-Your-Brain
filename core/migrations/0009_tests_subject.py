# Generated by Django 4.2.5 on 2023-10-15 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='tests',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.subject'),
        ),
    ]
