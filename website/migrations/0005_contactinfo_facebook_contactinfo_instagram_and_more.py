# Generated by Django 4.0.6 on 2024-01-06 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_attraction'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='facebook',
            field=models.URLField(blank=True, null=True, verbose_name='Facebook URL'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram URL'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='linkedin',
            field=models.URLField(blank=True, null=True, verbose_name='LinkedIn URL'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='twitter',
            field=models.URLField(blank=True, null=True, verbose_name='Twitter URL'),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='youtube',
            field=models.URLField(blank=True, null=True, verbose_name='Youtube URL'),
        ),
    ]
