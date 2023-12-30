from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('type/add/', views.add_type),
    path('type/add/addrecord', views.add_type_record),
    path('type/update/<int:id>', views.update_type),
    path('type/update/updaterecord/<int:id>', views.update_type_record),
    path('type/delete/<int:id>', views.delete_type),
    path('room/add/', views.add_room),
    path('room/add/addrecord', views.add_room_record),
    path('room/update/<int:id>', views.room),
    path('room/update/updaterecord/<int:id>', views.update_room_record),
    path('room/delete/<int:id>', views.delete_room),    
]