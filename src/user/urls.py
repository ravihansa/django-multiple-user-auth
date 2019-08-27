from django.conf.urls import url
from rest_framework import routers
from .views import (CustomerRegisterView, MerchantRegisterView, UserLoginView, UserPasswordChangeView,
                    UserProfileview)

urlpatterns = [
    url(r"^customer/register/$", CustomerRegisterView.as_view(),
        name="customer-register"),
    url(r"^merchant/register/$", MerchantRegisterView.as_view(),
        name="merchant-register"),
    url(r"^login/$", UserLoginView.as_view(), name="user-login"),
    url(r"^password-change/$", UserPasswordChangeView.as_view(),
        name="user-password-change"),
    url(r"^profile/$", UserProfileview.as_view(),
        name="user-profile"),
]
