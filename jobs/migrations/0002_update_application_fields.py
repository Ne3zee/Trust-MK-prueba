from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="sales_experience",
            field=models.CharField(
                choices=[
                    ("sin_experiencia", "No"),
                    ("menos_1", "< 1 año"),
                    ("1_3", "1-3 años"),
                    ("mas_3", "+3 años"),
                ],
                max_length=20,
                verbose_name="Experiencia en ventas",
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="availability",
            field=models.TextField(verbose_name="Disponibilidad"),
        ),
    ]
