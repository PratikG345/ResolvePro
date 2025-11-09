from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('complaint/',views.complaints),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('assign_vendor/<int:job_id>/', views.assign_vendor, name='assign_vendor'),
    path('mark_resolved/<int:job_id>/', views.mark_resolved, name='mark_resolved'),
    path('admin/', admin.site.urls),
]
