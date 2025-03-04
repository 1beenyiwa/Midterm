# Generated by Django 5.1.6 on 2025-03-03 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Textbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('edition', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('course_code', models.CharField(max_length=20)),
                ('availability', models.BooleanField(default=True)),
                ('condition', models.CharField(choices=[('new', 'New'), ('written', 'Written'), ('old', 'Old')], max_length=10)),
            ],
        ),
    ]
