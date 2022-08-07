from django.contrib import admin
from django.urls import include, path

from dictionary.views import AllWords, WordOfTheDay

urlpatterns = [
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('api/wod/', WordOfTheDay.as_view(), name="wod"),
    path('api/all/', AllWords.as_view(), name="all")
]
