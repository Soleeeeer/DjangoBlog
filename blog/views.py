from rest_framework import generics, permissions
from .models import Category, Publication
from .serializers import CategorySerializers, PublicationSerializers
from .permissions import IsOwnerOrReadOnly



class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

class CategoryRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


class PublicationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PublicationSerializers
    queryset = Publication.objects.filter(is_archived=False)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PublicationRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublicationSerializers
    queryset = Publication.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
