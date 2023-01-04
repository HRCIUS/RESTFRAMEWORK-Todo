from rest_framework import viewsets
from app.models import Todo
from app.serializers import Todoserializers

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = Todoserializers