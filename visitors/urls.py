from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path("",views.index, name="homepage"),
    path("buycrypto", views.buycrypto, name="buycrypto"),
    path("cryptoloan", views.cryptoloan, name="cryptoloan"),
    path("debitcard", views.debitcard, name="debitcard"),
    path("earn", views.earn, name="earn"),
    path("market", views.market, name="market")
    
]
