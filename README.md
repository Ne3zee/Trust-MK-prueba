# TrustMarket Web Redesign (Django)

Rediseño corporativo moderno para TrustMarket y módulo de postulación integrado para reclutamiento de ejecutivos de call center.

## Flujo visual implementado

- Header sticky con navegación principal y CTA "Trabaja con Nosotros".
- Hero con propuesta de valor de Contact Center & BPO.
- Sección de Servicios con 4 cards (IVR, Mail Marketing, Contact Center, Bots).
- Banner de decisión para contacto con agente humano.
- Sección Quiénes Somos en layout de dos columnas.
- Sección de Contacto con mapa y formulario comercial.
- Footer corporativo con enlaces, redes y texto legal.

## Módulo de Postulación

- Sección dedicada "Únete a nuestro Equipo de Ventas".
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

## URLs

- `/` → Home principal
- `/trabaja-con-nosotros/` → Formulario de postulación
- `/admin/` → Administración Django

## Ejecución local

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
