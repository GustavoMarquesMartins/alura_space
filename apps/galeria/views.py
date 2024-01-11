from django.shortcuts import render, get_object_or_404, redirect

from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='login')
def index(request):
    return render(request, 'galeria/index.html', {"cards": get_fotografias()})


@login_required(login_url='login')
def imagem(request, foto_id):
    return render(request, 'galeria/imagem.html', {"fotografia": get_fotografia(foto_id)})


@login_required(login_url='login')
def buscar(request):
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']

        if nome_a_buscar:
            fotografias = get_fotografias().filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/index.html", {"cards": fotografias})


@login_required(login_url='login')
def salvar(request):
    form = FotografiaForms()

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)

        if form.is_valid():
            fotografia = form.save(commit=False)
            fotografia.usuario = request.user
            fotografia.save()
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {'form': form})


@login_required(login_url='login')
def editar(request, foto_id):
    fotografia = get_fotografia(foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)

        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})


@login_required(login_url='login')
def deletar(request, foto_id):
    fotografia = get_fotografia(foto_id)
    fotografia.foto.delete()
    fotografia.delete()
    messages.success(request, 'Deleção feita com sucesso')
    return redirect('index')


@login_required(login_url='login')
def categoria(request, categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)
    return render(request, 'galeria/index.html', {"cards": fotografias})


@login_required(login_url='login')
def favoritar(request, fotografia_id):
    fotografia = get_fotografia(fotografia_id)
    fotografia.favoritado = not fotografia.favoritado
    fotografia.save()
    return redirect('index')


@login_required(login_url='login')
def favoritados(request):
    fotografias = Fotografia.objects.filter(favoritado=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})


@login_required(login_url='login')
def minhas_publicacoes(request):
    fotografias = Fotografia.objects.filter(usuario=request.user)
    return render(request, 'galeria/index.html', {'cards': fotografias})


def get_fotografias():
    return Fotografia.objects.order_by("data_fotografia").filter(publicada=True)


def get_fotografia(foto_id):
    return get_object_or_404(Fotografia, pk=foto_id)


# Parte para desenvolvimento
@login_required(login_url='login')
def deletar_todos(request):
    fotografias = Fotografia.objects.filter(publicada=True)
    if fotografias:
        for fotografia in fotografias:
            fotografia.foto.delete()
            fotografia.delete()
    else:
        messages.error(request, 'Todas  as imagems já foram deletadas !')
    return redirect('index')


def adicionar_um_apenas_para_testar(request):
    usuario = User.objects.get(username='gustavo')
    fotografia = Fotografia(nome='nome', legenda='teste', categoria='NEBULOSA', descricao='teste', foto=None,
                            publicada=True, usuario=usuario)
    fotografia.save()
    return redirect('index')
