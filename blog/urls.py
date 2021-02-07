from django.contrib import admin
from django.urls import path
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
			path('',views.show_main),
			path('main/',views.show_main),
			path('structure/',views.show_structure),
			path('moving/',views.show_moving),
			path('using/',views.show_using),
			path('news/',views.show_news),
			path('news/<int:news_id>/',views.show_one_news,  name='one_news'),
]












if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#f