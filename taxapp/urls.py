# urls.py
from django.urls import path

from.import views
from .views import *
app_name = "taxapp"


urlpatterns = [
    
    path('', views.home, name="home"),
    path('search/', views.search, name="search"),
    path('tinlist/', views.tinlist, name="tinlist"),
    path('notfound/', views.notfound, name="notfound"),
    path('cb/', views.cb, name="cb"),
    
    path('dashboard/', views.dashboard, name="dashboard"),
    path('bwise/', views.bwise, name="bwise"),
    path('bwise2/<str:bname>/', views.bwise2, name="bwise2"),
   
    path('search/', views.search_view2, name="search_view2"),
    path('search_view2', views.search_view2, name="search_view2"),
    path('search/search_view2', views.search_view2, name="search_view2"),
    path('cb2/<int:r>/', views.cb2, name="cb2"),
    path('admin/', views.admin, name="admin"),
    
]
