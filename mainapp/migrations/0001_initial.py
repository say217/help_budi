# Generated by Django 3.1 on 2020-10-17 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('depth', models.IntegerField()),
                ('material', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=500)),
                ('colours', models.ManyToManyField(to='mainapp.Color')),
            ],
        ),
    ]
