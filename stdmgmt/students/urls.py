from django.urls import path
from students import views as students_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/students/', students_views.student_list),
    path('api/students/<int:pk>/', students_views.student_detail)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
