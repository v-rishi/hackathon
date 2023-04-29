import secrets
import string

from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class GenerateRandomPasswordAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for i in range(8))
        return Response({'status':'success', 'password':password})