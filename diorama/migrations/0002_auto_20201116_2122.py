# Generated by Django 3.1.3 on 2020-11-16 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diorama', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/')),
                ('image_name', models.CharField(max_length=25)),
                ('image_description', models.TextField(max_length=250)),
                ('image_category', models.ManyToManyField(to='diorama.Category')),
            ],
            options={
                'ordering': ['image_name'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Editor',
        ),
        migrations.DeleteModel(
            name='tags',
        ),
        migrations.AddField(
            model_name='image',
            name='image_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diorama.location'),
        ),
    ]