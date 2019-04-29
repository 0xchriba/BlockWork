from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
import profiles.urls
import accounts.urls
from . import views
from . import modelo
from django.views.static import serve


# Personalized admin site settings like title and header
admin.site.site_title = "Blockwork Site Admin"
admin.site.site_header = "Blockwork Administration"

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("about/", views.AboutPage.as_view(), name="about"),
    path("users/", include(profiles.urls)),
    path("admin/", admin.site.urls),
    path("new-project/", views.NewProjectPage.as_view(), name="new-project"),
    path("new-project/result/", views.NewProjectPage.as_view(), name="new-project-result"),
    path("find-freelancer/", views.FindFreelancerPage.as_view(), name="find-freelancer"),
    path("find-freelancer/result/", views.FindFreelancerPage.as_view(), name="find-freelancer"),
    path("project-status/", views.ProjectStatusPage, name="project-status"),
    path("project-history/", views.ProjectHistoryPage, name="project-history"),
    path("submit-code/", views.SubmitCodePage, name="submit-code"),
    path("code-result/", views.CodeResultPage, name="code-result"),
    path("finish-project/", views.FinishProjectPage.as_view(), name="finish-project"),
    path("my-project/", views.MyProjectPage, name="my-project"),
    path("free-portal/", views.FreePortalPage.as_view(), name="free-portal"),
    path("", include(accounts.urls)),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
