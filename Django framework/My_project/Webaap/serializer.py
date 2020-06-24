from rest_framework import serializers

from .models import student


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        # field=('first_name','last_name')
        fields = '__all__'
