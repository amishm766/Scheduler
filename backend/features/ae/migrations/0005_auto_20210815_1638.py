# Generated by Django 3.2.5 on 2021-08-15 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ae', '0004_auto_20210815_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='execution',
            name='schedule',
        ),
        migrations.AddField(
            model_name='execution',
            name='trigger',
            field=models.ForeignKey(default=24, on_delete=django.db.models.deletion.CASCADE, to='ae.trigger'),
            preserve_default=False,
        ),
    ]
