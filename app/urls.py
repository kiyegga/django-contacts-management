from os import name
from django.urls import path, re_path
from .views import ContactCreateView, HomePageView, ContactDetailView, search, ContactUpdateView, ContactDeleteView  # home, detail,


app_name = 'app'
urlpatterns = [
   # path('', home, name="home"), 
   path('', HomePageView.as_view(), name="home"),
   # path('detail/<int:id>/', detail, name="detail"),
   # path('detail/<int:pk>/', ContactDetailView.as_view(), name="detail"), 
   path('detail/<slug:slug>/',
         ContactDetailView.as_view(), name="detail"),
   path('search', search, name="search"),
   path('contacts/create', ContactCreateView.as_view(), name="create"),
   path('contacts/update/<int:pk>', ContactUpdateView.as_view(), name="update"),
   path('contacts/delete/<int:pk>', ContactDeleteView.as_view(), name="delete"),
]
