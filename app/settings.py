from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_URLCONF = 'learning_manager.urls'

WSGI_APPLICATION = 'learning_manager.wsgi.application'
