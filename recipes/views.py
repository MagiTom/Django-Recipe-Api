from rest_framework import viewsets, permissions, status
from .models import Recipe, Category
from .serializers import RecipeSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied, NotFound

@api_view(['GET'])
def test_view(request):
    return Response({"message": "API działa!"})

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "message": "Kategoria została dodana!",
            "data": response.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response({
            "message": "Kategoria została zaktualizowana!",
            "data": response.data
        })

    def destroy(self, request, *args, **kwargs):
        self.perform_destroy(self.get_object())
        return Response({
            "message": "Kategoria została usunięta."
        }, status=status.HTTP_204_NO_CONTENT)


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Recipe.objects.filter(user=self.request.user)
        category_id = self.request.query_params.get('category', None)
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            "message": "Przepis został dodany!",
            "data": response.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied("Nie masz uprawnień do edycji tego przepisu.")
        response = super().update(request, *args, **kwargs)
        return Response({
            "message": "Przepis został zaktualizowany!",
            "data": response.data
        })

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied("Nie masz uprawnień do usunięcia tego przepisu.")
        self.perform_destroy(instance)
        return Response({
            "message": "Przepis został usunięty."
        }, status=status.HTTP_204_NO_CONTENT)

