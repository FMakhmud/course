from rest_framework.serializers import ModelSerializer
from .models import Lesson, LessonAnalysis


class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'title',
            'vide_link',
            'viewing_duration',
        )


# class LessonProgressSerializer(ModelSerializer):
#     class Meta:
#         model = LessonAnalysis
#         fields = ('watched_time_seconds', 'status', 'last_viewed')
#
#
# class LessonsSerializer(ModelSerializer):
#     progress = LessonProgressSerializer(many=True)
#
#     class Meta:
#         model = Lesson
#         fields = (
#             'id',
#             'title',
#             'video_link',
#             'viewing_duration',
#             'progress'
#         )
