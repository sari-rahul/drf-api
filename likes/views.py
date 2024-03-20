from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikesSerializer
# Create your views here.

class LikeList(generics.ListCreateAPIView):
    serializer_class = LikesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    serializer_class = LikesSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()
