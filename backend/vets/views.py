# from rest_framework import viewsets
# from .serializer import VetSerializer
# from .models import Vet

# # Create your views here.
# class VetView(viewsets.ModelViewSet):
#     serializer_class = VetSerializer
#     queryset = Vet.objects.all()

# vets/views.py
from rest_framework import generics
from .models import Vet
from .serializer import VetSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class VetListByUserView(generics.ListAPIView):
    serializer_class = VetSerializer
    #permission_classes = [IsAuthenticated]  # Opcional: Asegura que el usuario esté autenticado

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Vet.objects.filter(user=user_id)
    


# Create your views here.
class VetView(viewsets.ModelViewSet):
    serializer_class = VetSerializer
    queryset = Vet.objects.all()