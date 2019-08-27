from rest_framework import serializers
from .models import User, Customer, Merchant
import bcrypt


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "phone_no",
            "password",
            "pic_path",
        )

    def create(self, validated_data):
        salt = self.saltSecret()
        user = User.objects.create(
            email=validated_data["email"],
            phone_no=validated_data["phone_no"],
            is_customer=True,
            password=bcrypt.hashpw(
                validated_data["password"].encode("utf8"), salt),
        )
        return user

    def saltSecret(self):
        return bcrypt.gensalt()


class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "phone_no",
            "password",
            "pic_path",
        )

    def create(self, validated_data):
        salt = self.saltSecret()
        user = User.objects.create(
            email=validated_data["email"],
            phone_no=validated_data["phone_no"],
            is_merchant=True,
            password=bcrypt.hashpw(
                validated_data["password"].encode("utf8"), salt),
        )
        return user

    def saltSecret(self):
        return bcrypt.gensalt()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "phone_no",
            "pic_path",
        )
