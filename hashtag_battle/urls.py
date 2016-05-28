from django.contrib import admin
from django.conf.urls import url, include
from battle import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'battle', views.BattleViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),    
]
