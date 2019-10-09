# Generated by Django 2.2.3 on 2019-09-12 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noticeapp', '0017_notices_issuing_authority'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hostel_Management_Commitee',
            new_name='Hostel_Management_Committee',
        ),
        migrations.CreateModel(
            name='Wardens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('contact', models.CharField(max_length=15)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='noticeapp.Hostels')),
            ],
        ),
        migrations.CreateModel(
            name='Mess_Management_Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mess_secretary_email', models.CharField(max_length=50)),
                ('mess_manager_email', models.CharField(max_length=50)),
                ('hostel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='noticeapp.Hostels')),
            ],
        ),
    ]