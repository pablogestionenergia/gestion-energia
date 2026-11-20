"""Generador de la web multipágina de Gestión Energía.
Cambiar de dominio = cambiar BASE y volver a ejecutar build.py."""
import json, os, re, html

BASE = "https://pablogestionenergia.github.io/gestion-energia/"
PHONE = "34604822007"
PHONE_TXT = "604 822 007"
EMAIL = "pablo.gestionenergia@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/pablo-massera-742a80319/"
INSTAGRAM = "https://www.instagram.com/gestionenergia/"
# Estadísticas sin cookies (GoatCounter). Crea una cuenta gratis en https://www.goatcounter.com,
# pon aquí el código elegido (por ejemplo "gestionenergia") y regenera. Vacío = sin estadísticas.
GOATCOUNTER = "gestionenergia"
# Clave de Web3Forms (se pide gratis en https://web3forms.com con el email de arriba)
WEB3FORMS_KEY = "0ca97bbb-d14f-40f3-90f5-8e3803a09660"
TODAY = "2026-11-20"

PAGES = []

def page(**kw):
    kw.setdefault("faq", None)
    kw.setdefault("article", None)
    kw.setdefault("noindex", False)
    PAGES.append(kw)

def find(group, lang):
    for p in PAGES:
        if p["group"] == group and p["lang"] == lang:
            return p
    return None

def esc(s):
    return html.escape(s, quote=True)

# ---------- iconos ----------
WA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.008-.57-.008-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.870 9.870 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.860 9.860 0 01-1.510-5.260c.001-5.450 4.436-9.884 9.888-9.884 2.640 0 5.122 1.030 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.450-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.050 0C5.495 0 .160 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.890-5.335 11.893-11.893a11.821 11.821 0 00-3.480-8.413Z"/></svg>'
TEL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 0 0-1.01.24l-2.2 2.2a15.161 15.161 0 0 1-6.59-6.59l2.2-2.21a.96.96 0 0 0 .25-1.01A11.36 11.36 0 0 1 8.5 4c0-.55-.45-1-1-1H4c-.55 0-1 .45-1 1c0 9.39 7.61 17 17 17c.55 0 1-.45 1-1v-3.5c0-.55-.45-1-1-1z"/></svg>'
MAIL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5l-8-5V6l8 5l8-5v2z"/></svg>'
LI = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.640-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.13 2.06 2.06 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>'
IG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41a3.7 3.7 0 0 1-1.38-.9 3.7 3.7 0 0 1-.9-1.38c-.16-.42-.36-1.06-.41-2.23C2.17 15.58 2.16 15.2 2.16 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.17 8.8 2.16 12 2.16M12 0C8.74 0 8.33.01 7.05.07 5.78.13 4.9.33 4.14.63a5.88 5.88 0 0 0-2.13 1.38A5.88 5.88 0 0 0 .63 4.14C.33 4.9.13 5.78.07 7.05.01 8.33 0 8.74 0 12s.01 3.67.07 4.95c.06 1.27.26 2.15.56 2.91.31.79.72 1.46 1.38 2.13a5.88 5.88 0 0 0 2.13 1.38c.76.3 1.64.5 2.91.56C8.33 23.99 8.74 24 12 24s3.67-.01 4.95-.07c1.27-.06 2.15-.26 2.91-.56a5.88 5.88 0 0 0 2.13-1.38 5.88 5.88 0 0 0 1.38-2.13c.3-.76.5-1.64.56-2.91.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.06-1.27-.26-2.15-.56-2.91a5.88 5.88 0 0 0-1.38-2.13A5.88 5.88 0 0 0 19.86.63C19.1.33 18.22.13 16.95.07 15.67.01 15.26 0 12 0zm0 5.84a6.16 6.16 0 1 0 0 12.32 6.16 6.16 0 0 0 0-12.32zM12 16a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.41-11.85a1.44 1.44 0 1 0 0 2.88 1.44 1.44 0 0 0 0-2.88z"/></svg>'
I_EURO = '<svg class="icon-gold" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
I_CLOCK = '<svg class="icon-gold" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14" stroke-linecap="round" stroke-linejoin="round"/></svg>'
I_SHIELD = '<svg class="icon-gold" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke-linecap="round" stroke-linejoin="round"/></svg>'
I_HOUSE = '<svg class="icon-gold" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 10.5 12 3l9 7.5V21H3z" stroke-linejoin="round"/><path d="M9 21v-6h6v6" stroke-linejoin="round"/></svg>'
I_BUILD = '<svg class="icon-gold" viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="2" width="16" height="20" rx="1"/><path d="M9 6h1M14 6h1M9 10h1M14 10h1M9 14h1M14 14h1M10 22v-4h4v4" stroke-linecap="round"/></svg>'
I_GLOBE = '<svg class="icon-gold" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg>'
MENU_ICON = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" stroke-linecap="round"/></svg>'

# ---------- textos comunes por idioma ----------
T = {
 "es": dict(
   name="ES", full="Castellano", skip="Saltar al contenido", tag="Consultoría y gestión de<br>servicios energéticos",
   newtab=" (se abre en una pestaña nueva)", menu="Menú", home_label="Gestión Energía, inicio",
   nav=[("home","Inicio"),("agencias","Inmobiliarias"),("admin","Administradores de fincas"),("modelos","Modelos"),("guias","Guías"),("sobre","Sobre mí"),("contacto","Contacto")],
   wa_msg="Hola Pablo, me interesa colaborar con Gestión Energía.",
   logos="Operamos con las principales comercializadoras del mercado", logos_more="…y muchas más",
   clients_eyebrow="Confían en nosotros", clients_title="Nuestros clientes",
   cta_title="¿Hablamos de negocios?", cta_lead="Estudio tu cartera de clientes y te presento una propuesta personalizada.",
   cta_form="Escríbeme desde el formulario", wa_btn="WhatsApp", call="Llamar al",
   footer="Consultoría y gestión de servicios energéticos", legal="Aviso legal", privacy="Privacidad",
   langs_label="Idioma", crumbs_home="Inicio",
 ),
 "ca": dict(
   name="CA", full="Català", skip="Salta al contingut", tag="Consultoria i gestió de<br>serveis energètics",
   newtab=" (s'obre en una pestanya nova)", menu="Menú", home_label="Gestión Energía, inici",
   nav=[("home","Inici"),("agencias","Immobiliàries"),("admin","Administradors de finques"),("modelos","Models"),("guias","Guies"),("sobre","Sobre mi"),("contacto","Contacte")],
   wa_msg="Hola Pablo, m'interessa col·laborar amb Gestión Energía.",
   logos="Treballem amb les principals comercialitzadores del mercat", logos_more="…i moltes més",
   clients_eyebrow="Confien en nosaltres", clients_title="Els nostres clients",
   cta_title="Parlem de negocis?", cta_lead="Estudio la teva cartera de clients i et presento una proposta personalitzada.",
   cta_form="Escriu-me des del formulari", wa_btn="WhatsApp", call="Truca al",
   footer="Consultoria i gestió de serveis energètics", legal="Avís legal", privacy="Privacitat",
   langs_label="Idioma", crumbs_home="Inici",
 ),
 "en": dict(
   name="EN", full="English", skip="Skip to content", tag="Energy services<br>consulting & management",
   newtab=" (opens in a new tab)", menu="Menu", home_label="Gestión Energía, home",
   nav=[("home","Home"),("agencias","Estate agencies"),("admin","Property managers"),("modelos","Partnership models"),("guias","Guides"),("sobre","About"),("contacto","Contact")],
   wa_msg="Hi Pablo, I'd like to talk about working with Gestión Energía.",
   logos="We work with Spain's leading energy suppliers", logos_more="…and many more",
   clients_eyebrow="They trust us", clients_title="Our clients",
   cta_title="Shall we talk business?", cta_lead="I'll review your client portfolio and send you a tailored proposal.",
   cta_form="Write to me using the form", wa_btn="WhatsApp", call="Call",
   footer="Energy services consulting & management", legal="Legal notice", privacy="Privacy",
   langs_label="Language", crumbs_home="Home",
 ),
}
LANGS = ["es", "ca", "en"]
HREFLANG = {"es": "es-ES", "ca": "ca-ES", "en": "en"}
OG_LOCALE = {"es": "es_ES", "ca": "ca_ES", "en": "en_GB"}

def wa(msg):
    from urllib.parse import quote
    return f"https://wa.me/{PHONE}?text={quote(msg)}"

# ---------- bloques reutilizables ----------
def logos_block(lang):
    t = T[lang]
    imgs = "".join(f'<li><img src="{{R}}{f}" alt="{a}" width="120" height="46"></li>' for f, a in
                   [("endesa.png","Endesa"),("naturgy.png","Naturgy"),("iberdrola.png","Iberdrola"),("repsol.png","Repsol"),("total.png","TotalEnergies")])
    return f'''<section class="logos"><div class="wrap">
<h2 class="logos-title">{t["logos"]}</h2>
<ul class="logos-grid">{imgs}</ul>
<p class="logos-more">{t["logos_more"]}</p>
</div></section>'''

def clients_block(lang):
    t = T[lang]
    return f'''<section class="section clientes"><div class="wrap center">
<div class="eyebrow">{t["clients_eyebrow"]}</div>
<h2 class="section-title">{t["clients_title"]}</h2>
<ul class="clients-grid">
<li class="client-card"><img src="{{R}}putxet.png" alt="Fincas Putxet" loading="lazy"></li>
<li class="client-card"><img src="{{R}}smart.png" alt="Smart Property Management" loading="lazy"></li>
<li class="client-card"><img src="{{R}}fincastema.png" alt="Fincas Tema" loading="lazy"></li>
</ul></div></section>'''

def cta_block(lang, msg=None):
    t = T[lang]
    nt = f'<span class="sr-only">{t["newtab"]}</span>'
    return f'''<section class="section contacto on-dark"><div class="wrap">
<h2 class="section-title">{t["cta_title"]}</h2>
<p class="section-lead">{t["cta_lead"]}</p>
<div class="contact-flex">
<a class="contact-item" href="@@contacto@@">{MAIL} {t["cta_form"]}</a>
<a class="contact-item" href="{wa(msg or t["wa_msg"])}" target="_blank" rel="noopener">{WA} {t["wa_btn"]} {PHONE_TXT}{nt}</a>
<a class="contact-item" href="tel:+{PHONE}">{TEL} {t["call"]} {PHONE_TXT}</a>
</div></div></section>'''

def faq_block(lang, items, title, eyebrow):
    det = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items)
    return f'''<section class="section faq-wrap"><div class="wrap">
<div class="center"><div class="eyebrow">{eyebrow}</div><h2 class="section-title">{title}</h2></div>
<div class="faq">{det}</div></div></section>'''

def page_hero(lang, h1, lead, crumbs=None, ctas=""):
    t = T[lang]
    cr = ""
    if crumbs:
        parts = [f'<a href="@@home@@">{t["crumbs_home"]}</a>'] + [
            (f'<a href="{href}">{lab}</a>' if href else f'<span aria-current="page">{lab}</span>') for lab, href in crumbs]
        cr = f'<nav class="crumbs" aria-label="Breadcrumb">{" › ".join(parts)}</nav>'
    return f'''<section class="page-hero on-dark"><div class="wrap">{cr}
<h1>{h1}</h1><p class="lead">{lead}</p>{ctas}</div></section>'''

# ---------- plantilla ----------
def org_jsonld():
    return {
        "@context": "https://schema.org", "@type": "ProfessionalService", "@id": BASE + "#empresa",
        "name": "Gestión Energía",
        "description": "Servicio B2B para inmobiliarias y administradores de fincas: altas, cambios de titular e incidencias de luz y gas, con comisión por cada alta.",
        "url": BASE, "logo": BASE + "logo.png", "image": BASE + "og-image.jpg",
        "telephone": "+" + PHONE, "email": EMAIL,
        "areaServed": {"@type": "Country", "name": "España"},
        "knowsLanguage": ["es", "ca", "en"],
        "serviceType": ["Alta de suministro de luz y gas", "Cambio de titular de luz y gas", "Gestión de incidencias de suministro"],
        "founder": {"@type": "Person", "name": "Pablo Massera", "jobTitle": "Fundador", "sameAs": [LINKEDIN]},
        "sameAs": [INSTAGRAM, LINKEDIN],
    }

def depth(path):
    return path.count("/")

def render(p):
    lang, t = p["lang"], T[p["lang"]]
    R = "../" * depth(p["path"])
    url = BASE + p["path"]
    nt = f'<span class="sr-only">{t["newtab"]}</span>'

    # alternativas de idioma
    alts = {l: find(p["group"], l) for l in LANGS}
    hreflang = ""
    if sum(1 for a in alts.values() if a) > 1:
        for l, a in alts.items():
            if a:
                hreflang += f'<link rel="alternate" hreflang="{HREFLANG[l]}" href="{BASE + a["path"]}">\n'
        if alts["es"]:
            hreflang += f'<link rel="alternate" hreflang="x-default" href="{BASE + alts["es"]["path"]}">\n'

    sw = ""
    for l in LANGS:
        target = alts[l] or find("home", l)
        cur = ' aria-current="true"' if l == lang else ""
        sw += f'<a href="{R}{target["path"]}" lang="{l}" hreflang="{l}"{cur} title="{T[l]["full"]}"><span aria-hidden="true">{T[l]["name"]}</span><span class="sr-only">{T[l]["full"]}</span></a>'

    navgroup = p.get("nav", p["group"])
    links = ""
    for g, lab in t["nav"]:
        if g == "home":
            continue
        tp = find(g, lang) or find(g, "es")
        cur = ' aria-current="page"' if g == navgroup else ""
        links += f'<a href="{R}{tp["path"]}"{cur}>{lab}</a>'

    gc_script = (f'<script data-goatcounter="https://{GOATCOUNTER}.goatcounter.com/count" async src="https://gc.zgo.at/count.js"></script>\n' if GOATCOUNTER else "")
    ld = [org_jsonld()]
    if p["faq"]:
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": re.sub("<[^>]+>", "", q), "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
            for q, a in p["faq"]]})
    if p["article"]:
        ld.append({"@context": "https://schema.org", "@type": "Article", "headline": p["article"]["headline"],
                   "description": p["desc"], "inLanguage": HREFLANG[lang], "datePublished": p["article"]["date"],
                   "dateModified": p["article"]["date"], "mainEntityOfPage": url, "image": BASE + "og-image.jpg",
                   "author": {"@type": "Person", "name": "Pablo Massera", "url": LINKEDIN},
                   "publisher": {"@id": BASE + "#empresa"}})
    ld_html = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)

    body = p["body"]
    # @@grupo@@ o @@lang:grupo@@ -> enlace relativo
    def sub(m):
        spec = m.group(1)
        if ":" in spec:
            l, g = spec.split(":", 1)
        else:
            l, g = lang, spec
        tp = find(g, l) or find(g, "es")
        if not tp:
            raise SystemExit(f"Enlace roto: {spec} en {p['path']}")
        return R + tp["path"]
    body = re.sub(r"@@([a-z:\-]+)@@", sub, body).replace("{R}", R)

    legal_es = find("aviso", lang) or find("aviso", "es")
    priv_es = find("privacidad", lang) or find("privacidad", "es")
    robots = '<meta name="robots" content="noindex">' if p["noindex"] else ""

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["desc"])}">
{robots}<link rel="canonical" href="{url}">
{hreflang}<meta property="og:type" content="{'article' if p['article'] else 'website'}">
<meta property="og:site_name" content="Gestión Energía">
<meta property="og:title" content="{esc(p["title"])}">
<meta property="og:description" content="{esc(p["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{OG_LOCALE[lang]}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="{R}favicon.png">
<link rel="apple-touch-icon" href="{R}apple-touch-icon.png">
<meta name="theme-color" content="#153e32">
<meta name="format-detection" content="telephone=no">
<link rel="preload" href="{R}montserrat-800.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{R}montserrat-700.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="{R}open-sans-400.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{R}site.css?v={TODAY}">
{ld_html}
</head>
<body>
<a class="skip-link" href="#contenido">{t["skip"]}</a>
<header>
<div class="wrap header-inner">
<a href="{R}{find("home", lang)["path"]}" class="brand" aria-label="{t["home_label"]}">
<img src="{R}logo.png" alt="Gestión Energía" width="88" height="89">
<span class="brand-tag">{t["tag"]}</span>
</a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu-principal">{MENU_ICON}{t["menu"]}</button>
<div class="header-right" id="menu-principal">
<nav class="nav-main" aria-label="{t["menu"]}">{links}</nav>
<div class="lang-switch" role="group" aria-label="{t["langs_label"]}">{sw}</div>
<a href="{wa(t["wa_msg"])}" class="phone-btn" target="_blank" rel="noopener">{WA}{PHONE_TXT}{nt}</a>
</div>
</div>
</header>
<main id="contenido" tabindex="-1">
{body}
</main>
<footer>
<div class="wrap footer-inner">
<span>© 2026 Gestión Energía · {t["footer"]}</span>
<span class="footer-links">
<a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram{nt}</a>
<a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn{nt}</a>
<a href="mailto:{EMAIL}">Email</a>
<a href="{R}{legal_es["path"]}">{t["legal"]}</a>
<a href="{R}{priv_es["path"]}">{t["privacy"]}</a>
</span>
</div>
</footer>
<a class="wa-float" href="{wa(t["wa_msg"])}" target="_blank" rel="noopener" aria-label="WhatsApp{t["newtab"]}">{WA}</a>
<script>
(function(){{var h=document.querySelector('header'),b=h.querySelector('.menu-btn');
b.addEventListener('click',function(){{var o=h.classList.toggle('open');b.setAttribute('aria-expanded',o);}});
h.querySelectorAll('.header-right a').forEach(function(a){{a.addEventListener('click',function(){{h.classList.remove('open');b.setAttribute('aria-expanded','false');}});}});
document.addEventListener('keydown',function(e){{if(e.key==='Escape'&&h.classList.contains('open')){{h.classList.remove('open');b.setAttribute('aria-expanded','false');b.focus();}}}});}})();
</script>
{p.get("script","")}
{gc_script}</body>
</html>
'''
