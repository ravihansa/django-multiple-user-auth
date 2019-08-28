from django.conf.urls import url
from rest_framework import routers
from .views import (CustomerRegisterView, MerchantRegisterView, UserLoginView, UserPasswordChangeView,
                    CustomerProfileview, MerchantProfileview)

urlpatterns = [
    url(r"^customer/register/$", CustomerRegisterView.as_view(),
        name="customer-register"),
    url(r"^merchant/register/$", MerchantRegisterView.as_view(),
        name="merchant-register"),
    url(r"^login/$", UserLoginView.as_view(), name="user-login"),
    url(r"^password-change/$", UserPasswordChangeView.as_view(),
        name="user-password-change"),
    url(r"^customer/profile/$", CustomerProfileview.as_view(),
        name="user-profile"),
    url(r"^merchant/profile/$", MerchantProfileview.as_view(),
        name="user-profile"),
]
