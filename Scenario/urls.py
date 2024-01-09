from django.contrib import admin
from django.urls import path, include
from mainapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login_view),
    path('logout/', logoutView),
    path('prompts/', list_of_scenario),
    path('profile/', profile),
    path('get-answers/', GetAnswersView.as_view(), name='get_answers'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwNDc5MTg3NiwiaWF0IjoxNzA0NzA1NDc2LCJqdGkiOiIzZjQ5OGM5YTRkMWY0ZmFkYTI1MmRjMzc2YTA5OWM2NiIsInVzZXJfaWQiOjF9.m45dbvhBEPQC1MpMiFMoq6bYLSze6Y5WTrPDFccHa7k",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA0NzA1Nzc2LCJpYXQiOjE3MDQ3MDU0NzYsImp0aSI6IjBiMTVlMzUxNGU2NDRiOGE4ZTdiZWI1YTFkYWVmZGM0IiwidXNlcl9pZCI6MX0.2ZeXi05lK8B1avw7lFXCwFllBAOLuuEgGADN7bKhjqE"
}
"""