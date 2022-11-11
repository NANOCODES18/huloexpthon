from django.urls import path
from . import views

urlpatterns = [
    path("user/",views.dashboard, name="dashboard"),
    path("user/contractTrading",views.contractTrading, name="contractTrading"),
    path("user/general",views.general, name="general"),
    path("user/spotTrading",views.spotTrading, name="spotTrading"),
    path("user/mywallet",views.mywallet, name="mywallet"),
   path("user/verification",views.verification, name="verification"),
   path("user/security",views.security, name="security"),
    path("user/general/update",views.general_update, name="general_update"),
]