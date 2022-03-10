from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from ..models import Note
from .serializers import NoteSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = {
        'Access Token': 'api/token/',
        'Refresh Token': 'api/token/refresh/',
    }
    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    try:
        user = request.user
        qs = user.note_set.all()
        serializer = NoteSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except PermissionError:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    except (ConnectionAbortedError, ConnectionError, ConnectionRefusedError, ConnectionResetError):
        return Response(status=status.HTTP_502_BAD_GATEWAY)