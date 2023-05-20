from rest_framework import routers
from .api import ProjectViewSet

route = routers.DefaultRouter()
route.register('api/projects', ProjectViewSet, 'projects')

urlpatterns = route.urls
