from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name="snippet-add"),
    path('langs/add', views.add_lang, name="lang-add"),
    path('snippets/list', views.snippets_page, name="snippet-list"),
    path('snippets/my', views.snippets_my, name="snippet-my"),
    path('snippet/<int:snippet_id>', views.snippet_detail, name="snippet-detail"),
    path('snippet/<int:snippet_id>/delete', views.snippet_delete, name="snippet-delete"),
    path('comment/add', views.add_comment, name="comment-add"),
    path('registration/', views.register, name='registration'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
