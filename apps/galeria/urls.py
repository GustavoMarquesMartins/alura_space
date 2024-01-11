from django.urls import path
from apps.galeria.views import \
    index, buscar, salvar, editar, deletar, imagem, categoria, deletar_todos, adicionar_um_apenas_para_testar, favoritar, favoritados, minhas_publicacoes
urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('salvar', salvar, name='salvar'),
    path('editar/<int:foto_id>', editar, name='editar'),
    path('deletar/<int:foto_id>', deletar, name='deletar'),
    path('categoria/<str:categoria>', categoria, name='categoria'),
    path('favoritar/<int:fotografia_id>', favoritar, name='favoritar'),
    path('favoritados',favoritados, name='favoritados'),
    path('minhas-publicacoes',minhas_publicacoes, name='minhas_publicacoes'),

    path('deletar-todos', deletar_todos, name='deletar_todos'),
    path('adicionar-um-apenas-para-testar', adicionar_um_apenas_para_testar, name='adicionar_um_apenas_para_testar'),
]
