# Generated by Django 4.1.7 on 2023-04-04 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=36)),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name': 'Sales',
            },
        ),
    ]
