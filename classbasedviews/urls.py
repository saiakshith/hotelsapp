
from django.contrib import admin
from django.urls import path
from resumeapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', CustomListView.as_view(), name='hotels'),
    path('searchprice', search_by_price, name='searchprice'),
    path('checkouthotel/<int:pk>/', CustomDetailView.as_view(), name='checkouthotel'),
    path('bookedhotels/', bookedhotels, name='bookedhotels'),
    path('signup/', CustomSignupView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logoutview, name='logout'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
