# Generated by Django 2.0.7 on 2018-08-25 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogmodel_blogsequence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='blogsequence',
        ),
        migrations.AddField(
            model_name='blogmodel',
            name='blogFather',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.BlogModel', verbose_name='父类章节'),
        ),
    ]
