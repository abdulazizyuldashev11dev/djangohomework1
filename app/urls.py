from django.urls import path
from .views import CreateAPiView, ListAPiView, UpdateStatus

urlpatterns = [
    path('create/', CreateAPiView.as_view()),
    path('all/', ListAPiView.as_view()),
    path('update_status/<int:news_id>/', UpdateStatus.as_view()),
]
