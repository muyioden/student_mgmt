from django.urls import path
from students import views as students_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', students_views.index.as_view(), name='home'),
    path('api/students/', students_views.tutorial_list),
    path('api/students/<int:pk>/', students_views.tutorial_detail),
    path('api/students/published/', students_views.tutorial_list_published)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
