# PLEIA

> Premium Technology E-commerce desarrollado con Django.

PLEIA es un proyecto de e-commerce desarrollado como proyecto final de la certificación **Full Stack con Django**. La aplicación integra autenticación de usuarios, catálogo de productos, carrito de compras, proceso de checkout y un panel de administración para la gestión de productos.

Además del desarrollo técnico, el proyecto incorpora una identidad de marca propia, un Design System y una arquitectura frontend documentada, con el objetivo de construir una experiencia consistente y escalable.

---

# Características

## Backend

- Autenticación de usuarios.
- Gestión de roles (Administrador / Cliente).
- Catálogo de productos conectado a la base de datos.
- CRUD de productos desde el panel de administración.
- Carrito de compras.
- Actualización de cantidades.
- Eliminación de productos del carrito.
- Generación de órdenes de compra.
- Persistencia mediante ORM de Django.

## Frontend

- Diseño responsive.
- Página Home completamente implementada.
- Sistema de componentes reutilizables.
- Navegación clara.
- Arquitectura modular.
- Branding e identidad visual propios.

---

# Tecnologías utilizadas

## Backend

- Python
- Django
- Django ORM
- SQLite

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Herramientas

- Git
- GitHub
- Figma
- Visual Studio Code

---

# Estado del proyecto

PLEIA se encuentra actualmente en una etapa de desarrollo activo.

El **desarrollo del backend se encuentra completamente implementado**, cumpliendo con los requisitos funcionales del proyecto, incluyendo autenticación de usuarios, gestión de productos, carrito de compras y flujo de compra.

En cuanto al frontend, se desarrolló una primera implementación funcional de la página de inicio (**Home**) como muestra del lenguaje visual y la experiencia de usuario propuesta para el proyecto.

De forma complementaria, se creó una identidad de marca completa para PLEIA, incluyendo un **Brand Book**, un **Design System** y una **Frontend Architecture Guide**, con el objetivo de proporcionar una base visual sólida y escalable.

Si bien el desarrollo técnico del frontend continúa en construcción, la experiencia completa del e-commerce ya fue diseñada mediante mockups de alta fidelidad para Desktop, Tablet y Mobile.

---

# Instalación

1. Clona este repositorio.

```bash
git clone https://github.com/TU-USUARIO/TU-REPOSITORIO.git
```

2. Accede a la carpeta del proyecto.

```bash
cd TU-REPOSITORIO
```

3. Crea y activa un entorno virtual.

4. Instala las dependencias necesarias para ejecutar el proyecto.

5. Ejecuta las migraciones.

```bash
python manage.py migrate
```

6. Inicia el servidor de desarrollo.

```bash
python manage.py runserver
```

La aplicación estará disponible en:

```
http://127.0.0.1:8000/
```

---

# Rutas principales

| Ruta | Descripción |
|------|-------------|
| `/` | Home |
| `/catalogo` | Catálogo |
| `/producto/<id>` | Detalle del producto |
| `/carrito` | Carrito |
| `/checkout` | Checkout |
| `/login` | Inicio de sesión |
| `/admin` | Panel de administración |

---

# Credenciales de prueba

## Administrador

Correo

```
admin@example.com
```

Contraseña

```
********
```

## Cliente

Correo

```
cliente@example.com
```

Contraseña

```
********
```

---

# Arquitectura del proyecto

```
PLEIA/

ecommerce/
tienda/
usuarios/
carrito/
pedidos/

static/
templates/
media/

manage.py
README.md
db.sqlite3
```

---

# Documentación del proyecto

Además del código fuente, el proyecto cuenta con documentación de diseño y planificación desarrollada durante el proceso de construcción.

## Brand Book

Describe la identidad visual y conceptual de la marca PLEIA.

https://drive.google.com/file/d/1XTmG5auvQSZWNDcdqYG78QEPU3_LwcD5/view?usp=sharing

---

## Design System

Define los componentes visuales reutilizables, colores, tipografía y reglas de diseño utilizadas durante el desarrollo.

https://drive.google.com/file/d/1gECuuAaQxdlQB_iLEaofCb6RYjviNB-b/view?usp=sharing

---

## Frontend Architecture Guide

Documenta la estructura del frontend, organización de componentes y principios de desarrollo.

https://drive.google.com/file/d/1cK9YNxWp6bM7nlvYtF9a7s67lPUigVwd/view?usp=sharing

---

# Mockups

La experiencia completa del e-commerce fue diseñada previamente mediante mockups de alta fidelidad para Desktop, Tablet y Mobile.

Incluye las siguientes vistas:

- Home
- Catálogo
- Detalle del producto
- Carrito
- Login
- Checkout

Los mockups representan la propuesta completa de la experiencia de usuario y sirven como guía para la implementación del frontend actualmente en desarrollo.

---

# Portfolio

Puedes revisar este y otros proyectos en mi portafolio:

https://agnusalfa.github.io/joao-belvedere/portfolio.html

---

# Próximas mejoras

- Continuar el desarrollo del frontend según los mockups definidos.
- Integración con pasarela de pago.
- Sistema de favoritos.
- Búsqueda avanzada.
- Filtros dinámicos.
- Optimización SEO.
- Despliegue en producción.
- Pruebas automatizadas.

---

# Autor

**Joao Paulo Pérez Huerta**  
*(AKA Joao Belvedere)*

Proyecto desarrollado como entrega final de la **Certificación Full Stack con Django**.

© 2025

