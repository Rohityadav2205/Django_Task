from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path("create", views.create),
    path("retrieve", views.retrieve),
    path("edit", views.edit),
    path("show1data", views.show1data),
    path("delete", views.delete),
    path("update", views.update),
path("jsonall", views.jsonall),

]
