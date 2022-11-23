from rest_framework import serializers
from .models import Application
from rest_framework.authtoken.views import Token
from django.contrib.auth.models import User 




class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"
        
        

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','email', 'username', 'password']
#         extra_kwargs = {'password':{
#             'write_only':True,
#             'required':True
#         }}
        
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         Token.objects.create(user=user)
#         return user 