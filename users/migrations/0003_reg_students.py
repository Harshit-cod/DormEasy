# Generated by Django 2.2.4 on 2019-09-03 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190903_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reg_Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50)),
                ('regno', models.PositiveIntegerField(max_length=10)),
                ('sem', models.CharField(max_length=1)),
                ('Gender', models.CharField(max_length=1)),
            ],
        ),
    ]
