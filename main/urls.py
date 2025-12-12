from django.urls import path
from main.views import show_main, profil_sekolah

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('profil/', profil_sekolah, name='profil_sekolah'),
]