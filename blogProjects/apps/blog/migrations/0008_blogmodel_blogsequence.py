# Generated by Django 2.0.7 on 2018-08-25 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180824_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='blogsequence',
            field=models.DecimalField(decimal_places=3, default=1, max_digits=5, verbose_name='章节顺序'),
            preserve_default=False,
        ),
    ]
