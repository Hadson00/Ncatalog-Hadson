from django.shortcuts import redirect, render
from myapp.models import  *
from myapp.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home_view(request):
    return render(request, 'site/home.html')

def index(request):
    
    return render(request, 'site/index.html',{"itens": Clothes.objects.all()})

def create(request):
    form = ClothesForm
    if request.method == "POST":
        form = ClothesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'item cadastrada com sucesso!')
            return redirect('index')
        
    return render(request, "site/create.html", {"forms":form})



def edit(request, id):
    item = Clothes.objects.get(pk=id)
    form = ClothesForm(instance=item)
    return render(request, "site/update.html",{"form":form, "item":item})


def update(request, id):
    try:
        if request.method == "POST":
            item = Clothes.objects.get(pk=id)
            form = ClothesForm(request.POST, request.FILES, instance=item)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'item foi alterada com sucesso!')
                return redirect('index')
    except Exception as e:
        messages.error(request, e)
        return redirect('index')
            
def read(request, id):
    item = Clothes.objects.get(pk=id)
    return render(request, "site/read.html", {"item":item})

def delete(request, id):
    item = Clothes.objects.get(pk=id)
    item.delete()
    messages.success(request, 'item foi deletada com sucesso!')
    return redirect('index')

def all(request):
    return render(request, 'site/clothes_list.html',{"itens": Clothes.objects.all()})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        messages.error(request, 'Usuário ou senha incorretos.')
        return render(request, 'site/index.html')

def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Usuário Deslogado!')
    return redirect(index)

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(index) # Substitua 'home' pela URL desejada após o cadastro
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})