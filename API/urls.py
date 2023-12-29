from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'employees', views.EmployeesViewSet)
router.register(r'menus', views.MenuViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'foods', views.FoodViewSet)
router.register(r'tables', views.TableViewSet)
router.register(r'billHeader', views.BillHeaderViewSet)
router.register(r'billDetails', views.BillDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]