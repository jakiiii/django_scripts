from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class GenerateDocuments(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    product = models.CharField(
        max_length=100
    )
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.product

    class Meta:
        ordering = ('-created_at',)
        verbose_name = "Generate Document"
        verbose_name_plural = "Generate Documents"
        db_table = "generate_documents"

