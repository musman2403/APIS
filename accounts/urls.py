from django.urls import path
from . import views
from .views import profile_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', profile_view, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
