"""City and service-area pages, the #1 organic lever from the teardown.
Each page: exact-match title & H1, ~450-600 words of genuinely local copy,
pricing anchor, a real review, localized FAQ (FAQPage schema), CTA."""

from build import BIZ, CITIES_SERVED
from content_core import TRUSTBAR, CTA, PRICING_TIERS
from content_gallery import BA_HOME, ba_section

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
            ba_section(
                "Recent transformations",
                "Real before-and-afters from customer vehicles around the corridor.",
                BA_HOME,
                more_link="/gallery/",
            ),
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
    ("They left my car smelling fresh new & deep detailed, and they were able to remove a smell I had in my car.", "Kimberly García", "Google review"),
    ("Anthony has done work for me for years now and I trust him implicitly and his prices are very fair.", "Suanne Dunn", "Google review · Local Guide"),
    ("Recently had my two trucks detailed. Literally came back brand new.", "Jase Archer", "Google review"),
]

FAQ_TRAVEL = (
    "Is there a travel fee?",
    "<p>No. This is inside our standard service area. The price on the <a href='/pricing/'>pricing page</a> is the price.</p>",
)
FAQ_HOA = (
    "I'm in an HOA or apartment. Can you still come?",
    "<p>Almost always. Driveways are simple; for apartments and HOA streets Anthony works tidy and self-contained, and will confirm any property rules with you when booking.</p>",
)


CITY_PAGES = [
    city(
        "/car-detailing-casa-grande-az/",
        "Casa Grande",
        "Mobile Car Detailing in Casa Grande, AZ, We Come to You | Supreme Clean Detailing",
        "Casa Grande's own 5.0★ mobile detailer. Interior, exterior & full details at your driveway, with fair upfront prices and no prepayment. ☎ (520) 840-2452",
        "Car detailing in Casa Grande, AZ, from the detailer who actually lives here",
        "Supreme Clean Detailing is based in Casa Grande. No travel fees and no big-city markup, just 5.0-star work at your driveway.",
        f"""
<p>Casa Grande is home base. From Mission Royale and Coyote Ranch to the new builds pushing out toward
the Lucid plant, Anthony details where you park, whether that's your driveway, the curb or your workplace lot off Florence
Boulevard. That means <strong>no travel fees and no “route day” waiting</strong> like you get from Phoenix
companies quoting our zip codes.</p>
<p>Local vehicles fight local problems: ag-field dust that works into every vent along Jimmie Kerr and
I-8, monsoon haboobs that coat a freshly washed truck in an afternoon, and a sun that bakes dashboards,
leather and clear coat eleven months a year. A drive-through tunnel wash drags that grit straight across
your paint. A <a href="/services/exterior-detailing/">proper hand wash</a> lifts it off, and an
<a href="/services/interior-detailing/">interior deep clean</a> pulls it out of the carpet, seams and
vents where it settles.</p>
<p>Whether it's the family SUV after a season of practices, a work truck that needs to make a good
impression, or getting top dollar before a trade-in at one of the dealerships on Florence Blvd,
you'll get the same treatment the <a href="/reviews/">reviews</a> describe: on time, fair price,
dealership-quality result, checked panel by panel with you before payment.</p>
""",
        [
            (
                "Do you really come to any part of Casa Grande?",
                "<p>Yes, citywide, from Mission Royale to Ghost Ranch to the industrial corridor, plus Stanfield and Toltec just outside town.</p>",
            ),
            FAQ_HOA,
            (
                "How fast can you get to me?",
                f"<p>Being local, we're often out within a couple of days, and same-week for spill or odor emergencies. <a href='sms:{TEL}'>Text {PHONE}</a> with a photo to grab the next slot.</p>",
            ),
        ],
        REV_A,
    ),
    city(
        "/car-detailing-maricopa-az/",
        "Maricopa",
        "Mobile Car Detailing in Maricopa, AZ, We Come to You | Supreme Clean Detailing",
        "Mobile car detailing in Maricopa AZ: Rancho El Dorado, Province, Tortosa & more. 5.0★, upfront quotes, no prepayment. ☎ (520) 840-2452",
        "Car detailing in Maricopa, AZ, without the drive up the 347",
        "Your SR-347 commute is hard enough. We bring the detail to Rancho El Dorado, Province, Glennwilde, Tortosa and anywhere else in Maricopa.",
        f"""
<p>Every Maricopa driver knows what the 347 does to a car: sixty-plus minutes a day of highway bugs,
brake dust and blowing dust between here and the Valley. Add school runs and weekend trips past the
Ak-Chin farmland, and even a newer vehicle looks tired fast.</p>
<p>Supreme Clean Detailing comes to you in Rancho El Dorado, Province, Homestead, Glennwilde, Tortosa,
Cobblestone Farms and Senita, while you work from home or take the day. The
<a href="/services/full-detail/">full detail</a> resets the whole vehicle; the
<a href="/services/exterior-detailing/">wash &amp; shine</a> on a monthly rotation keeps commuters
presentable; and the <a href="/services/pet-hair-removal/">pet hair</a> and
<a href="/services/odor-removal/">odor</a> services fix what the dog and the drive-through dinners
left behind.</p>
<p>Phoenix mobile detailers treat Maricopa as an out-of-area surcharge. For us it's a 20-minute hop on
238/347, at standard rates, on time, with the owner doing the work.</p>
""",
        [
            FAQ_TRAVEL,
            (
                "Can you detail at my workplace in Chandler or Ahwatukee instead?",
                "<p>Often yes. If you commute up the 347, ask about a workplace visit, and Anthony will confirm based on the schedule and parking.</p>",
            ),
            FAQ_HOA,
        ],
        REV_B,
    ),
    city(
        "/car-detailing-eloy-az/",
        "Eloy",
        "Mobile Car Detailing in Eloy, AZ, to Robson Ranch & Beyond | Supreme Clean Detailing",
        "Mobile car detailing in Eloy AZ, covering Robson Ranch, Toltec & Picacho. 5.0★ owner-operated service at your driveway. ☎ (520) 840-2452",
        "Car detailing in Eloy, AZ, Robson Ranch's driveway detailer",
        "From Robson Ranch golf-cart garages to work trucks off Sunshine Boulevard, we detail where you park.",
        f"""
<p>Eloy sits in the dustiest stretch of the corridor. Half the year the fields are working and the
other half the wind is. Supreme Clean Detailing is 15 minutes up the road in Casa Grande, which makes
Eloy, Toltec and Picacho standard service area, not a favor.</p>
<p><strong>Robson Ranch residents:</strong> you're our favorite kind of stop, with a shaded driveway, a
well-kept vehicle, and an owner who appreciates the difference between a cheap tunnel wash and a proper
<a href="/services/exterior-detailing/">hand wash and sealant</a>. Many neighbors rotate a
wash &amp; shine monthly and a <a href="/services/full-detail/">full detail</a> once or twice a year.
Ask about the maintenance plan and keep both cars on schedule.</p>
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
                f"<p>Yes, carts love a detail too. Text {PHONE} for a quick cart quote (they're fast and affordable).</p>",
            ),
        ],
        REV_A,
    ),
    city(
        "/car-detailing-coolidge-az/",
        "Coolidge",
        "Mobile Car Detailing in Coolidge, AZ, at Your Door | Supreme Clean Detailing",
        "Mobile car detailing in Coolidge AZ, 5.0★ owner-operated, with upfront quotes, no prepayment, and we come to you. ☎ (520) 840-2452",
        "Car detailing in Coolidge, AZ, big-city results with hometown treatment",
        "Fifteen minutes from our Casa Grande base. New-build driveways off Arizona Blvd, CAC staff lots and farm trucks, all standard service.",
        f"""
<p>Coolidge is growing fast, with new subdivisions filling in along Arizona Boulevard and Vah Ki Inn Rd,
commuters splitting toward Florence, Casa Grande and the Valley, but detailing options haven't kept
up. Most residents either burn a Saturday driving to a shop or settle for the gas-station wash.</p>
<p>Supreme Clean fixes that the simple way: <strong>we come to your driveway</strong>. A
<a href="/services/full-detail/">full detail</a> for the family SUV, an
<a href="/services/interior-detailing/">interior deep clean</a> for the truck that hauls crew and
tools all week, <a href="/services/headlight-restoration/">headlight restoration</a> before you list a
vehicle on Marketplace. Students and staff at Central Arizona College: a workplace-lot detail while
you're in class is the easiest clean car you'll ever get.</p>
<p>You'll know the price before we start (see <a href="/pricing/">pricing</a>), you pay nothing up
front, and you approve the work panel by panel before we leave, the same 5.0-star treatment in every
<a href="/reviews/">review</a>.</p>
""",
        [
            FAQ_TRAVEL,
            FAQ_HOA,
            (
                "Farm and ranch vehicles?",
                "<p>Bring us your worst, whether it's ag dust, feed or dogs. Condition pricing is quoted honestly from photos before we start.</p>",
            ),
        ],
        REV_B,
    ),
    city(
        "/car-detailing-florence-az/",
        "Florence",
        "Mobile Car Detailing in Florence, AZ, to Anthem & Historic Florence | Supreme Clean Detailing",
        "Mobile car detailing in Florence AZ, covering Anthem at Merrill Ranch, Crestfield & historic downtown. 5.0★, we come to you. ☎ (520) 840-2452",
        "Car detailing in Florence, AZ, from Anthem to the historic district",
        "Anthem at Merrill Ranch, Crestfield Manor, Magic Ranch and downtown. Supreme Clean details at your driveway, on your schedule.",
        f"""
<p>Florence stretches a long way, from the golf-cart streets of Anthem at Merrill Ranch down through
the oldest main street in the state, and none of it is close to a real detail shop. That's the point
of mobile: <strong>the shop comes to you.</strong></p>
<p>Anthem residents keep two-car garages full of well-loved vehicles that deserve better than dust
covers; a monthly <a href="/services/exterior-detailing/">wash &amp; shine</a> plus an annual
<a href="/services/full-detail/">full detail</a> keeps them showroom-side. Along Hunt Highway and the
newer builds, commuter SUVs collect the same 79/Hunt dust and drive-through crumbs as everywhere else, and
the <a href="/services/interior-detailing/">interior deep clean</a> resets them in an afternoon.</p>
<p>Selling or trading? Between a detail and a <a href="/services/headlight-restoration/">headlight
restoration</a>, most sellers make the cost back several times over at the negotiation table.</p>
""",
        [
            FAQ_TRAVEL,
            (
                "Do you come out to Anthem at Merrill Ranch?",
                "<p>Yes. Anthem, Crestfield, Magic Ranch and the historic district are all standard service area, with no surcharge.</p>",
            ),
            FAQ_HOA,
        ],
        REV_A,
    ),
    city(
        "/car-detailing-arizona-city-az/",
        "Arizona City",
        "Mobile Car Detailing in Arizona City, AZ, We Come to You | Supreme Clean Detailing",
        "Mobile car detailing in Arizona City AZ, 5.0★ owner-operated, with upfront quotes, no travel fees and no prepayment. ☎ (520) 840-2452",
        "Car detailing in Arizona City, no shop required, we're at your door",
        "Ten minutes from our base. Lakeside homes, commuter cars and desert toys, all detailed in your driveway at standard rates.",
        f"""
<p>Arizona City might be the most underserved zip code in the corridor: no detail shop for miles, and
Phoenix or Tucson mobile outfits either decline the trip or pad the bill for it. We're ten minutes away
in Casa Grande, so for us this is <strong>standard service area at standard prices</strong>.</p>
<p>Homes around the lake deal with a special combo of dust plus hard-water spotting from sprinklers;
our <a href="/services/exterior-detailing/">hand wash</a> handles the light spotting, and dedicated
water-spot treatment is available when the mineral etching has had a summer to bake in. Commuters
running Sunland Gin to I-10 every day book the monthly wash rotation; families call us for the
<a href="/services/interior-detailing/">interior deep clean</a> when the school-run backseat finally
reaches critical mass, and for whatever the <a href="/services/odor-removal/">smell</a> turns out
to be.</p>
<p>Same deal as everywhere we work: exact price from your photos before booking, no prepayment, and a
walk-around before you pay a dollar.</p>
""",
        [
            FAQ_TRAVEL,
            (
                "Sand toys and side-by-sides?",
                f"<p>Post-dunes cleanups welcome. Text {PHONE} a photo of the carnage for a straight quote.</p>",
            ),
            FAQ_HOA,
        ],
        REV_B,
    ),
    city(
        "/car-detailing-san-tan-valley-az/",
        "San Tan Valley",
        "Mobile Car Detailing in San Tan Valley, AZ | Supreme Clean Detailing",
        "Mobile car detailing in San Tan Valley AZ, covering Johnson Ranch, San Tan Heights and Copper Basin. 5.0★, we come to you. ☎ (520) 840-2452",
        "Car detailing in San Tan Valley, Johnson Ranch to Copper Basin",
        "Hunt Highway traffic, desert dust and busy families: the perfect storm for a driveway detail. We handle all of it, at your address.",
        f"""
<p>San Tan Valley grew faster than its services, including car care. Between Hunt Highway construction
dust, San Tan Mountain trail days and the daily grind to Queen Creek and Gilbert jobs, STV vehicles work
hard. Supreme Clean covers Johnson Ranch, San Tan Heights, Copper Basin, Skyline Ranch, Morning Sun
Farms and everything between, all <strong>at your driveway, at standard rates</strong>.</p>
<p>Most-booked here: the <a href="/services/full-detail/">full detail</a> for family SUVs and trucks
(three-row pricing is on the <a href="/pricing/">pricing page</a> in black and white), the
<a href="/services/pet-hair-removal/">pet-hair package</a> for the dogs who own the back seat, and
pre-sale spruce-ups, because STV's Marketplace car scene is busy, and a professional detail routinely adds several
times that to a sale price.</p>
<p>You get the owner, on time, with everything needed on board. Check the
<a href="/reviews/">reviews</a>, where “dealership quality” isn't our phrase, it's a customer's.</p>
""",
        [
            FAQ_TRAVEL,
            FAQ_HOA,
            (
                "Weekend appointments?",
                "<p>Yes. Weekends book first in STV, so grab a slot a few days ahead when you can.</p>",
            ),
        ],
        REV_A,
    ),
    city(
        "/car-detailing-queen-creek-az/",
        "Queen Creek",
        "Mobile Car Detailing in Queen Creek, AZ, at Your Home | Supreme Clean Detailing",
        "Mobile car detailing in Queen Creek AZ, Encanterra to Harvest. 5.0★ owner-operated, upfront prices, no prepayment, we come to you. ☎ (520) 840-2452",
        "Car detailing in Queen Creek, without Phoenix-metro pricing",
        "Encanterra, Harvest, Emperor Estates, the Ellsworth corridor: detailed at your driveway by the 5.0-star owner-operator from just down the road.",
        f"""
<p>Queen Creek sits at the edge of the Phoenix metro, which means metro detailers quote metro prices
and often add a surcharge for “the drive.” We come up from the Casa Grande side, so Queen Creek and the
Encanterra corridor are <strong>standard service area</strong> for us: same fair pricing our
<a href="/reviews/">reviews</a> call “half of the quotes I received.”</p>
<p>QC garages hold nice vehicles, and nice vehicles deserve the careful version of everything: two-bucket
<a href="/services/exterior-detailing/">hand washing</a> (never a tunnel brush), leather cleaned and
conditioned against the sun, and a <a href="/services/full-detail/">full detail</a> finished with a
panel-by-panel walk-around before you pay. Horse property along Sossaman or Hawes? Dust and hay ride
home in every vent, and the <a href="/services/interior-detailing/">interior deep clean</a> is built for
exactly that.</p>
<p>Golf-community residents at Encanterra: ask about pairing your vehicles on one visit, because two-car
appointments are our specialty (<em>“did an excellent job detailing both my cars,”</em> per Ron's
review).</p>
""",
        [
            (
                "Is Queen Creek really in your service area?",
                "<p>Yes. It's our northern edge and a regular route. Standard pricing applies, and there's no drive surcharge.</p>",
            ),
            FAQ_HOA,
            (
                "Can you do two vehicles in one visit?",
                "<p>Gladly. It's the most efficient way to book us, and multi-vehicle visits get priority scheduling.</p>",
            ),
        ],
        REV_B,
    ),
]
