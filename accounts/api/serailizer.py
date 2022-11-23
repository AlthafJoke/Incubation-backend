from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers


User=get_user_model()

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['admin'] = user.is_admin
        return token
    
class AccoutsSerializer(serializers.ModelSerializer):
  class Meta:
    model=User
    fields = [ 'email', 'password','phone_no','first_name','last_name','Company']
    # extra_kwargs = {'password': {'write_only': True}}

  def create(self, validated_data):
      user = super().create(validated_data)
      user.set_password(validated_data['password'])
      user.save()
      return user 