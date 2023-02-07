"""eckard URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('eckardapi/admin/', admin.site.urls),
    path('eckardapi/auth/', include('eckard_api.urls.auth')),
    path('eckardapi/account/', include('eckard_api.urls.account')),
    path('eckardapi/auction_type/', include('eckard_api.urls.auction_type')),
    path('eckardapi/constraint/', include('eckard_api.urls.constraint')),
    path('eckardapi/cash_flow/', include('eckard_api.urls.cash_flow')),
    path('eckardapi/contact/', include('eckard_api.urls.contact')),
    path('eckardapi/investment/', include('eckard_api.urls.investment')),
    path('eckardapi/income/', include('eckard_api.urls.income')),
    path('eckardapi/listing_type/', include('eckard_api.urls.listing_type')),
    path('eckardapi/listing/', include('eckard_api.urls.listing')),
    path('eckardapi/offer/', include('eckard_api.urls.offer')),
    path('eckardapi/project/', include('eckard_api.urls.project')),
    path('eckardapi/status/', include('eckard_api.urls.status')),
    path('eckardapi/tract/', include('eckard_api.urls.tract')),
    path('eckardapi/cash_config/', include('eckard_api.urls.cash_config')),

    path('eckardapi/key_value/', include('eckard_api.urls.key_value')),
]
