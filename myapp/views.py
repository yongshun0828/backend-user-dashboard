from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .models import Record
from .serializers import RecordSerializer


class RecordListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/records/        — list all records (supports ?search=)
    POST /api/records/        — create a new record
    """
    serializer_class = RecordSerializer

    def get_queryset(self):
        qs     = Record.objects.all()
        search = self.request.query_params.get('search', '').strip()
        if search:
            qs = qs.filter(
                Q(name__icontains=search) |
                Q(email__icontains=search) |
                Q(category__icontains=search) |
                Q(description__icontains=search)
            )
        return qs


class RecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/records/<id>/  — retrieve one record
    PUT    /api/records/<id>/  — full update
    PATCH  /api/records/<id>/  — partial update
    DELETE /api/records/<id>/  — delete
    """
    queryset         = Record.objects.all()
    serializer_class = RecordSerializer


class RecordStatsView(APIView):
    """
    GET /api/records/stats/  — summary counts for the dashboard
    """
    def get(self, request):
        from django.db.models import Count
        total      = Record.objects.count()
        by_cat     = (
            Record.objects
            .values('category')
            .annotate(count=Count('id'))
            .order_by('-count')
        )
        return Response({
            'total': total,
            'by_category': list(by_cat),
        })
