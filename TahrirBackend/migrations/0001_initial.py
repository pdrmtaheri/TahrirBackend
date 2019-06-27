# Generated by Django 2.2.1 on 2019-06-27 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersianWord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('submitter_name', models.CharField(max_length=50)),
                ('rating', models.PositiveSmallIntegerField()),
                ('translation_obj_id', models.PositiveIntegerField()),
                ('translation_ct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='FaToEnTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('submitter_name', models.CharField(max_length=50)),
                ('translation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TahrirBackend.EnglishWord')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TahrirBackend.PersianWord')),
            ],
            options={
                'unique_together': {('word', 'translation')},
            },
        ),
        migrations.CreateModel(
            name='EnToFaTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('submitter_name', models.CharField(max_length=50)),
                ('translation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TahrirBackend.PersianWord')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TahrirBackend.EnglishWord')),
            ],
            options={
                'unique_together': {('word', 'translation')},
            },
        ),
    ]
