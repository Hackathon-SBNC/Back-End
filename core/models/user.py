"""
Database models.
"""

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    """Manager for users."""

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("Users must have an email address.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create, save and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# class Professor(AbstractBaseUser, PermissionsMixin):
#     """Professor model in the system."""
#     email = models.EmailField(
#         max_length=255,
#         unique=True,
#         verbose_name=_("email"),
#         help_text=_("Email")
#     )
#     name = models.CharField(
#         max_length=255,
#         blank=True,
#         null=True,
#         verbose_name=_("name"),
#         help_text=_("Username")
#     )
#     siap = models.CharField(
#         max_length=7,
#         unique=True,
#         verbose_name=_("SIAP"),
#         help_text=_("Sistema de Informações da Administração Pública")
#     )
#     is_active = models.BooleanField(
#         default=True,
#         verbose_name=_("Professor está ativo"),
#         help_text=_("Indica que este professor está ativo.")
#     )
#     is_staff = models.BooleanField(
#         default=False,
#         verbose_name=_("Professor é da equipe"),
#         help_text=_("Indica que este professor pode acessar o Admin.")
#     )

#     objects = UserManager()

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []

#     class Meta:
#         """Meta options for the model."""

#         verbose_name = "Professor"
#         verbose_name_plural = "Professores"
    

class User(AbstractBaseUser, PermissionsMixin):
    """User model in the system."""
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name=_("email"),
        help_text=_("Email")
        )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("name"),
        help_text=_("Username")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Usuário está ativo"),
        help_text=_("Indica que este usuário está ativo.")
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("Usuário é da equipe"),
        help_text=_("Indica que este usuário pode acessar o Admin.")
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        """Meta options for the model."""

        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
