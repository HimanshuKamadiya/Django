# Generated by Django 4.2.3 on 2023-07-12 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamadiya', '0002_rename_text_service_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('page_no', models.CharField(max_length=200)),
            ],
        ),
    ]
