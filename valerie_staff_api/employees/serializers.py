from rest_framework import serializers
from .models import Manager, Intern, Address

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'first_name', 'last_name', 'email', 'department', 'get_role']
        read_only_fields = ['has_company_card']

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = ['id', 'first_name', 'last_name', 'email', 'mentor', 'internship_end', 'get_role']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '_all_'