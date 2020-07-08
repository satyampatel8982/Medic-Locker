"""MedicLocker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include # include is defined in another file
from django.conf.urls.static import static  #static for adding the static
from django.conf import settings # it is a django feature
from django.views.generic import RedirectView # redirectviews to default home page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ml/', include("ml.urls")), #aditional include path to map urls
    path('accounts/', include('django.contrib.auth.urls')),  # adding accounts urls in application
    path('', RedirectView.as_view(url='/ml/', permanent=True)), #it will add a new direction to page

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
          # it is using for the noraml settings
          # adding Static file content to the site
