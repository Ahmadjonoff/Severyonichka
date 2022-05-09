from django.urls import path
from .views import *

urlpatterns = [
    path('bolim/', Catalog.as_view(), name = 'bolim'),
    path('bolim/<int:pk>/', Mahsulotlar.as_view(), name = 'mahsulotlar'),
    path('mahsulot/<int:pk>/', Mahsulot.as_view(), name = 'mahsulot'),
]