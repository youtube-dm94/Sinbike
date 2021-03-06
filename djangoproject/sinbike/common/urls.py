from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns=[
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('faq/',views.faq, name='faq'),
    path('about/',views.about, name='about'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)