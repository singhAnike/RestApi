# Generated by Django 4.1.6 on 2023-06-01 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_board', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Medium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_medium', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_standard', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentsdata.address')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentsdata.board')),
                ('medium', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentsdata.medium')),
                ('standard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentsdata.standard')),
            ],
        ),
    ]
