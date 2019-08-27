from rest_framework import generics, mixins, views, status, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.settings import api_settings
from django.http import HttpResponse
from django.shortcuts import render
from .serializers import UserSerializer, MerchantSerializer, UserProfileSerializer
from .models import User
import bcrypt
import json
import ast


class CustomerRegisterView(generics.CreateAPIView):
    lookup_field = "pk"
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MerchantRegisterView(generics.CreateAPIView):
    lookup_field = "pk"
    serializer_class = MerchantSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserLoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        if not request.data:
            return HttpResponse(
                {"Error": "Please provide your email and password"}, status="400"
            )

        email = request.data["email"]
        password = request.data["password"].encode("utf8")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponse(
                json.dumps({"Error": "Invalid email"}),
                status=400,
                content_type="application/json",
            )
        if user:
            usrPassword = ast.literal_eval(user.password)
            if bcrypt.checkpw(password, usrPassword):
                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return HttpResponse(
                    json.dumps({"token": token}),
                    status=200,
                    content_type="application/json",
                )
            else:
                return HttpResponse(
                    json.dumps({"Error": "Invalid password"}),
                    status=400,
                    content_type="application/json",
                )


class UserPasswordChangeView(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if not request.data:
            return HttpResponse(
                {"Error": "Please provide your passwords"}, status="400"
            )

        email = request.user
        password = request.data["password"].encode("utf8")
        newPassword = request.data["new_password"].encode("utf8")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponse(
                json.dumps({"Error": "Invalid user"}),
                status=400,
                content_type="application/json",
            )
        if user:
            userPassword = ast.literal_eval(user.password)
            if bcrypt.checkpw(password, userPassword):
                salt = self.saltSecret()
                hashedPassword = bcrypt.hashpw(newPassword, salt)
                User.objects.filter(email=email).update(
                    password=hashedPassword)

                return HttpResponse(
                    json.dumps({"Sucess": "Password changed successfully"}),
                    status=200,
                    content_type="application/json",
                )
            else:
                return HttpResponse(
                    json.dumps({"Error": "Invalid passowrd"}),
                    status=400,
                    content_type="application/json",
                )

    def saltSecret(self):
        return bcrypt.gensalt()


class UserProfileview(views.APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user
        queryset = User.objects.filter(id=user.id)
        serializer = UserProfileSerializer(queryset, many=True)
        user = serializer.data
        return HttpResponse(
            json.dumps({"data": user}),
            status=200,
            content_type="application/json",
        )
