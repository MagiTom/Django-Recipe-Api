import traceback
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomTokenObtainPairSerializer

class CustomLoginView(APIView):
    def post(self, request):
        try:
            serializer = CustomTokenObtainPairSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        except Exception as e:
            print("🔴 Login failed:", str(e))
            traceback.print_exc()
            return Response({"detail": "Internal server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
