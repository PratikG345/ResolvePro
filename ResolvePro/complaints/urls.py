from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('complaint/',views.complaints),
    path('dashboard/',views.dashboard),
    path('admin/', admin.site.urls),
]
