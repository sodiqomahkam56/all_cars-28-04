from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from cars import views

urlpatterns=[
    path('', views.get_cars, name='cars-list'),
    path('update/<int:id>/', views.car_update, name='car-update'),
    path('delete/<int:id>/', views.delete_car, name='delete-car'),
    path('form/', views.create_car_form, name='create-form'),
    path('car/<int:id>/', views.car_detail, name='car-detail'),
    path('create/', views.create_car, name='create-car'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)