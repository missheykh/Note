from django.urls import path
from django.urls.conf import include
from notify.views import send_note

urlpatterns = [
    
    path('sendnote/<str:r>/<str:c>',send_note)
]
