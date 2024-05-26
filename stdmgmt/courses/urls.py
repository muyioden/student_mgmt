from django.urls import path
from courses import views as courses_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/courses/', courses_views.course_list),
    path('api/courses/<int:pk>/', courses_views.course_detail)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
