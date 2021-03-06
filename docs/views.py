"""
docs/views.py
"""

import os

from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.contrib.auth.decorators import permission_required, login_required


@permission_required('User.is_mkdocs')
@login_required
def serve_docs(request, path=''):
    docs_path = os.path.join(settings.DOCS_DIR, path)

    if os.path.isdir(docs_path):
        path = os.path.join(path, 'index.html')

    path = os.path.join(settings.DOCS_STATIC_NAMESPACE, path)

    return serve(request, path, insecure=True)
