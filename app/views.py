from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def atletas(request):
    atletas = [
        {"nome": "Lionel Messi", "idade": "37", 
         "posicao": "meia-atacante", 
         "nascimento": "Rosario - AR", 
         "foto": "messi.webp"},
        {"nome": "Neymar Jr.", "idade": "32", 
         "posicao": "ponta esquerda", 
         "nascimento": "Santos-SP", 
         "foto": "neymar.jpg"},

    ]

    context = {
        "atletas": atletas,
    }
    return render(request, "atletas.html", context)

def sobre(request):
    return render(request, "sobre.html")
