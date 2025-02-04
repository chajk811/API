# Generated by Django 2.2.4 on 2020-01-13 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageId', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('ingredients', models.CharField(max_length=200)),
                ('monthlySales', models.IntegerField()),
                ('oily_point', models.IntegerField()),
                ('dry_point', models.IntegerField()),
                ('sensitive_point', models.IntegerField()),
            ],
        ),
    ]
