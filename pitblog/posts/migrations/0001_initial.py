# Generated by Django 4.1.3 on 2022-12-16 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('conteudo', models.TextField()),
                ('excerto', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='img_post/%Y/%m')),
                ('publicado', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='categorias.categoria')),
            ],
        ),
    ]
