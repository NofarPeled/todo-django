from django.contrib import admin
from django.urls import include,path
from todo.urls import todo_router
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todo/', include(todo_router.urls)),
    path('api/auth/', include('user.urls')),
    path('', TemplateView.as_view(template_name = 'index.html'))
]

