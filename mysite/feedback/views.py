from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.response import Response


class UserView(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	queryset = User.objects.all()

	def create(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		email = request.POST.get('email')
		try:
			user = User.objects.create_user(username, email, password)
			return Response({'message' : 'User created successfully!!'}, status=200)
		except:
			return Response({'message' : 'Sorry! The user already exsists'}, status=200)

	def list(self, request):
		serializer = UserSerializer(self.get_queryset(), many=True)
		return Response(serializer.data)

	def retrieve(self, request, pk=None):
		user = get_object_or_404(self.get_queryset(), pk=pk)
		serializer = UserSerializer(user)
		return Response(serializer.data)

	def destroy(self, request, pk=None):
		user = get_object_or_404(self.get_queryset(), pk=pk)
		user.delete()
		return Response(status=200)