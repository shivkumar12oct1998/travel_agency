from .models import adminsidedetail,usersideinfo
from rest_framework import serializers
class serializer1(serializers.ModelSerializer):
    class Meta:
        model=adminsidedetail()
        fields='__all__'
class serializer2(serializers.ModelSerializer):
    class Meta:
        model=usersideinfo()
        fields='__all__'