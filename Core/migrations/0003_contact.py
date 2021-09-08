# Generated by Django 3.2.6 on 2021-09-08 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_rename_services_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=100)),
                ('Subject', models.CharField(max_length=100)),
                ('Message', models.TextField()),
            ],
        ),
    ]
