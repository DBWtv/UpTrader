from django.urls import path
from .views import start_page

urlpatterns = [
    path('', start_page),
    path('<slug:url>', start_page, name='url')
]