# Generated by Django 3.1.5 on 2021-04-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smoking', '0002_auto_20210416_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borough',
            name='boroughcode',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='자치구 코드'),
        ),
        migrations.AlterField(
            model_name='fine',
            name='finecode',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='과태료 코드'),
        ),
        migrations.AlterField(
            model_name='smokingareatype',
            name='typecode',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='유형 코드'),
        ),
    ]
