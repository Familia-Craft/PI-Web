# Generated by Django 4.2.2 on 2023-07-02 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PI_WEB', '0002_ferramenta_imagem_servidor_last_login_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servidor',
            name='funcao',
            field=models.CharField(choices=[('P', 'Profesosr'), ('B', 'Bolsista')], max_length=1),
        ),
    ]