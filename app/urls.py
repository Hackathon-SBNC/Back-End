from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework.routers import DefaultRouter

from core.views import UserViewSet, CursoViewSet, ObservacaoViewSet, NotaViewSet, TurmaViewSet, DisciplinaViewSet, AlunoViewSet, TrimestreViewSet, OcorrenciaViewSet, ResponsavelViewSet, ProfessorViewSet


router = DefaultRouter()

router.register(r"usuarios", UserViewSet, basename="usuarios")
router.register(r"alunos", AlunoViewSet, basename="alunos")
router.register(r"cursos", CursoViewSet, basename="cursos")
router.register(r"disciplinas", DisciplinaViewSet, basename="disciplinas")
router.register(r"notas", NotaViewSet, basename="notas")
router.register(r"observacoes", ObservacaoViewSet, basename="observacoes")
router.register(r"ocorrencias", OcorrenciaViewSet, basename="ocorrencias")
router.register(r"responsaveis", ResponsavelViewSet, basename="responsaveis")
router.register(r"trimestres", TrimestreViewSet, basename="trimestres")
router.register(r"turmas", TurmaViewSet, basename="turmas")
router.register(r"professores", ProfessorViewSet, basename="professores")

urlpatterns = [
    path("admin/", admin.site.urls),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    # API
    path("api/", include(router.urls)),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
