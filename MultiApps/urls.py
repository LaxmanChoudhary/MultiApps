"""MultiApps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#readyToUse views-for-auth
from django.contrib.auth import views as auth_views

#from django.conf.urls import url


urlpatterns = [
    #home
    path('', include('home.urls')),

    path('admin/', admin.site.urls),

    #user-login, no imports
    path('accounts/', include('django.contrib.auth.urls')),

    #social-auth-app-django
    #path('oauth/', include('social_django.urls'), namespace='social'),

    #apps
    path('logger/', include('logger.urls')),
    path('todo/', include('todo.urls')),

]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()


# social-django-urls-added
'''
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
        path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
    )
    print('Using ',social_login,' as the login template')
except:
    print('Using registration/login.html as the login template')
'''