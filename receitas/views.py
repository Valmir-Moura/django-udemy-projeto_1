from django.shortcuts import render


def home(request):
    return render(request, 'receitas_2/home.html', context={
        'nome': 'Valmir Roberto',
    })
