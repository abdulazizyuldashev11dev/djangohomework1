from django.urls import path
from .views import AppCreateView, AppListApiView, AppUpdateView

urlpatterns = [
    path('create/', AppCreateView.as_view()),
    path('all/', AppListApiView.as_view()),
    path('update_status/<int:id>/', AppUpdateView.as_view()),
]