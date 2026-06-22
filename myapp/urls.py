from django.urls import path,include
from . import views

urlpatterns=[
    path("",views.home),
    path("services/",views.services_view,name='services'),
    path('accounts/',include("django.contrib.auth.urls")),
    path("signup/",views.signup_view,name='signup'),
    path('createaccount/',views.create_acount_view,name='createaccount'),
    path('deposit/',views.deposit_view,name='deposit'),
    path('withdraw/',views.withdraw_view,name='withdraw'),
    path('profileview/',views.profile_view,name='profileview'),
    path('loans/', views.loans, name='loans'),
    path('services_main/',views.services_main_view,name='services_main'),
    path('money_transfer/',views.money_transfer_view,name='money_transfer')
]