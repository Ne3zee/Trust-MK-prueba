from django.db import models


class Application(models.Model):
    EXPERIENCE_CHOICES = [
        ("sin_experiencia", "No"),
        ("menos_1", "< 1 año"),
        ("1_3", "1-3 años"),
        ("mas_3", "+3 años"),
    ]

    full_name = models.CharField("Nombre completo", max_length=160)
    phone = models.CharField("Teléfono / WhatsApp", max_length=30)
    email = models.EmailField("Correo electrónico")
    age = models.PositiveSmallIntegerField("Edad")
    sales_experience = models.CharField(
        "Experiencia en ventas", max_length=20, choices=EXPERIENCE_CHOICES
    )
    availability = models.TextField("Disponibilidad")
    additional_comments = models.TextField("Comentarios adicionales", blank=True)
    created_at = models.DateTimeField("Fecha de postulación", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Postulación"
        verbose_name_plural = "Postulaciones"

    def __str__(self) -> str:
        return f"{self.full_name} - {self.created_at:%d/%m/%Y}"
