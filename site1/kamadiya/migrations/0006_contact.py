# Generated by Django 4.2.3 on 2023-07-24 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kamadiya', '0005_blog_alter_book_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
