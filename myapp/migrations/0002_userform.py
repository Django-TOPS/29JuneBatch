# Generated by Django 3.2.7 on 2021-09-29 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('option', models.CharField(max_length=100)),
                ('select_file', models.FileField(upload_to='MyFiles')),
                ('disc', models.TextField()),
            ],
        ),
    ]
