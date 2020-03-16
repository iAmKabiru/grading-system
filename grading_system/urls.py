from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('grading.urls'))
]

admin.site.site_header = 'Grading System'
admin.site.site_title = 'Grading System'