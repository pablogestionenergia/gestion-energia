# Generador de la web de Gestión Energía

Las páginas HTML de la web se generan desde estos archivos. No edites a mano los `index.html`: edita aquí y regenera.

- `engine.py`: plantilla común, datos de contacto, dominio (`BASE`) y clave del formulario (`WEB3FORMS_KEY`).
- `content_es.py`, `content_ca.py`, `content_en.py`: páginas en cada idioma.
- `guias_es.py`: guías (blog). Para añadir una guía, añade un elemento a `GUIAS`.
- `base.css` + `extra.css`: estilos (se combinan en `site.css`).

Regenerar: `python3 _generador/build.py` desde la raíz del repositorio.

Cambio a dominio propio: cambia `BASE` en `engine.py`, regenera y añade el archivo `CNAME`.

La carpeta empieza por `_` para que GitHub Pages no la publique.
