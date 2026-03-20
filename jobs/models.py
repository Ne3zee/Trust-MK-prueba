from django.db import models


class Application(models.Model):
    AVAILABILITY_CHOICES = [
        ("inmediata", "Inmediata"),
        ("2_semanas", "En 2 semanas"),
        ("1_mes", "En 1 mes"),
        ("otro", "Otro"),
    ]

    full_name = models.CharField("Nombre completo", max_length=160)
    phone = models.CharField("Teléfono / WhatsApp", max_length=30)
    email = models.EmailField("Correo electrónico")
    age = models.PositiveSmallIntegerField("Edad")
    sales_experience = models.TextField("Experiencia en ventas")
    availability = models.CharField(
        "Disponibilidad", max_length=20, choices=AVAILABILITY_CHOICES
    )
    additional_comments = models.TextField("Comentarios adicionales", blank=True)
    created_at = models.DateTimeField("Fecha de postulación", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Postulación"
        verbose_name_plural = "Postulaciones"

    def __str__(self) -> str:
        return f"{self.full_name} - {self.created_at:%d/%m/%Y}"
