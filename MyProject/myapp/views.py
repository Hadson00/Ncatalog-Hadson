from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def home(request):
    clothes = Clothes.objects.all()
    return render(request, 'site/home.html', {'clothes': clothes})

def index(request):
    user = request.user    
    clothes = Clothes.objects.all()
    data_clothes = []
    for item in clothes:    
        data_clothes.append(    
            {
            'item': item,
            'liked': item.user_liked(user) if user.is_authenticated else False,
            'comments': Comment.objects.filter(clothes=item)
            }
        )
    return render(request, 'site/index.html', {'item': data_clothes})

@login_required
def like_clothes(request, clothes_id):
    clothes = get_object_or_404(Clothes, id=clothes_id)
    like, created = Like.objects.get_or_create(user=request.user, clothes=clothes)
    if not created:
        like.delete()
    return redirect('index')

@login_required
def comment_clothes(request, clothes_id):
    clothes = get_object_or_404(Clothes, id=clothes_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(user=request.user, clothes=clothes, content=content)
    return redirect('index')

@login_required
def create(request):
    if request.method == 'POST':
        form = ClothesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Roupa cadastrada com sucesso!')
            return redirect('home')
    else:
        form = ClothesForm()
    return render(request, 'site/create.html', {'form': form})

@login_required
def edit(request, clothes_id):
    clothes = get_object_or_404(Clothes, id=clothes_id)
    if request.method == 'POST':
        form = ClothesForm(request.POST, request.FILES, instance=clothes)
        if form.is_valid():
            form.save()
            messages.success(request, 'Roupa editada com sucesso!')
            return redirect('index')
    else:
        form = ClothesForm(instance=clothes)
    return render(request, "site/update.html",{"form":form, "clothes":clothes})

@login_required
def delete_clothes(request, clothes_id):
    clothes = get_object_or_404(Clothes, id=clothes_id)
    if request.method == 'POST':
        clothes.delete()
        messages.success(request, 'Roupa deletada com sucesso!')
        return redirect('home')
    return render(request, 'site/delete.html', {'clothes': clothes})

@login_required
def cart(request, clothes_id):
    clothes = get_object_or_404(Clothes, id=clothes_id)
    return render(request, "site/cart.html",{"clothes":clothes})

def cart_delete(request, clothes_id):
    clothes = Clothes.objects.get(pk=clothes_id)
    clothes.delete()
    messages.success(request, 'Item foi deletada com sucesso!')
    return redirect('index')