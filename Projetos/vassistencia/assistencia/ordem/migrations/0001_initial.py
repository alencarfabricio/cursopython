# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordem',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('situacao', models.CharField(max_length=1, choices=[('0', 'Em conserto'), ('1', 'Pronto'), ('2', 'Aguardando pe\x87a')])),
                ('data', models.DateField(auto_now_add=True)),
                ('codigo_consulta', models.CharField(max_length=10, editable=False)),
                ('cliente', models.ForeignKey(to='cliente.Cliente')),
            ],
            options={
                'verbose_name_plural': 'Ordens de servico',
                'verbose_name': 'Ordem de servico',
            },
        ),
        migrations.CreateModel(
            name='TabelaCadastro',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('tabelacadastro_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='ordem.TabelaCadastro', serialize=False, parent_link=True)),
            ],
            bases=('ordem.tabelacadastro',),
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('tabelacadastro_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='ordem.TabelaCadastro', serialize=False, parent_link=True)),
            ],
            bases=('ordem.tabelacadastro',),
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('tabelacadastro_ptr', models.OneToOneField(primary_key=True, auto_created=True, to='ordem.TabelaCadastro', serialize=False, parent_link=True)),
            ],
            bases=('ordem.tabelacadastro',),
        ),
        migrations.AddField(
            model_name='ordem',
            name='marca',
            field=models.ForeignKey(to='ordem.Marca'),
        ),
        migrations.AddField(
            model_name='ordem',
            name='modelo',
            field=models.ForeignKey(to='ordem.Modelo'),
        ),
        migrations.AddField(
            model_name='ordem',
            name='produto',
            field=models.ForeignKey(to='ordem.Produto'),
        ),
    ]
