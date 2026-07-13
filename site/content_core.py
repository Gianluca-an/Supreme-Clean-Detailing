"""Core pages: home, services hub, pricing, book, reviews, gallery, about, faq,
contact, service-areas hub, 404.

PRICING NOTE (owner action): every dollar figure below is a market-informed
"starting at" placeholder based on the competitive teardown (value-positioned
under Clean AZ $177-277 and Cool Auto $79-445, consistent with review feedback
"half of the quotes I received"). Anthony must confirm/adjust before launch —
all prices live in PRICING_TIERS and ADDONS only.
"""

from build import BIZ, CITIES_SERVED

TEL = BIZ["phone_e164"]
PHONE = BIZ["phone_display"]

# ------------------------------------------------------------ shared blocks --

TRUSTBAR = (
    "trustbar",
    {
        "items": [
            {"icon": "star", "text": "5.0 ★ on Google (20 reviews)"},
            {"icon": "truck", "text": "Mobile — we come to you"},
            {"icon": "clock", "text": "On time, every time"},
            {"icon": "cash", "text": "Fair, upfront pricing"},
            {"icon": "shield", "text": "100% satisfaction guarantee"},
        ]
    },
)

PRICING_TIERS = {
    "title": "Simple, upfront pricing",
    "sub": "Starting prices by vehicle size — no games, no prepayment. Heavier soiling (pet hair, deep stains, sand) may add time; Anthony confirms your exact price before he starts.",
    "tiers": [
        {
            "name": "Exterior Wash & Shine",
            "tagline": "Hand wash the desert dust off — never a scratchy tunnel wash.",
            "prices": [("Car / coupe", "$69"), ("Truck / SUV", "$89"), ("XL / 3-row / lifted", "$109")],
            "time": "About 1–1.5 hours",
            "includes": [
                "Foam hand wash &amp; soft-towel dry",
                "Wheels, tires &amp; wheel wells cleaned",
                "Tire shine + trim dressing",
                "Bug &amp; light water-spot removal",
                "Streak-free exterior glass",
                "Spray sealant for gloss &amp; protection",
            ],
        },
        {
            "name": "Interior Deep Clean",
            "tagline": "Every vent, seam and cupholder — like the day you bought it.",
            "prices": [("Car / coupe", "$139"), ("Truck / SUV", "$169"), ("XL / 3-row / van", "$199")],
            "time": "About 2–3 hours",
            "includes": [
                "Full vacuum incl. trunk &amp; seat rails",
                "Steam clean of hard surfaces",
                "Carpet &amp; mat shampoo (light stains)",
                "Seats deep-cleaned (cloth or leather)",
                "Door jambs, vents, console detailed",
                "Interior glass + fresh finish scent",
            ],
        },
        {
            "name": "Full Detail",
            "tagline": "Interior + exterior in one visit. Our most-booked service.",
            "popular": True,
            "prices": [("Car / coupe", "$199"), ("Truck / SUV", "$249"), ("XL / 3-row / van", "$299")],
            "time": "About 3–5 hours",
            "includes": [
                "Everything in Interior Deep Clean",
                "Everything in Exterior Wash &amp; Shine",
                "Door jambs &amp; trunk seals detailed",
                "Engine bay wipe-down on request",
                "Final walk-around with you before we leave",
            ],
        },
    ],
    "note": "Prices are starting points for average-condition vehicles and may adjust for heavy pet hair, sand, spills or long-neglected interiors — you'll always know the number before work starts. Ask about the maintenance plan: booked monthly or every other month, returning customers save on every visit.",
}

ADDONS = (
    "addons",
    {
        "title": "Popular add-ons",
        "sub": "Bolt these onto any package — or book them on their own.",
        "items": [
            ("Pet hair removal", "from $40", "Our two-step process pulls embedded hair out of carpet and seats."),
            ("Odor elimination", "from $75", "Smoke, pets, spilled milk — deep-source treatment, not perfume. Per Kimberly's review: “they were able to remove a smell I had in my car.”"),
            ("Headlight restoration", "$60 / pair", "Cloudy, yellowed lenses restored and sealed — see (and pass inspection) again."),
            ("Seat & carpet shampoo", "from $60", "Hot-water extraction for tough stains — water spots and set-in marks included."),
            ("Engine bay detail", "$50", "Careful degrease, rinse and dress — shows like a dealer lot."),
            ("Wax / sealant upgrade", "$45", "Longer-lasting protection against the Arizona sun."),
        ],
    },
)

STEPS = (
    "steps",
    {
        "title": "Booked in 60 seconds, detailed at your driveway",
        "items": [
            (
                "Text or book online",
                f'Send a photo of your vehicle to <a href="sms:{TEL}">{PHONE}</a> or use the booking form. Anthony replies the same day with your exact price.',
            ),
            (
                "We come to you",
                "Home, work, anywhere in the Casa Grande–Maricopa–San Tan corridor. Supplies, water and power arrangements are on us — just point at the vehicle.",
            ),
            (
                "Walk around, then drive happy",
                "You inspect every panel and seat with Anthony before he leaves. Not thrilled with a spot? He re-does it on the spot. Then you pay — never before.",
            ),
        ],
    },
)

REVIEWS_HOME = (
    "reviews",
    {
        "title": "Casa Grande drivers rate us 5.0 out of 5",
        "sub": "Every review below is a real, public Google review of Supreme Clean Detailing.",
        "items": [
            (
                "Pricing was half of the quotes I received from several others! Arrived on time, did an excellent job detailing both my cars.",
                "Ron McClure",
                "Google review",
            ),
            (
                "They left my car smelling fresh new & deep detailed. Also they were able to remove a smell I had in my car.",
                "Kimberly García",
                "Google review",
            ),
            (
                "Anthony has done work for me for years now and I trust him implicitly and his prices are very fair.",
                "Suanne Dunn",
                "Google review · Local Guide",
            ),
            (
                "This young man works hard to make your vehicle look like dealership quality. Great customer service with very reasonable prices.",
                "Kim Rupert",
                "Google review",
            ),
            (
                "He left it spotless and was able to get tough water stains out of my seat. He truly goes above and beyond.",
                "Anahi Sanchez",
                "Google review",
            ),
            (
                "I'm not sure I could imagine a better overall mobile car detailing service. On-time, reasonably priced, and incredible work.",
                "Baby Stuey",
                "Google review · Local Guide",
            ),
        ],
        "all_link": "/reviews/",
    },
)

CTA = ("cta", {
    "title": "Your driveway. Our supplies. A car that looks brand new.",
    "sub": f"Same-day replies from {BIZ['owner']}, the owner — not a call center.",
})

AREAS = (
    "areas",
    {
        "title": "Mobile detailing across the I-10 corridor",
        "sub": "Based in Casa Grande — serving the towns between Phoenix and Tucson. Don't see your area? Text us; if it's close, we'll make it work.",
        "cities": CITIES_SERVED,
    },
)

# ------------------------------------------------------------------- pages --

CORE_PAGES = [
    # ------------------------------------------------------------------ home
    {
        "slug": "",
        "nav_active": "/",
        "priority": "1.0",
        "title": "Supreme Clean Detailing: Mobile Car Detailing in Casa Grande, AZ | (520) 840-2452",
        "desc": "Top-rated mobile car detailing in Casa Grande, AZ ✔ 5.0★ on Google ✔ Owner-operated ✔ Fair upfront prices ✔ We come to you ☎ (520) 840-2452",
        "h1": "Mobile car detailing that comes to you — Casa Grande &amp; the I-10 corridor",
        "hero_sub": f"Owner-operated by {BIZ['owner']}. Dealership-quality interior and exterior details at your home or office — at prices customers call “half of the quotes I received.”",
        "hero_badges": [
            {"icon": "truck", "text": "We come to you — home or work"},
            {"icon": "cash", "text": "No prepayment, ever"},
            {"icon": "shield", "text": "Satisfaction guaranteed"},
        ],
        "sections": [
            TRUSTBAR,
            (
                "cards",
                {
                    "title": "What we detail",
                    "sub": "Cars, trucks, SUVs, work vehicles — if it drives through Pinal County dust, we make it new again.",
                    "items": [
                        {"icon": "sparkle", "title": "Full Detail", "text": "Interior + exterior in one visit. The full reset.", "price": "from $199", "href": "/services/full-detail/"},
                        {"icon": "seat", "title": "Interior Deep Clean", "text": "Steam, shampoo, every vent and seam.", "price": "from $139", "href": "/services/interior-detailing/"},
                        {"icon": "drop", "title": "Exterior Wash & Shine", "text": "Hand wash, wheels, sealant — zero swirl marks.", "price": "from $69", "href": "/services/exterior-detailing/"},
                        {"icon": "nose", "title": "Odor Removal", "text": "Smoke, pets, mystery smells — gone at the source.", "price": "from $75", "href": "/services/odor-removal/"},
                        {"icon": "paw", "title": "Pet Hair Removal", "text": "Embedded hair out of carpets and seats.", "price": "from $40", "href": "/services/pet-hair-removal/"},
                        {"icon": "beam", "title": "Headlight Restoration", "text": "Cloudy lenses crystal-clear and sealed.", "price": "$60 / pair", "href": "/services/headlight-restoration/"},
                    ],
                },
            ),
            STEPS,
            ("pricing", PRICING_TIERS),
            ADDONS,
            REVIEWS_HOME,
            (
                "prose",
                {
                    "title": "Why Casa Grande cars need more than a drive-through wash",
                    "html": """
<p>Between the I-10 haul, monsoon haboobs and summer sun, Pinal County is one of the hardest places in
America to keep a vehicle clean. Blowing dust works into every vent and seat rail. UV bakes dashboards
and clear coat. Automatic tunnel washes just drag that grit across your paint in a dirty brush.</p>
<p><strong>Supreme Clean Detailing does it the right way:</strong> a proper hand wash and interior deep clean at your
home or workplace, using our own supplies, with the owner doing the work — not a rotating crew. That's
why our <a href="/reviews/">Google reviews</a> talk about trucks that “came back brand new,” water stains pulled out of
seats, and smells other shops couldn't fix.</p>
<p>We're based in <a href="/car-detailing-casa-grande-az/">Casa Grande</a> and cover
<a href="/car-detailing-maricopa-az/">Maricopa</a>, <a href="/car-detailing-eloy-az/">Eloy</a>,
<a href="/car-detailing-coolidge-az/">Coolidge</a>, <a href="/car-detailing-florence-az/">Florence</a>,
<a href="/car-detailing-arizona-city-az/">Arizona City</a>,
<a href="/car-detailing-san-tan-valley-az/">San Tan Valley</a> and
<a href="/car-detailing-queen-creek-az/">Queen Creek</a> — the whole corridor between Phoenix and Tucson.</p>
""",
                },
            ),
            AREAS,
            (
                "faq",
                {
                    "title": "Quick answers",
                    "sub": 'More on the <a href="/faq/">full FAQ page</a>.',
                    "items": [
                        (
                            "How much does mobile detailing cost?",
                            '<p>Exterior wash &amp; shine from $69, interior deep clean from $139, full detail from $199 — by vehicle size, confirmed before we start. See <a href="/pricing/">full pricing</a>.</p>',
                        ),
                        (
                            "Do I need to provide water or power?",
                            "<p>Usually no — tell us where the vehicle will be and Anthony arranges what's needed. Driveways, apartment lots and workplaces are all fine in most cases.</p>",
                        ),
                        (
                            "How do I book?",
                            f'<p>Fastest: <a href="sms:{TEL}">text {PHONE}</a> with your vehicle and a photo. You can also <a href="/book/">book online</a> or call. No prepayment — you pay when you\'re happy.</p>',
                        ),
                        (
                            "How far will you travel?",
                            '<p>Anywhere in the Casa Grande–Maricopa–Eloy–Coolidge–Florence area, up through San Tan Valley and Queen Creek. Nearby but not listed? <a href="/contact/">Ask</a> — if it\'s close, we\'ll make it work.</p>',
                        ),
                        (
                            "Is there a guarantee?",
                            "<p>Yes — 100% satisfaction. You walk the vehicle with Anthony before he leaves; anything you're not happy with gets re-done on the spot.</p>",
                        ),
                    ],
                },
            ),
            CTA,
        ],
    },
    # ---------------------------------------------------------- services hub
    {
        "slug": "services",
        "nav_active": "/services/",
        "priority": "0.9",
        "title": "Mobile Detailing Services in Casa Grande, AZ | Supreme Clean Detailing",
        "desc": "Full details, interior deep cleans, exterior hand wash, odor removal, pet hair, headlight restoration & fleet detailing — mobile across Casa Grande, Maricopa & San Tan Valley. ☎ (520) 840-2452",
        "h1": "Detailing services — brought to your driveway",
        "hero_sub": "Pick a service or text a photo and let Anthony recommend the right one. Upfront pricing on everything.",
        "crumbs": [("Services", None)],
        "sections": [
            TRUSTBAR,
            (
                "cards",
                {
                    "title": "All services",
                    "items": [
                        {"icon": "sparkle", "title": "Full Detail", "text": "Complete interior + exterior reset in one visit.", "price": "from $199", "href": "/services/full-detail/"},
                        {"icon": "seat", "title": "Interior Deep Clean", "text": "Vacuum, steam, shampoo, condition — every surface.", "price": "from $139", "href": "/services/interior-detailing/"},
                        {"icon": "drop", "title": "Exterior Wash & Shine", "text": "Two-bucket hand wash, wheels, glass, sealant.", "price": "from $69", "href": "/services/exterior-detailing/"},
                        {"icon": "nose", "title": "Odor Removal", "text": "Treat the source — smoke, pets, food, moisture.", "price": "from $75", "href": "/services/odor-removal/"},
                        {"icon": "paw", "title": "Pet Hair Removal", "text": "Embedded fur lifted from carpet and upholstery.", "price": "from $40", "href": "/services/pet-hair-removal/"},
                        {"icon": "beam", "title": "Headlight Restoration", "text": "Sand, polish, seal — clear lenses that last.", "price": "$60 / pair", "href": "/services/headlight-restoration/"},
                        {"icon": "truck", "title": "Fleet & Business", "text": "Work trucks and small fleets on a schedule, at your yard.", "price": "custom quote", "href": "/services/fleet-detailing/"},
                    ],
                },
            ),
            ("pricing", PRICING_TIERS),
            REVIEWS_HOME,
            CTA,
        ],
    },
    # ---------------------------------------------------------------- pricing
    {
        "slug": "pricing",
        "nav_active": "/pricing/",
        "priority": "0.9",
        "title": "Car Detailing Prices — Casa Grande, AZ | Supreme Clean Detailing",
        "desc": "Transparent detailing prices: exterior from $69, interior deep clean from $139, full detail from $199 by vehicle size. No prepayment. Casa Grande, Maricopa & nearby. ☎ (520) 840-2452",
        "h1": "Upfront pricing. No surprises, no prepayment.",
        "hero_sub": "Most detailers make you call for a price. Here's ours in black and white — the same fair pricing customers call “half of the quotes I received.”",
        "crumbs": [("Pricing", None)],
        "sections": [
            TRUSTBAR,
            ("pricing", PRICING_TIERS),
            ADDONS,
            (
                "faq",
                {
                    "title": "Pricing questions",
                    "items": [
                        (
                            "Why 'starting at'?",
                            "<p>A commuter sedan and a work truck full of dog hair are different jobs. The starting price covers an average-condition vehicle; heavy pet hair, sand, spills or years of buildup add time. Anthony confirms your exact number from your photos <em>before</em> booking — the price you're told is the price you pay.</p>",
                        ),
                        (
                            "Do you charge extra to drive to me?",
                            "<p>No travel fees anywhere in our listed service areas — Casa Grande, Maricopa, Eloy, Coolidge, Florence, Arizona City, San Tan Valley and Queen Creek.</p>",
                        ),
                        (
                            "How do I pay?",
                            "<p>After the walk-around, once you're happy. Cash, card, or the usual apps. Never a deposit, never prepayment.</p>",
                        ),
                        (
                            "Is there a discount for regulars?",
                            "<p>Yes — maintenance customers on a monthly or every-other-month rotation save on every visit and get priority scheduling. Ask Anthony when you book.</p>",
                        ),
                        (
                            "Gift certificates?",
                            f"<p>Absolutely — a detail is a great gift. <a href=\"sms:{TEL}\">Text {PHONE}</a> and Anthony will set one up for any service or amount.</p>",
                        ),
                    ],
                },
            ),
            CTA,
        ],
    },
    # ------------------------------------------------------------------- book
    {
        "slug": "book",
        "nav_active": "",
        "priority": "0.9",
        "title": "Book Mobile Detailing in Casa Grande, AZ | Supreme Clean Detailing",
        "desc": "Book your mobile detail in 60 seconds — text (520) 840-2452 with a photo or send the form. Same-day reply from the owner. No prepayment.",
        "h1": "Book your detail",
        "hero_sub": "Three ways, all fast: text a photo, call, or send the form below. Anthony answers personally, same day.",
        "crumbs": [("Book", None)],
        "sections": [
            TRUSTBAR,
            ("form", {}),
            ("steps", STEPS[1]),
            (
                "reviews",
                {
                    "title": "Booked by your neighbors, rated 5.0",
                    "items": [
                        ("Anthony was very professional with scheduling my appointment as well as timely follow-up.", "Ron McClure", "Google review"),
                        ("An amazing experience! We would highly recommend for timeliness, attention to detail, and amazing prices!", "Clifton Taylor", "Google review"),
                        ("On-time, reasonably priced, and performed incredible work. Thank you!", "Baby Stuey", "Google review · Local Guide"),
                    ],
                    "all_link": "/reviews/",
                },
            ),
        ],
    },
    # ---------------------------------------------------------------- reviews
    {
        "slug": "reviews",
        "nav_active": "/reviews/",
        "priority": "0.8",
        "title": "Reviews — Supreme Clean Detailing, Casa Grande AZ (5.0★, 20 Google Reviews)",
        "desc": "Read real Google reviews of Supreme Clean Detailing: 5.0 stars across 20 reviews. On-time, fair prices, dealership-quality results in Casa Grande & Maricopa, AZ.",
        "h1": "5.0 stars. Every single review.",
        "hero_sub": "All quotes below are from public Google reviews of Supreme Clean Detailing. We'd love to earn yours next.",
        "crumbs": [("Reviews", None)],
        "sections": [
            TRUSTBAR,
            (
                "reviews",
                {
                    "title": "What customers say",
                    "items": [
                        ("Anthony was very professional with scheduling my appointment as well as timely follow-up. Arrived on time, did an excellent job detailing both my cars. Pricing was half of the quotes I received from several others! I highly recommend his services.", "Ron McClure", "Google review"),
                        ("Such an amazing project! Arrived on time, kept me updated on what they were constantly doing to my car. They left my car smelling fresh new & deep detailed. Also they were able to remove a smell I had in my car.", "Kimberly García", "Google review"),
                        ("My car came back looking beautiful after Anthony detailed it. Anthony has done work for me for years now and I trust him implicitly and his prices are very fair. Give him a try, I know you'll be impressed with his professionalism and attention to “detail”!", "Suanne Dunn", "Google review · Local Guide"),
                        ("This young man works hard to make your vehicle look like dealership quality. Anthony has great customer service with very reasonable prices for all he does. I recommend him to everyone wanting to get their vehicle looking brand new.", "Kim Rupert", "Google review"),
                        ("Anthony did an amazing job detailing my car! He left it spotless and was able to get tough water stains out of my seat. He truly goes above and beyond with his work. Highly recommend booking with him!", "Anahi Sanchez", "Google review"),
                        ("Amazing work! Above and beyond! My cars always get compliments after getting washed!", "David J.", "Google review"),
                        ("Great work! Very nice and polite young man. Very thorough and much respect on his work ethic, something you don't see much these days. Highly recommend.", "Mike Touby", "Google review"),
                        ("Good detail, love the job, love the guy, good customer service — must try again.", "Carlos Encinas", "Google review"),
                        ("I'm not sure I could imagine a better overall mobile car detailing service. He was on-time, reasonably priced, and performed incredible work. Thank you!", "Baby Stuey", "Google review · Local Guide"),
                        ("Recently had my two trucks detailed — amazing job, literally came back brand new, smelled new and looked even newer. Would highly recommend. I am for sure going back.", "Jase Archer", "Google review"),
                        ("Great detail, great person — really helped bring my car alive again. Definitely recommend.", "Conner Holl", "Google review"),
                        ("An amazing experience! We would highly recommend for timeliness, attention to detail, and amazing prices!", "Clifton Taylor", "Google review"),
                        ("Best detailer ever! My car can get pretty dirty at times and every time I get my detail from here, it looks brand new! Feels so clean.", "Bella Tristan", "Google review"),
                        ("Supreme Clean did a great job on the Vette! I recommend them!", "Mark Bedore", "Google review"),
                        ("Anthony did an amazing job with my truck. I don't think it's been this clean since I bought it. Highly recommend!", "Carolyn Miller", "Google review"),
                        ("He's amazing 🙌", "Ahgelina Lao", "Google review"),
                    ],
                },
            ),
            (
                "prose",
                {
                    "html": f"""
<p class="center"><a class="btn btn-primary btn-lg" href="{BIZ['gbp_url']}">See all reviews on Google →</a>
&nbsp; <a class="btn btn-ghost btn-lg" href="{BIZ['review_url']}">Had a detail? Leave a review</a></p>
<p class="center">Anthony reads and responds to every review — good or bad. That's what owner-operated means.</p>
""",
                },
            ),
            CTA,
        ],
    },
    # ---------------------------------------------------------------- gallery
    {
        "slug": "gallery",
        "nav_active": "",
        "priority": "0.6",
        "title": "Before & After Gallery | Supreme Clean Detailing — Casa Grande, AZ",
        "desc": "Before-and-after photos from real Supreme Clean Detailing jobs across Casa Grande and Maricopa, AZ — interiors, exteriors, trucks and Corvettes alike.",
        "h1": "The work speaks for itself",
        "hero_sub": "Real vehicles, real transformations. (Photos coming online now — in the meantime, our reviews describe the results better than we ever could.)",
        "crumbs": [("Gallery", None)],
        "sections": [
            ("gallery_ph", {"title": "Recent work", "sub": "Check back — new before/afters are added after every few jobs."}),
            REVIEWS_HOME,
            CTA,
        ],
    },
    # ------------------------------------------------------------------ about
    {
        "slug": "about",
        "nav_active": "/about/",
        "priority": "0.7",
        "title": "About Anthony — Supreme Clean Detailing | Casa Grande, AZ",
        "desc": "Supreme Clean Detailing is owner-operated by Anthony in Casa Grande, AZ. On-time, fair prices, and a work ethic customers write reviews about. ☎ (520) 840-2452",
        "h1": "The owner does the work. That's the whole secret.",
        "hero_sub": "Supreme Clean Detailing is Anthony — a Casa Grande detailer building a business one spotless car at a time.",
        "crumbs": [("About", None)],
        "sections": [
            TRUSTBAR,
            (
                "prose",
                {
                    "html": f"""
<p>When you book Supreme Clean Detailing, you don't get a rotating crew or a franchise script.
You get <strong>{BIZ['owner']}</strong> — the owner — showing up on time at your driveway with everything needed
to make your vehicle look new again.</p>
<p>Customers keep writing the same three things in their <a href="/reviews/">reviews</a>:</p>
<ul>
<li><strong>He shows up when he says he will.</strong> “Arrived on time… timely follow-up.” (Ron M.)</li>
<li><strong>The price is fair — genuinely.</strong> “Pricing was half of the quotes I received from several others.” (Ron M.) “Very reasonable prices for all he does.” (Kim R.)</li>
<li><strong>The work goes beyond expectations.</strong> “Dealership quality.” (Kim R.) “Able to get tough water stains out of my seat.” (Anahi S.) “Removed a smell I had in my car.” (Kimberly G.)</li>
</ul>
<p>One review says it best: <em>“much respect on his work ethic, something you don't see much these days.”</em>
That work ethic is the business plan. No upsell games, no prepayment, and a simple promise:
<strong>if you're not happy with a panel or a seat, it gets re-done before Anthony leaves.</strong></p>
<h3>Where we work</h3>
<p>Based in Casa Grande, serving the whole I-10 corridor between Phoenix and Tucson —
<a href="/car-detailing-maricopa-az/">Maricopa</a>, <a href="/car-detailing-eloy-az/">Eloy</a>,
<a href="/car-detailing-coolidge-az/">Coolidge</a>, <a href="/car-detailing-florence-az/">Florence</a>,
<a href="/car-detailing-arizona-city-az/">Arizona City</a>,
<a href="/car-detailing-san-tan-valley-az/">San Tan Valley</a> and
<a href="/car-detailing-queen-creek-az/">Queen Creek</a>.</p>
""",
                },
            ),
            (
                "reviews",
                {
                    "title": "Don't take our word for it",
                    "items": [
                        ("This young man works hard to make your vehicle look like dealership quality… helping a local, hard working young man build his business.", "Kim Rupert", "Google review"),
                        ("Anthony has done work for me for years now and I trust him implicitly.", "Suanne Dunn", "Google review · Local Guide"),
                        ("Great work! Very thorough and much respect on his work ethic.", "Mike Touby", "Google review"),
                    ],
                    "all_link": "/reviews/",
                },
            ),
            CTA,
        ],
    },
    # -------------------------------------------------------------------- faq
    {
        "slug": "faq",
        "nav_active": "/faq/",
        "priority": "0.7",
        "title": "Mobile Detailing FAQ — Casa Grande, AZ | Supreme Clean Detailing",
        "desc": "Everything about booking mobile detailing in Casa Grande & Maricopa AZ: pricing, what's included, water & power, pet hair, odor removal, payment and guarantees.",
        "h1": "Questions, answered straight",
        "hero_sub": f"Anything else — <a href='sms:{TEL}'>text {PHONE}</a> and ask Anthony directly.",
        "crumbs": [("FAQ", None)],
        "sections": [
            (
                "faq",
                {
                    "title": "Booking & service",
                    "items": [
                        ("How fast can I get an appointment?", "<p>Often within a few days — text a photo of your vehicle and Anthony will offer the next open slots. Mornings book fastest in summer.</p>"),
                        ("Where do you detail the car?", "<p>Wherever it sits: driveway, curb (where permitted), apartment lot or your workplace parking. Shade helps in summer but isn't required.</p>"),
                        ("Do I need to be there the whole time?", "<p>No — most customers hand over keys and get on with their day. You'll want to be there for the final walk-around, which is when you approve the work (and only then pay).</p>"),
                        ("Do you need my water or power?", "<p>Usually not — mention your location when booking and Anthony arranges what's needed.</p>"),
                        ("How long does a detail take?", "<p>Exterior wash &amp; shine: 1–1.5 h. Interior deep clean: 2–3 h. Full detail: 3–5 h depending on size and condition.</p>"),
                    ],
                },
            ),
            (
                "faq",
                {
                    "title": "Pricing & payment",
                    "items": [
                        ("How much will my vehicle cost?", '<p>Start from the <a href="/pricing/">pricing page</a>, then text photos for your exact number — confirmed before booking, honored on the day.</p>'),
                        ("Do you require a deposit?", "<p>No. You pay after the walk-around, when you're happy. Cash, card or app.</p>"),
                        ("Why are you cheaper than the big Phoenix companies?", "<p>Owner-operated and local: no office, no crew overhead, no franchise fees, no travel surcharges from the city. Same professional products and process — see the reviews.</p>"),
                    ],
                },
            ),
            (
                "faq",
                {
                    "title": "The messy stuff",
                    "items": [
                        ("Can you really remove pet hair?", '<p>Yes — it\'s a <a href="/services/pet-hair-removal/">dedicated service</a>. Embedded hair takes a two-step process and real time, which is why drive-through washes never touch it.</p>'),
                        ("My car smells — smoke / milk / dog. Fixable?", '<p>Usually, yes. We treat the source: extraction, steam and odor treatment. One customer\'s review: “they were able to remove a smell I had in my car.” See <a href="/services/odor-removal/">odor removal</a>.</p>'),
                        ("Water stains on seats?", "<p>Hot-water extraction handles most water marks and set-in stains — exactly what Anahi's review describes (“tough water stains out of my seat”). Send a photo for a straight answer.</p>"),
                        ("Do you do engine bays?", "<p>Yes, as an add-on ($50) — degreased, rinsed carefully and dressed.</p>"),
                        ("Foul weather?", "<p>Monsoon day? Anthony will reschedule you first thing — and yes, post-haboob details are our busiest days.</p>"),
                    ],
                },
            ),
            CTA,
        ],
    },
    # ---------------------------------------------------------------- contact
    {
        "slug": "contact",
        "nav_active": "",
        "priority": "0.8",
        "title": "Contact Supreme Clean Detailing — Casa Grande, AZ | (520) 840-2452",
        "desc": "Call or text (520) 840-2452 for mobile car detailing in Casa Grande, Maricopa, Eloy, Coolidge & San Tan Valley AZ. Email supremecleandetailing01@gmail.com. Mon–Sat 8–6.",
        "h1": "Talk to Anthony",
        "hero_sub": "Text is fastest. Calls welcome. Form works too. Same-day replies, Mon–Sat.",
        "crumbs": [("Contact", None)],
        "sections": [
            (
                "cards",
                {
                    "title": "Reach us",
                    "items": [
                        {"icon": "chat", "title": "Text (fastest)", "text": f"Send your vehicle + a photo to {PHONE} for an exact quote.", "href": f"sms:{TEL}"},
                        {"icon": "phone", "title": "Call", "text": f"{PHONE} — Mon–Sat, 8 AM–6 PM.", "href": f"tel:{TEL}"},
                        {"icon": "pin", "title": "Service area", "text": "Based in Casa Grande 85122 · mobile across the Phoenix–Tucson corridor.", "href": "/service-areas/"},
                    ],
                },
            ),
            ("form", {}),
            ("map", {}),
            CTA,
        ],
    },
    # ---------------------------------------------------------- areas hub
    {
        "slug": "service-areas",
        "nav_active": "/service-areas/",
        "priority": "0.8",
        "title": "Service Areas — Mobile Detailing Casa Grande to Queen Creek | Supreme Clean Detailing",
        "desc": "Mobile car detailing across Pinal County: Casa Grande, Maricopa, Eloy, Coolidge, Florence, Arizona City, San Tan Valley & Queen Creek AZ. We come to you. ☎ (520) 840-2452",
        "h1": "We cover the corridor between Phoenix and Tucson",
        "hero_sub": "Based in Casa Grande — which means the towns the big-city detailers charge extra to reach (or won't drive to at all) are our home turf.",
        "crumbs": [("Service areas", None)],
        "sections": [
            TRUSTBAR,
            AREAS,
            (
                "prose",
                {
                    "title": "The local advantage",
                    "html": """
<p>Phoenix mobile detailers quote Pinal County jobs with travel fees — when they take them at all. Tucson
shops are an hour the other way. Supreme Clean Detailing is based <em>here</em>, in Casa Grande, so
Maricopa, Eloy, Coolidge, Florence, Arizona City, San Tan Valley and Queen Creek are all standard-rate
service — no surcharges, no “minimum job size,” no waiting a week for a route day.</p>
<p>Every city page below covers local pricing, what's included, and answers for that area. If you're just
outside the map — Stanfield, Toltec, Picacho, Sacaton — text us anyway. If it's close, we'll make it work.</p>
""",
                },
            ),
            REVIEWS_HOME,
            CTA,
        ],
    },
    # -------------------------------------------------------------------- 404
    {
        "slug": "404",
        "nav_active": "",
        "noindex": True,
        "title": "Page not found | Supreme Clean Detailing",
        "desc": "That page took a wrong turn. Head back to Supreme Clean Detailing — mobile car detailing in Casa Grande, AZ.",
        "h1": "That page drove off…",
        "hero_sub": "No problem — everything useful is one tap away.",
        "sections": [
            (
                "cards",
                {
                    "title": "Popular destinations",
                    "items": [
                        {"icon": "cash", "title": "Pricing", "text": "Upfront prices by vehicle size.", "href": "/pricing/"},
                        {"icon": "sparkle", "title": "Services", "text": "Full details, interiors, odor, pet hair.", "href": "/services/"},
                        {"icon": "chat", "title": "Book now", "text": "Text a photo, get a same-day quote.", "href": "/book/"},
                    ],
                },
            ),
        ],
    },
]
