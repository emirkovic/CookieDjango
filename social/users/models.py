import logging

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

logger = logging.getLogger(__name__)


class PageModel(models.Model):
    def __str__(self):
        return f"PageModel id={self.id}"

    def get_url(self, language):
        urls = self.urls.filter(language=language)
        if urls.exists():
            if urls.count() > 1:
                logger.warning(
                    "Multiple URLs found for language %s: %s",
                    language,
                    list(urls.values("id", "url")),
                )
            return urls.first()  # Consistently return the first URL
        return None


class PageUrl(models.Model):
    page = models.ForeignKey(
        PageModel,
        on_delete=models.CASCADE,
        related_name="urls",
    )
    language = models.CharField(max_length=10)
    url = models.CharField(max_length=255)

    class Meta:
        unique_together = ("page", "language")
        indexes = [models.Index(fields=["language"])]

    def __str__(self):
        return f"Page URL for {self.language}: {self.url}"


class User(AbstractUser):
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # Disable first_name field
    last_name = None  # Disable last_name field

    def __str__(self):
        return self.name or self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
