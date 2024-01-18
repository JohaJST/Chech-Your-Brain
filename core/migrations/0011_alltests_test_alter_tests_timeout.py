# Generated by Django 4.2.5 on 2023-10-17 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_tests_timeout'),
    ]

    operations = [
        migrations.AddField(
            model_name='alltests',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tests'),
        ),
        migrations.AlterField(
            model_name='tests',
            name='timeout',
            field=models.IntegerField(default=40, verbose_name='Testlarni ishlashga beriladigan vaqt'),
        ),
    ]
