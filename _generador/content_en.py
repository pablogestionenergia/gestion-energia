from engine import *
from content_es import contact_page

L = "en"
NT = '<span class="sr-only"> (opens in a new tab)</span>'
WA_AG = "Hi Pablo, I run an estate agency and I'd like to talk about working with Gestión Energía."

def steps():
    return '''<ol class="pasos">
<li class="paso"><h3>You send us the client</h3><p>When you close a sale or a rental, you send us the buyer's or tenant's details.</p></li>
<li class="paso"><h3>We handle the utilities</h3><p>New connection, change of account holder or change of supplier for electricity and gas, on the tariff that fits best.</p></li>
<li class="paso"><h3>You earn your commission</h3><p>Your agency earns a commission for every new contract we handle. We let you know when everything is done.</p></li>
</ol>'''

page(lang=L, group="home", path="en/",
 title="Gestión Energía | Electricity and gas set-up for estate agencies in Spain",
 desc="We handle electricity and gas connections and changes of account holder for your property deals in Spain, and your agency earns a commission on every new contract.",
 body=f'''<section class="hero"><div class="hero-left on-dark">
<h1>Turn utilities<br>into <span>extra revenue</span></h1>
<p class="hero-text">A B2B service for estate agencies and property managers in Spain. We take care of the electricity and gas in every deal —new connections, changes of account holder and incidents— and your agency earns a commission on every new contract.</p>
<div class="hero-ctas"><a href="@@modelos@@" class="btn btn-oro">See partnership models</a>
<a href="{wa(WA_AG)}" class="btn btn-linea" target="_blank" rel="noopener">Chat on WhatsApp{NT}</a></div>
</div><div class="hero-right" aria-hidden="true"></div></section>
{logos_block(L)}
<section class="section beneficios"><div class="wrap">
<div class="center"><div class="eyebrow">Your energy partner</div>
<h2 class="section-title">You sell and let homes.<br>We take care of the rest.</h2>
<p class="section-lead">Switching the electricity and gas is the last thing an agent wants to deal with, and the first thing a tenant complains about when it goes wrong.</p></div>
<div class="cards-3">
<div class="card">{I_EURO}<h3>Commission on every contract</h3><p>A task that earns you nothing today becomes extra income for your agency, deal after deal.</p></div>
<div class="card">{I_CLOCK}<h3>No waiting on hold</h3><p>Forget supplier call centres. We handle connections and changes of account holder directly with the supplier.</p></div>
<div class="card">{I_SHIELD}<h3>Incidents solved</h3><p>If a tenant is left without supply, we deal with it. Your reputation stays safe.</p></div>
</div></div></section>
<section class="section"><div class="wrap"><div class="eyebrow">How we work</div>
<h2 class="section-title">Three steps, one contact</h2>
<p class="section-lead">No time on the phone with suppliers and no paperwork for your team. You close the deal; we get the utilities ready.</p>{steps()}</div></section>
<section class="section beneficios"><div class="wrap">
<div class="center"><div class="eyebrow">Who we work with</div><h2 class="section-title">Built for the property sector</h2></div>
<div class="cards-2">
<a class="card" href="@@agencias@@">{I_HOUSE}<h3>Estate agencies</h3><p>Sales and long-term rentals, including agencies letting to international tenants: they move in with utilities in their name.</p><span class="mas">Service for agencies →</span></a>
<a class="card" href="@@guia-expats@@">{I_GLOBE}<h3>Expat tenants</h3><p>What an international tenant needs to set up electricity and gas in Spain, and how the agency can help.</p><span class="mas">Read the guide →</span></a>
</div></div></section>
<section class="section modelos on-dark"><div class="wrap center">
<div class="eyebrow">Partnership models</div><h2 class="section-title">Choose how involved you want to be</h2>
<p class="section-lead">Hybrid: you bring the client, we handle the paperwork. Partner: your team processes contracts on our platform with our support.</p>
<p style="margin-top:30px"><a class="btn btn-oro" href="@@modelos@@">Compare both models</a></p></div></section>
{clients_block(L)}
{cta_block(L)}''')

FAQ_AG = [
 ("What does my agency need to do?", "Just send us the buyer's or tenant's details when you close the deal. We contact them, set up the utilities and let you know when it's done."),
 ("How does my agency get paid?", "Your agency earns a commission on every new contract we handle. The amount depends on the partnership model; I'll send it to you privately with a proposal tailored to your volume."),
 ("What if the property has no electricity?", "We request a new connection and tell you in advance whether an electrical installation certificate (boletín / CIE) or any other document is needed."),
 ("Do you work outside Barcelona?", "Yes. We work fully online with agencies all over Spain."),
]
page(lang=L, group="agencias", path="en/estate-agencies/", faq=FAQ_AG,
 title="Electricity and gas set-up for estate agencies | Gestión Energía",
 desc="New connections and changes of account holder for electricity and gas in every sale or rental in Spain. Your agency saves time and earns a commission on every contract.",
 body=page_hero(L, "Utilities ready in every deal, <span>plus a commission for your agency</span>",
   "When you close a sale or a rental, we put the utilities in the new client's name. Your team makes no calls and fills in no forms.",
   crumbs=[("Estate agencies", None)],
   ctas=f'<div class="hero-ctas"><a class="btn btn-oro" href="@@contacto@@">I want to partner</a><a class="btn btn-linea" href="{wa(WA_AG)}" target="_blank" rel="noopener">WhatsApp{NT}</a></div>')
 + f'''<section class="section"><div class="wrap"><div class="eyebrow">What we do for your agency</div>
<h2 class="section-title">Everything that happens with electricity and gas after signing</h2>
<div class="split"><div><ul class="checks">
<li><strong>Change of account holder</strong> for electricity and gas into the buyer's or tenant's name.</li>
<li><strong>New connections</strong> in properties with no supply or a cancelled contract.</li>
<li><strong>Change of supplier</strong> if another tariff suits the client better.</li>
<li><strong>Incidents</strong>: if the client is left without supply, we deal with the supplier.</li>
</ul></div>
<div class="box"><h3>Letting to expats?</h3><p>International tenants often stay for years but struggle with Spanish paperwork. We can set everything up before they arrive. Read our <a href="@@guia-expats@@" style="text-decoration:underline">guide to utilities for expat tenants</a>.</p></div>
</div></div></section>
<section class="section beneficios"><div class="wrap"><div class="eyebrow">How we work</div><h2 class="section-title">Three steps, one contact</h2>{steps()}</div></section>
{faq_block(L, FAQ_AG, "FAQ for estate agencies", "Common questions")}
{cta_block(L, WA_AG)}''')

page(lang=L, group="admin", path="en/property-managers/",
 title="Electricity and gas for property managers in Spain | Gestión Energía",
 desc="Changes of account holder and new electricity and gas connections in the buildings you manage in Spain, with no workload for your office and a commission on every contract.",
 body=page_hero(L, "Utilities in your buildings, <span>sorted without phone calls</span>",
   "When a new owner or tenant moves into a property you manage, we take care of the electricity and gas. Your office earns a commission on every new contract.",
   crumbs=[("Property managers", None)], ctas='<div class="hero-ctas"><a class="btn btn-oro" href="@@contacto@@">Get in touch</a></div>')
 + f'''<section class="section"><div class="wrap"><div class="split"><div><ul class="checks">
<li><strong>Changes of account holder</strong> when a home or commercial unit is sold or let.</li>
<li><strong>New connections</strong> for cancelled supplies, telling you in advance whether a certificate or inspection is needed.</li>
<li><strong>Incidents</strong> with the supplier, without your office spending time on the phone.</li>
</ul></div>
<div class="box"><h3>Fewer calls to your office</h3><p>Owners' and tenants' questions about electricity and gas often end up with the property manager. We answer them directly, and what used to be unpaid admin generates a commission for your office.</p></div>
</div></div></section>
{cta_block(L)}''')

page(lang=L, group="modelos", path="en/partnership-models/",
 title="Hybrid and Partner models | Gestión Energía",
 desc="Two ways to work with Gestión Energía: the Hybrid model (you bring the client, we handle the paperwork) and the Partner model (your team uses our platform).",
 body=page_hero(L, "Choose how involved <span>you want to be</span>", "Two ways to work with us, depending on your agency's team.", crumbs=[("Partnership models", None)])
 + f'''<section class="section modelos on-dark"><div class="wrap"><div class="modelos-grid" style="margin-top:0">
<div class="modelo"><div class="modelo-tag">Operational balance</div><h2 style="font-size:1.8rem;color:var(--verde);margin-bottom:14px">Hybrid model</h2>
<p class="modelo-intro">You focus on bringing in clients; we handle the paperwork.</p>
<div class="roles"><div class="rol"><strong>Your part</strong><span>Bringing in the client, basic admin and signature.</span></div>
<div class="rol"><strong>Our part</strong><span>All the technical work: connections and processing with the supplier.</span></div></div>
<div class="ideal"><strong>Ideal for</strong> agencies focused on closing deals fast that want smoother processes.</div>
<a href="{wa("Hi Pablo, I'd like to receive the terms of the Hybrid model.")}" class="btn btn-verde" target="_blank" rel="noopener">Request terms{NT}</a></div>
<div class="modelo"><div class="modelo-tag">Maximum return</div><h2 style="font-size:1.8rem;color:var(--verde);margin-bottom:14px">Partner model</h2>
<p class="modelo-intro">Your agency runs the whole process on our platform, with our support.</p>
<div class="roles"><div class="rol"><strong>Your part</strong><span>Processing contracts on our platform, admin and contract signing.</span></div>
<div class="rol"><strong>Our part</strong><span>The platform and ongoing technical support.</span></div></div>
<div class="ideal"><strong>Ideal for</strong> agencies with their own admin team that want to maximise margins.</div>
<a href="{wa("Hi Pablo, I'd like to receive the terms of the Partner model.")}" class="btn btn-verde" target="_blank" rel="noopener">Request terms{NT}</a></div>
</div><p class="modelos-nota">I'll send you the commission for each model privately, with a proposal tailored to your portfolio.</p></div></section>
{cta_block(L)}''')

page(lang=L, group="sobre", path="en/about/",
 title="Pablo Massera, founder of Gestión Energía",
 desc="Pablo Massera, founder of Gestión Energía: energy retail experience at the service of estate agencies and property managers in Spain.",
 body=page_hero(L, "One contact <span>who gets back to you</span>", "Meet the person behind Gestión Energía.", crumbs=[("About", None)])
 + f'''<section class="section"><div class="wrap sobre">
<div class="foto"><img src="{{R}}pablo.jpg" alt="Pablo Massera, founder of Gestión Energía" width="1024" height="1024"></div>
<div><div class="eyebrow">About me</div><h2 class="sobre-nombre">Pablo Massera</h2><div class="cargo">Founder · Gestión Energía</div>
<blockquote class="cita"><p>"My goal is for you to focus on selling homes while I make sure they have electricity and gas at the best price."</p></blockquote>
<p class="txt">I come from the energy retail sector and know from the inside how new connections, changes of account holder and incidents work. With Gestión Energía I put that experience at the service of estate agencies and property managers: one contact who gets back to you.</p>
<a class="linkedin-link" href="{LINKEDIN}" target="_blank" rel="noopener">{LI} Follow me on LinkedIn{NT}</a>
</div></div></section>
{cta_block(L)}''')

contact_page(L, "contacto", "en/contact/",
 "Contact | Gestión Energía", "Write to us using the form, on WhatsApp, by phone or by email and we'll send you a proposal for your agency or office.",
 "Let's talk about <span>your portfolio</span>", "Tell me how your agency or office works and I'll send you a tailored proposal with the terms.", "Contact",
 dict(subject="New contact from the website (EN)", name="Name", company="Agency or company", optional="(optional)", phone="Phone",
      type="I am…", types=["An estate agency","A property manager","Other"], message="Message",
      placeholder="For example: how many deals you close per month and where you operate.",
      consent='I have read and accept the <a href="@@privacidad@@">privacy policy</a> (in Spanish).', send="Send message",
      direct="Or get in touch directly", reply="I reply personally."),
 dict(invalid="Please check the required fields: name, email, message and the privacy box.", sending="Sending…",
      ok="Thank you! I've received your message and will reply as soon as possible.",
      err='The message could not be sent. Email me at <a href="mailto:' + EMAIL + '">' + EMAIL + '</a> or use WhatsApp.'))

# ---- Guía expats (EN) ----
page(lang=L, group="guia-expats", path="en/guides/utilities-for-expat-tenants/", nav="guias",
 title="Electricity and gas for expat tenants in Spain: what they need | Gestión Energía",
 desc="What an international tenant needs to put electricity and gas in their name in Spain, and how the letting agency can help: NIE or passport, bank account and language.",
 article=dict(headline="Electricity and gas for expat tenants in Spain", date=TODAY),
 body=page_hero(L, "Electricity and gas for expat tenants in Spain", "NIE or passport, bank account and language: how to get utilities in an international tenant's name.",
   crumbs=[("Guides", None)])
 + f'''<section class="section"><div class="wrap"><article class="prose">
<p class="meta">For agencies letting to expats · Updated November 2026 · <a href="@@es:guia-expats@@" hreflang="es">Leer en castellano</a></p>
<p>International tenants who come to Spain to work or live for a while are a great profile for an agency: they tend to stay for years. But dealing with Spanish energy suppliers, in another language and with different documents, can be frustrating. If the agency solves it for them, it gains a grateful client.</p>
<h2>Usual documents</h2>
<ul>
<li><strong>ID:</strong> NIE (foreigner identity number) if they already have it; if not, some suppliers accept a passport.</li>
<li><strong>A bank account (IBAN)</strong> for direct debit of the bills.</li>
<li><strong>Contact details:</strong> mobile number and email.</li>
<li>The property's <strong>CUPS</strong> (supply point code, shown on any previous bill) and sometimes the rental contract.</li>
</ul>
<h2>Common problems</h2>
<ul>
<li><strong>Language:</strong> contracts, calls and bills in Spanish.</li>
<li><strong>Timing:</strong> tenants arrive on a fixed date and need power from day one.</li>
<li><strong>Tariffs:</strong> they don't know the Spanish market and may end up on a tariff that doesn't suit them.</li>
</ul>
<h2>Change of account holder or new connection?</h2>
<p>If the property already has electricity, the contract just needs to be transferred to the tenant (a change of account holder), without cutting the supply. If the previous holder cancelled the contract, a new connection is needed, and an electrical installation certificate may be required in some cases.</p>
<h2>What the agency can do</h2>
<p>The simplest approach is to have the utilities set up before the tenant arrives and explain to them what has been contracted. Gestión Energía can do this for you, and your agency earns a commission on every new contract.</p>
<div class="cta-inline"><h2>Letting to expats?</h2><p>Send us your tenant's contact details and we'll put electricity and gas in their name before they arrive.</p>
<a class="btn btn-oro" href="@@contacto@@">Contact Gestión Energía</a></div>
</article></div></section>''')
