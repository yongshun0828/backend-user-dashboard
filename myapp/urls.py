from django.urls import path
from .views import RecordListCreateView, RecordDetailView, RecordStatsView

urlpatterns = [
    path('records/',        RecordListCreateView.as_view(), name='record-list-create'),
    path('records/stats/',  RecordStatsView.as_view(),      name='record-stats'),
    path('records/<int:pk>/', RecordDetailView.as_view(),   name='record-detail'),
]
