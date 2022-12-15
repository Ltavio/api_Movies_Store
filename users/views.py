from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404

from .permissions import IsEmployeeOrReadOnly, IsAuthenticateOrReadOnly, IsUserOwner
from .serializer import UsersNormalSerializer, UsersEmploySerializer
from .models import Users


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


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserOwner]

    def get(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(Users, pk=user_id)
        self.check_object_permissions(request, user)

        serializer = UsersEmploySerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)


class LoginView(TokenObtainPairView):
    ...
