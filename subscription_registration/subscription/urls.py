from django.urls import path
from subscription.views import AsyncAddressListCreateView, AsyncAddressDetailView

urlpatterns = [
    path("addresses/<str:address_id>/", AsyncAddressDetailView.as_view()),
    path("addresses/", AsyncAddressListCreateView.as_view()),    
]
