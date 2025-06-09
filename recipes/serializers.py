from rest_framework import serializers
from .models import Recipe, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['user']

    def update(self, instance, validated_data):
        if "image" in self.initial_data:
            image = self.initial_data.get("image")
            if image in [None, "", "null"] and instance.image:
                instance.image.delete(save=False)
                instance.image = None

        return super().update(instance, validated_data)


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ['user']

    def update(self, instance, validated_data):
        if "image" in self.initial_data:
            image = self.initial_data.get("image")
            if image in [None, "", "null"] and instance.image:
                instance.image.delete(save=False)
                instance.image = None

        return super().update(instance, validated_data)
