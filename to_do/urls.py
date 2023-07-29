from django.urls import path

from to_do.views import get_list, list_detail

urlpatterns = [
    path('list/', get_list),
    path('detail/<int:pk>/', list_detail)
]
