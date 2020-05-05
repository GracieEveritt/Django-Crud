from django.conf.urls import url, include
# from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AllProjectViews, ByProjectTypeView

# router = routers.DefaultRouter()
#
# router.register(r'projects', AllProjectViews, basename='projects')
# router.register(r'projects/{lookup}$', ByProjectTypeView, basename='type')
#
# urlpatterns = router.urls

urlpatterns = {
    url(r'^projects/$', AllProjectViews.as_view(), name='parks'),
    url(r'^projects/(?P<pk>[0-9]+)/$', ByProjectTypeView.as_view(), name='parks-edit'),
}

urlpatterns = format_suffix_patterns(urlpatterns)