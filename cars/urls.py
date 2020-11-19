from django.urls import path
from cars import views


app_name='cars'

urlpatterns=[
    path('create/', views.createCarView.as_view(), name='create'),
]