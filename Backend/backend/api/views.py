from .serializers import SubjectSerializer
from .models import Subject
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

class SubjectList(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
