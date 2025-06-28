from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManagerViewSet, InternViewSet, AddressViewSet

router = DefaultRouter()
router.register(f'managers', ManagerViewSet)
router.register(f'interns', InternViewSet)
router.register(f'addresses', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]