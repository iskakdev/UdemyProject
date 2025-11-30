from django.shortcuts import render
from .models import (UserProfile, Course, Category,
                     SubCategory, Review, Certificate, Exam)
from .serializers import (UserProfileListSerializer, UserProfileDetailSerializer,
                          CategoryListSerializer, CategoryDetailSerializer,
                          SubCategoryListSerializer, SubCategoryDetailSerializer,
                          CourseListSerializer, CourseDetailSerializer,
                          ReviewCreateSerializer, CertificateSerializer, ExamSerializer,
                          CreateCourseSerializer)
from rest_framework import viewsets, generics


class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class UserProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class SubCategoryListAPIView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryListSerializer


class SubCategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryDetailSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer



class CreateCourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CreateCourseSerializer

    def get_queryset(self):
        return Course.objects.filter(teacher=self.request.user)


class CourseDetailAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)


class ReviewEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def get_queryset(self):
        return Review.objects.filter(student=self.request.user)
