from conf.settings.django import env

EMAIL_HOST = env("EMAIL_HOST", cast=str)
EMAIL_PORT = env("EMAIL_PORT", cast=int)
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
SERVER_EMAIL = env("EMAIL_ADDRESS", cast=str)
DEFAULT_FROM_EMAIL = env("EMAIL_ADDRESS", cast=str)
EMAIL_HOST_USER = env("EMAIL_ADDRESS", cast=str)
EMAIL_HOST_PASSWORD = env("EMAIL_ADDRESS_PASSWORD", cast=str)

ADMIN_EMAIL_ADDRESS = env("ADMIN_EMAIL_ADDRESS", cast=str)