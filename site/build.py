#!/usr/bin/env python3
"""Supreme Clean Detailing — zero-dependency static site generator.

Usage:  python3 site/build.py          (writes the site into ./public)

Design goals (from research/az-detailing-market-teardown.md):
  * 0 JavaScript, 1 CSS file, system font stack  -> beats every competitor's CWV
  * price + proof + book visible on every page
  * LocalBusiness/Service/FAQPage/Breadcrumb JSON-LD sitewide
  * tel: AND sms: CTAs (only one competitor in the market has click-to-text)
"""
from __future__ import annotations

import html as H
import json
import re
import shutil
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT.parent / "public"

# ---------------------------------------------------------------- business ---
SITE_URL = "https://supremecleandetailingpro.com"

# GoHighLevel booking calendar — renders on /book/ with the request form as
# fallback. primaryColor set to brand aqua 5FB8C4 (the link's original
# 9F0E13 red clashes with the site palette; swap the param back if the red
# was intentional).
GHL_CALENDAR_URL = (
    "https://api.leadconnectorhq.com/widget/booking/vkmRhebji6NFtGUXYuxl"
    "?backgroundColor=%23ffffff&primaryColor=%235FB8C4"
    "&buttonText=Schedule+Appointment&showCalendarTitle=true"
    "&showCalendarDescription=true&showCalendarDetails=true&default=false"
)

# Google Analytics 4 (gtag.js) — injected near the top of <head> on every page
# via the shared render_page() template. This is the site's one sitewide
# external script; it is async, so it does not block render.
GA_SNIPPET = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-LY3BJ5ZR2N"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-LY3BJ5ZR2N');
</script>"""

# Meta (Facebook) Pixel — injected in <head> on every page via render_page().
# Async loader (fbevents.js), so it does not block render.
META_PIXEL = """<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '919522911215586');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=919522911215586&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->"""

# Real, owner-confirmed pricing is live (Anthony's July 2025 list, raised 5% and
# rounded to clean $5s). Re-enables Service/AggregateOffer + priceRange schema.
PRICES_LIVE = True
BIZ = {
    "name": "Supreme Clean Detailing",
    "owner": "Anthony",
    "phone_display": "(520) 840-2452",
    "phone_e164": "+15208402452",
    "email": "supremecleandetailing01@gmail.com",
    "street": "1746 E Wildflower Ln",          # matches Google Business Profile
    "city": "Casa Grande",
    "region": "AZ",
    "zip": "85122",
    "rating": "5.0",
    "review_count": "20",
    "hours_human": "Mon–Sat 8:00 AM – 6:00 PM",
    "hours_schema": ["Mo-Sa 08:00-18:00"],
    # Owner's real Google Business Profile (share link) — powers "Find us on
    # Google", the rating link, and schema sameAs.
    "gbp_url": "https://share.google/82HKSp4gcInryGLCi",
    # TODO(owner): swap for the direct "write a review" deep link from the GBP
    # dashboard when available; the listing link works (reviews are one tap in).
    "review_url": "https://share.google/82HKSp4gcInryGLCi",
    "instagram": "https://www.instagram.com/supremeclean__detailing/",
    "tiktok": "https://www.tiktok.com/@supremecleancardetailing",
}
CURRENT_YEAR = date.today().year

CITIES_SERVED = [
    ("Casa Grande", "/car-detailing-casa-grande-az/"),
    ("Maricopa", "/car-detailing-maricopa-az/"),
    ("Eloy", "/car-detailing-eloy-az/"),
    ("Coolidge", "/car-detailing-coolidge-az/"),
    ("Florence", "/car-detailing-florence-az/"),
    ("Arizona City", "/car-detailing-arizona-city-az/"),
    ("San Tan Valley", "/car-detailing-san-tan-valley-az/"),
    ("Queen Creek", "/car-detailing-queen-creek-az/"),
]

SERVICES_NAV = [
    ("Full Detail", "/services/full-detail/"),
    ("Interior Deep Clean", "/services/interior-detailing/"),
    ("Exterior Wash & Shine", "/services/exterior-detailing/"),
    ("Odor Removal", "/services/odor-removal/"),
    ("Pet Hair Removal", "/services/pet-hair-removal/"),
    ("Headlight Restoration", "/services/headlight-restoration/"),
    ("Fleet & Business", "/services/fleet-detailing/"),
]

# ------------------------------------------------------------------- icons ---
ICONS = {
    "star": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2l2.9 6.26 6.6.7-4.95 4.5 1.4 6.54L12 16.77 6.05 20l1.4-6.54L2.5 8.96l6.6-.7z"/></svg>',
    "pin": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5z"/></svg>',
    "phone": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6.6 10.8a15.6 15.6 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.58 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1 11.4 11.4 0 0 0 .57 3.6 1 1 0 0 1-.25 1z"/></svg>',
    "chat": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 4h16a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H8l-5 4V6a2 2 0 0 1 2-2zm3 5h10v2H7z"/></svg>',
    "check": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z"/></svg>',
    "shield": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2 4 5v6c0 5 3.4 9.7 8 11 4.6-1.3 8-6 8-11V5z"/></svg>',
    "clock": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2zm1 11H7v-2h4V6h2z"/></svg>',
    "truck": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M3 5h11v10H3zM14 8h4l3 3v4h-7zM6 19a2 2 0 1 1 2-2 2 2 0 0 1-2 2zm11 0a2 2 0 1 1 2-2 2 2 0 0 1-2 2z"/></svg>',
    "sparkle": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2l1.8 5.6L19 9l-5.2 1.7L12 16l-1.8-5.3L5 9l5.2-1.4zM19 15l.9 2.6L22 19l-2.1.9L19 22l-.9-2.1L16 19l2.1-1.4zM5 14l.7 2 2 .7-2 .9L5 20l-.7-2.4L2 16.7l2.3-.7z"/></svg>',
    "seat": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M7 3h6l-1 9h6a2 2 0 0 1 2 2v2h-2v-1H8a3 3 0 0 1-3-3V6a3 3 0 0 1 2-2.8zM5 18h14v3H5z"/></svg>',
    "paw": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><circle fill="currentColor" cx="6" cy="9" r="2"/><circle fill="currentColor" cx="10" cy="5.5" r="2"/><circle fill="currentColor" cx="14" cy="5.5" r="2"/><circle fill="currentColor" cx="18" cy="9" r="2"/><path fill="currentColor" d="M12 10c3 0 6 3.2 6 6a3 3 0 0 1-3 3c-1.2 0-2.1-.5-3-.5s-1.8.5-3 .5a3 3 0 0 1-3-3c0-2.8 3-6 6-6z"/></svg>',
    "beam": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M14 5a7 7 0 0 0 0 14c4 0 7-3 8-7-1-4-4-7-8-7zm0 10a3 3 0 1 1 3-3 3 3 0 0 1-3 3zM2 8h6v2H2zm0 6h6v2H2zm2-3h5v2H4z"/></svg>',
    "drop": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2s7 7.6 7 12.5a7 7 0 0 1-14 0C5 9.6 12 2 12 2z"/></svg>',
    "nose": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 3c2 4 5 5.5 5 9.5a5 5 0 0 1-10 0C7 8.5 10 7 12 3zm-6 15c1.5 2 3.7 3 6 3s4.5-1 6-3l-1.6-1.2A5.9 5.9 0 0 1 12 19a5.9 5.9 0 0 1-4.4-2.2z"/></svg>',
    "cash": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M2 6h20v12H2zm10 2.5A3.5 3.5 0 1 0 15.5 12 3.5 3.5 0 0 0 12 8.5zM4 8a2 2 0 0 1-2 2V8zm18 0v2a2 2 0 0 1-2-2zM2 14a2 2 0 0 1 2 2H2zm20 0v2h-2a2 2 0 0 1 2-2z"/></svg>',
    "instagram": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.3 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.3 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.3-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.3-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 1.8c-3.1 0-3.5 0-4.7.1-1.1.1-1.7.2-2.1.4-.5.2-.9.4-1.3.8-.4.4-.6.8-.8 1.3-.2.4-.3 1-.4 2.1C2.6 9.9 2.6 10.3 2.6 12s0 2.1.1 3.3c.1 1.1.2 1.7.4 2.1.2.5.4.9.8 1.3.4.4.8.6 1.3.8.4.2 1 .3 2.1.4 1.2.1 1.6.1 4.7.1s3.5 0 4.7-.1c1.1-.1 1.7-.2 2.1-.4.5-.2.9-.4 1.3-.8.4-.4.6-.8.8-1.3.2-.4.3-1 .4-2.1.1-1.2.1-1.6.1-4.7s0-2.1-.1-3.3c-.1-1.1-.2-1.7-.4-2.1-.2-.5-.4-.9-.8-1.3-.4-.4-.8-.6-1.3-.8-.4-.2-1-.3-2.1-.4C15.5 4 15.1 4 12 4zm0 3.1a4.9 4.9 0 1 0 0 9.8 4.9 4.9 0 0 0 0-9.8zm0 8.1a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4zm6.2-8.3a1.15 1.15 0 1 1-2.3 0 1.15 1.15 0 0 1 2.3 0z"/></svg>',
    "tiktok": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M16.7 5.8a4.8 4.8 0 0 1-1.4-3.8h-3.1v13c0 1.5-1.2 2.7-2.7 2.7A2.7 2.7 0 0 1 7.5 12c.3 0 .6 0 .9.1V9c-.3 0-.6-.1-.9-.1A5.6 5.6 0 1 0 13.1 14.6V8.1a7.7 7.7 0 0 0 4.5 1.4V6.4a4.8 4.8 0 0 1-.9-.6z"/></svg>',
    "google": '<svg class="ic" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M21.6 12.2c0-.7-.1-1.3-.2-1.9H12v3.7h5.4c-.2 1.2-.9 2.3-2 3v2.5h3.2c1.9-1.7 3-4.3 3-7.3z"/><path fill="currentColor" d="M12 22c2.7 0 5-.9 6.6-2.5l-3.2-2.5c-.9.6-2 1-3.4 1-2.6 0-4.8-1.8-5.6-4.1H3.1v2.6A10 10 0 0 0 12 22z"/><path fill="currentColor" d="M6.4 13.9c-.2-.6-.3-1.2-.3-1.9s.1-1.3.3-1.9V7.5H3.1a10 10 0 0 0 0 9l3.3-2.6z"/><path fill="currentColor" d="M12 6c1.5 0 2.8.5 3.8 1.5l2.8-2.8A10 10 0 0 0 3.1 7.5l3.3 2.6C7.2 7.8 9.4 6 12 6z"/></svg>',
}


def icon(name: str) -> str:
    return ICONS.get(name, ICONS["sparkle"])


LOGO = (
    '<span class="logo" aria-hidden="true">'
    '<svg viewBox="0 0 40 40" width="30" height="30" fill="none">'
    '<path d="M20 4 C 26 14, 32 18, 32 26 a12 12 0 0 1 -24 0 c0-8 6-12 12-22z" '
    'stroke="#9fe0e8" stroke-width="1.4" fill="rgba(159,224,232,.09)"/>'
    '<circle cx="20" cy="26" r="3" fill="#9fe0e8"/>'
    "</svg></span>"
)

SIG_CAR_SVG = """<svg viewBox="0 0 400 160" class="sig-car" role="img" aria-label="Illustration of a freshly detailed car with water beading on the paint">
<defs>
<linearGradient id="sigbody" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#cfe7ea" stop-opacity=".9"/>
<stop offset="100%" stop-color="#5fb8c4" stop-opacity=".4"/>
</linearGradient>
<linearGradient id="sigglass" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="#9fe0e8" stop-opacity=".7"/>
<stop offset="100%" stop-color="#11484f" stop-opacity=".6"/>
</linearGradient>
</defs>
<path d="M40,110 C60,70 100,55 160,52 C200,50 220,40 250,40 C300,40 330,55 360,75 L380,95 C388,100 390,108 388,115 L380,120 L350,120 L340,128 L320,128 L310,120 L100,120 L90,128 L70,128 L60,120 L40,118 C32,116 30,112 40,110 Z" fill="url(#sigbody)" stroke="rgba(243,249,250,.4)" stroke-width="1"/>
<path d="M120,75 C150,55 200,50 260,55 L290,75 L260,95 L150,95 Z" fill="url(#sigglass)" opacity=".85"/>
<circle cx="95" cy="120" r="18" fill="#061821" stroke="#5fb8c4" stroke-width="1.5"/>
<circle cx="95" cy="120" r="7" fill="#9fe0e8"/>
<circle cx="305" cy="120" r="18" fill="#061821" stroke="#5fb8c4" stroke-width="1.5"/>
<circle cx="305" cy="120" r="7" fill="#9fe0e8"/>
<circle cx="200" cy="70" r="3" fill="rgba(255,255,255,.7)"/>
<circle cx="180" cy="85" r="2" fill="rgba(255,255,255,.5)"/>
<circle cx="230" cy="78" r="2.5" fill="rgba(255,255,255,.6)"/>
</svg>"""

# deterministic ambient bubbles (size px, left %, duration s, delay s)
BUBBLES = [
    (9, 6, 14, 0), (22, 14, 19, 4), (7, 22, 12, 8), (30, 31, 22, 2),
    (12, 44, 16, 10), (18, 55, 20, 6), (8, 63, 13, 12), (26, 72, 21, 1),
    (10, 81, 15, 9), (34, 89, 24, 5), (14, 95, 17, 13), (6, 37, 11, 15),
]


def bubbles_html() -> str:
    spans = "".join(
        f'<span class="bubble" style="width:{s}px;height:{s}px;left:{l}%;'
        f'animation-duration:{d}s;animation-delay:{y}s"></span>'
        for s, l, d, y in BUBBLES
    )
    return f'<div class="bubbles" aria-hidden="true">{spans}</div>'


def wash_html() -> str:
    """Homepage-only 'clean beginning' intro wash — falling droplets + a squeegee
    blade wipe over the brand mark. Content renders behind it (SEO intact); it
    auto-dismisses (CSS fallback + JS), plays once per session, and is skippable."""
    import random

    rnd = random.Random(7)  # seeded -> identical output every build
    drops = "".join(
        f'<span class="droplet" style="left:{rnd.uniform(1,99):.1f}%;'
        f'height:{rnd.uniform(8,22):.0f}px;'
        f'animation-duration:{rnd.uniform(1.1,2.6):.2f}s;'
        f'animation-delay:{rnd.uniform(0,1.2):.2f}s;'
        f'opacity:{rnd.uniform(.35,.9):.2f}"></span>'
        for _ in range(40)
    )
    return (
        '<div id="wash" aria-hidden="true"><div class="blade"></div>'
        f"{drops}"
        '<div class="wash-in">'
        '<p class="eyebrow">Supreme Clean Detailing · Casa Grande, AZ</p>'
        '<h1>A clean <em>beginning</em>.</h1>'
        '<p>The water, the foam, and the patience of a perfect finish — brought to your driveway.</p>'
        "</div>"
        '<button type="button" class="wash-skip" aria-label="Skip intro">Skip intro</button>'
        "</div>"
    )


WASH_JS = (
    "<script>(function(){var w=document.getElementById('wash');if(!w)return;"
    "var m=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;"
    "function d(){w.classList.add('gone');document.documentElement.style.overflow='';"
    "setTimeout(function(){w.style.display='none';},600);}"
    "if(m||sessionStorage.getItem('scd_intro')){w.style.display='none';return;}"
    "try{sessionStorage.setItem('scd_intro','1');}catch(e){}"
    "document.documentElement.style.overflow='hidden';"
    "var b=w.querySelector('.wash-skip');if(b)b.addEventListener('click',d);"
    "setTimeout(d,3400);})();</script>"
)

# ----------------------------------------------------------------- helpers ---


def esc(s: str) -> str:
    return H.escape(s, quote=True)


def slug_url(slug: str) -> str:
    return "/" if slug == "" else f"/{slug.strip('/')}/"


def stars(n: int = 5) -> str:
    return f'<span class="stars" aria-label="{n} out of 5 stars">' + icon("star") * n + "</span>"


# ---------------------------------------------------------------- sections ---


def s_trustbar(d) -> str:
    items = "".join(f'<li>{icon(i.get("icon","check"))}<span>{i["text"]}</span></li>' for i in d["items"])
    return f'<section class="trustbar" aria-label="Why choose us"><ul class="wrap">{items}</ul></section>'


def s_cards(d) -> str:
    cards = []
    for it in d["items"]:
        inner = (
            f'<div class="card-ic">{icon(it.get("icon","sparkle"))}</div>'
            f'<h3>{it["title"]}</h3><p>{it["text"]}</p>'
        )
        if it.get("price"):
            inner += f'<p class="card-price">{it["price"]}</p>'
        if it.get("href"):
            cards.append(f'<a class="card" href="{it["href"]}">{inner}<span class="card-link">Learn more →</span></a>')
        else:
            cards.append(f'<div class="card">{inner}</div>')
    head = section_head(d)
    return f'<section class="sec"><div class="wrap">{head}<div class="grid g3">{"".join(cards)}</div></div></section>'


def s_pricing(d) -> str:
    tiers = []
    for t in d["tiers"]:
        # each price row is (size_label, price) or (size_label, price, was_price)
        rows = ""
        for row in t["prices"]:
            label, price = row[0], row[1]
            was = f'<span class="p-was">{row[2]}</span>' if len(row) > 2 and row[2] else ""
            rows += (
                f'<div class="p-row"><span>{label}</span>'
                f'<span class="p-price">{was}<strong>{price}</strong></span></div>'
            )
        inc = "".join(f"<li>{icon('check')}{x}</li>" for x in t.get("includes", []))
        badge = '<span class="badge">Most popular</span>' if t.get("popular") else ""
        time_line = f'<p class="p-time">{icon("clock")} {t["time"]}</p>' if t.get("time") else ""
        save_line = f'<p class="p-save">{icon("sparkle")}<span>{t["save"]}</span></p>' if t.get("save") else ""
        tiers.append(
            f'<div class="tier{" tier-pop" if t.get("popular") else ""}">{badge}'
            f'<h3>{t["name"]}</h3><p class="p-tag">{t["tagline"]}</p>'
            f'<div class="p-rows">{rows}</div>{time_line}{save_line}'
            f'<ul class="p-inc">{inc}</ul>'
            f'<a class="btn btn-primary" href="/book/">Book this detail</a></div>'
        )
    note = f'<p class="p-note">{d["note"]}</p>' if d.get("note") else ""
    head = section_head(d)
    # grid columns follow tier count: 1 -> centered solo, 2 -> pair, 4 -> quad, else 3
    grid = {1: "tiers-solo", 2: "g2 tiers", 4: "g4 tiers"}.get(len(d["tiers"]), "g3 tiers")
    return f'<section class="sec" id="pricing"><div class="wrap">{head}<div class="grid {grid}">{"".join(tiers)}</div>{note}</div></section>'


def s_addons(d) -> str:
    rows = "".join(
        f'<div class="addon"><div><h3>{n}</h3><p>{desc}</p></div><strong>{p}</strong></div>'
        for n, p, desc in d["items"]
    )
    head = section_head(d)
    return f'<section class="sec sec-alt"><div class="wrap">{head}<div class="grid g2 addons">{rows}</div></div></section>'


def s_steps(d) -> str:
    steps = "".join(
        f'<li><span class="step-n">{i+1}</span><div><h3>{t}</h3><p>{x}</p></div></li>'
        for i, (t, x) in enumerate(d["items"])
    )
    head = section_head(d)
    return f'<section class="sec"><div class="wrap">{head}<ol class="steps">{steps}</ol></div></section>'


def s_reviews(d) -> str:
    cards = "".join(
        f'<figure class="rev">{stars()}<blockquote>“{q}”</blockquote>'
        f"<figcaption><strong>{a}</strong><span>{m}</span></figcaption></figure>"
        for q, a, m in d["items"]
    )
    link = (
        f'<p class="center"><a class="btn btn-ghost" href="{d["all_link"]}">Read all {BIZ["review_count"]} Google reviews →</a></p>'
        if d.get("all_link")
        else ""
    )
    head = section_head(d)
    return f'<section class="sec sec-dark" id="reviews"><div class="wrap">{head}<div class="grid g3">{cards}</div>{link}</div></section>'


def s_faq(d) -> str:
    items = "".join(
        f"<details><summary>{q}</summary><div class=\"faq-a\">{a}</div></details>" for q, a in d["items"]
    )
    head = section_head(d)
    return f'<section class="sec" id="faq"><div class="wrap wrap-nar">{head}{items}</div></section>'


def s_prose(d) -> str:
    head = f'<h2>{d["title"]}</h2>' if d.get("title") else ""
    return f'<section class="sec"><div class="wrap wrap-nar prose">{head}{d["html"]}</div></section>'


def s_cta(d) -> str:
    sub = f"<p>{d['sub']}</p>" if d.get("sub") else ""
    return (
        '<section class="cta-band"><div class="wrap">'
        f'<h2>{d["title"]}</h2>{sub}'
        '<div class="hero-ctas">'
        f'<a class="btn btn-primary btn-lg" href="/book/">Get my price &amp; book</a>'
        f'<a class="btn btn-light btn-lg" href="tel:{BIZ["phone_e164"]}">{icon("phone")} Call {BIZ["phone_display"]}</a>'
        f'<a class="btn btn-light btn-lg" href="sms:{BIZ["phone_e164"]}">{icon("chat")} Text a photo for a quote</a>'
        "</div></div></section>"
    )


def s_areas(d) -> str:
    cities = "".join(f'<a class="chip" href="{href}">{icon("pin")}{name}</a>' for name, href in d["cities"])
    head = section_head(d)
    return f'<section class="sec sec-alt" id="areas"><div class="wrap">{head}<div class="chips">{cities}</div></div></section>'


def s_gallery_ph(d) -> str:
    """Photo-drop pipeline: put JPG/PNG/WebP files in site/assets/gallery/ and
    rebuild — they render automatically (alt text from the filename, e.g.
    'interior-deep-clean-f150-before-after.jpg'). Until then: labelled slots."""
    gal = ROOT / "assets" / "gallery"
    photos = sorted(p for p in gal.glob("*") if p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}) if gal.exists() else []
    if photos:
        tiles = "".join(
            '<figure class="g-tile"><img loading="lazy" src="/assets/gallery/{n}" alt="{a}"></figure>'.format(
                n=p.name, a=esc(p.stem.replace("-", " ").replace("_", " ").strip().capitalize())
            )
            for p in photos
        )
    else:
        tiles = "".join(
            '<div class="ph-tile"><span>Before / after photo slot — drop images into site/assets/gallery/ and rebuild</span></div>'
            for _ in range(6)
        )
    head = section_head(d)
    return f'<section class="sec"><div class="wrap">{head}<div class="grid g3">{tiles}</div></div></section>'


def s_beforeafter(d) -> str:
    """Real before/after pairs, two images per card with corner labels."""
    cards = []
    for it in d["items"]:
        cards.append(
            '<figure class="ba">'
            '<div class="ba-imgs">'
            '<div class="ba-half"><span class="ba-tag">Before</span>'
            f'<img loading="lazy" decoding="async" src="{it["before"]}" alt="{esc(it["alt"])} — before"></div>'
            '<div class="ba-half"><span class="ba-tag ba-tag-a">After</span>'
            f'<img loading="lazy" decoding="async" src="{it["after"]}" alt="{esc(it["alt"])} — after"></div>'
            "</div>"
            f'<figcaption class="ba-cap"><b>{it["title"]}</b><span>{it["service"]}</span></figcaption>'
            "</figure>"
        )
    more = (
        f'<p class="center"><a class="btn btn-ghost btn-lg" href="{d["more_link"]}">See the full gallery →</a></p>'
        if d.get("more_link") else ""
    )
    head = section_head(d)
    return f'<section class="sec" id="before-after"><div class="wrap">{head}<div class="ba-grid">{"".join(cards)}</div>{more}</div></section>'


def s_showcase(d) -> str:
    """Standalone glamour shots in a portrait-tile grid with caption overlays."""
    cards = []
    for it in d["items"]:
        sub = f'<span>{it["sub"]}</span>' if it.get("sub") else ""
        cards.append(
            f'<figure class="show"><img loading="lazy" decoding="async" src="{it["img"]}" alt="{esc(it["alt"])}">'
            f'<figcaption class="show-cap"><b>{it["title"]}</b>{sub}</figcaption></figure>'
        )
    head = section_head(d)
    return f'<section class="sec sec-alt"><div class="wrap">{head}<div class="show-grid">{"".join(cards)}</div></div></section>'


def s_form(d) -> str:
    # When a GoHighLevel calendar is configured, embed it as the primary booking
    # path (books straight into the CRM pipeline); the request form stays below
    # as a fallback for people who don't want to pick a slot.
    ghl = ""
    form_title = "Request your appointment"
    if GHL_CALENDAR_URL and d.get("calendar", True):
        ghl = (
            '<h2>Pick your time</h2>'
            '<p class="sub">Live availability — booked straight onto '
            f"{BIZ['owner']}'s calendar. No prepayment.</p>"
            f'<div class="ghl-embed"><iframe src="{GHL_CALENDAR_URL}" '
            'title="Book your detailing appointment" loading="lazy" '
            'scrolling="no" id="ghl-booking"></iframe></div>'
            '<script src="https://link.msgsndr.com/js/form_embed.js" async></script>'
        )
        form_title = "Prefer to send details instead?"
    # FormSubmit relay: first submission emails a one-time activation link to the
    # business inbox; after confirming, submissions arrive as email. No account needed.
    action = f"https://formsubmit.co/{BIZ['email']}"
    return f"""<section class="sec"><div class="wrap wrap-nar">
{ghl}<h2>{form_title}</h2>
<p class="sub">Fastest: <a href="sms:{BIZ['phone_e164']}">text {BIZ['phone_display']}</a> with your vehicle + a photo or two.
Prefer a form? This goes straight to {BIZ['owner']} and he replies the same day.</p>
<form class="book-form" action="{action}" method="POST">
  <input type="hidden" name="_subject" value="New booking request — supremecleandetailing.com">
  <input type="hidden" name="_captcha" value="false">
  <input type="text" name="_honey" style="display:none" tabindex="-1" aria-hidden="true">
  <div class="f-grid">
    <label>Name<input required name="name" autocomplete="name"></label>
    <label>Phone<input required type="tel" name="phone" autocomplete="tel"></label>
    <label>Email<input type="email" name="email" autocomplete="email"></label>
    <label>City<select name="city">{''.join(f'<option>{c}</option>' for c, _ in CITIES_SERVED)}<option>Other nearby</option></select></label>
    <label>Vehicle (year / make / model)<input required name="vehicle" placeholder="2021 Toyota Tacoma"></label>
    <label>Service<select name="service"><option>Full Detail</option><option>Interior Deep Clean</option><option>Exterior Wash &amp; Shine</option><option>Odor Removal</option><option>Pet Hair Removal</option><option>Headlight Restoration</option><option>Fleet / multiple vehicles</option><option>Not sure — recommend for me</option></select></label>
    <label>Preferred day<input type="date" name="preferred_date"></label>
    <label class="f-full">Anything we should know? (stains, pets, smells, parking)<textarea name="message" rows="4"></textarea></label>
  </div>
  <button class="btn btn-primary btn-lg" type="submit">Send booking request</button>
  <p class="form-note">No prepayment. {BIZ['owner']} confirms your time by text. If it's urgent, just call
  <a href="tel:{BIZ['phone_e164']}">{BIZ['phone_display']}</a>.</p>
</form></div></section>"""


def s_map(d) -> str:
    q = H.escape("Supreme Clean Detailing Casa Grande AZ", quote=True).replace(" ", "+")
    return (
        '<section class="sec"><div class="wrap">'
        '<h2>Find us on Google</h2>'
        f'<div class="map-wrap"><iframe title="Supreme Clean Detailing on Google Maps" loading="lazy" '
        f'src="https://www.google.com/maps?q={q}&output=embed" allowfullscreen></iframe></div>'
        "</div></section>"
    )


def s_socials(d) -> str:
    head = section_head(d)
    return f'<section class="sec"><div class="wrap wrap-nar center-sec">{head}{socials_html("lg")}</div></section>'


def section_head(d) -> str:
    out = ""
    if d.get("title"):
        out += f"<h2>{d['title']}</h2>"
    if d.get("sub"):
        out += f'<p class="sub">{d["sub"]}</p>'
    return out


RENDER = {
    "trustbar": s_trustbar,
    "cards": s_cards,
    "pricing": s_pricing,
    "addons": s_addons,
    "steps": s_steps,
    "reviews": s_reviews,
    "faq": s_faq,
    "prose": s_prose,
    "cta": s_cta,
    "areas": s_areas,
    "gallery_ph": s_gallery_ph,
    "beforeafter": s_beforeafter,
    "showcase": s_showcase,
    "form": s_form,
    "map": s_map,
    "socials": s_socials,
}

# ------------------------------------------------------------------ layout ---


def nav_html(active: str) -> str:
    links = [
        ("Services", "/services/"),
        ("Pricing", "/pricing/"),
        ("Reviews", "/reviews/"),
        ("Service areas", "/service-areas/"),
        ("About", "/about/"),
        ("FAQ", "/faq/"),
    ]
    parts = []
    for label, href in links:
        cls = ' class="on"' if href == active else ""
        parts.append(f'<a href="{href}"{cls}>{label}</a>')
    return "".join(parts)


def header(active: str) -> str:
    # (Promo bar removed. To add a real seasonal offer later, drop a
    #  <div class="promo"><p>…</p></div> here — the .promo styles still exist.)
    return f"""<a class="skip" href="#main">Skip to content</a>
<header class="hd"><div class="wrap hd-in">
  <a class="brand" href="/">{LOGO}<span class="brand-t">Supreme Clean<em>Detailing</em></span></a>
  <input id="nav-t" type="checkbox" class="nav-t" aria-hidden="true">
  <label for="nav-t" class="nav-b" aria-label="Open menu"><span></span><span></span><span></span></label>
  <nav class="nav" aria-label="Main">{nav_html(active)}</nav>
  <div class="hd-cta">
    <a class="hd-tel" href="tel:{BIZ['phone_e164']}">{icon('phone')}<span>{BIZ['phone_display']}</span></a>
    <a class="btn btn-primary" href="/book/">Get my price</a>
  </div>
</div></header>"""


def socials_html(variant: str = "ft") -> str:
    items = [
        ("instagram", BIZ["instagram"], "Instagram"),
        ("tiktok", BIZ["tiktok"], "TikTok"),
        ("google", BIZ["gbp_url"], "Google"),
    ]
    cls = "socials socials-lg" if variant == "lg" else "socials"
    links = "".join(
        f'<a class="social" href="{href}" target="_blank" rel="noopener" aria-label="{label}">'
        f"{icon(ic)}<span>{label}</span></a>"
        for ic, href, label in items
    )
    return f'<div class="{cls}">{links}</div>'


def footer_map() -> str:
    """Google Maps embed band that sits at the bottom of every page (lazy-loaded,
    so it only fetches when a visitor scrolls to it). Uses a business-name search
    so it mirrors whatever the GBP shows (exact address or service area)."""
    q = H.escape(f"{BIZ['name']} {BIZ['city']} {BIZ['region']}", quote=True).replace(" ", "+")
    return (
        '<section class="ft-map-band" aria-label="Where we are"><div class="wrap">'
        '<div class="ft-map-head">'
        f'<h2>Based in {BIZ["city"]} — mobile across the I-10 corridor</h2>'
        f'<a class="btn btn-outline" href="{BIZ["gbp_url"]}" target="_blank" rel="noopener">'
        f'{icon("pin")} Open in Google Maps</a></div>'
        f'<div class="map-wrap"><iframe title="{BIZ["name"]} on Google Maps" loading="lazy" '
        f'src="https://www.google.com/maps?q={q}&output=embed"></iframe></div>'
        "</div></section>"
    )


def footer() -> str:
    svc = "".join(f'<li><a href="{href}">{n}</a></li>' for n, href in SERVICES_NAV)
    cities = "".join(f'<li><a href="{href}">Car detailing {n}, AZ</a></li>' for n, href in CITIES_SERVED)
    return f"""{footer_map()}<footer class="ft"><div class="wrap ft-grid">
  <div>
    <a class="brand brand-ft" href="/">{LOGO}<span class="brand-t">Supreme Clean<em>Detailing</em></span></a>
    <p>Owner-operated mobile car detailing by {BIZ['owner']}. Based in {BIZ['city']}, {BIZ['region']} {BIZ['zip']} —
    serving the I-10 corridor between Phoenix and Tucson. We come to you.</p>
    <p class="ft-rating"><a href="{BIZ['gbp_url']}">{stars()} {BIZ['rating']} · {BIZ['review_count']} Google reviews</a></p>
  </div>
  <div><h3>Services</h3><ul>{svc}</ul></div>
  <div><h3>Service areas</h3><ul>{cities}</ul></div>
  <div><h3>Contact</h3><ul class="ft-contact">
    <li><a href="tel:{BIZ['phone_e164']}">{icon('phone')} {BIZ['phone_display']}</a></li>
    <li><a href="sms:{BIZ['phone_e164']}">{icon('chat')} Text us a photo for a quote</a></li>
    <li><a href="mailto:{BIZ['email']}">{BIZ['email']}</a></li>
    <li>{icon('clock')} {BIZ['hours_human']}</li>
    <li><a href="{BIZ['gbp_url']}" target="_blank" rel="noopener">{icon('pin')} Find us on Google Maps</a></li>
    <li><a href="{BIZ['review_url']}" target="_blank" rel="noopener">{icon('star')} Leave us a review</a></li>
  </ul>
  <div class="ft-follow"><span class="ft-follow-l">Follow the work</span>{socials_html()}</div></div>
</div>
<div class="wrap ft-legal">
<span>© {CURRENT_YEAR} {BIZ['name']} · {BIZ['city']}, {BIZ['region']}</span>
<span>On time · Fair prices · Satisfaction guaranteed</span>
<span><a href="/privacy/">Privacy Policy</a> · <a href="/sitemap.xml">Sitemap</a></span></div>
</footer>
<div class="mobile-bar" aria-label="Quick actions">
  <a href="tel:{BIZ['phone_e164']}">{icon('phone')} Call</a>
  <a href="sms:{BIZ['phone_e164']}">{icon('chat')} Text</a>
  <a class="mb-book" href="/book/">Book now</a>
</div>"""


def sig_card(c) -> str:
    rows = "".join(
        f'<div class="sig-row"><b><span class="sig-dot"></span>{text}</b><em>{meta}</em></div>'
        for text, meta in c["rows"]
    )
    return f"""<div class="sig rv rv-3">
  <div class="gleam"></div>
  <div class="sig-head"><span>{c['label']}</span><span class="sig-price">{c['price']}</span></div>
  <div class="sig-art">{SIG_CAR_SVG}</div>
  <div class="sig-rows">{rows}</div>
  <a class="btn btn-outline" href="{c['btn_href']}">{c['btn_text']}</a>
</div>"""


def hero(p) -> str:
    badges = "".join(f"<li>{icon(b.get('icon','check'))}{b['text']}</li>" for b in p.get("hero_badges", []))
    badges_html = f'<ul class="hero-badges rv rv-3">{badges}</ul>' if badges else ""
    eyebrow = f'<p class="eyebrow rv">{p["hero_eyebrow"]}</p>' if p.get("hero_eyebrow") else ""
    rating = ""
    if not p.get("hero_stats"):
        rating = (
            f'<a class="hero-rating rv" href="{BIZ["gbp_url"]}">{stars()}'
            f'<strong>{BIZ["rating"]}</strong> · {BIZ["review_count"]} Google reviews</a>'
        )
    stats = ""
    if p.get("hero_stats"):
        cells = "".join(
            f'<div><div class="stat-num">{num}</div><div class="stat-lb">{label}</div></div>'
            for num, label in p["hero_stats"]
        )
        stats = f'<div class="hero-stats rv rv-3">{cells}</div>'
    sub = f'<p class="hero-sub rv rv-2">{p["hero_sub"]}</p>' if p.get("hero_sub") else ""
    left = f"""{rating}{eyebrow}
  <h1 class="rv">{p['h1']}</h1>
  {sub}
  <div class="hero-ctas rv rv-2">
    <a class="btn btn-primary btn-lg" href="/book/">Reserve a detail</a>
    <a class="btn btn-outline btn-lg" href="sms:{BIZ['phone_e164']}">{icon('chat')} Text {BIZ['phone_display']}</a>
  </div>
  {badges_html}{stats}"""
    if p.get("hero_card"):
        inner = f'<div class="hero-grid"><div>{left}</div>{sig_card(p["hero_card"])}</div>'
    else:
        inner = left
    return f"""<section class="hero">{bubbles_html()}<div class="wrap">
  {inner}
</div></section>"""


def crumbs_html(p) -> str:
    crumbs = p.get("crumbs")
    if not crumbs:
        return ""
    parts = ['<a href="/">Home</a>']
    for name, href in crumbs:
        parts.append(f'<a href="{href}">{name}</a>' if href else f"<span>{name}</span>")
    return f'<nav class="crumbs wrap" aria-label="Breadcrumb">{" › ".join(parts)}</nav>'


# ------------------------------------------------------------------ schema ---


def base_schema(p) -> list[dict]:
    url = SITE_URL + slug_url(p["slug"])
    biz = {
        "@context": "https://schema.org",
        "@type": ["AutoWash", "LocalBusiness"],
        "@id": SITE_URL + "/#business",
        "name": BIZ["name"],
        "description": "Owner-operated mobile car detailing serving Casa Grande, Maricopa, Eloy, Coolidge, Florence, San Tan Valley and Queen Creek, AZ. Interior, exterior and full details — we come to you.",
        "url": SITE_URL + "/",
        "telephone": BIZ["phone_e164"],
        "email": BIZ["email"],
        "image": SITE_URL + "/assets/og-card.png",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": BIZ["street"],
            "addressLocality": BIZ["city"],
            "addressRegion": BIZ["region"],
            "postalCode": BIZ["zip"],
            "addressCountry": "US",
        },
        "openingHours": BIZ["hours_schema"],
        "areaServed": [{"@type": "City", "name": f"{c}, AZ"} for c, _ in CITIES_SERVED],
        "founder": {"@type": "Person", "name": BIZ["owner"]},
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": BIZ["rating"],
            "reviewCount": BIZ["review_count"],
            "bestRating": "5",
        },
        "review": [
            {
                "@type": "Review",
                "author": {"@type": "Person", "name": "Ron McClure"},
                "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
                "reviewBody": "Anthony was very professional with scheduling my appointment as well as timely follow-up. Arrived on time, did an excellent job detailing both my cars. Pricing was half of the quotes I received from several others! I highly recommend his services.",
            },
            {
                "@type": "Review",
                "author": {"@type": "Person", "name": "Suanne Dunn"},
                "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
                "reviewBody": "My car came back looking beautiful after Anthony detailed it. Anthony has done work for me for years now and I trust him implicitly and his prices are very fair.",
            },
            {
                "@type": "Review",
                "author": {"@type": "Person", "name": "Kimberly García"},
                "reviewRating": {"@type": "Rating", "ratingValue": "5", "bestRating": "5"},
                "reviewBody": "Arrived on time, kept me updated on what they were doing to my car. They left my car smelling fresh and deep detailed — they were even able to remove a smell I had in my car.",
            },
        ],
        "sameAs": [BIZ["gbp_url"], BIZ["instagram"], BIZ["tiktok"]],
    }
    if PRICES_LIVE:
        biz["priceRange"] = "$45 - $225"
    out = [biz]
    if p["slug"] == "":
        out.append(
            {
                "@context": "https://schema.org",
                "@type": "WebSite",
                "name": BIZ["name"],
                "url": SITE_URL + "/",
            }
        )
    crumbs = p.get("crumbs")
    if crumbs:
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_URL + "/"}]
        for i, (name, href) in enumerate(crumbs, start=2):
            it = {"@type": "ListItem", "position": i, "name": re.sub(r"<[^>]+>", "", name)}
            it["item"] = SITE_URL + href if href else url
            items.append(it)
        out.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})
    for kind, data in p.get("sections", []):
        if kind == "faq":
            out.append(
                {
                    "@context": "https://schema.org",
                    "@type": "FAQPage",
                    "mainEntity": [
                        {
                            "@type": "Question",
                            "name": re.sub(r"<[^>]+>", "", q),
                            "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", " ", a).strip()},
                        }
                        for q, a in data["items"]
                    ],
                }
            )
    out.extend(p.get("schema_extra", []))
    return out


def service_schema(name: str, desc: str, url_path: str, low: int = 0, high: int = 0) -> dict:
    out = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "serviceType": name,
        "description": desc,
        "provider": {"@id": SITE_URL + "/#business"},
        "areaServed": [{"@type": "City", "name": f"{c}, AZ"} for c, _ in CITIES_SERVED],
        "url": SITE_URL + url_path,
    }
    if PRICES_LIVE and low and high:
        out["offers"] = {
            "@type": "AggregateOffer",
            "priceCurrency": "USD",
            "lowPrice": str(low),
            "highPrice": str(high),
            "url": SITE_URL + "/pricing/",
        }
    return out


def blogposting_schema(title: str, desc: str, url_path: str, published: str) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": title,
        "description": desc,
        "datePublished": published,
        "dateModified": published,
        "author": {"@type": "Person", "name": BIZ["owner"]},
        "publisher": {"@id": SITE_URL + "/#business"},
        "mainEntityOfPage": SITE_URL + url_path,
    }


# ------------------------------------------------------------------- pages ---


def render_page(p) -> str:
    url = SITE_URL + slug_url(p["slug"])
    schema = "".join(
        f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in base_schema(p)
    )
    body_sections = "".join(RENDER[kind](data) for kind, data in p.get("sections", []))
    hero_html = hero(p) if p.get("h1") else ""
    noindex = '<meta name="robots" content="noindex">' if p.get("noindex") else ""
    is_home = p["slug"] == ""
    wash = wash_html() if is_home else ""
    wash_js = WASH_JS if is_home else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{GA_SNIPPET}
{META_PIXEL}
<title>{esc(p['title'])}</title>
<meta name="description" content="{esc(p['desc'])}">
<link rel="canonical" href="{url}">
{noindex}<meta property="og:type" content="{p.get('og_type','website')}">
<meta property="og:site_name" content="{BIZ['name']}">
<meta property="og:title" content="{esc(p['title'])}">
<meta property="og:description" content="{esc(p['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE_URL}/assets/og-card.png">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(p['title'])}">
<meta name="twitter:description" content="{esc(p['desc'])}">
<meta name="twitter:image" content="{SITE_URL}/assets/og-card.png">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
{schema}
</head>
<body>
{wash}<div class="grain" aria-hidden="true"></div>
{header(p.get('nav_active',''))}
<main id="main">
{crumbs_html(p)}
{hero_html}
{body_sections}
</main>
{footer()}
{wash_js}</body>
</html>"""


def build(pages) -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    shutil.copy(ROOT / "assets" / "style.css", OUT / "assets" / "style.css")
    shutil.copy(ROOT / "assets" / "favicon.svg", OUT / "assets" / "favicon.svg")
    shutil.copy(ROOT / "assets" / "og-card.svg", OUT / "assets" / "og-card.svg")
    # og-card.png: generated separately if Pillow present; svg kept as source.
    png = ROOT / "assets" / "og-card.png"
    if png.exists():
        shutil.copy(png, OUT / "assets" / "og-card.png")
    gal = ROOT / "assets" / "gallery"
    if gal.exists() and any(gal.iterdir()):
        # ship only the optimized web images; keep full-res originals (_staging) out
        shutil.copytree(gal, OUT / "assets" / "gallery", ignore=shutil.ignore_patterns("_staging"))

    # Apache/LiteSpeed config for Namecheap cPanel hosting (ignored by Cloudflare)
    (OUT / ".htaccess").write_text(HTACCESS, encoding="utf-8")
    # Cloudflare Pages config: caching + security headers (HTTPS, clean URLs,
    # gzip/brotli and 404.html routing are automatic on Pages).
    (OUT / "_headers").write_text(CF_HEADERS, encoding="utf-8")

    urls = []
    for p in pages:
        path = OUT / p["slug"] / "index.html" if p["slug"] else OUT / "index.html"
        if p["slug"] == "404":
            path = OUT / "404.html"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(render_page(p), encoding="utf-8")
        if not p.get("noindex") and p["slug"] != "404":
            urls.append((slug_url(p["slug"]), p.get("priority", "0.7")))

    today = date.today().isoformat()
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, pr in urls:
        sm.append(f"<url><loc>{SITE_URL}{u}</loc><lastmod>{today}</lastmod><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    (OUT / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")

    # Namecheap-ready upload bundle: unzip the CONTENTS into public_html
    zip_path = OUT.parent / "supremecleandetailingpro-site"
    archive = shutil.make_archive(str(zip_path), "zip", OUT)
    print(f"Built {len(pages)} pages -> {OUT}")
    print(f"Upload bundle -> {archive}")


HTACCESS = f"""# Supreme Clean Detailing — Namecheap/cPanel (Apache/LiteSpeed)
Options -Indexes
ErrorDocument 404 /404.html

<IfModule mod_rewrite.c>
RewriteEngine On
# Force HTTPS + strip www (enable Namecheap AutoSSL first; harmless once live)
RewriteCond %{{HTTPS}} !=on [OR]
RewriteCond %{{HTTP_HOST}} ^www\\. [NC]
RewriteRule ^(.*)$ {SITE_URL}/$1 [L,R=301]
</IfModule>

<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css application/javascript image/svg+xml application/json
</IfModule>

<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType text/css "access plus 30 days"
ExpiresByType image/svg+xml "access plus 30 days"
ExpiresByType image/png "access plus 30 days"
ExpiresByType image/jpeg "access plus 30 days"
ExpiresByType image/webp "access plus 30 days"
ExpiresByType text/html "access plus 1 hour"
</IfModule>

<IfModule mod_headers.c>
Header always set X-Content-Type-Options "nosniff"
Header always set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
"""

# Cloudflare Pages _headers — applied top-down, most-specific path wins.
CF_HEADERS = """/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Cache-Control: public, max-age=3600, must-revalidate

/assets/*
  Cache-Control: public, max-age=31536000, immutable
"""


if __name__ == "__main__":
    from content_core import CORE_PAGES
    from content_services import SERVICE_PAGES
    from content_cities import CITY_PAGES
    from content_blog import BLOG_PAGES

    build(CORE_PAGES + SERVICE_PAGES + CITY_PAGES + BLOG_PAGES)
