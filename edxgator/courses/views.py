from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from .serializers import CourseSerializer
from .models import Course


class CourseViewSet(ListModelMixin, GenericViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = None
