# Generated by Django 3.1.2 on 2022-02-15 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bases_de_datos', '0001_initial'),
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.TextField()),
                ('servidor', models.CharField(max_length=200)),
                ('dominio', models.CharField(max_length=100)),
                ('path', models.CharField(max_length=200)),
                ('bases_de_datos', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='bases_de_datos.base')),
                ('lenguaje', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalogos.lenguajes')),
                ('situacion', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='catalogos.situacion')),
            ],
            options={
                'verbose_name': 'Sistema',
                'verbose_name_plural': 'Sistemas',
                'ordering': ['id'],
            },
        ),
    ]
