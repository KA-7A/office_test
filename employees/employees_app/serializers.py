from rest_framework import serializers
from .models import Usr_Dep

class Usr_Dep_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Usr_Dep
        fields = ('usr_id', 'dep_id', 'date_of_transition') 