# Generated by Django 4.2.1 on 2023-05-23 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=200)),
                ('cuerpo', models.TextField()),
                ('autor', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='article_images/')),
                ('creado_por', models.DateTimeField(auto_now_add=True)),
                ('editado_por', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
