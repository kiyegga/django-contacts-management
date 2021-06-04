from django.db import models
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm

# def home(request):
#     contacts = Contact.objects.all()
#     context = {
#         'contacts' : contacts
#     }
#     return render(request, 'index.html', context)

# def detail(request, id):
#     contact = get_object_or_404(Contact, pk=id)
#     context = {
#        'contact': contact
#     }
#     return render(request, 'detail.html', context)

class HomePageView(ListView): 
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contacts'


class ContactDetailView(DetailView):
    model = Contact
    slug_field = 'slug'
    template_name = 'detail.html'
    context_object_name = 'contacts'

def search(request):
    if request.GET:
        search_term = request.GET['search_term']
        search_results = Contact.objects.filter(
            Q(name__icontains=search_term) |
            Q(email__icontains=search_term) |
            Q(info__icontains=search_term) |
            Q(phone__iexact=search_term)
            )
        context = {
            'search_term': search_term,
            'contacts': search_results
        }
        return render(request, 'search.html', context)
    else:
        return redirect('home')  
    # if request.method == "GET":
    #     search_term = request.GET['search_term']
    #     context = {
    #         'search_term': search_term
    #     }
    #     return render(request, 'search.html', context)
    # else:
    #     return redirect('home') 
class ContactCreateView(CreateView):
    model = Contact
    template_name = 'create.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    success_url = '/'


class ContactUpdateView(UpdateView):
    model = Contact
    template_name = 'update.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    
    def form_valid(self, form):
        instance = form.save()
        return redirect('app:detail', instance.slug)


class ContactDeleteView(DeleteView):
    model = Contact
    template_name = 'delete.html'
    success_url = '/'


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = 'home '
