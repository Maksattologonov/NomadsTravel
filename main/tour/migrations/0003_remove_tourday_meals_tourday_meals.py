# Generated by Django 4.2.3 on 2025-01-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourday',
            name='meals',
        ),
        migrations.AddField(
            model_name='tourday',
            name='meals',
            field=models.CharField(choices=[('Звтрак', 'breakfast'), ('Обед', 'medium'), ('Ужин', 'hard')], max_length=50, null=True, verbose_name='Питание'),
        ),
    ]