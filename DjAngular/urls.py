from django.conf.urls import patterns, url

from DjAngular.views import IndexView

urlpatterns = patterns(
    '',

    url('^.*$', IndexView.as_view(), name='index'),
)
