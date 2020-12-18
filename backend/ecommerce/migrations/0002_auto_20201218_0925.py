# Generated by Django 3.1.4 on 2020-12-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('discount', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('type', models.IntegerField(choices=[(0, 'Jewellery'), (1, 'Cloth')])),
            ],
        ),
        migrations.DeleteModel(
            name='Hii',
        ),
    ]