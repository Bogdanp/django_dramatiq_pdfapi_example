from django.conf import settings
from django.db import models


class PDF(models.Model):
    STATUS_PENDING = "pending"
    STATUS_FAILED = "failed"
    STATUS_DONE = "done"
    STATUSES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_FAILED, "Failed"),
        (STATUS_DONE, "Done"),
    ]

    source_url = models.CharField(max_length=512)
    status = models.CharField(
        max_length=10,
        default=STATUS_PENDING,
        choices=STATUSES,
    )

    @property
    def filename(self):
        return f"{settings.MEDIA_ROOT}{self.pk}.pdf"

    @property
    def pdf_url(self):
        return f"{settings.MEDIA_URL}{self.pk}.pdf"
