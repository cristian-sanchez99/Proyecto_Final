# Generated by Django 4.0.5 on 2022-07-05 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Autos', '0003_camionetas_delete_categoria_alter_autos_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='autos',
            name='image',
            field=models.ImageField(default='', upload_to='autos'),
            preserve_default=False,
        ),
    ]