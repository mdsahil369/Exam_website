from rest_framework import serializers
from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subject', 'chapter', 'question', 'option01', 'option02', 'option03', 'option04', 'answer', 'board', 'univercity']