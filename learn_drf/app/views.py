from rest_framework import viewsets
from . import models
from rest_framework.decorators import api_view
from . import serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import status
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from .permissions import IsOwnArticleOrReadOnly

@csrf_exempt
@api_view(['POST'])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None and password is None:
        return Response({'error': 'Please provide user & password'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid credentials'},
                        status=status.HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=status.HTTP_200_OK)


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnArticleOrReadOnly]
