from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rating import views

router=DefaultRouter()
router.register('rating',views.RatingViewSet)
app_name='rating'
urlpatterns=[
    path('add/', views.AddRate.as_view(), name='add rating'),
]