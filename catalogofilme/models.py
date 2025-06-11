from django.db import models


class ModelBase(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)
    created_at = models.DateTimeField(db_column='dt_created', auto_now_add=True, null=True)
    modified_at = models.DateTimeField(db_column='dt_modified', auto_now=True, null=True)
    active = models.BooleanField(db_column='cs_active', default=True)

    class Meta:
        abstract = True
        managed = True


class Genero(ModelBase):
    nome = models.CharField(db_column='nome', max_length=100)

    class Meta:
        db_table = 'generos'


class Filme(ModelBase):
    titulo = models.CharField(db_column='titulo', max_length=255)
    sinopse = models.TextField(db_column='sinopse')
    imagem_uri = models.CharField(db_column='imagem_uri', max_length=255)
    data_criacao = models.DateField(db_column='data_de_criacao')
    generos = models.ManyToManyField(Genero, through='FilmeGenero')

    class Meta:
        db_table = 'filmes'


class FilmeGenero(models.Model):
    filme = models.ForeignKey(Filme, db_column='filme_id', on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, db_column='genero_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'filme_genero'
        unique_together = ('filme', 'genero')


class Elenco(ModelBase):
    nome = models.CharField(db_column='nome', max_length=255)

    class Meta:
        db_table = 'elenco'


class ElencoFilme(models.Model):
    filme = models.ForeignKey(Filme, db_column='filme_id', on_delete=models.CASCADE)
    elenco = models.ForeignKey(Elenco, db_column='elenco_id', on_delete=models.CASCADE)
    funcao = models.CharField(db_column='funcao', max_length=100)

    class Meta:
        db_table = 'elenco_filme'
        unique_together = ('filme', 'elenco')


class Usuario(ModelBase):
    nome = models.CharField(db_column='nome', max_length=255)
    email = models.EmailField(db_column='email', unique=True)
    senha = models.CharField(db_column='senha', max_length=255)

    class Meta:
        db_table = 'usuarios'


class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, db_column='usuarios_id', on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, db_column='filme_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'favoritos'
        unique_together = ('usuario', 'filme')
