from django.conf.urls import url
import django.contrib.auth.views
from search.views import SearchResultsView


urlpatterns = [
    # Examples:
    url(r'^$', SearchResultsView.as_view(), name='search_results'),
    ]
