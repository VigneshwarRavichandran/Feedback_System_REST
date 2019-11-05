from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.response import Response


class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

	def list(self, request):
		serializer = UserSerializer(self.get_queryset(), many=True)
		return Response(serializer.data)

	def destroy(self, request, pk=None):
		user = get_object_or_404(self.get_queryset(), pk=pk)
		user.delete()
		return Response(status=200)