"""
Base Django settings for sandbox

WARNING: Keep file "docs/dummy_settings.py" synchronized with this one.
"""
import os


BASE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..",
)
DATA_DIR = os.path.join(BASE_DIR, "..", "data")


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SECRET'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sandbox.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'sandbox.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Database

DATABASES = {
    # Development default database engine use sqlite3
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, 'db', 'db.sqlite3'),
    }
}
MIGRATION_MODULES = {}


# Internationalization

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'



"""
NOTE:
    * Every things above comes from default generated settings file (from Django startproject);
    * Every things below are needed settings for sandbox applications;
    * Don't edit default generated settings, instead override them below;
"""
SITE_ID = 1

INSTALLED_APPS = INSTALLED_APPS + [
    'icomoon',
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Use the Django admin login form for demo
LOGIN_URL = '/admin/login/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = os.path.join(DATA_DIR, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = os.path.join(DATA_DIR, "static")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

# Add sandbox template directory
TEMPLATES[0]['DIRS'] = (os.path.join(BASE_DIR, "templates"),)
