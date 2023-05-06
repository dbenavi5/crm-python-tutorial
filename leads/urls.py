from django.urls import path
from .views import (lead_list, lead_detail, lead_create, lead_update, lead_delete, LeadPageViews , LeadDetailViews, LeadCreateViews, LeadUpdateViews, LeadDeleteViews)

app_name = 'leads'

urlpatterns =[
    path('', LeadPageViews.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailViews.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateViews.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteViews.as_view(), name='lead-delete'),
    path('create/', LeadCreateViews.as_view(), name='lead-create'),
]