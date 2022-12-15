from rest_framework.views import APIView, Request, Response, status

from .serializer import UsersNormalSerializer, UsersEmploySerializer
from .models import Users

from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView


class UserRegisterView(APIView):
    def post(self, request: Request) -> Response:
        if "is_employee" not in request.data:
            # USUÁRIO COMUM
            serializer_user_normal = UsersNormalSerializer(data=request.data)
            serializer_user_normal.is_valid(raise_exception=True)
            serializer_user_normal.save()
            return Response(serializer_user_normal.data, status.HTTP_201_CREATED)

        # USUÁRIO EMPREGADO
        serializer_superuser = UsersEmploySerializer(data=request.data)
        serializer_superuser.is_valid(raise_exception=True)
        serializer_superuser.save()
        return Response(serializer_superuser.data, status.HTTP_201_CREATED)


class LoginView(TokenObtainPairView):
    ...
