from engine import *

L = "es"
D = TODAY

def cta(txt="¿Tienes una operación entre manos? Pásanos los datos del cliente y nos ocupamos de la luz y el gas. Tu agencia cobra una comisión por cada alta."):
    return f'''<div class="cta-inline"><h2>¿Lo gestionamos por ti?</h2><p>{txt}</p>
<a class="btn btn-oro" href="@@contacto@@">Contactar con Gestión Energía</a></div>'''

GUIAS = [
dict(group="guia-titular", slug="cambio-de-titular-luz-venta-alquiler", tag="Cambio de titular",
 h1="Cambio de titular de la luz al vender o alquilar un piso",
 title="Cambio de titular de la luz al vender o alquilar un piso: pasos y documentos",
 desc="Qué es el cambio de titular de la luz, qué documentos se necesitan, cuánto cuesta y cómo evitar heredar deudas en una compraventa o un alquiler.",
 resumen="Pasos, documentos y cómo evitar que el nuevo cliente herede deudas del titular anterior.",
 body=f'''<p class="meta">Guía para inmobiliarias y administradores de fincas · Actualizada en noviembre de 2026</p>
<p>Cada vez que se vende o se alquila un piso que ya tiene luz, alguien tiene que poner el contrato a nombre de la persona que entra a vivir. Es el <strong>cambio de titular</strong>. Si nadie lo hace, el vendedor o el propietario sigue pagando facturas de un consumo que no es suyo, y el comprador o el inquilino no puede gestionar su propio suministro.</p>
<h2>Cambio de titular no es lo mismo que alta</h2>
<ul>
<li><strong>Cambio de titular:</strong> el piso tiene luz y el contrato pasa a otra persona. No se corta el suministro.</li>
<li><strong>Alta:</strong> el suministro está dado de baja y hay que volver a activarlo. Lo explicamos en la guía <a href="@@guia-alta@@">alta de luz en un piso sin suministro</a>.</li>
</ul>
<h2>Qué documentos se necesitan</h2>
<ul>
<li>Nombre completo y DNI o NIE del nuevo titular.</li>
<li>El <a href="@@guia-cups@@">código CUPS</a> del suministro (aparece en cualquier factura).</li>
<li>Una cuenta bancaria (IBAN) para domiciliar los recibos.</li>
<li>Teléfono y email de contacto del nuevo titular.</li>
<li>En algunos casos, el contrato de alquiler o la escritura, como prueba de que la persona ocupa la vivienda.</li>
</ul>
<p>Tienes la lista completa, lista para pedírsela al cliente, en la <a href="@@guia-datos@@">checklist de datos para tramitar luz y gas</a>.</p>
<h2>¿Cuánto cuesta?</h2>
<p>Un cambio de titular que mantiene la misma potencia suele ser gratuito. Lo que sí puede tener coste es lo que se hace a la vez: subir la potencia contratada, por ejemplo, conlleva unos derechos regulados que cobra la distribuidora. Por eso conviene revisar la potencia antes de tramitar, no después.</p>
<h2>Cómo evitar que el cliente herede deudas</h2>
<p>Si el titular anterior dejó facturas sin pagar, lo recomendable es pedir el cambio <strong>sin subrogación</strong>: el contrato nuevo empieza desde cero a nombre del nuevo titular, sin asumir las deudas del anterior. Con subrogación, en cambio, el nuevo titular continúa el contrato existente con sus condiciones.</p>
<div class="nota"><strong>Consejo para la agencia:</strong> deja anotadas las lecturas de los contadores el día de la entrega de llaves (una foto basta). Evita discusiones sobre quién pagó qué consumo.</div>
<h2>¿Y el gas?</h2>
<p>El gas tiene su propio contrato y su propio CUPS, así que hay que hacer un cambio de titular aparte. Lo práctico es tramitar luz y gas a la vez.</p>
{cta()}'''),

dict(group="guia-alta", slug="alta-luz-piso-sin-suministro", tag="Alta de suministro",
 h1="Alta de luz en un piso sin suministro: cuándo hace falta boletín",
 title="Alta de luz en un piso sin suministro: boletín (CIE), costes y pasos",
 desc="Cómo dar de alta la luz en un piso con el suministro dado de baja: cuándo se pide el boletín eléctrico (CIE), qué derechos se pagan y cómo evitar retrasos en la entrega de llaves.",
 resumen="Cuándo se pide el boletín eléctrico (CIE), qué se paga y cómo no retrasar la entrega de llaves.",
 body=f'''<p class="meta">Guía para inmobiliarias y administradores de fincas · Actualizada en noviembre de 2026</p>
<p>Es una de las situaciones que más retrasa una entrega de llaves: el piso lleva tiempo vacío, el antiguo titular dio de baja la luz y el comprador o el inquilino quiere entrar a vivir ya. En ese caso no basta con un <a href="@@guia-titular@@">cambio de titular</a>: hay que pedir un <strong>alta</strong>.</p>
<h2>Paso 1: averigua desde cuándo está de baja</h2>
<p>El tiempo que el punto de suministro lleva sin contrato influye en lo que se paga. Según la normativa actual, si la baja tiene <strong>menos de tres años</strong> no se pagan los llamados derechos de extensión; si tiene más, sí. A eso se suman los derechos de acceso y de enganche, que son importes regulados y no los fija la comercializadora.</p>
<h2>Paso 2: comprueba si hace falta boletín eléctrico (CIE)</h2>
<p>El Certificado de Instalación Eléctrica (CIE), conocido como "boletín", lo emite un instalador autorizado y acredita que la instalación es segura. Lo normal es que lo pidan en estos casos:</p>
<ul>
<li>Primera alta de una vivienda de obra nueva.</li>
<li>Instalaciones antiguas, cuando el boletín tiene más de 20 años y la distribuidora pide actualizarlo.</li>
<li>Cuando se quiere contratar más potencia de la que figura como máxima en el boletín existente.</li>
</ul>
<p>Cada distribuidora puede revisar el caso concreto, así que lo mejor es confirmarlo antes de comprometer una fecha de entrega.</p>
<div class="nota"><strong>Consejo para la agencia:</strong> si el piso está vacío y sin luz, pregunta al propietario si conserva el boletín antes de publicar el anuncio. Encargar uno nuevo lleva días.</div>
<h2>Paso 3: solicita el alta con los datos del nuevo titular</h2>
<p>Hacen falta los mismos datos que para un cambio de titular (DNI o NIE, <a href="@@guia-cups@@">CUPS</a>, IBAN y contacto) más la potencia que se quiere contratar. Si no se sabe qué potencia elegir, mira la potencia que tenía el contrato anterior o pregúntanos.</p>
<h2>¿Cuánto tarda?</h2>
<p>Depende de la distribuidora y de si hace falta boletín o visita técnica. Por eso conviene empezar el trámite en cuanto se firma la operación, no el día de la mudanza.</p>
{cta()}'''),

dict(group="guia-cups", slug="que-es-el-cups", tag="Conceptos básicos",
 h1="Qué es el CUPS y dónde encontrarlo",
 title="Qué es el CUPS de la luz y el gas y dónde encontrarlo",
 desc="El CUPS es el código que identifica cada punto de suministro de luz o gas. Te explicamos para qué sirve y dónde encontrarlo en una vivienda que vendes o alquilas.",
 resumen="El código que identifica cada suministro y por qué lo vas a necesitar en cada operación.",
 body=f'''<p class="meta">Guía rápida · Actualizada en noviembre de 2026</p>
<p>El <strong>CUPS</strong> (Código Universal del Punto de Suministro) es la "matrícula" del suministro de una vivienda. Identifica el punto donde llega la luz o el gas, no a la persona: cuando cambia el titular o la comercializadora, el CUPS sigue siendo el mismo.</p>
<h2>Cómo es</h2>
<p>Empieza por <strong>ES</strong> y le siguen unos 20 caracteres entre números y letras. La luz y el gas de un mismo piso tienen <strong>CUPS distintos</strong>.</p>
<h2>Dónde encontrarlo</h2>
<ul>
<li>En cualquier factura de luz o de gas de la vivienda, normalmente en el apartado de datos del contrato o del suministro.</li>
<li>En el contrato de suministro.</li>
<li>Si no hay facturas a mano, la distribuidora de la zona puede facilitarlo a partir de la dirección.</li>
</ul>
<h2>Para qué lo vas a necesitar</h2>
<p>Para cualquier trámite: <a href="@@guia-titular@@">cambio de titular</a>, <a href="@@guia-alta@@">alta</a> o cambio de comercializadora. Con el CUPS no hay dudas sobre qué vivienda es, aunque la dirección esté escrita de otra forma.</p>
<div class="nota"><strong>Consejo para la agencia:</strong> pide al propietario una factura reciente de luz y otra de gas cuando captes el inmueble. Tendrás los dos CUPS desde el principio.</div>
{cta()}'''),

dict(group="guia-datos", slug="datos-para-tramitar-luz-y-gas", tag="Checklist",
 h1="Checklist: datos del cliente para tramitar la luz y el gas",
 title="Checklist de datos para tramitar la luz y el gas en una compraventa o alquiler",
 desc="La lista de datos y documentos que hay que pedir al comprador o inquilino para tramitar el cambio de titular o el alta de luz y gas sin idas y vueltas.",
 resumen="La lista de lo que hay que pedir al comprador o inquilino, para hacerlo todo de una vez.",
 body=f'''<p class="meta">Para imprimir o copiar en tu CRM · Actualizada en noviembre de 2026</p>
<p>Casi todos los retrasos en los trámites de luz y gas vienen de un dato que falta. Si pides todo esto el día de la firma, el suministro puede quedar listo para la entrega de llaves.</p>
<h2>Del nuevo titular (comprador o inquilino)</h2>
<ul>
<li>Nombre y apellidos completos.</li>
<li>DNI, NIE o, en el caso de algunos extranjeros, pasaporte (ver la <a href="@@guia-expats@@">guía para inquilinos extranjeros</a>).</li>
<li>Teléfono móvil y email.</li>
<li>IBAN de la cuenta donde se domiciliarán los recibos.</li>
<li>Dirección para recibir las facturas, si no es la de la vivienda.</li>
</ul>
<h2>De la vivienda</h2>
<ul>
<li>Dirección completa (piso, puerta y código postal).</li>
<li><a href="@@guia-cups@@">CUPS</a> de la luz y CUPS del gas.</li>
<li>Si hay suministro activo o está dado de baja (y desde cuándo).</li>
<li>Boletín eléctrico (CIE), si el suministro está de baja y lo hay.</li>
<li>Foto de los contadores con la lectura el día de la entrega.</li>
</ul>
<h2>De la operación</h2>
<ul>
<li>Tipo: compraventa o alquiler.</li>
<li>Fecha prevista de entrega de llaves.</li>
<li>Si el cliente quiere mantener la comercializadora actual o prefiere que le busquemos otra tarifa.</li>
</ul>
<div class="nota"><strong>Con Gestión Energía:</strong> nos basta con el nombre y el teléfono del cliente y la dirección de la vivienda. El resto se lo pedimos nosotros.</div>
{cta()}'''),

dict(group="guia-expats", slug="suministros-inquilinos-extranjeros", tag="Expats",
 h1="Luz y gas para inquilinos extranjeros: lo que necesitan",
 title="Luz y gas para inquilinos extranjeros (expats) en España: documentos y consejos",
 desc="Qué necesita un inquilino extranjero para poner la luz y el gas a su nombre en España y cómo puede ayudarle la agencia: NIE o pasaporte, cuenta bancaria e idioma.",
 resumen="NIE o pasaporte, cuenta bancaria e idioma: cómo ayudar a un expat a tener los suministros a su nombre.",
 body=f'''<p class="meta">Guía para agencias que trabajan con expats · Actualizada en noviembre de 2026 · <a href="@@en:guia-expats@@" hreflang="en">Read in English</a></p>
<p>Los inquilinos extranjeros que vienen a trabajar o a vivir una temporada larga son un perfil muy interesante para una agencia: suelen quedarse años. Pero el primer contacto con las compañías de luz y gas, en otro idioma y con otros documentos, puede complicarse. Si la agencia se lo resuelve, gana un cliente agradecido.</p>
<h2>Documentos habituales</h2>
<ul>
<li><strong>Identificación:</strong> NIE si ya lo tiene; si todavía no, algunas comercializadoras aceptan el pasaporte.</li>
<li><strong>Cuenta bancaria (IBAN)</strong> para domiciliar los recibos.</li>
<li><strong>Datos de contacto:</strong> móvil y email.</li>
<li>El <a href="@@guia-cups@@">CUPS</a> de la vivienda y, a veces, el contrato de alquiler.</li>
</ul>
<h2>Los problemas más comunes</h2>
<ul>
<li><strong>El idioma:</strong> contratos, llamadas y facturas en castellano.</li>
<li><strong>Los plazos:</strong> el inquilino llega con fecha fija y necesita luz desde el primer día.</li>
<li><strong>La tarifa:</strong> no conoce el mercado español y puede acabar con una tarifa que no le conviene.</li>
</ul>
<h2>Qué puede hacer la agencia</h2>
<p>Lo más sencillo es dejar los suministros tramitados antes de la llegada y explicarle qué ha contratado. En Gestión Energía nos ocupamos de todo el trámite, y la agencia cobra su comisión por cada alta.</p>
{cta("¿Alquilas a expats? Pásanos su contacto y dejamos la luz y el gas a su nombre antes de que llegue.")}'''),

dict(group="guia-errores", slug="errores-suministros-entrega-de-llaves", tag="Buenas prácticas",
 h1="7 errores con la luz y el gas en la entrega de llaves",
 title="7 errores con la luz y el gas en la entrega de llaves (y cómo evitarlos)",
 desc="Los fallos más habituales con los suministros en compraventas y alquileres, y cómo evitarlos desde la agencia para que el cliente entre a vivir con todo funcionando.",
 resumen="Los fallos que más quejas generan después de firmar, y cómo evitarlos desde la agencia.",
 body=f'''<p class="meta">Guía para inmobiliarias · Actualizada en noviembre de 2026</p>
<p>Después de meses de trabajo, una operación puede acabar con un cliente enfadado por algo tan simple como no tener luz el primer día. Estos son los errores que más vemos.</p>
<h2>1. Dar de baja la luz en lugar de cambiar el titular</h2>
<p>El vendedor o el inquilino saliente da de baja el contrato "para no pagar más" y el piso se queda sin suministro. Volver a darlo de alta cuesta tiempo y dinero. Lo correcto es un <a href="@@guia-titular@@">cambio de titular</a>.</p>
<h2>2. Esperar al día de la mudanza</h2>
<p>Los trámites tienen plazos. Empieza en cuanto se firma la operación.</p>
<h2>3. No anotar las lecturas de los contadores</h2>
<p>Sin una foto de la lectura del día de la entrega, cualquier discusión sobre consumos es difícil de resolver.</p>
<h2>4. Olvidarse del gas</h2>
<p>La luz y el gas son contratos distintos, con <a href="@@guia-cups@@">CUPS distintos</a>. Hay que tramitar los dos.</p>
<h2>5. Heredar deudas del titular anterior</h2>
<p>Si había facturas pendientes, pide el cambio sin subrogación para que el contrato nuevo empiece desde cero.</p>
<h2>6. No comprobar el boletín en pisos vacíos</h2>
<p>Si el suministro está de baja, puede hacer falta un boletín eléctrico. Lo explicamos en la guía de <a href="@@guia-alta@@">alta de luz en un piso sin suministro</a>.</p>
<h2>7. Dejarlo en manos del cliente sin ayuda</h2>
<p>El cliente no conoce el proceso, y cuando algo falla, llama a la agencia. Delegarlo en un especialista ahorra llamadas y, además, puede generar un ingreso.</p>
{cta()}'''),
]

for g in GUIAS:
    page(lang=L, group=g["group"], path=f'guias/{g["slug"]}/', nav="guias",
         title=g["title"] + " | Gestión Energía", desc=g["desc"],
         article=dict(headline=g["h1"], date=D),
         body=page_hero(L, g["h1"], g["resumen"], crumbs=[("Guías", "@@guias@@"), (g["tag"], None)])
              + f'<section class="section"><div class="wrap"><article class="prose">{g["body"]}</article></div></section>')

cards = "".join(f'<a class="guia-card" href="@@{g["group"]}@@"><span class="tag">{g["tag"]}</span><h3>{g["h1"]}</h3><p>{g["resumen"]}</p></a>' for g in GUIAS)
page(lang=L, group="guias", path="guias/",
 title="Guías de luz y gas para inmobiliarias y administradores | Gestión Energía",
 desc="Guías prácticas sobre cambio de titular, altas de luz, boletín eléctrico, CUPS y suministros para expats, pensadas para inmobiliarias y administradores de fincas.",
 body=page_hero(L, "Guías de luz y gas <span>para el sector inmobiliario</span>",
   "Respuestas claras a las dudas de suministro que aparecen en cada compraventa y cada alquiler.", crumbs=[("Guías", None)])
 + f'<section class="section"><div class="wrap"><div class="guias-grid" style="margin-top:0">{cards}</div></div></section>' + cta_block(L))
