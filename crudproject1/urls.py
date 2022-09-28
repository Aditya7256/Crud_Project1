from django.contrib import admin
from django.urls import path
from crud_app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_show, name = 'addandshow'),
    path('delete/<int:id>/', views.delete_data,name = 'deletedata' ),
    path('<int:id>/', views.update_data,name = 'updatedata' ),
]

