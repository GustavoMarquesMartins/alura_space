from django.urls import path
from apps.galeria.views import \
     index, buscar, salvar, editar, deletar, imagem, categoria

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('salvar', salvar, name='salvar'),
    path('editar/<int:foto_id>', editar, name='editar'),
    path('deletar/<int:foto_id>',deletar, name='deletar'),
    path('categoria/<str:categoria>', categoria, name='categoria')
] 