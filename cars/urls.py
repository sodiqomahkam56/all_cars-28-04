from django.urls import path
from cars import views

urlpatterns=[
    path('', views.get_cars, name='cars-list'),
    path('update/<int:id>/', views.car_update, name='car-update'),
    path('form/', views.create_car_form, name='create-form'),
    path('car/<int:id>/', views.car_detail, name='car-detail'),
    path('create/', views.create_car, name='create-car'),
]