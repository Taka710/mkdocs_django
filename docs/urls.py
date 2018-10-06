"""
docs/urls.py
"""

from django.urls import path
from .views import serve_docs

urlpatterns = [
    path('<path:path>', serve_docs),
    path('', serve_docs),
]
