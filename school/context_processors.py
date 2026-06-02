from .models import SchoolInfo, DeveloperInfo


def school_info(request):
    info = SchoolInfo.objects.first()
    return {'school_info': info, 'developer_info': DeveloperInfo.objects.filter(is_active=True).first()}
