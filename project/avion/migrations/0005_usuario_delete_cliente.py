# Generated by Django 5.0.6 on 2024-05-24 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avion', '0004_avion_capacidad_maxima_avion_fecha_incorporacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('celular', models.IntegerField()),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatares')),
            ],
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]