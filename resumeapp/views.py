from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUCF, LoginForm
from .models import Hotels, UserBookedHotels
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def bookedhotels(request):
  
  hotels = UserBookedHotels.objects.all()
  print('--------------------hotels ----------------------------------')
  for hotel in hotels:
    print(hotel.hotel_names)
    print(type(hotel))
  
  return render(request, 'resumeapp/testing.html', {'hotels': hotels})
  

class CustomListView( LoginRequiredMixin, ListView):
  model = Hotels
  template_name = 'resumeapp/hotels.html'
  context_object_name = 'hotels'
  # ordering = ['total_rooms']
  
  
def search_by_price(request):
  search_price = request.GET.get('search-price')
  print('---------------------testing-----------------')
  print(search_price)
  if search_price:
    hotels = Hotels.objects.filter(starting_price__lte=search_price)
    return render(request, 'resumeapp/hotels.html', {'hotels': hotels})
  
  
class CustomDetailView(LoginRequiredMixin, DetailView):
  model = Hotels
  template_name = 'resumeapp/checkouthotel.html'
  context_object_name = 'hotel'
  

  
  
class CustomSignupView(CreateView):
  template_name = 'resumeapp/signup.html'
  form_class = CustomUCF
  success_url = 'login'
  def get(self, request, *ars, **kwargs):
    signupform = self.get_form_class()
    return render(request, self.template_name, {'signupform': signupform})
  
  def post(self, request, *args, **kwargs):
    # print('----------------------testing-----------------------------')
    # print(request.POST)
    signupform = self.form_class(request.POST)
    if signupform.is_valid():
      signupform.save()
      messages.success(request, f"Your account have been created successfully. ")
      return render(request, self.template_name, {'signupform': signupform})
    else:
      return render(request, self.template_name, {'signupform': signupform})
  
  
class CustomLoginView(LoginView):
  form_class = LoginForm
  # success_url = 'hotels'
  template_name = 'resumeapp/login.html'
  
  def get(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return render(request, 'resumeapp/hotels.html')
    else:
      loginform = self.get_form_class()
      print('------------------loginform---------------')
      print(loginform)
      return render(request, self.template_name, {'loginform': loginform})

  def post(self, request, *args, **kwargs):
    loginform = self.form_class(request, request.POST)
    if loginform.is_valid():
      return super().form_valid(loginform)
    else:
        return render(request, self.template_name, {'loginform': loginform})

  def get_success_url(self):
    return reverse('hotels')
  
@login_required
def logoutview(request):
  logout(request)
  messages.success(request, "You have successfully logged out !!! ")
  return render(request, 'resumeapp/logout.html')
    
  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  