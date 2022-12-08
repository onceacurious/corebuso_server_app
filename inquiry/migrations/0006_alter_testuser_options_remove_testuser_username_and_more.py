# Generated by Django 4.1.3 on 2022-12-03 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0005_rename_user_testuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testuser',
            options={'ordering': ['-registered_at'], 'verbose_name_plural': 'Test Users'},
        ),
        migrations.RemoveField(
            model_name='testuser',
            name='username',
        ),
        migrations.AddField(
            model_name='testuser',
            name='designation',
            field=models.CharField(default='staff', max_length=50),
        ),
    ]
