# Generated by Django 3.2.6 on 2021-09-03 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EQuest', '0007_auto_20210903_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EQuest.category'),
        ),
    ]