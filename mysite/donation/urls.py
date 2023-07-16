from django.urls import path
from donation import views

urlpatterns = [
    path('inst-api/', views.InstitutionPaginatorAPI.as_view(), name='inst_api'),

    path('add-donation/', views.AddDonation.as_view(), name='add_donation'),
    path('profile/', views.Profil.as_view(), name='profile'),
    path('donation/<int:pk>/', views.DonateDetails.as_view(), name='donate_details'),
    path('contact/', views.Contact.as_view(), name='contact'),
]