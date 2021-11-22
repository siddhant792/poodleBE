from rest_framework import generics as rest_framwork_generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token as AuthToken
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from apps.accounts import serializers as accounts_serializers


class RegisterUserView(rest_framwork_generics.CreateAPIView):
    serializer_class = accounts_serializers.UserSerializer
    permission_classes = [AllowAny]


class LoginUserView(rest_framwork_generics.CreateAPIView):
    """
    Login API
    """
    serializer_class = accounts_serializers.LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        login_serializer = self.serializer_class(data=request.data)
        login_serializer.is_valid(raise_exception=True)
        token = AuthToken.objects.get(user = login_serializer.validated_data['user']).key
        return Response({'token': token})


class LogoutUserView(rest_framwork_generics.DestroyAPIView):
    """
    LogOut the current user
    """
    query_set = AuthToken.objects.all()

    def destroy(self, request, *args, **kwargs):
        token_key = request.headers.get("Authorization")
        token = self.query_set.filter(key=token_key)
        if token:
            token.delete()
            return Response({'message': "Logout Successful"}, status=HTTP_200_OK)
        return Response({'message': "Logout Failed"}, status=HTTP_400_BAD_REQUEST)
