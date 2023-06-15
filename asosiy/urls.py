from django.urls import path
from .views import *

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('<int:pk>/mahsulotlar/',MasulotlarView.as_view(),name='mahsulotlar'),
    path('mahsulot/<int:son>/',BittaMahsulotView.as_view(),name='mahsulot   '),
    path('bolimlar/',HammaBolimView.as_view(),name='bolimlar'),
]