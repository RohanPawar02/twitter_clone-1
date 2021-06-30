from django.urls import path
from . import views


urlpatterns = [
    path('',views.Tweet,name='Tweet'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete),
    path('like/<int:id>/',views.like),
   
]
