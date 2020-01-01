from django.conf import settings


def global_settings(request):
    # return any necessary values
    return {
        'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
        'DARKSKY_SECRET': settings.DARKSKY_SECRET
    }