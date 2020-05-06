from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AllProjectViews, ByProjectTypeView, ProjectFilterView #, ProjectFilterViewSet
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'category', ProjectFilterViewSet, basename="filter-category")
#
# router.register(r'projects', AllProjectViews, basename='projects')
# # router.register(r'projects/{lookup}$', ByProjectTypeView, basename='type')
#
# urlpatterns = router.urls

urlpatterns = {
    url(r'^projects/$', AllProjectViews.as_view(), name='projects'),
    url(r'^projects/(?P<pk>[0-9]+)/$', ByProjectTypeView.as_view(), name='projects-edit'),
    url(r'^filter/$', ProjectFilterView.as_view(), name='filter'),

    # url(r'^filter/view$', ProjectFilterViewSet.as_view({'get':'list'}), name='filter-view')
}

# urlpatterns = router.urls
# urlpatterns += custom_urlpatterns
urlpatterns = format_suffix_patterns(urlpatterns)
