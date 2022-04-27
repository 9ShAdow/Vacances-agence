from django.shortcuts import render


def index(request):
    return render(request,"index2.html")


def formulaire(request):
    return render(request,"formulaire.html")



def main(request):
    return render(request,"main.html")

def bmain(request):
    return render(request,"bmain.html")

def bonjour(request):
    nom = request.GET["nom"]
    prenom = request.GET["prenom"]
    return render(request, 'bonjour.html', {"nom": nom, "prenom": prenom})