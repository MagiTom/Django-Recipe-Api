from rest_framework import viewsets, permissions, status
from .models import Recipe, Category
from .serializers import RecipeSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied, NotFound
from rest_framework.pagination import PageNumberPagination


@api_view(["GET"])
def test_view(request):
    return Response({"message": "API działa!"})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("Nie masz dostępu do tej kategorii.")
        return obj

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise PermissionDenied("Nie masz dostępu do tej kategorii.")
        return obj

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "Kategoria została dodana!", "data": response.data},
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(
            {"message": "Kategoria została zaktualizowana!", "data": response.data}
        )

    def destroy(self, request, *args, **kwargs):
        self.perform_destroy(self.get_object())
        return Response(
            {"message": "Kategoria została usunięta."},
            status=status.HTTP_204_NO_CONTENT,
        )


class RecipePagination(PageNumberPagination):
    page_size = 10


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = RecipePagination

    def get_queryset(self):
        queryset = Recipe.objects.filter(user=self.request.user)

        if self.request.query_params.get("favourite") == "true":
            queryset = queryset.filter(favourite=True)

        category = self.request.query_params.get("category")
        try:
            if category is not None:
                category_id = int(category)
                queryset = queryset.filter(category_id=category_id)
        except (TypeError, ValueError):
            pass

        title_query = self.request.query_params.get("title")
        if title_query:
            queryset = queryset.filter(title__icontains=title_query)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(
            {"message": "Przepis został dodany!", "data": response.data},
            status=status.HTTP_201_CREATED,
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied("Nie masz uprawnień do edycji tego przepisu.")
        response = super().update(request, *args, **kwargs)
        return Response(
            {"message": "Przepis został zaktualizowany!", "data": response.data}
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            raise PermissionDenied("Nie masz uprawnień do usunięcia tego przepisu.")
        self.perform_destroy(instance)
        return Response(
            {"message": "Przepis został usunięty."}, status=status.HTTP_204_NO_CONTENT
        )
