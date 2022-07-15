from rest_framework import serializers

from .models import Form

class FormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Form
        fields = (
            'id',
            'teacher_name',
            'q1',
            'q2',
            'q3',
            'q4',
            'q5',
            'q6',
            'q7',
            'q8',
        )