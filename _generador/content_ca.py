from engine import *
from content_es import contact_page

L = "ca"
NT = '<span class="sr-only"> (s\'obre en una pestanya nova)</span>'
WA_AG = "Hola Pablo, tinc una immobiliària i m'interessa col·laborar amb Gestión Energía."

def pasos():
    return '''<ol class="pasos">
<li class="paso"><h3>Ens passes el client</h3><p>Quan tanques una compravenda o un lloguer, ens envies les dades del comprador o de l'inquilí.</p></li>
<li class="paso"><h3>Tramitem el subministrament</h3><p>Alta, canvi de titular o canvi de companyia de llum i gas, amb la tarifa que millor encaixa.</p></li>
<li class="paso"><h3>Cobres la teva comissió</h3><p>Per cada alta gestionada, la teva agència rep la seva comissió. T'avisem quan tot està fet.</p></li>
</ol>'''

page(lang=L, group="home", path="ca/",
 title="Gestión Energía | Llum i gas per a immobiliàries i administradors de finques",
 desc="Gestionem les altes i els canvis de titular de llum i gas de les teves operacions immobiliàries i la teva agència cobra una comissió per cada alta. Servei B2B a tot l'Estat.",
 body=f'''<section class="hero"><div class="hero-left on-dark">
<h1>Converteix l'energia<br>en <span>Rendibilitat Neta</span></h1>
<p class="hero-text">Servei B2B per a immobiliàries i administradors de finques. Ens ocupem de la llum i el gas de cada operació —altes, canvis de titular i incidències— i la teva agència cobra una comissió per cada alta.</p>
<div class="hero-ctas"><a href="@@modelos@@" class="btn btn-oro">Veure models de col·laboració</a>
<a href="{wa(WA_AG)}" class="btn btn-linea" target="_blank" rel="noopener">Parlem per WhatsApp{NT}</a></div>
</div><div class="hero-right" aria-hidden="true"></div></section>
{logos_block(L)}
<section class="section beneficios"><div class="wrap">
<div class="center"><div class="eyebrow">El teu partner energètic</div>
<h2 class="section-title">Tu vens i llogues pisos.<br>Nosaltres ens ocupem de la resta.</h2>
<p class="section-lead">El canvi de llum i gas és l'últim que vol gestionar un agent, i el primer del qual es queixa un inquilí si falla.</p></div>
<div class="cards-3">
<div class="card">{I_EURO}<h3>Comissions per cada alta</h3><p>Un tràmit que avui no t'aporta res es converteix en un ingrés extra per a la teva agència, operació rere operació.</p></div>
<div class="card">{I_CLOCK}<h3>Zero temps d'espera</h3><p>Oblida't de les músiques d'espera de les companyies. Gestionem altes i canvis de titular directament amb la comercialitzadora.</p></div>
<div class="card">{I_SHIELD}<h3>Incidències resoltes</h3><p>Si un inquilí es queda sense subministrament, ens n'ocupem nosaltres. La teva reputació queda a resguard.</p></div>
</div></div></section>
<section class="section"><div class="wrap"><div class="eyebrow">Com treballem</div>
<h2 class="section-title">Tres passos, un sol contacte</h2>
<p class="section-lead">Sense esperes al telèfon de la companyia ni paperassa per al teu equip. Tu tanques l'operació; nosaltres deixem els subministraments a punt.</p>{pasos()}</div></section>
<section class="section beneficios"><div class="wrap">
<div class="center"><div class="eyebrow">Per a qui treballem</div><h2 class="section-title">Un servei pensat per al sector immobiliari</h2></div>
<div class="cards-2">
<a class="card" href="@@agencias@@">{I_HOUSE}<h3>Immobiliàries</h3><p>Compravendes i lloguers de llarga durada: el comprador o l'inquilí entra a viure amb la llum i el gas al seu nom, i la teva agència cobra per cada alta.</p><span class="mas">Veure el servei per a immobiliàries →</span></a>
<a class="card" href="@@admin@@">{I_BUILD}<h3>Administradors de finques</h3><p>Cada canvi de propietari o d'inquilí a les finques que gestiones, resolt sense que el teu despatx hagi de trucar a cap companyia.</p><span class="mas">Veure el servei per a administradors →</span></a>
</div></div></section>
<section class="section modelos on-dark"><div class="wrap center">
<div class="eyebrow">Models de col·laboració</div><h2 class="section-title">Tria quant vols implicar-te</h2>
<p class="section-lead">Model Híbrid: tu captes i nosaltres tramitem. Model Partner: el teu equip tramita amb la nostra plataforma i el nostre suport.</p>
<p style="margin-top:30px"><a class="btn btn-oro" href="@@modelos@@">Comparar els dos models</a></p></div></section>
{clients_block(L)}
{cta_block(L)}''')

FAQ_AG = [
 ("Què ha de fer la meva agència?", "Només passar-nos les dades del comprador o de l'inquilí quan tanques l'operació. Nosaltres hi parlem, tramitem el subministrament i t'avisem quan està fet."),
 ("Com cobra la meva agència?", "La teva agència rep una comissió per cada alta que gestionem. L'import depèn del model de col·laboració i te l'envio en privat amb una proposta adaptada al teu volum."),
 ("Què passa si el pis no té llum o el subministrament està donat de baixa?", "Tramitem l'alta. Abans et diem si cal butlletí elèctric (CIE) o algun altre document, perquè no hi hagi sorpreses el dia de l'entrega de claus."),
 ("Amb quines comercialitzadores treballeu?", "Amb les principals del mercat (Endesa, Naturgy, Iberdrola, Repsol, TotalEnergies) i moltes més. Triem la tarifa que millor encaixa amb cada client."),
 ("Treballeu fora de Barcelona?", "Sí. Treballem 100 % en línia i atenem immobiliàries de tot l'Estat."),
]
page(lang=L, group="agencias", path="ca/immobiliaries/", faq=FAQ_AG,
 title="Gestió de llum i gas per a immobiliàries | Gestión Energía",
 desc="Altes i canvis de titular de llum i gas a cada compravenda o lloguer. La teva agència no perd temps amb les companyies i cobra una comissió per cada alta.",
 body=page_hero(L, "Llum i gas a punt a cada operació, <span>i una comissió per a la teva agència</span>",
   "Quan tanques una compravenda o un lloguer, nosaltres posem els subministraments a nom del client nou. El teu equip no fa trucades ni paperassa.",
   crumbs=[("Immobiliàries", None)],
   ctas=f'<div class="hero-ctas"><a class="btn btn-oro" href="@@contacto@@">Vull col·laborar</a><a class="btn btn-linea" href="{wa(WA_AG)}" target="_blank" rel="noopener">WhatsApp{NT}</a></div>')
 + f'''<section class="section"><div class="wrap"><div class="eyebrow">Què fem per la teva agència</div>
<h2 class="section-title">Tot el que passa amb la llum i el gas després de signar</h2>
<div class="split"><div><ul class="checks">
<li><strong>Canvi de titular</strong> de llum i gas a nom del comprador o de l'inquilí.</li>
<li><strong>Alta de subministrament</strong> en pisos sense llum o amb el contracte donat de baixa.</li>
<li><strong>Canvi de comercialitzadora</strong> si al client li convé una altra tarifa.</li>
<li><strong>Incidències</strong>: si el client es queda sense subministrament, parlem nosaltres amb la companyia.</li>
<li><strong>Seguiment</strong>: t'avisem quan tot està fet.</li>
</ul></div>
<div class="box"><h3>Operacions en què encaixem</h3><p>Compravendes i lloguers de llarga durada, que és on canvia el titular del subministrament. També treballem amb agències que lloguen a inquilins estrangers, que s'hi queden anys i necessiten que algú els resolgui el tràmit.</p></div>
</div></div></section>
<section class="section beneficios"><div class="wrap"><div class="eyebrow">Com treballem</div><h2 class="section-title">Tres passos, un sol contacte</h2>{pasos()}</div></section>
{faq_block(L, FAQ_AG, "Preguntes freqüents d'immobiliàries", "Dubtes habituals")}
{cta_block(L, WA_AG)}''')

FAQ_AD = [
 ("En quins casos ens podeu ajudar?", "Cada vegada que canvia el propietari o l'inquilí d'un habitatge o local que gestiones i cal posar la llum o el gas a nom de la persona nova, o donar d'alta un subministrament que estava de baixa."),
 ("Té cost per al despatx?", "No: el teu despatx rep una comissió per cada alta que gestionem. Les condicions te les envio en privat."),
 ("Qui parla amb el propietari o l'inquilí?", "Nosaltres. Tu només ens facilites el contacte i et mantenim informat."),
]
page(lang=L, group="admin", path="ca/administradors-de-finques/", faq=FAQ_AD,
 title="Llum i gas per a administradors de finques | Gestión Energía",
 desc="Canvis de titular i altes de llum i gas a les finques que administres, sense càrrega per al teu despatx i amb comissió per cada alta.",
 body=page_hero(L, "Els subministraments de les teves finques, <span>resolts sense trucades</span>",
   "Quan entra un propietari o un inquilí nou en una finca que administres, ens ocupem de la llum i el gas. El teu despatx cobra una comissió per cada alta.",
   crumbs=[("Administradors de finques", None)],
   ctas='<div class="hero-ctas"><a class="btn btn-oro" href="@@contacto@@">Demanar informació</a></div>')
 + f'''<section class="section"><div class="wrap"><div class="eyebrow">Què fem</div>
<h2 class="section-title">Un interlocutor per a tots els canvis de subministrament</h2>
<div class="split"><div><ul class="checks">
<li><strong>Canvis de titular</strong> de llum i gas quan es ven o es lloga un habitatge o un local.</li>
<li><strong>Altes</strong> de subministraments donats de baixa, avisant abans de si cal butlletí o revisió.</li>
<li><strong>Incidències</strong> amb la comercialitzadora, sense que el teu despatx hagi d'estar al telèfon.</li>
</ul></div>
<div class="box"><h3>Menys trucades al teu despatx</h3><p>Els dubtes de llum i gas de propietaris i inquilins acaben sovint al telèfon de l'administrador. Nosaltres els resolem directament amb ells, i el que abans era una gestió sense retorn genera una comissió per al teu despatx.</p></div>
</div></div></section>
{faq_block(L, FAQ_AD, "Preguntes freqüents d'administradors", "Dubtes habituals")}
{cta_block(L)}''')

page(lang=L, group="modelos", path="ca/models-de-collaboracio/",
 title="Models de col·laboració Híbrid i Partner | Gestión Energía",
 desc="Dues maneres de col·laborar amb Gestión Energía: Model Híbrid (tu captes, nosaltres tramitem) i Model Partner (el teu equip tramita amb la nostra plataforma).",
 body=page_hero(L, "Tria quant vols <span>implicar-te</span>", "Dues maneres de treballar amb nosaltres, segons l'equip que tingui la teva agència o el teu despatx.", crumbs=[("Models de col·laboració", None)])
 + f'''<section class="section modelos on-dark"><div class="wrap"><div class="modelos-grid" style="margin-top:0">
<div class="modelo"><div class="modelo-tag">Equilibri operatiu</div><h2 style="font-size:1.8rem;color:var(--verde);margin-bottom:14px">Model Híbrid</h2>
<p class="modelo-intro">Tu et centres en la captació comercial; nosaltres ens ocupem de la tramitació.</p>
<div class="roles"><div class="rol"><strong>La teva part</strong><span>Captar el client, l'administració bàsica i la signatura.</span></div>
<div class="rol"><strong>La nostra part</strong><span>Tota l'operació tècnica: altes i tramitació amb la comercialitzadora.</span></div></div>
<div class="ideal"><strong>Ideal per a</strong> immobiliàries centrades a tancar operacions ràpid que volen agilitzar processos.</div>
<a href="{wa("Hola Pablo, m'agradaria rebre les condicions del Model Híbrid.")}" class="btn btn-verde" target="_blank" rel="noopener">Demanar condicions{NT}</a></div>
<div class="modelo"><div class="modelo-tag">Màxima rendibilitat</div><h2 style="font-size:1.8rem;color:var(--verde);margin-bottom:14px">Model Partner</h2>
<p class="modelo-intro">La teva agència porta tota l'operativa amb la nostra plataforma i el nostre suport.</p>
<div class="roles"><div class="rol"><strong>La teva part</strong><span>Tramitar les altes des de la nostra plataforma, l'administració i la signatura de contractes.</span></div>
<div class="rol"><strong>La nostra part</strong><span>La plataforma i el suport tècnic continu.</span></div></div>
<div class="ideal"><strong>Ideal per a</strong> agències amb equip administratiu propi que volen maximitzar els marges.</div>
<a href="{wa("Hola Pablo, m'agradaria rebre les condicions del Model Partner.")}" class="btn btn-verde" target="_blank" rel="noopener">Demanar condicions{NT}</a></div>
</div><p class="modelos-nota">Les comissions de cada model te les envio en privat, amb una proposta adaptada a la teva cartera.</p></div></section>
{cta_block(L)}''')

page(lang=L, group="sobre", path="ca/sobre-mi/",
 title="Pablo Massera, fundador de Gestión Energía",
 desc="Pablo Massera, fundador de Gestión Energía: experiència en comercialització energètica al servei d'immobiliàries i administradors de finques.",
 body=page_hero(L, "Un únic interlocutor <span>que respon</span>", "Coneix qui hi ha darrere de Gestión Energía.", crumbs=[("Sobre mi", None)])
 + f'''<section class="section"><div class="wrap sobre">
<div class="foto"><img src="{{R}}pablo.jpg" alt="Pablo Massera, fundador de Gestión Energía" width="1024" height="1024"></div>
<div><div class="eyebrow">Sobre mi</div><h2 class="sobre-nombre">Pablo Massera</h2><div class="cargo">Fundador · Gestión Energía</div>
<blockquote class="cita"><p>«El meu objectiu és que tu et dediquis a vendre pisos, mentre jo m'ocupo que tinguin llum i gas al millor preu.»</p></blockquote>
<p class="txt">Vinc del sector de la comercialització energètica i conec per dins com funcionen les altes, els canvis de titular i les incidències. Amb Gestión Energía poso aquesta experiència al servei d'immobiliàries i administradors de finques: un únic interlocutor que respon.</p>
<a class="linkedin-link" href="{LINKEDIN}" target="_blank" rel="noopener">{LI} Segueix-me a LinkedIn{NT}</a>
</div></div></section>
{cta_block(L)}''')

contact_page(L, "contacto", "ca/contacte/",
 "Contacte | Gestión Energía", "Escriu-nos des del formulari, per WhatsApp, per telèfon o per email i t'enviem una proposta per a la teva immobiliària o despatx.",
 "Parlem de <span>la teva cartera</span>", "Explica'm com treballa la teva agència o el teu despatx i t'envio una proposta personalitzada amb les condicions.", "Contacte",
 dict(subject="Nou contacte des de la web (CA)", name="Nom", company="Agència o empresa", optional="(opcional)", phone="Telèfon",
      type="Soc…", types=["Immobiliària","Administrador de finques","Altre"], message="Missatge",
      placeholder="Per exemple: quantes operacions tanqueu al mes i en quina zona treballeu.",
      consent='He llegit i accepto la <a href="@@privacidad@@">política de privacitat</a> (en castellà).', send="Enviar missatge",
      direct="O contacta directament", reply="Responc personalment."),
 dict(invalid="Revisa els camps obligatoris: nom, email, missatge i la casella de privacitat.", sending="Enviant…",
      ok="Gràcies! He rebut el teu missatge i et respondré al més aviat possible.",
      err="No s'ha pogut enviar. Escriu-me a <a href=\"mailto:" + EMAIL + "\">" + EMAIL + "</a> o per WhatsApp."))
