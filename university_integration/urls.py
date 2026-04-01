from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from student_app.views import StudentViewSet
from library_app.views import LibraryViewSet
from payment_app.views import PaymentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'library', LibraryViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/integration/', include('integration_hub.urls')),
]