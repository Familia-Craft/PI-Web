# Generated by Django 4.2.2 on 2023-07-01 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PI_WEB', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ferramenta',
            name='imagem',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AddField(
            model_name='servidor',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='servidor',
            name='password',
            field=models.CharField(default='senha123', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]