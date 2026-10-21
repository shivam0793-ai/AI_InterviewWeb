from rest_framework.serializers import ModelSerializer
from interviews.models import interview

class modelserializer(ModelSerializer):
    class Meta:
        model=interview
        fields='__all__'