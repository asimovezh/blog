# Generated by Django 2.0.7 on 2018-08-25 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180825_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='blogsequence',
            field=models.DecimalField(decimal_places=2, max_digits=4, verbose_name='章节顺序'),
        ),
    ]