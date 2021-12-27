from django.urls import path
#from . import views
from .views import home,detail

urlpatterns = [
    #path('',views.home, name="home"),
    path('', home.as_view(), name="home"),
    path('article/<int:pk>',detail.as_view(), name="article-detail"),

]
