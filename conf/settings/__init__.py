from split_settings.tools import include

settings = [
    "django.py",  # standard django settings
    "database.py",  # postgres
    "rest_framework.py",  # rest-framework settings
    "swagger.py",  # swagger settings
    "corsheaders.py",  # corsheaders settings
    "smtp.py",  # swagger settings
]

# Include settings:
include(*settings)
