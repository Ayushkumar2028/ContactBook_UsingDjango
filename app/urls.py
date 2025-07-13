from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<int:contact_id>/',views.delete_contact,name='delete_contact'),
    path('edit/<int:contact_id>/',views.edit_contact,name='edit_contact'),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'), 
]
