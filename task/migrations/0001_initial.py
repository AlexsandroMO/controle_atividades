# Generated by Django 4.0 on 2022-04-29 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_acting', models.CharField(max_length=255, verbose_name='ÁREA')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='NOME')),
                ('photo', models.FileField(blank=True, null=True, upload_to='uploads/photos/', verbose_name='FOTO')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('control_acting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.acting', verbose_name='ÁREA')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj_name', models.CharField(max_length=255, verbose_name='STATUS')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_status', models.CharField(max_length=255, verbose_name='STATUS')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arq', models.FileField(help_text='localizar Arquivo', upload_to='uploads/')),
                ('update_arq', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_proj1', models.CharField(max_length=255, verbose_name='PROJETO A')),
                ('control_status1', models.CharField(max_length=255, verbose_name='STATUS A')),
                ('control_proj2', models.CharField(max_length=255, verbose_name='PROJETO B')),
                ('control_status2', models.CharField(max_length=255, verbose_name='STATUS B')),
                ('control_proj3', models.CharField(max_length=255, verbose_name='PROJETO C')),
                ('control_status3', models.CharField(max_length=255, verbose_name='STATUS C')),
                ('control_proj4', models.CharField(max_length=255, verbose_name='PROJETO D')),
                ('control_status4', models.CharField(max_length=255, verbose_name='STATUS D')),
                ('control_proj5', models.CharField(max_length=255, verbose_name='PROJETO E')),
                ('control_status5', models.CharField(max_length=255, verbose_name='STATUS E')),
                ('control_proj6', models.CharField(max_length=255, verbose_name='PROJETO F')),
                ('control_status6', models.CharField(max_length=255, verbose_name='STATUS F')),
                ('control_obs', models.CharField(max_length=255, verbose_name='OBS')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('control_acting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.acting', verbose_name='FUNÇÃO')),
                ('control_nome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.profissional', verbose_name='NOME')),
            ],
        ),
    ]
