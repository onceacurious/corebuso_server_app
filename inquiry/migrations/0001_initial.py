# Generated by Django 4.1.3 on 2022-12-08 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name="client's complete name")),
                ('contact', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('company', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('inquiry_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('R', 'Reviewed'), ('D', 'Done')], default='P', max_length=1)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'inquiries',
                'ordering': ['-inquiry_at'],
            },
        ),
        migrations.CreateModel(
            name='TestUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(default='staff', max_length=50)),
                ('registered_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Test Users',
                'ordering': ['-registered_at'],
            },
        ),
    ]
