from .models import SchoolInfo


def school_info(request):
    info = SchoolInfo.objects.first()
    return {'school_info': info}
