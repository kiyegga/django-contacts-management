from os import name
from django.urls import path, re_path
#from .views import ContactCreateView, HomePageView, ContactDetailView, search, ContactUpdateView, ContactDeleteView  # home, detail,
from . import views


app_name = 'app'
urlpatterns = [
   # path('', home, name="home"), 
   path('', views.HomePageView.as_view(), name="home"),
   # path('detail/<int:id>/', detail, name="detail"),
   # path('detail/<int:pk>/', ContactDetailView.as_view(), name="detail"), 
   path('detail/<slug:slug>/',
        views.ContactDetailView.as_view(), name="detail"),
   path('search', views.search, name="search"),
   path('contacts/create', views.ContactCreateView.as_view(), name="create"),
   path('contacts/update/<int:pk>',
        views.ContactUpdateView.as_view(), name="update"),
   path('contacts/delete/<int:pk>',
        views.ContactDeleteView.as_view(), name="delete"),
   path('signup/', views.SignUpView.as_view(), name="signup"),
]
