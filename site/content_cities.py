"""City / service-area pages — the #1 organic lever from the teardown.
Each page: exact-match title & H1, ~450-600 words of genuinely local copy,
pricing anchor, a real review, localized FAQ (FAQPage schema), CTA."""

from build import BIZ, CITIES_SERVED
from content_core import TRUSTBAR, CTA, PRICING_TIERS

TEL = BIZ["phone_e164"]
PHONE = BIZ["phone_display"]

AREAS_MINI = (
    "areas",
    {
        "title": "Also serving",
        "cities": CITIES_SERVED,
    },
)


def city(slug, name, title, desc, h1, sub, local_html, faq_items, review):
    return {
        "slug": slug.strip("/"),
        "nav_active": "/service-areas/",
        "priority": "0.8",
        "title": title,
        "desc": desc,
        "h1": h1,
        "hero_sub": sub,
        "crumbs": [("Service areas", "/service-areas/"), (name, None)],
        "sections": [
            TRUSTBAR,
            ("prose", {"title": f"Mobile detailing in {name}, done at your driveway", "html": local_html}),
            ("pricing", PRICING_TIERS),
            (
                "reviews",
                {
                    "title": f"Rated 5.0 by drivers near {name}",
                    "items": review,
                    "all_link": "/reviews/",
                },
            ),
            ("faq", {"title": f"{name} questions", "items": faq_items}),
            AREAS_MINI,
            CTA,
        ],
    }


REV_A = [
    ("Pricing was half of the quotes I received from several others! Arrived on time, did an excellent job detailing both my cars.", "Ron McClure", "Google review"),
    ("This young man works hard to make your vehicle look like dealership quality.", "Kim Rupert", "Google review"),
    ("On-time, reasonably priced, and performed incredible work.", "Baby Stuey", "Google review · Local Guide"),
]
REV_B = [
    ("They left my car smelling fresh new & deep detailed — they were able to remove a smell I had in my car.", "Kimberly García", "Google review"),
    ("Anthony has done work for me for years now and I trust him implicitly and his prices are very fair.", "Suanne Dunn", "Google review · Local Guide"),
    ("Recently had my two trucks detailed — literally came back brand new.", "Jase Archer", "Google review"),
]

FAQ_TRAVEL = (
    "Is there a travel fee?",
    "<p>No — this is inside our standard service area. The price on the <a href='/pricing/'>pricing page</a> is the price.</p>",
)
FAQ_HOA = (
    "I'm in an HOA / apartment — can you still come?",
    "<p>Almost always. Driveways are simple; for apartments and HOA streets Anthony works tidy and self-contained, and will confirm any property rules with you when booking.</p>",
)


CITY_PAGES = [
    city(
        "/car-detailing-casa-grande-az/",
        "Casa Grande",
        "Car Detailing Casa Grande, AZ — Mobile, from $69 | Supreme Clean Detailing",
        "Casa Grande's own 5.0★ mobile detailer. Interior, exterior & full details at your driveway — fair upfront prices, no prepayment. ☎ (520) 840-2452",
        "Car detailing in Casa Grande, AZ — from the detailer who actually lives here",
        "Supreme Clean Detailing is based in Casa Grande. No travel fees, no big-city markup — just 5.0-star work at your driveway.",
        f"""
<p>Casa Grande is home base. From Mission Royale and Coyote Ranch to the new builds pushing out toward
the Lucid plant, Anthony details where you park — driveway, curb or your workplace lot off Florence
Boulevard. That means <strong>no travel fees and no “route day” waiting</strong> like you get from Phoenix
companies quoting our zip codes.</p>
<p>Local vehicles fight local problems: ag-field dust that works into every vent along Jimmie Kerr and
I-8, monsoon haboobs that coat a freshly washed truck in an afternoon, and a sun that bakes dashboards,
leather and clear coat eleven months a year. A drive-through tunnel wash drags that grit straight across
your paint. A <a href="/services/exterior-detailing/">proper hand wash</a> lifts it off — and an
<a href="/services/interior-detailing/">interior deep clean</a> pulls it out of the carpet, seams and
vents where it settles.</p>
<p>Whether it's the family SUV after a season of practices, a work truck that needs to make a good
impression, or getting top dollar before a trade-in at one of the dealerships on Florence Blvd,
you'll get the same treatment the <a href="/reviews/">reviews</a> describe: on time, fair price,
dealership-quality result — checked panel by panel with you before payment.</p>
""",
        [
            (
                "Do you really come to any part of Casa Grande?",
                "<p>Yes — citywide, from Mission Royale to Ghost Ranch to the industrial corridor, plus Stanfield and Toltec just outside town.</p>",
            ),
            FAQ_HOA,
            (
                "How fast can you get to me?",
                f"<p>Being local, often within a couple of days — and same-week for spill/odor emergencies. <a href='sms:{TEL}'>Text {PHONE}</a> with a photo to grab the next slot.</p>",
            ),
        ],
        REV_A,
    ),
    city(
        "/car-detailing-maricopa-az/",
        "Maricopa",
        "Car Detailing Maricopa, AZ — Mobile, We Come to You | Supreme Clean Detailing",
        "Mobile car detailing in Maricopa AZ: Rancho El Dorado, Province, Tortosa & more. 5.0★, upfront prices from $69, no prepayment. ☎ (520) 840-2452",
        "Car detailing in Maricopa, AZ — without the drive up the 347",
        "Your SR-347 commute is hard enough. We bring the detail to Rancho El Dorado, Province, Glennwilde, Tortosa — anywhere in Maricopa.",
        f"""
<p>Every Maricopa driver knows what the 347 does to a car: sixty-plus minutes a day of highway bugs,
brake dust and blowing dust between here and the Valley. Add school runs and weekend trips past the
Ak-Chin farmland, and even a newer vehicle looks tired fast.</p>
<p>Supreme Clean Detailing comes to you — Rancho El Dorado, Province, Homestead, Glennwilde, Tortosa,
Cobblestone Farms, Senita — while you work from home or take the day. The
<a href="/services/full-detail/">full detail</a> resets the whole vehicle; the
<a href="/services/exterior-detailing/">wash &amp; shine</a> on a monthly rotation keeps commuters
presentable; and the <a href="/services/pet-hair-removal/">pet hair</a> and
<a href="/services/odor-removal/">odor</a> services fix what the dog and the drive-through dinners
left behind.</p>
<p>Phoenix mobile detailers treat Maricopa as an out-of-area surcharge. For us it's a 20-minute hop on
238/347 — standard rates, on time, with the owner doing the work.</p>
""",
        [
            FAQ_TRAVEL,
            (
                "Can you detail at my workplace in Chandler or Ahwatukee instead?",
                "<p>Often yes — if you commute up the 347, ask about a workplace visit; Anthony will confirm based on the schedule and parking.</p>",
            ),
            FAQ_HOA,
        ],
        REV_B,
    ),
    city(
        "/car-detailing-eloy-az/",
        "Eloy",
        "Car Detailing Eloy, AZ — Mobile to Robson Ranch & Beyond | Supreme Clean Detailing",
        "Mobile car detailing in Eloy AZ — Robson Ranch, Toltec & Picacho. 5.0★ owner-operated service at your driveway, from $69. ☎ (520) 840-2452",
        "Car detailing in Eloy, AZ — Robson Ranch's driveway detailer",
        "From Robson Ranch golf-cart garages to work trucks off Sunshine Boulevard, we detail where you park.",
        f"""
<p>Eloy sits in the dustiest stretch of the corridor — half the year the fields are working and the
other half the wind is. Supreme Clean Detailing is 15 minutes up the road in Casa Grande, which makes
Eloy, Toltec and Picacho standard service area, not a favor.</p>
<p><strong>Robson Ranch residents:</strong> you're our favorite kind of stop — a shaded driveway, a
well-kept vehicle, and an owner who appreciates the difference between a $10 tunnel wash and a proper
<a href="/services/exterior-detailing/">hand wash and sealant</a>. Many neighbors rotate a
wash &amp; shine monthly and a <a href="/services/full-detail/">full detail</a> once or twice a year —
ask about the maintenance plan and keep both cars on schedule.</p>
<p>And if you've just watched the jumpers land at Skydive Arizona with the windows down, we know exactly
what the inside of your car looks like. The <a href="/services/interior-detailing/">interior deep
clean</a> gets the desert back out of it.</p>
""",
        [
            FAQ_TRAVEL,
            (
                "Do you work inside Robson Ranch?",
                "<p>Regularly. Anthony works clean and quiet, respects community rules, and can coordinate gate access when you book.</p>",
            ),
            (
                "Golf cart detailing?",
                f"<p>Yes — carts love a detail too. Text {PHONE} for a quick cart quote (they're fast and affordable).</p>",
            ),
        ],
        REV_A,
    ),
    city(
        "/car-detailing-coolidge-az/",
        "Coolidge",
        "Car Detailing Coolidge, AZ — Mobile Detailing at Your Door | Supreme Clean Detailing",
        "Mobile car detailing in Coolidge AZ — 5.0★ owner-operated, upfront prices from $69, no prepayment, we come to you. ☎ (520) 840-2452",
        "Car detailing in Coolidge, AZ — big-city results, hometown treatment",
        "Fifteen minutes from our Casa Grande base. New-build driveways off Arizona Blvd, CAC staff lots, farm trucks — all standard service.",
        f"""
<p>Coolidge is growing fast — new subdivisions filling in along Arizona Boulevard and Vah Ki Inn Rd,
commuters splitting toward Florence, Casa Grande and the Valley — but detailing options haven't kept
up. Most residents either burn a Saturday driving to a shop or settle for the gas-station wash.</p>
<p>Supreme Clean fixes that the simple way: <strong>we come to your driveway</strong>. A
<a href="/services/full-detail/">full detail</a> for the family SUV, an
<a href="/services/interior-detailing/">interior deep clean</a> for the truck that hauls crew and
tools all week, <a href="/services/headlight-restoration/">headlight restoration</a> before you list a
vehicle on Marketplace. Students and staff at Central Arizona College: a workplace-lot detail while
you're in class is the easiest clean car you'll ever get.</p>
<p>You'll know the price before we start (see <a href="/pricing/">pricing</a>), you pay nothing up
front, and you approve the work panel by panel before we leave — the same 5.0-star treatment in every
<a href="/reviews/">review</a>.</p>
""",
        [
            FAQ_TRAVEL,
            FAQ_HOA,
            (
                "Farm and ranch vehicles?",
                "<p>Bring us your worst — ag dust, feed, dogs and all. Condition pricing is quoted honestly from photos before we start.</p>",
            ),
        ],
        REV_B,
    ),
    city(
        "/car-detailing-florence-az/",
        "Florence",
        "Car Detailing Florence, AZ — Mobile to Anthem & Historic Florence | Supreme Clean Detailing",
        "Mobile car detailing in Florence AZ — Anthem at Merrill Ranch, Crestfield & historic downtown. 5.0★, from $69, we come to you. ☎ (520) 840-2452",
        "Car detailing in Florence, AZ — from Anthem to the historic district",
        "Anthem at Merrill Ranch, Crestfield Manor, Magic Ranch, downtown — Supreme Clean details at your driveway, on your schedule.",
        f"""
<p>Florence stretches a long way — from the golf-cart streets of Anthem at Merrill Ranch down through
the oldest main street in the state — and none of it is close to a real detail shop. That's the point
of mobile: <strong>the shop comes to you.</strong></p>
<p>Anthem residents keep two-car garages full of well-loved vehicles that deserve better than dust
covers; a monthly <a href="/services/exterior-detailing/">wash &amp; shine</a> plus an annual
<a href="/services/full-detail/">full detail</a> keeps them showroom-side. Along Hunt Highway and the
newer builds, commuter SUVs collect the same 79/Hunt dust and drive-through crumbs as everywhere else —
the <a href="/services/interior-detailing/">interior deep clean</a> resets them in an afternoon.</p>
<p>Selling or trading? Between the detail and a $60 <a href="/services/headlight-restoration/">headlight
restoration</a>, most sellers make the cost back several times over at the negotiation table.</p>
""",
        [
            FAQ_TRAVEL,
            (
                "Do you come out to Anthem at Merrill Ranch?",
                "<p>Yes — Anthem, Crestfield, Magic Ranch and the historic district are all standard service area, no surcharge.</p>",
            ),
            FAQ_HOA,
        ],
        REV_A,
    ),
    city(
        "/car-detailing-arizona-city-az/",
        "Arizona City",
        "Car Detailing Arizona City, AZ — Mobile, We Come to You | Supreme Clean Detailing",
        "Mobile car detailing in Arizona City AZ — 5.0★ owner-operated, upfront pricing from $69, no travel fees, no prepayment. ☎ (520) 840-2452",
        "Car detailing in Arizona City — no shop required, we're at your door",
        "Ten minutes from our base. Lakeside homes, commuter cars and desert toys — detailed in your driveway at standard rates.",
        f"""
<p>Arizona City might be the most underserved zip code in the corridor: no detail shop for miles, and
Phoenix or Tucson mobile outfits either decline the trip or pad the bill for it. We're ten minutes away
in Casa Grande — for us this is <strong>standard service area at standard prices</strong>.</p>
<p>Homes around the lake deal with a special combo of dust plus hard-water spotting from sprinklers;
our <a href="/services/exterior-detailing/">hand wash</a> handles the light spotting, and dedicated
water-spot treatment is available when the mineral etching has had a summer to bake in. Commuters
running Sunland Gin to I-10 every day book the monthly wash rotation; families call us for the
<a href="/services/interior-detailing/">interior deep clean</a> when the school-run backseat finally
reaches critical mass — and for whatever the <a href="/services/odor-removal/">smell</a> turns out
to be.</p>
<p>Same deal as everywhere we work: exact price from your photos before booking, no prepayment, and a
walk-around before you pay a dollar.</p>
""",
        [
            FAQ_TRAVEL,
            (
                "Sand toys and side-by-sides?",
                f"<p>Post-dunes cleanups welcome — text {PHONE} a photo of the carnage for a straight quote.</p>",
            ),
            FAQ_HOA,
        ],
        REV_B,
    ),
    city(
        "/car-detailing-san-tan-valley-az/",
        "San Tan Valley",
        "Car Detailing San Tan Valley, AZ — Mobile Detailing | Supreme Clean Detailing",
        "Mobile car detailing in San Tan Valley AZ — Johnson Ranch, San Tan Heights, Copper Basin. 5.0★, from $69, we come to you. ☎ (520) 840-2452",
        "Car detailing in San Tan Valley — Johnson Ranch to Copper Basin",
        "Hunt Highway traffic, desert dust and busy families: the perfect storm for a driveway detail. We handle all of it, at your address.",
        f"""
<p>San Tan Valley grew faster than its services — including car care. Between Hunt Highway construction
dust, San Tan Mountain trail days and the daily grind to Queen Creek and Gilbert jobs, STV vehicles work
hard. Supreme Clean covers Johnson Ranch, San Tan Heights, Copper Basin, Skyline Ranch, Morning Sun
Farms and everything between — <strong>at your driveway, standard rates</strong>.</p>
<p>Most-booked here: the <a href="/services/full-detail/">full detail</a> for family SUVs and trucks
(three-row pricing is on the <a href="/pricing/">pricing page</a> in black and white), the
<a href="/services/pet-hair-removal/">pet-hair package</a> for the dogs who own the back seat, and
pre-sale spruce-ups — STV's Marketplace car scene is busy, and a $199 detail routinely adds several
times that to a sale price.</p>
<p>You get the owner, on time, with everything needed on board. Check the
<a href="/reviews/">reviews</a> — “dealership quality” isn't our phrase, it's a customer's.</p>
""",
        [
            FAQ_TRAVEL,
            FAQ_HOA,
            (
                "Weekend appointments?",
                "<p>Yes — weekends book first in STV, so grab a slot a few days ahead when you can.</p>",
            ),
        ],
        REV_A,
    ),
    city(
        "/car-detailing-queen-creek-az/",
        "Queen Creek",
        "Car Detailing Queen Creek, AZ — Mobile Detailing at Your Home | Supreme Clean Detailing",
        "Mobile car detailing in Queen Creek AZ — Encanterra to Harvest. 5.0★ owner-operated, upfront prices, no prepayment, we come to you. ☎ (520) 840-2452",
        "Car detailing in Queen Creek — without Phoenix-metro pricing",
        "Encanterra, Harvest, Emperor Estates, the Ellsworth corridor: detailed at your driveway by the 5.0-star owner-operator from just down the road.",
        f"""
<p>Queen Creek sits at the edge of the Phoenix metro, which means metro detailers quote metro prices —
and often add a surcharge for “the drive.” We come up from the Casa Grande side, so Queen Creek and the
Encanterra corridor are <strong>standard service area</strong> for us: same fair pricing our
<a href="/reviews/">reviews</a> call “half of the quotes I received.”</p>
<p>QC garages hold nice vehicles, and nice vehicles deserve the careful version of everything: two-bucket
<a href="/services/exterior-detailing/">hand washing</a> (never a tunnel brush), leather cleaned and
conditioned against the sun, and a <a href="/services/full-detail/">full detail</a> finished with a
panel-by-panel walk-around before you pay. Horse property along Sossaman or Hawes? Dust and hay ride
home in every vent — the <a href="/services/interior-detailing/">interior deep clean</a> is built for
exactly that.</p>
<p>Golf-community residents at Encanterra: ask about pairing your vehicles on one visit — two-car
appointments are our specialty (<em>“did an excellent job detailing both my cars,”</em> per Ron's
review).</p>
""",
        [
            (
                "Is Queen Creek really in your service area?",
                "<p>Yes — it's our northern edge and a regular route. Standard pricing applies; there's no drive surcharge.</p>",
            ),
            FAQ_HOA,
            (
                "Can you do two vehicles in one visit?",
                "<p>Gladly — it's the most efficient way to book us, and multi-vehicle visits get priority scheduling.</p>",
            ),
        ],
        REV_B,
    ),
]
