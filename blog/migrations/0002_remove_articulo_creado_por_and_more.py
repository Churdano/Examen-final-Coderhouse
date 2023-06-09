# Generated by Django 4.2.1 on 2023-05-23 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='creado_por',
        ),
        migrations.RemoveField(
            model_name='articulo',
            name='editado_por',
        ),
        migrations.AddField(
            model_name='articulo',
            name='creador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='articulo_imagen/'),
        ),
    ]
