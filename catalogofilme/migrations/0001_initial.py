# Generated by Django 5.2.3 on 2025-06-11 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elenco',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('nome', models.CharField(db_column='nome', max_length=255)),
            ],
            options={
                'db_table': 'elenco',
            },
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('titulo', models.CharField(db_column='titulo', max_length=255)),
                ('sinopse', models.TextField(db_column='sinopse')),
                ('imagem_uri', models.CharField(db_column='imagem_uri', max_length=255)),
                ('data_criacao', models.DateField(db_column='data_de_criacao')),
            ],
            options={
                'db_table': 'filmes',
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('nome', models.CharField(db_column='nome', max_length=100)),
            ],
            options={
                'db_table': 'generos',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='dt_created', null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, db_column='dt_modified', null=True)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('nome', models.CharField(db_column='nome', max_length=255)),
                ('email', models.EmailField(db_column='email', max_length=254, unique=True)),
                ('senha', models.CharField(db_column='senha', max_length=255)),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='FilmeGenero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filme', models.ForeignKey(db_column='filme_id', on_delete=django.db.models.deletion.CASCADE, to='catalogofilme.filme')),
                ('genero', models.ForeignKey(db_column='genero_id', on_delete=django.db.models.deletion.CASCADE, to='catalogofilme.genero')),
            ],
            options={
                'db_table': 'filme_genero',
                'unique_together': {('filme', 'genero')},
            },
        ),
        migrations.AddField(
            model_name='filme',
            name='generos',
            field=models.ManyToManyField(through='catalogofilme.FilmeGenero', to='catalogofilme.genero'),
        ),
        migrations.CreateModel(
            name='ElencoFilme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcao', models.CharField(db_column='funcao', max_length=100)),
                ('elenco', models.ForeignKey(db_column='elenco_id', on_delete=django.db.models.deletion.CASCADE, to='catalogofilme.elenco')),
                ('filme', models.ForeignKey(db_column='filme_id', on_delete=django.db.models.deletion.CASCADE, to='catalogofilme.filme')),
            ],
            options={
                'db_table': 'elenco_filme',
                'unique_together': {('filme', 'elenco')},
            },
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filme', models.ForeignKey(db_column='filme_id', on_delete=django.db.models.deletion.CASCADE, to='catalogofilme.filme')),
                ('usuario', models.ForeignKey(db_column='usuarios_id', on_delete=django.db.models.deletion.CASCADE, to='catalogofilme.usuario')),
            ],
            options={
                'db_table': 'favoritos',
                'unique_together': {('usuario', 'filme')},
            },
        ),
    ]
