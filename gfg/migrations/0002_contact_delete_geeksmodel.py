# Generated by Django 4.1.2 on 2022-10-09 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gfg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='GeeksModel',
        ),
    ]
