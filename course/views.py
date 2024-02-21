from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Category, Lesson, LessonAnalysis
from rest_framework.permissions import IsAuthenticated


class LessonsAPIView(ListAPIView):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        lessons = Lesson.objects.filter(products__owner=user)

        for i in lessons:
            lesson_progress = LessonAnalysis.objects.filter(lesson_v=i, user=user).first()
            if lesson_progress:
                i.progress_status = lesson_progress.status
                i.watched_time_seconds = lesson_progress.watched_time_seconds
        return lessons




