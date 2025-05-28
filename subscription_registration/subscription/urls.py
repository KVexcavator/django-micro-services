from django.urls import path
from subscription.views import AsyncAddressListCreateView

urlpatterns = [
    path("addresses/", AsyncAddressListCreateView.as_view()),
]
