from django.urls import path
from .views import PropertyListView, PropertyDetailView, SellPropertyListView, SellPropertyDetailView


app_name = 'property'

urlpatterns = [
    path('', PropertyListView.as_view(), name='property'),
    path('sell/', SellPropertyListView.as_view(), name='property'),
    path('<slug:slug>/', PropertyDetailView.as_view(), name='property_detail'),
    path('<slug:slug>/', SellPropertyDetailView.as_view(), name='sell_property_detail')
]


