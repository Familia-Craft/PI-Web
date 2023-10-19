"""PI_WEB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from PI_WEB.views import home, auth, actions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.home, name='home-page'),
    path('login', auth.login, name='login-page'),
    path('cadastrar', auth.cadastro, name='cadastro-page'),
    path('logout', auth.deslogar, name='logout-page'),
    path('ferramenta/<id>', actions.ferramenta, name='ferramenta-page'),
    path('cadastrar_ferramenta', actions.cadastrar_ferramenta, name='cadastrar_ferramenta-page'),
    path('fluxo', actions.fluxo, name='fluxo-page')
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
