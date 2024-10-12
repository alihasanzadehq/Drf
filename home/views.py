from django.shortcuts import render
from rest_framework.views import APIView
# from rest_framework.decorators import api_view
from  rest_framework.response import Response
from . import models
from .models import Person , Question, Answer
from .serializers import  PersonSerializer , QuestionSerializer,AnswerSerializer
from  rest_framework.permissions import IsAuthenticated , IsAdminUser
from rest_framework import status
from permissions import IsOwnerOrReadOnly
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
class HomeView(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self, request):
        # name = request.query_params.get('name')
        person = Person.objects.all()
        ser_data = QuestionSerializer(instance=person, many=True)
        return  Response(data=ser_data.data)

    def post(self, request):
        name = request.data['name']
        return  Response({"name": name})


class QuestionListView(APIView):
    """
    Create New question
    """
    throttle_classes = [UserRateThrottle,AnonRateThrottle]
    def get(self, request):
        question = Question.objects.all()
        srz_data = QuestionSerializer(question, many=True)
        return Response(srz_data.data)


class QuestionCrateView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = QuestionSerializer


    def post(self, request):
        srz_data = QuestionSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]
    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request,question)

        srz_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]
    def Delete(self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({"message": 'Deleted Successfuly'})
