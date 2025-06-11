from rest_framework import serializers
from .models import (
    Genero,
    Filme,
    FilmeGenero,
    Elenco,
    ElencoFilme,
    Usuario,
    Favorito
)


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['id', 'nome']


class FilmeGeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmeGenero
        fields = ['filme', 'genero']


class ElencoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elenco
        fields = ['id', 'nome']


class ElencoFilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElencoFilme
        fields = ['filme', 'elenco', 'funcao']


class FilmeSerializer(serializers.ModelSerializer):
    generos = GeneroSerializer(many=True, read_only=True)
    elenco = serializers.SerializerMethodField()

    class Meta:
        model = Filme
        fields = ['id', 'titulo', 'sinopse', 'imagem_uri', 'data_criacao', 'generos', 'elenco']

    def get_elenco(self, obj):
        elenco_filme = ElencoFilme.objects.filter(filme=obj)
        return ElencoFilmeSerializer(elenco_filme, many=True).data



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'senha']
        extra_kwargs = {
            'senha': {'write_only': True}
        }


class FavoritoSerializer(serializers.ModelSerializer):
    filme = FilmeSerializer(read_only=True)
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())

    class Meta:
        model = Favorito
        fields = ['id', 'usuario', 'filme']
