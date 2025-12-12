from django.shortcuts import render

def show_main(request):
    return render(request, "LandingPage.html")

def profil_sekolah(request):
    return render(request, "ProfilSekolah.html")