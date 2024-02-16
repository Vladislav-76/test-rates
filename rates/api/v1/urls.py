from api.v1.views import RateListView
from django.urls import path

urlpatterns = [
    path('rate/', RateListView.as_view()),
]
