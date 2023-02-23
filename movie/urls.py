from django.contrib import admin
from django.urls import path
from movie import views
# from .views import MovieList,MovieDetail
urlpatterns = [
    path('',views.index,name="index"),
    path('about/<str:title>/',views.about,name="about"),
    path('toprate',views.toprate,name="toprate"),
    path('most',views.most,name="most"),
    path('latest',views.latest,name="latest"),
    path('search',views.search,name="search")
    # path('<int:pk>',MovieDetail.as_view,name="moviedetail")
]
