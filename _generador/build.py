import os, shutil, sys, base64, re
sys.path.insert(0, os.path.dirname(__file__))
import engine
from engine import PAGES, BASE, render, find, LANGS, HREFLANG, TODAY
import content_es, guias_es, content_ca, content_en  # registran las páginas

# Uso: python3 _generador/build.py   (desde la raíz del repositorio)
# Regenera las páginas HTML, site.css, sitemap.xml, robots.txt y 404.html en la raíz.
# Las imágenes y fuentes ya están en la raíz y no se tocan.
OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

here = os.path.dirname(os.path.abspath(__file__))
css = open(f"{here}/base.css").read() + open(f"{here}/extra.css").read()
open(f"{OUT}/site.css", "w").write("/* Gestión Energía — estilos comunes (generado por build.py) */\n" + css)

paths = set()
for p in PAGES:
    assert p["path"] not in paths, p["path"]; paths.add(p["path"])
    d = os.path.join(OUT, p["path"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w").write(render(p))

# sitemap con alternativas de idioma
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
for p in PAGES:
    if p["noindex"]: continue
    sm.append(f'  <url><loc>{BASE + p["path"]}</loc><lastmod>{TODAY}</lastmod>')
    alts = [(l, find(p["group"], l)) for l in LANGS]
    alts = [(l, a) for l, a in alts if a]
    if len(alts) > 1:
        for l, a in alts:
            sm.append(f'    <xhtml:link rel="alternate" hreflang="{HREFLANG[l]}" href="{BASE + a["path"]}"/>')
    sm.append('  </url>')
sm.append('</urlset>')
open(f"{OUT}/sitemap.xml", "w").write("\n".join(sm) + "\n")
open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n")

# 404 (GitHub Pages lo sirve en cualquier ruta: enlaces absolutos)
p404 = dict(lang="es", group="404", path="", noindex=True, title="Página no encontrada | Gestión Energía",
            desc="La página que buscas no existe.", faq=None, article=None,
            body=engine.page_hero("es", "Esta página <span>no existe</span>", "Puede que el enlace haya cambiado. Vuelve al inicio o escríbenos.",
                 ctas=f'<div class="hero-ctas"><a class="btn btn-oro" href="{BASE}">Ir al inicio</a><a class="btn btn-linea" href="{BASE}contacto/">Contacto</a></div>'))
html404 = render(p404).replace('href="@@home@@"', f'href="{BASE}"')
html404 = re.sub(r'(href|src)="(?!https?:|mailto:|tel:|#|data:)([^"]*)"', lambda m: f'{m.group(1)}="{BASE}{m.group(2)}"', html404)
html404 = html404.replace(f'<link rel="canonical" href="{BASE}">\n', "")
open(f"{OUT}/404.html", "w").write(html404)
print(len(PAGES), "páginas generadas")
