from django.db import models
from django.db.models import Q, manager
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
#LoginRequiredMixin only works on class based views for the case function based views 
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

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


class HomePageView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Contact
    context_object_name = 'contacts'

    #overriding and display only current login user contacts
    def get_queryset(self):
        contacts = super().get_queryset()
        return contacts.filter(manager = self.request.user)


class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact
    slug_field = 'slug'
    template_name = 'detail.html'
    context_object_name = 'contacts'


@login_required
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
            'contacts': search_results.filter(manager=request.user) #only search for current login user
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


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    template_name = 'create.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    
    #atouching the saved contact to current login user as manager of that contact
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.manager = self.request.user
        instance.save()
        return redirect('app:home')


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    template_name = 'update.html'
    fields = ['name', 'email', 'phone', 'info', 'gender', 'image']
    
    def form_valid(self, form):
        instance = form.save()
        return redirect('app:detail', instance.slug)


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    template_name = 'delete.html'
    success_url = '/'


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    # success_url = 'app:home'
    success_url = reverse_lazy('app:home')
