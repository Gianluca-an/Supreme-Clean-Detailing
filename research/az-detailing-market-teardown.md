# Phoenix + Tucson Car-Detailing Website Market Teardown
**Prepared for Supreme Clean Detailing — 2026-07-12**

Evidence base: fresh Firecrawl SERPs (13 geo-located queries), full `firecrawl_map` URL inventories, `firecrawl_scrape` (markdown + raw HTML + links + screenshots) of every important page of 20 verified-Arizona sites, raw-HTML technical audits (titles, meta, H-hierarchy, canonicals, Open Graph, alt coverage, JSON-LD schema, page weight, script counts), and off-site authority checks (Google/Yelp/Facebook/BBB/Carfax/LLC filings). All supporting artifacts live in [`research/data/`](data/): per-site dossiers (`T1…T10`, `B1…B10`), [`serp-log.md`](data/serp-log.md), [`cohorts.md`](data/cohorts.md), [`offsite-authority.md`](data/offsite-authority.md), and above-the-fold screenshot contact sheets ([top-10](data/screenshots/SHEET-top10.jpg) / [bottom-10](data/screenshots/SHEET-bottom10.jpg)).

---

## 1. Executive summary — the ten findings that matter

1. **The gap is total, and it's quantifiable: top-10 sites average 76/100 on our weighted scorecard; bottom-10 average 14/100.** The bottom sites aren't "worse at SEO" — they are absent from every layer of the stack at once: domain, content, schema, local signals, conversion path, proof, and reviews.

2. **Every top site sits on a custom domain; every invisible site sits on a rented free subdomain** (wixsite.com, square.site, godaddysites.com, weebly.com). Not one free-builder subdomain surfaced in any of the 13 money SERPs we pulled. The subdomain is the single most reliable predictor of invisibility in this market.

3. **Reviews are the market's real currency.** Winners put third-party review *counts* on every page: Clean AZ shows a live "EXCELLENT ★★★★★ 771 reviews" Google widget sitewide (even on the booking page); Adrian & Sons streams "5.0 (495)" Google reviews (freshest was 7 days old); Cool Auto leads with "Over 850 5-Star Reviews"; Buff & Shine's widget shows 234. The bottom ten show **zero** on-site reviews — and Zamo's aggregator listing literally reads "Rated 0 stars from 0 reviews" (hiredetailing.com).

4. **Winners publish prices; losers hide them.** 7 of the top 10 show real dollar pricing on-page (Clean AZ $177–$277 by vehicle size; Airpark's full 12-package price list $55–$410; Cool Auto's 6 tabbed tables $79–$445 with durations; Tucson Details puts "$75 sedans / $150 trucks" *in its meta descriptions*). Only high-ticket ceramic/PPF specialists (Bob Moses, Detail PHX, Ceramic Pro Tucson) run quote-only funnels — deliberately, for $1k–$7k tickets.

5. **Winners run real booking infrastructure — usually a detailing-specific SaaS.** fieldd (Adrian & Sons, Buff & Shine), OrbisX (Cool Auto), Urable (Airpark), Housecall Pro (Tucson Details), or an on-site wizard (Clean AZ's "book a detail in 60 seconds" vehicle-size calculator; Recon's per-service appointment funnels). An entire industry vendor ecosystem exists that the bottom ten don't know about — Adrian & Sons' site is built by **Detailers Roadmap**, an agency exclusively for detailers; Cool Auto embeds an AI photo-quote chat ("Luna") and Microsoft Clarity session recording.

6. **Local-page architecture is the #1 organic-rank lever.** Clean AZ (rank #1 "car detailing Phoenix") runs 7 city pages + service silo + pricing + FAQ + blog (~60 URLs). Adrian & Sons runs 6 city pages **plus 8 neighborhood pages** (Arcadia, Biltmore, Sunnyslope…). Tucson Details runs 9 neighborhood pages. Bob Moses runs 12+ location pages, 7 vehicle-type pages, and 9 car-brand pages ("Tesla ceramic coating"). Bottom sites average 1–4 pages, none geo-targeted.

7. **Technical SEO is table stakes the bottom can't clear — but perfection isn't required to rank.** Clean AZ ships 14 flawless JSON-LD blocks (LocalBusiness, Service, OfferCatalog, AggregateRating, Review, FAQPage, HowTo, Breadcrumb…) and 151/151 alt texts. Yet Buff & Shine ranks #1 for "mobile detailing Tucson" with **zero schema, no meta description, no canonical** — carried purely by 2,400 words of keyworded copy + 234 Google reviews + Yelp. Meanwhile two top sites are sitting on live landmines: **Detail PHX's homepage serves `<meta name="robots" content="noindex">`** (a second robots tag) and Buff & Shine served the same to our crawler — both still rank, but one Google re-interpretation could vaporize them. That's a takeover opportunity.

8. **The bottom ten fail before SEO even starts — at the level of "is this a website?"** Landeros' title tag is Square's factory default, "Appointments | My Business." Lively still shows three unedited "Service Name" template placeholders and its H1 is "Subscribe Form." Heyzee's title is "Home," its OG title "My Site," its visible H1 "An error occurred." (a broken video embed) — and its **canonical tag points to a YouTube URL**, telling Google its homepage's true version is YouTube. Mike's Mobile (GoDaddy) canonicals to a Vimeo player. Wyatts has literally zero CTAs. J&C displays two different phone numbers on one page and three typos in its meta description ("atuo detailing… upholstry stain remvoal… headlight restoratioln").

9. **SERP real estate is bigger than websites.** Yelp holds top-5 slots on 7 of 9 localized queries; Reddit threads on 8 of 9 (Cool Auto and Bob Moses each effectively own an extra ranking via Reddit endorsements); Panda Hub, Groupon, Instagram, Facebook and YellowPages fill mid-slots. Recon's own Yelp page ranks top-5 for "car detailing Tucson" — a second front door. A winning strategy must farm Yelp/Reddit/GBP presence, not just the website.

10. **Nobody in the market is BBB-accredited, almost nobody uses sms: click-to-text (only Bob Moses), no one combines transparent pricing + memberships + live review feed + neighborhood pages + FAQ schema in one site.** Every winner has visible holes (Airpark: zero on-site social proof; Bob Moses: 23% alt coverage, no online booking; Cool Auto: missing canonical, 72 scripts; Tucson Details: 1.17 MB pages). **The composite "best of all ten" site does not exist in this market — that's the opening for Supreme Clean Detailing.**

---

## 2. The SERP landscape (fresh pulls, 2026-07-12)

Full log with all 13 queries and positions: [`data/serp-log.md`](data/serp-log.md).

**Phoenix organic leaders:** cleanmobiledetail.com (#1 car detailing, #2 near-me), adrianandsonsmobileautodetail.com (#2 across four queries), airparkautodetailing.com (#1 auto detailing), bobmosescc.com (#1 ceramic coating + Reddit rec at #2 + Yelp biz at #8 = 3 slots), detailphx.com (#4 ceramic). Supporting cast: effortlessmobileauto, prodetailaz, motorcityautodetailing, autothisworlddetailing (Ceramic Pro North Phoenix), kenyonmobiledetailing (532 Yelp reviews).

**Tucson organic leaders:** coolautoinc.com (#1 car detailing, #2 auto, #3 ceramic, #1 near-me — most dominant site in either city), tucsondetails.com (#2 mobile, #3 car), buffshineaz.com (#1 mobile), recondetail.com (#3 auto + its Yelp page #4), ceramicprotucson.com (#1 ceramic).

**Aggregator/UGC share of top-12 slots (9 localized queries):** Yelp appeared in 9/9 (top-5 in 7), Reddit 8/9, Panda Hub 4, Instagram/Facebook 6, Groupon 1, YellowPages/Yahoo tails. Roughly **a third of page-one is not winnable by a website at all** — it must be won on Yelp, Reddit, GBP and social.

**Note on geo-targeting:** a bare "detailing near me" query returns national results unless the city is in the query; all cohort ranking claims use city-qualified queries geo-located to Phoenix/Tucson.

---

## 3. Weighted scorecard (0–100)

Weights: Technical SEO 15 · Content depth 15 · Local SEO 15 · CTA/Conversion 20 · Trust/Proof 15 · Design/UX 10 · Off-site authority 10. Sub-scores 0–10 from the documented evidence in each dossier.

| # | Site | Tech SEO | Content | Local | CTA/Conv | Trust | Design | Authority | **TOTAL** |
|---|------|---------|---------|-------|----------|-------|--------|-----------|-----------|
| T1 | cleanmobiledetail.com | 9 | 9 | 9 | 10 | 9 | 9 | 8 | **91** |
| T6 | coolautoinc.com | 8.5 | 9.5 | 8 | 9.5 | 9.5 | 9 | 9 | **89** |
| T9 | recondetail.com | 8 | 8.5 | 7.5 | 8.5 | 8 | 7 | 8 | **80** |
| T10 | ceramicprotucson.com | 7.5 | 7.5 | 7 | 8.5 | 8.5 | 8.5 | 8 | **79** |
| T2 | adrianandsonsmobileautodetail.com | 6.5 | 7 | 8 | 9 | 8 | 8 | 8 | **78** |
| T7 | tucsondetails.com | 7.5 | 8.5 | 8.5 | 8.5 | 6.5 | 7.5 | 6.5 | **78** |
| T4 | bobmosescc.com | 6.5 | 9 | 8 | 7 | 8 | 5 | 9 | **75** |
| T5 | detailphx.com | 5 | 8 | 6 | 8 | 7 | 8 | 7 | **70** |
| T3 | airparkautodetailing.com | 6 | 5 | 7 | 6 | 5 | 7 | 7 | **61** |
| T8 | buffshineaz.com | 3 | 6 | 6 | 7.5 | 6 | 6.5 | 7 | **60** |
| — | **TOP-10 AVERAGE** | | | | | | | | **76** |
| B8 | zamo-mobile-detailing-llc.square.site | 1.5 | 1.5 | 3.5 | 4 | 0 | 1.5 | 1 | **20** |
| B9 | performance-auto-detailingaz.square.site | 2.5 | 1 | 2.5 | 3 | 0 | 2 | 1.5 | **19** |
| B1 | jcaccessories.wixsite.com | 2 | 1.5 | 3 | 1.5 | 0 | 2 | 2 | **17** |
| B5 | richierich-details.square.site | 1 | 1 | 1.5 | 3.5 | 1 | 1.5 | 1 | **16** |
| B7 | cleanerimagedetailspecialist.godaddysites.com | 1 | 1.5 | 2 | 1 | 1 | 2 | 1.5 | **14** |
| B6 | livelymarketer.wixsite.com/livelyautodetail | 1 | 1.5 | 0.5 | 2.5 | 0.5 | 2 | 0.5 | **13** |
| B2 | my-business-101101-103077.square.site | 0.5 | 0.5 | 1.5 | 3 | 0 | 1 | 1 | **12** |
| B4 | azcustomz.weebly.com | 1 | 1.5 | 1.5 | 0.5 | 0.5 | 2 | 0.5 | **10** |
| B3 | wyattspremiumautodetailing.godaddysites.com | 1 | 1 | 1 | 0.5 | 0 | 2 | 0.5 | **8** |
| B10 | heyzeemobiledetailing.weebly.com | 0.5 | 2 | 0.5 | 0 | 0.5 | 1 | 0.5 | **7** |
| — | **BOTTOM-10 AVERAGE** | | | | | | | | **14** |

The widest single-dimension gaps: **Trust/Proof (top avg ≈ 7.6 vs bottom ≈ 0.35 — a 20× gap)** and **CTA/Conversion (8.3 vs 2.0)**. Even "design," the dimension free builders supposedly solve, gaps 7.7 vs 1.8.

---

## 4. Per-site profiles (condensed; full 12-dimension dossiers in `research/data/`)

### THE TOP 10

**T1 — Clean Mobile Detailing AZ · cleanmobiledetail.com · Gilbert/Phoenix (mobile) · 91/100** — [dossier](data/T1-cleanmobiledetail.md)
WordPress/Divi + WP Rocket + CDN. ~60-URL architecture: services silo, **7 city pages**, pricing, FAQ, service-areas, membership ("Clean Club"), active blog. Phone number *inside title tags* ("Clean AZ: Mobile Car Detailing in Phoenix | 623-400-7708"). **14 JSON-LD blocks** covering LocalBusiness→FAQPage→HowTo→AggregateRating; 151/151 image alts. Transparent pricing ($177–$277 by size; every add-on priced; membership $117–$227 w/ "Save $80 per detail"); "No upfront payments," "100% Clean Car Guarantee," first child seat free. Sitewide Trustindex widget: **"EXCELLENT ★★★★★ 771 Google reviews."** Every CTA (CALCULATE MY PRICE / BOOK NOW / GIFT A DETAIL) funnels to a 60-second vehicle-size booking wizard, and every placement carries its own `utm_source` — they A/B-measure their buttons. Weaknesses: 954 KB HTML, 29 scripts, `user-scalable=0`, no ceramic/paint-correction line, no BBB.

**T2 — Adrian & Sons Mobile Auto Detail · adrianandsonsmobileautodetail.com · Phoenix (mobile) · 78/100** — [dossier](data/T2-adrianandsons.md)
Duda site built by **Detailers Roadmap** (industry-niche agency). 6 city + **8 neighborhood pages** (Arcadia, Biltmore District, Sunnyslope…). Header triple-CTA (SCHEDULE ONLINE → fieldd SaaS / CALL / QUICK QUOTE) + sitewide promo "15% OFF PLATINUM — CODE 'FULL'". /reviews streams **live Google reviews 5.0 (495)** via Elfsight. Premium pricing partially shown (Platinum $449.99–$499.99); maintenance plans -10/-15/-20%. Schema = AutoWash/geo/hours only — no rating/FAQ markup despite having the content. No street address (SAB), no guarantee language, blog thin.

**T3 — Airpark Auto Detailing · airparkautodetailing.com · Scottsdale/Phoenix/Peoria (4 shops) · 61/100** — [dossier](data/T3-airpark.md)
WordPress/Elementor. "Serving the Valley since 1984" — deepest tenure in market; B2B dealer-services line. **Full à-la-carte price list** (12 packages, $55–$410, inclusions itemized). Booking = pick-a-location → external Urable virtual shop (3+ clicks). Homepage thin (~460 words), **zero on-site reviews/testimonials/gallery**, no blog/FAQ, H1 unkeyworded, phone not tappable, 25 CSS files, one broken CTA link ("/scheule-appointment/"). Ranks on age/authority/GBP; converts worse than it ranks.

**T4 — Bob Moses Ceramic Coating · bobmosescc.com · Phoenix + Tucson (multi-state) · 75/100** — [dossier](data/T4-bobmoses.md)
WordPress/AIOSEO. Biggest architecture in cohort (~140 URLs): 12+ location pages, vehicle-type silo (RV/boat/moto/semi/SxS), **9 car-brand pages** (Tesla/BMW/Porsche…), ~60-post blog targeting question queries ("How long does ceramic coating last in Arizona?"), separate ad-landers with per-city thank-you pages (funnel tracking). Location pages: exact-match title/H1, 1,600 words AZ-heat narrative, **embedded Google Map**, split sales/support numbers with call-tracking, and the market's only **sms: click-to-text**. Person-brand + YouTube influencer reviews + RV-forum advocacy → it owns 3 of the top-10 ceramic-PHX slots (site + Reddit + Yelp). No pricing, no online booking, dated design, 13/56 alts, no LocalBusiness schema on location pages.

**T5 — Detail PHX · detailphx.com · North Phoenix (shop) · 70/100** — [dossier](data/T5-detailphx.md)
WordPress + GoHighLevel CRM forms (vehicle year/make/model + photo upload → automated follow-up). Six service silos + Tesla page + FAQs + promos + ~35-post Phoenix-localized blog (XPEL/PPF education moat). LocalBusiness schema w/ GBP kgmid + Product/AggregateRating/Review markup (count = 3, thin). **Landmine: homepage carries a second robots meta — `noindex` — yet still ranks #4** for "ceramic coating Phoenix"; one recrawl could delist it. Brand-only H1, no city pages, BBB profile exists but not accredited.

**T6 — Cool Auto Detail · coolautoinc.com · Tucson (shop, since 1992) · 89/100** — [dossier](data/T6-coolauto.md)
Webflow + GTM/GA4/**Microsoft Clarity**/FB Pixel + "Luna" AI photo-quote chat (MMS quoting) + **OrbisX** instant booking + 27 buyable /product/ pages (services & membership tiers "B Cool / B Cooler / B Coolest") + Square gift cards. Meta description engineered for SERP CTR: "Rated #1 … ✔ 33+ Years ✔ Family Owned ✔ Fully Bonded & Insured ☎ (520) 292-9560". Packages page = market's pricing masterclass (6 tabbed tables by 6 vehicle sizes, durations, honest expectation copy — "2-4x more labor than what 70-80% of detailers sell"), 10-question FAQ, footer "Popular Searches" internal-link block. Trust stack: **34+ years / 850+ 5-star reviews / licensed, bonded, insured / family owned** + B2B partner-logo wall. Flaws: canonical missing, 72 scripts, prices hedged as "estimates," only one suburb page (Oro Valley).

**T7 — Tucson Details LLC · tucsondetails.com · Tucson (mobile) · 78/100** — [dossier](data/T7-tucsondetails.md)
WordPress/Divi + Slider Revolution. Geo-brand domain. **9 neighborhood pages** + 9-service silo + ~45 blog posts (top content velocity in Tucson) + live Instagram-reels feed. Starting prices on the homepage and *inside title tags* ("Headlight Restoration – Car Detailing $150"). Booking via Housecall Pro; "Tap to Call"/"Call or text" mobile CTAs. Weak spots: 1.17 MB homepage, `user-scalable=0`, duplicate FAQ pages + default-slug posts, no on-page review count (Yelp shows 47), no membership.

**T8 — Buff & Shine Detailing · buffshineaz.com · Tucson (mobile + Oracle Rd address) · 60/100** — [dossier](data/T8-buffshine.md)
The counter-example: **no meta description, no canonical, no schema, brand-only title, and a `noindex` served to our crawler — yet #1 for "mobile detailing Tucson."** Carried by a 2,400-word keyword-dense homepage (H1 "Car Detailing Tucson"), on-page package prices ($100–$250), on-page FAQ, fieldd booking + customer accounts, and **234 Google reviews / 5-star Yelp**. Gallery page still contains lorem ipsum. Proof that off-site authority + long local copy can outweigh technical polish — and how fragile that is.

**T9 — Recon Auto Detailing · recondetail.com · Tucson (shop, N Oracle Rd) · 80/100** — [dossier](data/T9-recondetail.md)
WordPress; best perf discipline in cohort (CSS inlined, 9 scripts). 4,500-word homepage; RV/boat/tint/PPF/Ceramic-Pro silos; **per-service booking funnels** (ppf-appointment, ceramic-pro-appointment…); ~20 Tucson-localized posts ("Monsoon Car Care in Tucson") + **9 Google Web Stories** (unique in market) + portfolio pages; rich single schema graph (AutoRepair, AggregateRating, Review, Offer, Service…). Runs a second domain (ceramicprowesttucson.com) for its Ceramic Pro franchise; its Yelp page (116 reviews) itself ranks top-5. No homepage pricing; double-H1 template artifact; an SEO-agency boilerplate leak in one web story.

**T10 — Ceramic Pro Tucson (Harrison Auto Spa) · ceramicprotucson.com · Tucson (franchise shop) · 79/100** — [dossier](data/T10-ceramicprotucson.md)
Franchise-grade WP build. Product-line silos (8 PPF variants, coating tiers Bronze→ION, 3 tint lines), **interactive wrap/tint visualizer**, aftercare/warranty page, **10 per-product free-quote funnels** + thank-you tracking. Sitewide urgency bar: "10% OFF ALL PPF, TINT & CERAMIC PACKAGES! CALL TODAY!" Elite-Dealer exclusivity + lifetime-warranty framing + embedded Google reviews; corporate ceramicpro.com dealer page backlinks it (and also ranks itself). Quote-only (no pricing), no blog, 41 scripts.

### THE BOTTOM 10 (all real, verified-AZ businesses; none appear in any money SERP)

**B8 — Zamo Mobile Detailing LLC · square.site · Tucson · 20/100** — [dossier](data/B7-B8-cleanerimage-zamo.md) — Best of the worst: name in title, tappable phone, map embed, hours, prices $40–$200. But **2.99 MB of Square runtime for 181 words**, no meta/schema/reviews ("Rated 0 stars from 0 reviews" on hiredetailing.com), Gmail address. AZ LLC verified via Bizapedia.
**B9 — Performance Auto Detailing · square.site · Tucson · 19/100** — [dossier](data/B9-B10-performanceaz-heyzee.md) — Real title/meta, then squanders it: only H1 = "Sign up for our newsletter," 3.01 MB page, newsletter modal blocking the hero, no phone link, no schema, 255 words.
**B1 — J&C Accessories · wixsite.com · Phoenix (shop) · 17/100** — [dossier](data/B1-B2-jcaccessories-landeros.md) — ALL-CAPS spam title, **three typos in the meta description**, 237 words, **two different phone numbers on the same page**, Wix free-plan ad banner, zero trust elements; GBP/Yelp/Nextdoor exist but lead to a site that can't convert.
**B5 — Richie Rich Details · square.site · Phoenix · 16/100** — [dossier](data/B5-B6-richierich-lively.md) — decent booking microcopy ("Choose your package — then lock in your time") rendered only by JS; crawlers (and our screenshot) see a solid red void. Claims "5.0 real Google reviews" where Google can't read it.
**B7 — Cleaner Image Detail Specialist · godaddysites.com · Tucson · 14/100** — [dossier](data/B7-B8-cleanerimage-zamo.md) — brand-only title, GoDaddy **stock-library hero photo**, motorcycle-template filler copy ("Find your own road. Fuel for the soul."), e-commerce headings ("New Products / Best Value") on a services business, no tel: link. Has "20 years" and a 10%-off gift-card promo nobody will ever see.
**B6 — The Lively Auto Detail · wixsite.com · Tucson · 13/100** — [dossier](data/B5-B6-richierich-lively.md) — three literal **"Service Name"** placeholder headings, H1 "Subscribe Form," keywords meta of garbage tokens ("The, deserve., service, you"), ~1 MB page for 384 words, **no phone anywhere**. Wix Bookings flow exists — unreachable.
**B2 — Landeros Auto Detailing · square.site · Phoenix · 12/100** — [dossier](data/B1-B2-jcaccessories-landeros.md) — title **"Appointments | My Business"** (factory default), no H1/desc/schema/phone-link, 45 words, blank-white screenshot. Active on TikTok/Instagram — **with a different phone number than the website** (602-527-1113 vs 602-527-3613).
**B4 — AZ Customz · weebly.com · Phoenix · 10/100** — [dossier](data/B3-B4-wyatts-azcustomz.md) — **no viewport meta (fails mobile entirely)**, zero heading tags, 0/8 alt, unescaped quote truncates its meta description, "Powered by Weebly" badge, no links out, no CTA.
**B3 — Wyatts Premium Auto Detailing · godaddysites.com · Mesa/Phoenix · 8/100** — [dossier](data/B3-B4-wyatts-azcustomz.md) — brand-only title, no description/canonical/schema, 137 words, Pexels stock hero, **zero CTAs of any kind**. A dead end in both directions.
**B10 — Heyzee Mobile Detailing · weebly.com · Tucson · 7/100** — [dossier](data/B9-B10-performanceaz-heyzee.md) — title "Home," OG title "My Site," visible H1 **"An error occurred."**, **canonical pointing to a YouTube video**, no phone/address/CTA. 554 words of decent press-release copy that will never be found.

**Cohort integrity:** original pick pristinedetailservicestucson.weebly.com **died during the study** (Weebly 404 while still indexed) — bottom-tier sites don't just underperform, they vanish. mikesmobiledetailing4.godaddysites.com was excluded after verification (copy says "here in San Diego"); "Phoenix Auto Detailing" on Wix is in **British Columbia**; 9 more AZ-sounding out-of-state sites logged in [`cohorts.md`](data/cohorts.md).

---

## 5. Top-10 vs bottom-10: side-by-side patterns

| Dimension | TOP 10 pattern | BOTTOM 10 pattern |
|---|---|---|
| **Domain** | 10/10 custom domains, several keyword/geo-branded (tucsondetails.com, detailphx.com, ceramicprotucson.com) | 10/10 free builder subdomains; one machine-named ("my-business-101101-103077"); one leaks the owner's account handle ("livelymarketer") |
| **Platform** | WordPress ×6 (Divi/Elementor + WP Rocket), Webflow, Duda; 2 built by detailing-specialist vendors (Detailers Roadmap, Optemyz/GHL) | Raw Wix ×2, Square Online ×4, GoDaddy ×2, Weebly ×2 — all free tiers, three showing platform ad banners/badges |
| **Pages** | 10–140 URLs; avg ≈ 60. Service silos + city/neighborhood pages + pricing + FAQ + gallery + blog | 1–4 URLs. No silo, no city pages, no FAQ page, no blog — anywhere |
| **Title tags** | Keyword + city + brand (+ phone at Clean AZ; + price at Tucson Details); CTR-engineered metas w/ ✔☎ (Cool Auto) | "Home", "My Business", "Appointments", brand-only, or ALL-CAPS keyword mash; metas missing (7/10) or typo-ridden |
| **H1** | 9/10 single keyworded H1 ("#1 Auto Detailing and Protection Tucson, AZ") | "Welcome to…", "An error occurred.", "Sign up for our newsletter", "Subscribe Form", or none at all |
| **Schema** | 8/10 ship JSON-LD; leaders ship LocalBusiness+Service+Offer+AggregateRating+Review+FAQPage (Clean AZ 14 blocks; Recon/Cool Auto full graphs) | **0/10 ship any JSON-LD** except Wix's auto-LocalBusiness on B1 |
| **Canonical/robots** | Self-canonicals, index/follow (2 worrying noindex flags noted) | Missing canonicals, or canonicals pointing at **YouTube/Vimeo**; robots defaults |
| **Alt text** | 75–100% coverage (T1 100%, T9 98%) | 0–50% typical (B4 0%) |
| **Page weight** | 147 KB–1.2 MB; scripts 9–72; the disciplined (Recon) inline CSS | 49 KB empty shells → **3 MB booking stubs**; builder runtime dwarfs content |
| **Word count (home)** | 460–4,550 words; avg ≈ 1,900 | 37–554 words; avg ≈ 230 |
| **Blog** | 7/10 have one; leaders post monthly+ with AZ-specific topics (monsoon, packrats, AZ sun, tint law) | 0/10 |
| **Local signals** | NAP consistent sitewide; map embeds (Bob Moses, Zamo excepted); GBP linked; city/suburb/neighborhood pages ×6–12; hours everywhere | NAP absent, buried, or **self-contradicting (two phones on one page; different number on TikTok)**; 2/10 map embeds; zero geo pages |
| **CTAs** | 3–10 per page, paired action+fallback ("BOOK NOW" + "CALL/TEXT"), sticky headers, promo bars w/ codes, UTM-tagged | 0–1; three sites have literally none; phones often not tappable |
| **Booking** | 9/10 online booking (fieldd ×2, OrbisX, Urable, Housecall Pro, native wizards); 2–3 clicks | Square appointment stubs (works but naked) or nothing |
| **Pricing** | 7/10 publish real prices by vehicle size; memberships ×3 (Clean Club, B Cool tiers, maintenance plans); gift cards ×4; promo codes ×3 | One stray number ($120, $19.99) or prices hidden inside JS widgets |
| **Trust** | Review widgets w/ counts (771 / 495 / 850+ / 234), guarantees ("100% Clean Car Guarantee"), licensed/bonded/insured, years (34+, since 1984, since 1992), brand certifications (Ceramic Pro Elite, XPEL, Shine Supply, IGL), galleries, B2B logos, named staff | **Zero on-site proof across all ten.** Best case: the word "guarantee" floating unanchored |
| **Off-site** | 771–850+ Google reviews at top; Yelp pages that rank on their own; Reddit endorsements; YouTube; Carfax; dealer-locator backlinks | 0-review profiles; social-only presence (TikTok) disconnected from web; one LLC registered but reviewless |
| **Design (screenshots)** | Real vehicle photography, dark premium or bright branded palettes, benefit icons, visible ratings above the fold | Blank white/red voids, stock photos, template placeholders, platform ad banners, newsletter popup over hero |

---

## 6. Root-cause analysis

### Why the top sites rank
1. **Entity strength Google can verify**: custom domain + consistent NAP + GBP with hundreds of reviews + Yelp/Facebook/directory echoes + (for the best) LocalBusiness/Service/Review schema tying it together. Google cross-checks all of it; the winners never contradict themselves.
2. **A page for every intent**: "ceramic coating phoenix" hits Bob Moses' exact-match location page; "car detailing gilbert arizona" hits Clean AZ's Gilbert page; "tesla ceramic coating" hits a brand page; "how much does mobile detailing cost in phoenix" hits a blog post that funnels to the price calculator. The bottom ten have one page for zero intents.
3. **Local copy depth**: 800–4,500 words of *Arizona-specific* text (heat, dust, monsoon, packrats) — not generic filler. Google's helpful-content systems reward it; it also earns Reddit/word-of-mouth citations.
4. **Off-site moats**: review velocity (Adrian's newest Google review was 7 days old), Reddit threads that themselves rank, franchise/brand-network backlinks (Ceramic Pro dealer locator, XPEL), YouTube presence.
5. **Longevity + physical reality**: shops with addresses, careers pages, staff names, since-1984/1992 histories. Google's local trust model and humans both eat this up.

### Why the top sites convert
1. **Price transparency kills the #1 objection before contact** (Clean AZ calculator, Cool Auto tables, Airpark list). Where prices are hidden, it's a deliberate high-ticket consultative funnel with a free-quote form, tracked thank-you pages, and call/text options — never an accident.
2. **Booking in ≤3 clicks, 24/7**, on detailing-specific SaaS with live availability, SMS confirmations, accounts, photo upload.
3. **Proof adjacent to every ask**: review widget on the booking page (Clean AZ), review feed one click from every CTA (Adrian), 850+ badge next to "Book Now" (Cool Auto).
4. **Risk reversal + urgency**: "No upfront payments," "100% guarantee," seasonal promo codes (SHINE/FULL/10% OFF bars), membership savings framing ("Save $80 per detail").
5. **Mobile-first calls-to-action**: tappable phones, call-or-text, sticky headers. (Only Bob Moses uses a true sms: link — a market-wide gap.)

### Why the bottom sites stay invisible and lead-starved
1. **Rented subdomains with zero authority** — no links, no brand signals, competing against 30-year-old domains.
2. **Nothing to index**: 37–554 words, no headings (B4), no meta (7/10), JS-only content (Square trio), noindex-grade misconfigurations (canonical → YouTube/Vimeo).
3. **Google can't trust the entity**: no schema, inconsistent phones *within one page* and across platforms, Gmail addresses, "My Business" as a name.
4. **Zero proof**: no reviews on-site and (worse) no review base at all — "0 stars from 0 reviews" while shoppers pick competitors *because of* Google reviews (verbatim Ceramic Pro Tucson customer).
5. **No conversion machinery**: three sites have no CTA whatsoever; others hide the phone; one greets visitors with a newsletter popup. Even direct traffic (business cards, truck decals) leaks away.
6. **Effort collapse**: unedited placeholders ("Service Name"), lorem ipsum, stock heroes, dead sites (Pristine's 404). These read as abandonment to users and to Google's quality systems alike.
The bottom ten owners are often *good businesses* — Landeros has an engaged TikTok; Cleaner Image claims 20 years — but their web presence is an unconfigured cash register bolted to a void.

---

## 7. The Supreme Clean Detailing playbook — out-build the entire market (ordered by impact)

### Phase 0 — Foundations (week 1)
1. **Custom domain, one canonical host** (e.g., supremecleandetailing.com), WordPress (SEO ceiling: Clean AZ pattern) or Webflow (design+speed: Cool Auto pattern). Budget a hard performance ceiling the leaders all miss: **≤200 KB HTML, ≤15 scripts, no slider plugins, no `user-scalable=0`** — you'll beat every top-10 Core Web Vitals profile at launch.
2. **Set up Google Business Profiles** (one per city you physically serve from), matching name/phone/hours everywhere. Single tracked-but-consistent phone number; e-mail on your own domain (never Gmail). This is the entity Google will cross-check for every claim on the site.
3. **Wire a review engine from day one** (post-job SMS/email ask → Google). The market's rank order IS its review order (771/495/850+ at top; 0 at bottom). Target 50+ Google reviews in 90 days, 250+ in year one; respond to every one.

### Phase 1 — Site architecture (weeks 1–3): ~35 launch URLs
```
/                                → "Mobile Car Detailing in Phoenix, AZ | Supreme Clean Detailing"
/services/                       → hub
  /services/interior-detailing/    /services/exterior-detailing/
  /services/full-detail/           /services/ceramic-coating/
  /services/paint-correction/      /services/headlight-restoration/
  /services/pet-hair-removal/      /services/odor-removal-ozone/
  /services/fleet-detailing/       /services/rv-boat-detailing/
/pricing/                        → full tables by vehicle size (see §7.4)
/book/                           → embedded booking wizard
/reviews/                        → live Google feed + counts
/gallery/                        → before/after, organized by service
/about/  /contact/  /faq/  /gift-cards/  /membership/
/service-areas/ + city pages:
  /car-detailing-phoenix-az/  /car-detailing-scottsdale-az/  /car-detailing-tempe-az/
  /car-detailing-mesa-az/  /car-detailing-chandler-az/  /car-detailing-gilbert-az/
  /car-detailing-glendale-az/  /car-detailing-peoria-az/
/blog/ (2 posts/mo minimum)
```
Rationale: this is Clean AZ's proven skeleton + the specialty long-tail pages (pet hair, ozone, RV, fleet) that **nobody in either metro owns as dedicated pages**, + ceramic/paint-correction lines Clean AZ lacks. Phase-2 (months 3–6): neighborhood pages (Adrian/Tucson Details pattern — Arcadia, Ahwatukee, North Scottsdale…), vehicle-brand pages if pushing coatings (Bob Moses' Tesla-page pattern), and a second-city hub if expanding to Tucson.

4. **Internal linking**: breadcrumbs sitewide; every service page links its city variants and vice-versa; footer = NAP + service links + city links + review/booking links (Cool Auto's "Popular Searches" block, done tastefully).

### Phase 2 — On-page formulas (every page, no exceptions)
5. **Title**: `{Service} in {City}, AZ | Supreme Clean Detailing` (+ phone on home/booking: Clean AZ's trick; + "from $X" on priced services: Tucson Details' trick). **Meta description**: benefit + trust stack + phone, engineered like Cool Auto's: "Top-Rated Mobile Detailing in {City} ✔ 5-Star Reviews ✔ Licensed & Insured ✔ We Come to You ☎ (XXX) XXX-XXXX". One keyworded H1; H2s = package names/benefits/FAQs; 800–1,500 unique AZ-flavored words on money pages; 100% descriptive alt text; self-canonical; OG + Twitter cards; **audit for stray noindex/canonical hijacks at launch and quarterly** (it took down nobody yet only because Google is being lenient — see Detail PHX/Buff & Shine).
**Schema (JSON-LD)**: LocalBusiness(+AutoWash) w/ geo/hours/sameAs sitewide; Service+OfferCatalog+Offer on service/pricing pages; AggregateRating+Review (real counts only); FAQPage on FAQ + city pages; BreadcrumbList; HowTo on process content. That's Clean AZ's 14-block stack — no one in Tucson ships FAQPage at all.

### Phase 3 — Conversion machine
6. **Pricing display**: publish it. Tabbed tables by vehicle size (coupe/sedan/small SUV/large SUV/truck/van) with "starting at" + duration + what's-included checklists + condition disclaimer (Cool Auto pattern), and a 60-second "pick your vehicle → see price & availability" wizard as the primary CTA (Clean AZ pattern). Keep quote-only flow *only* for ceramic/PPF (with per-product quote pages + thank-you tracking, Ceramic Pro pattern).
7. **CTA system**: sticky header w/ tel: + sms: ("Call or Text (XXX) XXX-XXXX" — only Bob Moses does sms:, free differentiation) + high-contrast "BOOK NOW"; CTA pair at every scroll depth (action + lower-commitment fallback "Get My Price"/"Free Quote"); promo bar w/ seasonal code (SHINE/FULL pattern); **UTM-tag every CTA placement** (Clean AZ) and run GA4 + Clarity (Cool Auto) so you know which buttons pay.
8. **Booking**: detailing-native SaaS (fieldd, OrbisX, or Urable — all field-proven in this exact market) embedded on /book/ on your own domain; vehicle picker, photo upload, SMS confirmations, accounts, deposits optional. ≤3 clicks from any page. An Adrian & Sons customer literally reviews the *scheduling* as "the best I've ever experienced" — booking UX earns reviews itself.
9. **Risk reversal + offers**: "100% Satisfaction Guarantee — we re-clean it free," "No upfront payment," first child-seat/light pet-hair add-on free (Clean AZ's beloved hook), gift cards, referral program, and a **membership** (monthly/bi-monthly/quarterly by vehicle size with "Save $X per detail" framing — Clean Club / B Cool pattern) for recurring revenue.

### Phase 4 — Trust & proof (the 20× gap)
10. On every page: review badge w/ live count (Trustindex/Elfsight streaming Google reviews — Clean AZ/Adrian pattern); above the fold on home + booking. /reviews page with the raw feed + "Review us" links.
11. Trust bar: **Licensed • Bonded • Insured** (only Cool Auto says all three — say it and mean it) + years in business + "X,000+ vehicles detailed" counter + guarantees + certification logos as earned (IGL/Ceramic Pro/XPEL/Shine Supply). **Get BBB accredited (~$500/yr): literally zero competitors in either metro have it.**
12. Before/after gallery per service; short phone-shot process videos; team page with real names/faces (reviews naming "Juan" and "Christian" convert — people book people).

### Phase 5 — Local & off-site moat
13. **GBP excellence**: weekly photo posts, Q&A seeding, service menus w/ prices, booking link, review responses. The map-pack + Yelp occupy ~⅓ of page one — win them like a second website.
14. **Citations**: Yelp (complete w/ 100+ photos — Buff & Shine has 110), Facebook, Nextdoor, Apple Maps, Bing Places, YellowPages, Carfax (Airpark's 5/5×19 is a quiet weapon), hiredetailing.com, WhirLocal. NAP identical everywhere (the bottom cohort's same-page phone conflicts are the cautionary tale).
15. **Reddit/community presence**: genuinely helpful answers in r/phoenix and r/Tucson threads (they rank top-5 for money terms and mint customers — Cool Auto and Bob Moses get named organically). Never astroturf; sponsor local car meets, post OC before/afters.
16. **Content cadence**: 2 posts/month targeting question + local queries: "How much does mobile detailing cost in Phoenix?" (Clean AZ's does numbers), "Monsoon car care," "AZ sun vs your paint," "Packrat cleanup" (desert-unique, Cool Auto-proven), "AZ window tint laws." Add Google Web Stories (Recon is alone there) and short YouTube clips (Bob Moses' influencer moat started with one video).

### Phase 6 — Measurement & iteration
17. GA4 + Clarity + call tracking (pool numbers like Bob Moses, but keep GBP/site primary number consistent) + per-placement UTM reporting; monthly SERP checks against T1/T6; quarterly technical audit (canonicals, robots, schema validation, CWV).

**What "winning" looks like:** Clean AZ's architecture + Cool Auto's trust stack & booking + Adrian's live reviews & neighborhood mesh + Bob Moses' text-first contact & content moat + Ceramic Pro's funnels — at Recon's page speed, with none of their landmines (noindex tags, missing canonicals, 1 MB sliders, hidden pricing). Nobody in Phoenix or Tucson has assembled all of it. That composite site would enter the market technically better than #1 in both cities on day one; reviews + citations are the only pieces that take time, which is why the review engine starts before the site ships.

---
*Methodology caveats: SERP positions are point-in-time (2026-07-12) Firecrawl organic pulls; map-pack panels aren't directly observable via API (GBP strength inferred from review counts, embeds and links). Two sites (Detail PHX, Buff & Shine) served `noindex` robots meta to our crawler while ranking — treated as UA-conditional platform output and flagged as risk, not as proof Google sees the same. Bottom-cohort review footprints reflect what surfaced in targeted searches; absence of evidence noted as such in* [`offsite-authority.md`](data/offsite-authority.md).
