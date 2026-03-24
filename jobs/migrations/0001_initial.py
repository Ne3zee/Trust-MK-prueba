from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=160, verbose_name='Nombre completo')),
                ('phone', models.CharField(max_length=30, verbose_name='Teléfono / WhatsApp')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Edad')),
                ('sales_experience', models.TextField(verbose_name='Experiencia en ventas')),
                ('availability', models.CharField(choices=[('inmediata', 'Inmediata'), ('2_semanas', 'En 2 semanas'), ('1_mes', 'En 1 mes'), ('otro', 'Otro')], max_length=20, verbose_name='Disponibilidad')),
                ('additional_comments', models.TextField(blank=True, verbose_name='Comentarios adicionales')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de postulación')),
            ],
            options={
                'verbose_name': 'Postulación',
                'verbose_name_plural': 'Postulaciones',
                'ordering': ['-created_at'],
            },
        ),
    ]
