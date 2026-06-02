from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.urls import reverse


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "",
        f"Sitemap: {request.scheme}://{request.get_host()}/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def sitemap_xml(request):
    base = f"{request.scheme}://{request.get_host()}"
    urls_data = [
        {"loc": base + "/", "priority": "1.0", "changefreq": "weekly"},
        {"loc": base + "/about/", "priority": "0.9", "changefreq": "monthly"},
        {"loc": base + "/teachers/", "priority": "0.8", "changefreq": "monthly"},
        {"loc": base + "/headmasters/", "priority": "0.8", "changefreq": "monthly"},
        {"loc": base + "/notices/", "priority": "0.9", "changefreq": "weekly"},
        {"loc": base + "/clubs/", "priority": "0.7", "changefreq": "monthly"},
        {"loc": base + "/alumni/", "priority": "0.7", "changefreq": "monthly"},
        {"loc": base + "/achievements/", "priority": "0.8", "changefreq": "monthly"},
        {"loc": base + "/contact/", "priority": "0.6", "changefreq": "yearly"},
        {"loc": base + "/developer/", "priority": "0.4", "changefreq": "yearly"},
    ]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for u in urls_data:
        xml += "  <url>\n"
        xml += f"    <loc>{u['loc']}</loc>\n"
        xml += f"    <priority>{u['priority']}</priority>\n"
        xml += f"    <changefreq>{u['changefreq']}</changefreq>\n"
        xml += "  </url>\n"
    xml += "</urlset>"
    return HttpResponse(xml, content_type="application/xml")


urlpatterns = [
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap_xml),
    path('admin/', admin.site.urls),
    path('', include('school.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
