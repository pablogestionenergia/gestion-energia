from engine import *

L = "es"
NT = '<span class="sr-only"> (se abre en una pestaña nueva)</span>'

def pasos():
    return '''<ol class="pasos">
<li class="paso"><h3>Nos pasas el cliente</h3><p>Cuando cierras una compraventa o un alquiler, nos envías los datos del comprador o inquilino.</p></li>
<li class="paso"><h3>Tramitamos el suministro</h3><p>Alta, cambio de titular o cambio de compañía de luz y gas, con la tarifa que mejor encaja.</p></li>
<li class="paso"><h3>Cobras tu comisión</h3><p>Por cada alta gestionada, tu agencia recibe su comisión. Te avisamos cuando todo está hecho.</p></li>
</ol>'''

def guias_destacadas(n=3):
    from guias_es import GUIAS
    cards = "".join(f'<a class="guia-card" href="@@{g["group"]}@@"><span class="tag">{g["tag"]}</span><h3>{g["h1"]}</h3><p>{g["resumen"]}</p></a>' for g in GUIAS[:n])
    return f'''<section class="section"><div class="wrap">
<div class="eyebrow">Guías prácticas</div>
<h2 class="section-title">Resuelve las dudas de suministro de tus operaciones</h2>
<p class="section-lead">Lo que más nos preguntan los agentes y administradores, explicado paso a paso.</p>
<div class="guias-grid">{cards}</div>
<p style="margin-top:30px"><a class="btn btn-verde" href="@@guias@@">Ver todas las guías</a></p>
</div></section>'''

# ================= INICIO =================
page(lang=L, group="home", path="",
 title="Gestión Energía | Luz y gas para inmobiliarias y administradores de fincas",
 desc="Gestionamos las altas y cambios de titular de luz y gas de tus operaciones inmobiliarias y tu agencia cobra una comisión por cada alta. Servicio B2B en toda España.",
 body=f'''<section class="hero">
<div class="hero-left on-dark">
<h1>Convierte la energía<br>en <span>Rentabilidad Neta</span></h1>
<p class="hero-text">Servicio B2B para inmobiliarias y administradores de fincas. Nos ocupamos de la luz y el gas de cada operación —altas, cambios de titular e incidencias— y tu agencia cobra una comisión por cada alta.</p>
<div class="hero-ctas">
<a href="@@modelos@@" class="btn btn-oro">Ver modelos de colaboración</a>
<a href="{wa("Hola Pablo, tengo una inmobiliaria y me interesa colaborar con Gestión Energía.")}" class="btn btn-linea" target="_blank" rel="noopener">Hablemos por WhatsApp{NT}</a>
</div></div>
<div class="hero-right" aria-hidden="true"></div>
</section>
{logos_block(L)}
<section class="section beneficios"><div class="wrap">
<div class="center"><div class="eyebrow">Tu partner energético</div>
<h2 class="section-title">Tú vendes y alquilas pisos.<br>Nosotros nos ocupamos del resto.</h2>
<p class="section-lead">El cambio de luz y gas es lo último que quiere gestionar un agente, y lo primero de lo que se queja un inquilino si falla.</p></div>
<div class="cards-3">
<div class="card">{I_EURO}<h3>Comisiones por cada alta</h3><p>Un trámite que hoy no te aporta nada se convierte en un ingreso extra para tu agencia, operación tras operación.</p></div>
<div class="card">{I_CLOCK}<h3>Cero tiempos de espera</h3><p>Olvídate de las músicas de espera de las compañías. Gestionamos altas y cambios de titular directamente con la comercializadora.</p></div>
<div class="card">{I_SHIELD}<h3>Incidencias resueltas</h3><p>Si un inquilino se queda sin suministro, nos ocupamos nosotros. Tu reputación queda a salvo.</p></div>
</div></div></section>
<section class="section"><div class="wrap">
<div class="eyebrow">Cómo trabajamos</div>
<h2 class="section-title">Tres pasos, un solo contacto</h2>
<p class="section-lead">Sin esperas al teléfono de la compañía ni papeleo para tu equipo. Tú cierras la operación; nosotros dejamos los suministros listos.</p>
{pasos()}
</div></section>
<section class="section beneficios"><div class="wrap">
<div class="center"><div class="eyebrow">Para quién trabajamos</div>
<h2 class="section-title">Un servicio pensado para el sector inmobiliario</h2></div>
<div class="cards-2">
<a class="card" href="@@agencias@@">{I_HOUSE}<h3>Inmobiliarias</h3><p>Compraventas y alquileres de larga duración: el comprador o inquilino entra a vivir con la luz y el gas a su nombre, y tu agencia cobra por cada alta.</p><span class="mas">Ver servicio para inmobiliarias →</span></a>
<a class="card" href="@@admin@@">{I_BUILD}<h3>Administradores de fincas</h3><p>Cada cambio de propietario o de inquilino en las fincas que gestionas, resuelto sin que tu despacho tenga que llamar a ninguna compañía.</p><span class="mas">Ver servicio para administradores →</span></a>
</div></div></section>
<section class="section modelos on-dark"><div class="wrap center">
<div class="eyebrow">Modelos de colaboración</div>
<h2 class="section-title">Elige cuánto quieres implicarte</h2>
<p class="section-lead">Modelo Híbrido: tú captas y nosotros tramitamos. Modelo Partner: tu equipo tramita con nuestra plataforma y nuestro respaldo.</p>
<p style="margin-top:30px"><a class="btn btn-oro" href="@@modelos@@">Comparar los dos modelos</a></p>
</div></section>
{clients_block(L)}
{guias_destacadas()}
{cta_block(L)}''')

# ================= INMOBILIARIAS =================
FAQ_AG = [
 ("¿Qué tiene que hacer mi agencia?", "Solo pasarnos los datos del comprador o inquilino cuando cierras la operación. Nosotros hablamos con él, tramitamos el suministro y te avisamos cuando está hecho."),
 ("¿Cómo cobra mi agencia?", "Tu agencia recibe una comisión por cada alta que gestionamos. El importe depende del modelo de colaboración y te lo envío por privado junto con una propuesta adaptada a tu volumen."),
 ("¿Qué pasa si el piso no tiene luz o el suministro está dado de baja?", "Tramitamos el alta. Antes te decimos si hace falta boletín eléctrico (CIE) o algún otro documento, para que no haya sorpresas el día de la entrega de llaves."),
 ("¿El nuevo inquilino hereda las deudas del anterior?", "No debería: en el cambio de titular pedimos que el contrato nuevo se haga sin asumir las deudas del titular anterior."),
 ("¿Con qué comercializadoras trabajáis?", "Con las principales del mercado (Endesa, Naturgy, Iberdrola, Repsol, TotalEnergies) y muchas más. Elegimos la tarifa que mejor encaja con cada cliente."),
 ("¿Trabajáis fuera de Barcelona?", "Sí. Trabajamos 100 % en línea y atendemos inmobiliarias de toda España."),
]
page(lang=L, group="agencias", path="inmobiliarias/", faq=FAQ_AG,
 title="Gestión de luz y gas para inmobiliarias | Gestión Energía",
 desc="Altas y cambios de titular de luz y gas en cada compraventa o alquiler. Tu agencia no pierde tiempo con las compañías y cobra una comisión por cada alta.",
 body=page_hero(L, "Luz y gas listos en cada operación, <span>y una comisión para tu agencia</span>",
   "Cuando cierras una compraventa o un alquiler, nosotros ponemos los suministros a nombre del nuevo cliente. Tu equipo no hace llamadas ni papeleo.",
   crumbs=[("Inmobiliarias", None)],
   ctas=f'<div class="hero-ctas"><a class="btn btn-oro" href="@@contacto@@">Quiero colaborar</a><a class="btn btn-linea" href="{wa("Hola Pablo, tengo una inmobiliaria y me interesa colaborar con Gestión Energía.")}" target="_blank" rel="noopener">WhatsApp{NT}</a></div>')
 + f'''<section class="section"><div class="wrap">
<div class="eyebrow">Qué hacemos por tu agencia</div>
<h2 class="section-title">Todo lo que pasa con la luz y el gas después de firmar</h2>
<div class="split">
<div><ul class="checks">
<li><strong>Cambio de titular</strong> de luz y gas a nombre del comprador o del inquilino.</li>
<li><strong>Alta de suministro</strong> en pisos sin luz o con el contrato dado de baja.</li>
<li><strong>Cambio de comercializadora</strong> si al cliente le conviene otra tarifa.</li>
<li><strong>Incidencias</strong>: si el cliente se queda sin suministro, hablamos nosotros con la compañía.</li>
<li><strong>Seguimiento</strong>: te avisamos cuando todo está hecho.</li>
</ul></div>
<div class="box"><h3>Operaciones en las que encajamos</h3>
<p>Compraventas y alquileres de larga duración, que es donde cambia el titular del suministro. Trabajamos muy bien con agencias que alquilan a <a href="@@guia-expats@@" style="text-decoration:underline">inquilinos extranjeros</a>: se quedan años y necesitan que alguien les resuelva el trámite.</p>
<p>Si gestionas sobre todo alquiler por habitaciones o alquiler turístico, el titular no suele cambiar y no te aportaríamos tanto.</p></div>
</div></div></section>
<section class="section beneficios"><div class="wrap">
<div class="center"><div class="eyebrow">Ventajas</div><h2 class="section-title">Por qué las agencias trabajan con nosotros</h2></div>
<div class="cards-3">
<div class="card">{I_EURO}<h3>Ingreso extra</h3><p>Cada alta suma una comisión para tu agencia. Un trámite que antes era un coste de tiempo pasa a ser un ingreso.</p></div>
<div class="card">{I_CLOCK}<h3>Tu equipo, a vender</h3><p>Ni llamadas a la compañía ni formularios. Un solo contacto para todas tus operaciones.</p></div>
<div class="card">{I_SHIELD}<h3>Clientes contentos</h3><p>El cliente entra a vivir con todo funcionando. La buena experiencia se la lleva tu agencia.</p></div>
</div></div></section>
<section class="section"><div class="wrap"><div class="eyebrow">Cómo trabajamos</div><h2 class="section-title">Tres pasos, un solo contacto</h2>{pasos()}</div></section>
{faq_block(L, FAQ_AG, "Preguntas frecuentes de inmobiliarias", "Dudas habituales")}
{cta_block(L, "Hola Pablo, tengo una inmobiliaria y me interesa colaborar con Gestión Energía.")}''')

# ================= ADMINISTRADORES =================
FAQ_AD = [
 ("¿En qué casos nos podéis ayudar?", "Cada vez que cambia el propietario o el inquilino de una vivienda o local que gestionas y hay que poner la luz o el gas a nombre de la persona nueva, o dar de alta un suministro que estaba de baja."),
 ("¿Tiene coste para el despacho?", "No: tu despacho recibe una comisión por cada alta que gestionamos. Las condiciones te las envío por privado."),
 ("¿Quién habla con el propietario o el inquilino?", "Nosotros. Tú solo nos facilitas el contacto y te mantenemos informado."),
 ("¿Trabajáis con despachos fuera de Barcelona?", "Sí. Trabajamos en línea con despachos de toda España."),
]
page(lang=L, group="admin", path="administradores-de-fincas/", faq=FAQ_AD,
 title="Luz y gas para administradores de fincas | Gestión Energía",
 desc="Cambios de titular y altas de luz y gas en las fincas que administras, sin carga para tu despacho y con comisión por cada alta. Servicio en toda España.",
 body=page_hero(L, "Los suministros de tus fincas, <span>resueltos sin llamadas</span>",
   "Cuando entra un propietario o un inquilino nuevo en una finca que administras, nos ocupamos de la luz y el gas. Tu despacho cobra una comisión por cada alta.",
   crumbs=[("Administradores de fincas", None)],
   ctas=f'<div class="hero-ctas"><a class="btn btn-oro" href="@@contacto@@">Pedir información</a><a class="btn btn-linea" href="{wa("Hola Pablo, soy administrador de fincas y me interesa colaborar con Gestión Energía.")}" target="_blank" rel="noopener">WhatsApp{NT}</a></div>')
 + f'''<section class="section"><div class="wrap">
<div class="eyebrow">Qué hacemos</div>
<h2 class="section-title">Un interlocutor para todos los cambios de suministro</h2>
<div class="split">
<div><ul class="checks">
<li><strong>Cambios de titular</strong> de luz y gas cuando se vende o se alquila una vivienda o un local.</li>
<li><strong>Altas</strong> de suministros dados de baja, avisando antes de si hace falta boletín o revisión.</li>
<li><strong>Incidencias</strong> con la comercializadora, sin que tu despacho tenga que estar al teléfono.</li>
<li><strong>Información</strong>: te contamos cuándo está todo hecho para que puedas cerrar el expediente.</li>
</ul></div>
<div class="box"><h3>Menos llamadas a tu despacho</h3><p>Las dudas de luz y gas de propietarios e inquilinos acaban muchas veces en el teléfono del administrador. Nosotros las resolvemos directamente con ellos.</p><p>Y lo que antes era una gestión sin retorno pasa a generar una comisión para tu despacho.</p></div>
</div></div></section>
<section class="section beneficios"><div class="wrap"><div class="eyebrow">Cómo trabajamos</div><h2 class="section-title">Tres pasos, un solo contacto</h2>{pasos()}</div></section>
{faq_block(L, FAQ_AD, "Preguntas frecuentes de administradores", "Dudas habituales")}
{cta_block(L, "Hola Pablo, soy administrador de fincas y me interesa colaborar con Gestión Energía.")}''')

# ================= MODELOS =================
page(lang=L, group="modelos", path="modelos-de-colaboracion/",
 title="Modelos de colaboración Híbrido y Partner | Gestión Energía",
 desc="Dos formas de colaborar con Gestión Energía: Modelo Híbrido (tú captas, nosotros tramitamos) y Modelo Partner (tu equipo tramita con nuestra plataforma).",
 body=page_hero(L, "Elige cuánto quieres <span>implicarte</span>",
   "Dos formas de trabajar con nosotros, según el equipo que tenga tu agencia o tu despacho.", crumbs=[("Modelos de colaboración", None)])
 + f'''<section class="section modelos on-dark"><div class="wrap">
<div class="modelos-grid" style="margin-top:0">
<div class="modelo"><div class="modelo-tag">Equilibrio operativo</div><h2 style="font-size:1.8rem;color:var(--verde);margin-bottom:14px">Modelo Híbrido</h2>
<p class="modelo-intro">Tú te centras en la captación comercial; nosotros nos ocupamos de la tramitación.</p>
<div class="roles"><div class="rol"><strong>Tu parte</strong><span>Captar al cliente, la administración básica y la firma.</span></div>
<div class="rol"><strong>Nuestra parte</strong><span>Toda la operación técnica: altas y tramitación con la comercializadora.</span></div></div>
<div class="ideal"><strong>Ideal para</strong> inmobiliarias centradas en cerrar operaciones rápido que quieren agilizar procesos.</div>
<a href="{wa("Hola Pablo, me gustaría recibir las condiciones del Modelo Híbrido.")}" class="btn btn-verde" target="_blank" rel="noopener">Pedir condiciones{NT}</a></div>
<div class="modelo"><div class="modelo-tag">Máxima rentabilidad</div><h2 style="font-size:1.8rem;color:var(--verde);margin-bottom:14px">Modelo Partner</h2>
<p class="modelo-intro">Tu agencia lleva toda la operativa con nuestra plataforma y nuestro respaldo.</p>
<div class="roles"><div class="rol"><strong>Tu parte</strong><span>Tramitar las altas desde nuestra plataforma, la administración y la firma de contratos.</span></div>
<div class="rol"><strong>Nuestra parte</strong><span>La plataforma y el soporte técnico continuo.</span></div></div>
<div class="ideal"><strong>Ideal para</strong> agencias con equipo administrativo propio que quieren maximizar sus márgenes.</div>
<a href="{wa("Hola Pablo, me gustaría recibir las condiciones del Modelo Partner.")}" class="btn btn-verde" target="_blank" rel="noopener">Pedir condiciones{NT}</a></div>
</div>
<p class="modelos-nota">Las comisiones de cada modelo te las envío por privado, junto con una propuesta adaptada a tu cartera.</p>
</div></section>
<section class="section"><div class="wrap">
<div class="center"><div class="eyebrow">Comparativa</div><h2 class="section-title">Los dos modelos, lado a lado</h2></div>
<div class="tabla-wrap"><table class="tabla">
<thead><tr><th scope="col"></th><th scope="col">Híbrido</th><th scope="col">Partner</th></tr></thead>
<tbody>
<tr><th scope="row">Quién capta al cliente</th><td>Tu agencia</td><td>Tu agencia</td></tr>
<tr><th scope="row">Quién tramita el alta</th><td>Gestión Energía</td><td>Tu equipo, desde nuestra plataforma</td></tr>
<tr><th scope="row">Soporte</th><td>Nos ocupamos de toda la parte técnica</td><td>Soporte técnico continuo</td></tr>
<tr><th scope="row">Rentabilidad</th><td>Comisión por cada alta</td><td>Mayor margen por alta</td></tr>
<tr><th scope="row">Ideal para</th><td>Agencias que quieren despreocuparse</td><td>Agencias con equipo administrativo</td></tr>
</tbody></table></div>
</div></section>
{cta_block(L)}''')

# ================= SOBRE MÍ =================
page(lang=L, group="sobre", path="sobre-mi/",
 title="Pablo Massera, fundador de Gestión Energía",
 desc="Pablo Massera, fundador de Gestión Energía: experiencia en comercialización energética al servicio de inmobiliarias y administradores de fincas.",
 body=page_hero(L, "Un único interlocutor <span>que responde</span>", "Conoce quién está detrás de Gestión Energía.", crumbs=[("Sobre mí", None)])
 + f'''<section class="section"><div class="wrap sobre">
<div class="foto"><img src="{{R}}pablo.jpg" alt="Pablo Massera, fundador de Gestión Energía" width="1024" height="1024"></div>
<div><div class="eyebrow">Sobre mí</div>
<h2 class="sobre-nombre">Pablo Massera</h2>
<div class="cargo">Fundador · Gestión Energía</div>
<blockquote class="cita"><p>«Mi objetivo es que tú te dediques a vender pisos, mientras yo me ocupo de que tengan luz y gas al mejor precio.»</p></blockquote>
<p class="txt">Vengo del sector de la comercialización energética y conozco por dentro cómo funcionan las altas, los cambios de titular y las incidencias. Con Gestión Energía pongo esa experiencia al servicio de inmobiliarias y administradores de fincas: un único interlocutor que responde.</p>
<p class="txt">Trabajo de forma 100 % en línea con agencias y despachos de toda España.</p>
<a class="linkedin-link" href="{LINKEDIN}" target="_blank" rel="noopener">{LI} Sígueme en LinkedIn{NT}</a>
</div></div></section>
{clients_block(L)}
{cta_block(L)}''')

# ================= CONTACTO =================
def contact_page(lang, group, path, title, desc, h1, lead, crumb, labels, script_msgs):
    lb = labels
    form = f'''<form class="form" id="form-contacto" action="https://api.web3forms.com/submit" method="POST" novalidate>
<input type="hidden" name="access_key" value="{WEB3FORMS_KEY}">
<input type="hidden" name="subject" value="{lb["subject"]}">
<input type="hidden" name="from_name" value="Web Gestión Energía">
<input type="checkbox" name="botcheck" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<div class="row2">
<div><label for="f-nombre">{lb["name"]}</label><input id="f-nombre" name="name" autocomplete="name" required></div>
<div><label for="f-empresa">{lb["company"]} <span class="opt">{lb["optional"]}</span></label><input id="f-empresa" name="empresa" autocomplete="organization"></div>
</div>
<div class="row2">
<div><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email" inputmode="email" required></div>
<div><label for="f-tel">{lb["phone"]} <span class="opt">{lb["optional"]}</span></label><input id="f-tel" name="telefono" type="tel" autocomplete="tel" inputmode="tel"></div>
</div>
<div><label for="f-tipo">{lb["type"]}</label><select id="f-tipo" name="tipo">{"".join(f"<option>{o}</option>" for o in lb["types"])}</select></div>
<div><label for="f-msg">{lb["message"]}</label><textarea id="f-msg" name="message" required placeholder="{lb["placeholder"]}"></textarea></div>
<div class="consent"><input type="checkbox" id="f-ok" name="acepto_privacidad" value="si" required><label for="f-ok" style="font-family:inherit;font-weight:400;color:inherit;margin:0">{lb["consent"]}</label></div>
<button class="btn btn-verde" type="submit">{lb["send"]}</button>
<div class="form-msg" role="status" aria-live="polite"></div>
</form>'''
    t = T[lang]
    direct = f'''<div class="directo"><h2 class="section-title" style="font-size:1.6rem">{lb["direct"]}</h2>
<a class="contact-item" href="{wa(t["wa_msg"])}" target="_blank" rel="noopener">{WA} WhatsApp {PHONE_TXT}<span class="sr-only">{t["newtab"]}</span></a>
<a class="contact-item" href="tel:+{PHONE}">{TEL} {t["call"]} {PHONE_TXT}</a>
<a class="contact-item" href="mailto:{EMAIL}">{MAIL} <span class="email">{EMAIL.replace("@","@<wbr>")}</span></a>
<a class="contact-item" href="{LINKEDIN}" target="_blank" rel="noopener">{LI} LinkedIn<span class="sr-only">{t["newtab"]}</span></a>
<p style="color:var(--texto-suave);margin-top:6px">{lb["reply"]}</p></div>'''
    m = script_msgs
    script = f'''<script>
(function(){{var f=document.getElementById('form-contacto');if(!f)return;var box=f.querySelector('.form-msg'),btn=f.querySelector('button[type=submit]');
f.addEventListener('submit',function(e){{e.preventDefault();box.className='form-msg';
if(!f.checkValidity()){{box.textContent={json.dumps(m["invalid"])};box.className='form-msg err';var bad=f.querySelector(':invalid');if(bad)bad.focus();return;}}
var data=Object.fromEntries(new FormData(f));btn.disabled=true;var old=btn.textContent;btn.textContent={json.dumps(m["sending"])};
fetch(f.action,{{method:'POST',headers:{{'Content-Type':'application/json',Accept:'application/json'}},body:JSON.stringify(data)}})
.then(function(r){{return r.json();}}).then(function(j){{if(j.success){{f.reset();box.textContent={json.dumps(m["ok"])};box.className='form-msg ok';}}else{{throw new Error(j.message);}}}})
.catch(function(){{box.innerHTML={json.dumps(m["err"])};box.className='form-msg err';}})
.finally(function(){{btn.disabled=false;btn.textContent=old;}});}});}})();
</script>'''
    page(lang=lang, group=group, path=path, title=title, desc=desc, script=script,
         body=page_hero(lang, h1, lead, crumbs=[(crumb, None)])
         + f'''<section class="section beneficios"><div class="wrap contacto-grid">{form}{direct}</div></section>''')

contact_page(L, "contacto", "contacto/",
 "Contacto | Gestión Energía", "Escríbenos desde el formulario, por WhatsApp, por teléfono o por email y te enviamos una propuesta para tu inmobiliaria o despacho.",
 "Hablemos de <span>tu cartera</span>", "Cuéntame cómo trabaja tu agencia o tu despacho y te envío una propuesta personalizada con las condiciones.", "Contacto",
 dict(subject="Nuevo contacto desde la web (ES)", name="Nombre", company="Agencia o empresa", optional="(opcional)", phone="Teléfono",
      type="Soy…", types=["Inmobiliaria","Administrador de fincas","Otro"], message="Mensaje",
      placeholder="Por ejemplo: cuántas operaciones cerráis al mes y en qué zona trabajáis.",
      consent='He leído y acepto la <a href="@@privacidad@@">política de privacidad</a>.', send="Enviar mensaje",
      direct="O contacta directamente", reply="Respondo personalmente."),
 dict(invalid="Revisa los campos obligatorios: nombre, email, mensaje y la casilla de privacidad.", sending="Enviando…",
      ok="¡Gracias! He recibido tu mensaje y te respondo lo antes posible.",
      err='No se ha podido enviar. Escríbeme a <a href="mailto:' + EMAIL + '">' + EMAIL + '</a> o por WhatsApp.'))

# ================= LEGALES (solo en castellano) =================
P = lambda s: f'<mark>{s}</mark>'
page(lang=L, group="aviso", path="aviso-legal/", noindex=True,
 title="Aviso legal | Gestión Energía", desc="Aviso legal del sitio web de Gestión Energía.",
 body=page_hero(L, "Aviso legal", "Información sobre el titular de este sitio web.", crumbs=[("Aviso legal", None)])
 + f'''<section class="section"><div class="wrap"><div class="prose">
<h2>Titular del sitio web</h2>
<p>En cumplimiento del artículo 10 de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI-CE), se informa de los datos del titular de este sitio web:</p>
<ul>
<li><strong>Titular:</strong> {P("NOMBRE Y APELLIDOS COMPLETOS")}, que opera con el nombre comercial Gestión Energía</li>
<li><strong>NIF:</strong> {P("NIF")}</li>
<li><strong>Domicilio:</strong> {P("DOMICILIO FISCAL")}</li>
<li><strong>Email:</strong> <a href="mailto:{EMAIL}">{EMAIL}</a></li>
<li><strong>Teléfono:</strong> +34 {PHONE_TXT}</li>
</ul>
<h2>Objeto</h2>
<p>Este sitio web informa sobre los servicios de gestión de suministros de luz y gas que Gestión Energía ofrece a inmobiliarias, administradores de fincas y otros profesionales del sector inmobiliario.</p>
<h2>Condiciones de uso</h2>
<p>El acceso a este sitio web es gratuito y no exige registro. La persona usuaria se compromete a hacer un uso adecuado de los contenidos. La información de las guías es orientativa y no sustituye el asesoramiento sobre cada caso concreto; las condiciones de cada contratación las fija la comercializadora correspondiente.</p>
<h2>Propiedad intelectual e industrial</h2>
<p>Los textos, el diseño y el logotipo de Gestión Energía pertenecen a su titular. Las marcas y logotipos de las comercializadoras y de los clientes que aparecen en la web pertenecen a sus respectivos propietarios y se muestran únicamente a título informativo.</p>
<h2>Enlaces externos</h2>
<p>Este sitio contiene enlaces a servicios de terceros (WhatsApp, LinkedIn). Gestión Energía no se hace responsable de sus contenidos ni de sus políticas de privacidad.</p>
<h2>Legislación aplicable</h2>
<p>Este aviso legal se rige por la legislación española.</p>
</div></div></section>''')

page(lang=L, group="privacidad", path="privacidad/", noindex=True,
 title="Política de privacidad | Gestión Energía", desc="Cómo trata Gestión Energía los datos personales que recibe a través de su web.",
 body=page_hero(L, "Política de privacidad", "Cómo tratamos los datos que nos envías a través de esta web.", crumbs=[("Privacidad", None)])
 + f'''<section class="section"><div class="wrap"><div class="prose">
<h2>Responsable del tratamiento</h2>
<p>{P("NOMBRE Y APELLIDOS COMPLETOS")} (Gestión Energía), NIF {P("NIF")}, con domicilio en {P("DOMICILIO FISCAL")}. Contacto: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Qué datos tratamos y para qué</h2>
<p>Los datos que nos facilitas en el formulario de contacto (nombre, empresa, email, teléfono, tipo de negocio y mensaje), o al escribirnos por email o WhatsApp, se usan únicamente para responder a tu consulta y, si te interesa, enviarte una propuesta de colaboración.</p>
<h2>Base legal</h2>
<p>Tu consentimiento, que das al enviar el formulario marcando la casilla correspondiente, y la aplicación de medidas precontractuales a petición tuya.</p>
<h2>Cuánto tiempo los conservamos</h2>
<p>Mientras dure la relación o la conversación comercial y, después, durante los plazos legalmente exigibles. Si no llegamos a colaborar, los eliminamos cuando ya no sean necesarios para atender tu consulta.</p>
<h2>Destinatarios</h2>
<p>No cedemos tus datos a terceros salvo obligación legal. Para hacer llegar los mensajes del formulario a nuestro correo usamos el servicio Web3Forms, que actúa como encargado del tratamiento. Si nos escribes por WhatsApp o LinkedIn, esas plataformas tratan los datos según sus propias políticas.</p>
<h2>Tus derechos</h2>
<p>Puedes ejercer tus derechos de acceso, rectificación, supresión, oposición, limitación y portabilidad escribiendo a <a href="mailto:{EMAIL}">{EMAIL}</a>. Si consideras que no hemos tratado bien tus datos, puedes reclamar ante la Agencia Española de Protección de Datos (aepd.es).</p>
<h2>Cookies</h2>
<p>Esta web no utiliza cookies propias ni de analítica o publicidad.</p>
</div></div></section>''')
