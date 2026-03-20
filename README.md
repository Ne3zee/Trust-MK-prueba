# TrustMarket Web Redesign (Django)

Sitio corporativo y módulo de postulación para reclutamiento de ejecutivos de call center.

## Módulos implementados

- **Landing moderna y responsive** con secciones:
  - Inicio
  - Servicios
  - Sobre Nosotros
  - Contacto
- **Sección Trabaja con Nosotros** con formulario de postulación.
- **Persistencia de postulaciones** con modelo `Application`.
- **Notificación automática** por correo (backend de consola para desarrollo).
- **Administración** de postulantes en Django Admin.

## Campos capturados

- Nombre completo
- Teléfono / WhatsApp
- Email
- Edad
- Experiencia en ventas
- Disponibilidad
- Comentarios adicionales

## URLs

- `/` → Home principal
- `/trabaja-con-nosotros/` → Formulario de postulación
- `/admin/` → Administración Django

## Ejecución local

1. Crear entorno virtual e instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Aplicar migraciones:
   ```bash
   python manage.py migrate
   ```
3. Iniciar servidor:
   ```bash
   python manage.py runserver
   ```
