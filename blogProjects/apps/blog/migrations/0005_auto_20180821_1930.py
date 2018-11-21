# Generated by Django 2.0.7 on 2018-08-21 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_category_is_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='desc',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_finished',
            field=models.BooleanField(default=False, verbose_name='是否完成'),
        ),
    ]
