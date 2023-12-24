from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

from AppCoder.views import (
    cursos_view,
    cursos_buscar_view,
    cursos_todos_view,
    inicio_view,
    profesores_view,
    profesores_crud_delete_view,
    profesores_crud_read_view,
    profesores_crud_update_view,
    profesor_view,
    CursoCreateView,
    CursoDetail,
    CursoDeleteView,
    CursoListView,
    CursoUpdateView,
    login_view,
    registro_view,
    editar_perfil_view,
    crear_avatar_view,
    mostrar_profile_view,
    )


app_name = "AppCoder"

urlpatterns = [
    path("cursos/", cursos_view, name="cursos"),
    path("cursos/todos", cursos_todos_view, name="cursos-todos"),
    path("cursos/buscar", cursos_buscar_view, name="cursos-buscar"),
    path("comisiones/", profesores_view),
    path("inicio/", inicio_view, name="inicio"),
    path("nosotros/", views.nosotros, name="nosotros"),
    path("profesores/", profesor_view),
    path("profesores-lista/", profesores_crud_read_view),
    path("profesores-eliminar/<profesor_email>/", profesores_crud_delete_view),
    path("profesores-editar/<profesor_email>/", profesores_crud_update_view),
    path("curso/list", CursoListView.as_view(), name="curso-list"),
    path("curso/new", CursoCreateView.as_view(), name="curso-create"),
    path("curso/<pk>", CursoDetail.as_view(), name="curso-detail"),
    path("curso/<pk>/update", CursoUpdateView.as_view(), name="curso-update"),
    path("curso/<pk>/delete", CursoDeleteView.as_view(), name="curso-delete"),
    path("registro", registro_view, name="registro"),
    path("login", login_view, name="login"),
    path("logout", LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),
    path("editar-perfil", editar_perfil_view, name="editar-perfil"),
    path("crear-avatar", crear_avatar_view, name="crear-avatar"),
    path("profile/<user_id>", mostrar_profile_view, name="profile"),
]
