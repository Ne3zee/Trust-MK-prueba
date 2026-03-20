# TrustMarket Web Redesign (Django)

Rediseño corporativo moderno para TrustMarket y módulo de postulación integrado para reclutamiento de ejecutivos de call center.

## Flujo visual implementado

- Header sticky con branding TrustMarket (paleta azul/cian + verde CTA).
- Hero principal en Inicio.
- Landing independiente para cada opción del menú:
  - Inicio (`/`)
  - Servicios (`/servicios/`)
  - Quiénes Somos (`/quienes-somos/`)
  - Contacto (`/contacto/`)
- Footer corporativo con navegación rápida.

## Módulo de Postulación

- URL dedicada: `/trabaja-con-nosotros/`
- Stepper visual: "Tus Datos" → "Experiencia" → "Disponibilidad".
- Validaciones de campos obligatorios y edad mínima.
- Guardado en base de datos (`Application`).
- Notificación automática por correo (backend consola en desarrollo).
- Gestión de postulantes en Django Admin.

## Campos capturados

- Nombre completo
- Teléfono / WhatsApp
- Email
- Edad
- Experiencia en ventas (No, <1 año, 1-3 años, +3 años)
- Disponibilidad (Mañana, Tarde, Noche, Fines de semana)
- Comentarios adicionales

## Ejecución local

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
