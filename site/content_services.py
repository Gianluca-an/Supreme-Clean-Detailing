"""Service pages — one page per money intent, per the teardown playbook.
Each carries: keyworded title/H1, unique 500-900 word copy, its own price table,
FAQPage schema, a matching real review, and Service+AggregateOffer JSON-LD."""

from build import BIZ, service_schema
from content_core import TRUSTBAR, CTA, ADDONS

TEL = BIZ["phone_e164"]
PHONE = BIZ["phone_display"]


def svc(slug, nav_name, title, desc, h1, sub, price_low, price_high, sections):
    return {
        "slug": f"services/{slug}",
        "nav_active": "/services/",
        "priority": "0.9",
        "title": title,
        "desc": desc,
        "h1": h1,
        "hero_sub": sub,
        "crumbs": [("Services", "/services/"), (nav_name, None)],
        "schema_extra": [service_schema(nav_name, desc, f"/services/{slug}/", price_low, price_high)],
        "sections": [TRUSTBAR] + sections + [CTA],
    }


def price_block(title, sub, tiers, note=None):
    return ("pricing", {"title": title, "sub": sub, "tiers": tiers, "note": note})


SERVICE_PAGES = [
    # ------------------------------------------------------------ full detail
    svc(
        "full-detail",
        "Full Detail",
        "Full Car Detail in Casa Grande, AZ — from $199 | Supreme Clean Detailing",
        "Complete interior + exterior detail at your driveway in Casa Grande, Maricopa & nearby. From $199 by vehicle size, 5.0★ rated, no prepayment. ☎ (520) 840-2452",
        "The Full Detail: inside and out, back to day one",
        "Our most-booked service. A complete interior deep clean plus a proper exterior hand wash and protection — one visit, one fair price, at your home or work.",
        199,
        299,
        [
            (
                "prose",
                {
                    "title": "What a Supreme Clean full detail includes",
                    "html": """
<p>This is the full reset. Inside: complete vacuum (including trunk and seat rails), steam cleaning of
hard surfaces, carpet and mat shampoo, seats deep-cleaned whether cloth or leather, door jambs, vents,
console and cupholders detailed, streak-free interior glass and a clean, fresh finish — never a heavy
cover-up perfume.</p>
<p>Outside: a two-bucket foam hand wash (your paint never meets a dirty brush), wheels, tires and wheel
wells degreased and dressed, bug and light water-spot removal, exterior glass, and a spray sealant that
helps the finish shrug off Pinal County dust and sun.</p>
<p>Before Anthony leaves, you do a <strong>walk-around together</strong>. Anything you're not thrilled with gets
re-done on the spot — then you pay. That's the 100% satisfaction guarantee, and it's why customers write
things like <em>“literally came back brand new, smelled new and looked even newer.”</em></p>
<h3>Who books this</h3>
<ul>
<li>Selling or trading in — details routinely pay for themselves at appraisal</li>
<li>Post-monsoon-season recovery (dust in every seam)</li>
<li>New-to-you used cars — start fresh, not with someone else's crumbs</li>
<li>The yearly deep reset for daily drivers and work trucks</li>
</ul>
""",
                },
            ),
            price_block(
                "Full Detail pricing",
                "By vehicle size, confirmed from your photos before booking.",
                [
                    {
                        "name": "Car / Coupe",
                        "tagline": "Sedans, coupes, hatchbacks",
                        "prices": [("Full Detail", "$199")],
                        "time": "About 3–4 hours",
                        "includes": ["Complete interior deep clean", "Two-bucket exterior hand wash", "Wheels, tires &amp; wells", "Spray sealant protection", "Walk-around approval"],
                    },
                    {
                        "name": "Truck / SUV",
                        "tagline": "Half-tons, 2-row SUVs, crossovers",
                        "popular": True,
                        "prices": [("Full Detail", "$249")],
                        "time": "About 4–5 hours",
                        "includes": ["Everything in Car / Coupe", "Extra cabin volume covered", "Bed or cargo area cleaned", "Running boards &amp; steps"],
                    },
                    {
                        "name": "XL / 3-Row / Van",
                        "tagline": "Tahoes, minivans, lifted trucks",
                        "prices": [("Full Detail", "$299")],
                        "time": "About 5 hours",
                        "includes": ["Everything in Truck / SUV", "Third row + full cargo area", "Extra glass &amp; jambs"],
                    },
                ],
                note="Heavy pet hair, sand or long-neglected interiors may add time — you'll know the exact price before we start. Add-ons below can be bolted on same-visit.",
            ),
            ADDONS,
            (
                "reviews",
                {
                    "title": "Full details, reviewed",
                    "items": [
                        ("Recently had my two trucks detailed — amazing job, literally came back brand new, smelled new and looked even newer.", "Jase Archer", "Google review"),
                        ("Supreme Clean did a great job on the Vette! I recommend them!", "Mark Bedore", "Google review"),
                        ("Anthony did an amazing job with my truck. I don't think it's been this clean since I bought it.", "Carolyn Miller", "Google review"),
                    ],
                    "all_link": "/reviews/",
                },
            ),
            (
                "faq",
                {
                    "title": "Full detail FAQ",
                    "items": [
                        ("How long does a full detail take?", "<p>Plan on 3–5 hours depending on size and condition. Most customers hand over keys in the morning and take a like-new vehicle to lunch.</p>"),
                        ("Does it include engine bay cleaning?", "<p>On request — it's a $50 add-on, done carefully (degrease, gentle rinse, dress). Mention it when you book.</p>"),
                        ("Will it remove scratches?", "<p>A full detail maximizes gloss and removes surface contamination, but paint <em>correction</em> (machine-polishing scratches out) is a separate conversation — text photos and Anthony will tell you honestly what's possible.</p>"),
                        ("Is $199 really the price?", "<p>For an average-condition car, yes — that's the point of publishing it. Trucks/SUVs $249, XL $299. Condition surcharges (heavy pet hair, sand, spills) are quoted upfront from your photos, never sprung on you.</p>"),
                    ],
                },
            ),
        ],
    ),
    # ------------------------------------------------------- interior detail
    svc(
        "interior-detailing",
        "Interior Deep Clean",
        "Interior Car Detailing in Casa Grande, AZ — from $139 | Supreme Clean Detailing",
        "Interior deep clean at your driveway: steam, shampoo, stain & odor treatment. From $139 by vehicle size in Casa Grande, Maricopa & nearby. ☎ (520) 840-2452",
        "Interior deep clean: every vent, seam and cupholder",
        "The Arizona interior enemy list — dust, UV, spills, pet hair, mystery smells — handled in one visit at your home or office.",
        139,
        199,
        [
            (
                "prose",
                {
                    "title": "What's included",
                    "html": """
<p>Full vacuum including trunk, under seats and seat rails. High-temperature steam on hard surfaces —
dash, console, vents, cupholders, door panels — which cleans <em>and</em> sanitizes without soaking
electronics. Carpets and mats shampooed with hot-water extraction; light stain removal is included, and
tougher set-in stains (coffee, milk, water marks) are treated with the same process that got
<em>“tough water stains out of my seat”</em> in Anahi's review. Cloth seats are extracted; leather is
cleaned and conditioned against Arizona sun-cracking. Interior glass finished streak-free.</p>
<p>What you get back is the car you remember from the dealer lot — <em>“I don't think it's been this
clean since I bought it,”</em> as one review puts it.</p>
""",
                },
            ),
            price_block(
                "Interior Deep Clean pricing",
                "By vehicle size — exact quote from your photos before booking.",
                [
                    {"name": "Car / Coupe", "tagline": "Sedans, coupes, hatchbacks", "prices": [("Interior Deep Clean", "$139")], "time": "About 2 hours", "includes": ["Full vacuum incl. trunk", "Steam-clean hard surfaces", "Carpet &amp; mat shampoo", "Seats deep-cleaned", "Interior glass"]},
                    {"name": "Truck / SUV", "tagline": "Half-tons, 2-row SUVs", "popular": True, "prices": [("Interior Deep Clean", "$169")], "time": "About 2.5 hours", "includes": ["Everything in Car / Coupe", "Extra cabin volume", "Cargo area included"]},
                    {"name": "XL / 3-Row / Van", "tagline": "3-rows, minivans, crew cabs", "prices": [("Interior Deep Clean", "$199")], "time": "About 3 hours", "includes": ["Everything in Truck / SUV", "Third row + rear cargo", "Extra jambs &amp; glass"]},
                ],
            ),
            (
                "reviews",
                {
                    "title": "Interior results, in customers' words",
                    "items": [
                        ("He left it spotless and was able to get tough water stains out of my seat. He truly goes above and beyond.", "Anahi Sanchez", "Google review"),
                        ("They left my car smelling fresh new & deep detailed. Also they were able to remove a smell I had in my car.", "Kimberly García", "Google review"),
                        ("Best detailer ever! My car can get pretty dirty at times and every time … it looks brand new!", "Bella Tristan", "Google review"),
                    ],
                    "all_link": "/reviews/",
                },
            ),
            (
                "faq",
                {
                    "title": "Interior FAQ",
                    "items": [
                        ("Can you get stains out of seats?", "<p>Most, yes — hot-water extraction plus the right chemistry handles coffee, soda, milk and water marks. Text a photo for a straight yes/no before you book.</p>"),
                        ("Do you clean child seats?", "<p>We'll vacuum and wipe around them and clean beneath; for the seat itself we'll advise what's safe per the manufacturer. Just mention it when booking.</p>"),
                        ("My interior is… bad. Be honest.", "<p>Anthony has seen worse, promise. Worst case it's a condition surcharge quoted upfront — never a lecture.</p>"),
                        ("Leather seats?", "<p>Cleaned then conditioned — vital in Arizona, where UV turns unconditioned leather into jerky.</p>"),
                    ],
                },
            ),
        ],
    ),
    # ------------------------------------------------------- exterior detail
    svc(
        "exterior-detailing",
        "Exterior Wash & Shine",
        "Exterior Car Detailing & Hand Wash — Casa Grande, AZ from $69 | Supreme Clean Detailing",
        "Proper two-bucket hand wash, wheels, glass & sealant at your driveway — from $69. The safe alternative to tunnel washes in Casa Grande & Maricopa AZ. ☎ (520) 840-2452",
        "Exterior wash &amp; shine — never a swirl-mark tunnel wash",
        "Drive-through washes drag yesterday's grit across your clear coat. We hand-wash with clean media, panel by panel, then seal the shine against desert sun.",
        69,
        109,
        [
            (
                "prose",
                {
                    "title": "Why hand wash matters in Pinal County",
                    "html": """
<p>Desert dust is pulverized rock. A tunnel-brush wash grinds it into your paint like sandpaper; a proper
two-bucket hand wash lifts it off. Our exterior service covers foam pre-soak, hand wash and soft-towel
dry, wheels/tires/wheel wells degreased and dressed, bug and light water-spot removal, streak-free glass,
and a spray sealant for gloss and UV protection.</p>
<p>Booked every 2–4 weeks it keeps the finish protected year-round — that's exactly what the maintenance
plan is for (regulars save on every visit; ask when you book).</p>
""",
                },
            ),
            price_block(
                "Exterior pricing",
                "Flat by size, at your location — no travel fees in our service area.",
                [
                    {"name": "Car / Coupe", "tagline": "", "prices": [("Wash & Shine", "$69")], "time": "About 1 hour", "includes": ["Foam hand wash &amp; towel dry", "Wheels, tires &amp; wells", "Bug &amp; light spot removal", "Glass + spray sealant"]},
                    {"name": "Truck / SUV", "tagline": "", "popular": True, "prices": [("Wash & Shine", "$89")], "time": "About 1.25 hours", "includes": ["Everything in Car / Coupe", "Extra panel area", "Running boards &amp; steps"]},
                    {"name": "XL / 3-Row / Lifted", "tagline": "", "prices": [("Wash & Shine", "$109")], "time": "About 1.5 hours", "includes": ["Everything in Truck / SUV", "Lifted / dually friendly", "Extra glass &amp; trim"]},
                ],
                note="Add the wax/sealant upgrade ($45) for months of extra protection, or headlight restoration ($60/pair) while we're there.",
            ),
            (
                "reviews",
                {
                    "title": "Shine, verified",
                    "items": [
                        ("Amazing work! Above and beyond! My cars always get compliments after getting washed!", "David J.", "Google review"),
                        ("Great detail, great person — really helped bring my car alive again.", "Conner Holl", "Google review"),
                        ("Supreme Clean did a great job on the Vette!", "Mark Bedore", "Google review"),
                    ],
                    "all_link": "/reviews/",
                },
            ),
            (
                "faq",
                {
                    "title": "Exterior FAQ",
                    "items": [
                        ("Is hand washing really better than the $10 tunnel?", "<p>For the paint, hugely. Tunnels reuse brushes that just scoured a hundred dusty cars. Hand washing with clean mitts and two buckets is how swirl marks <em>don't</em> happen.</p>"),
                        ("Do you remove hard water spots?", "<p>Light spotting is included; baked-in mineral etching needs a dedicated treatment (from $50) — send a photo and we'll quote it straight.</p>"),
                        ("What about monsoon dust the day after?", "<p>It's the desert — it happens. Maintenance-plan customers get priority rebooking after big haboobs.</p>"),
                    ],
                },
            ),
        ],
    ),
    # ---------------------------------------------------------- odor removal
    svc(
        "odor-removal",
        "Odor Removal",
        "Car Odor Removal in Casa Grande, AZ — Smoke, Pet & Spill Smells | Supreme Clean Detailing",
        "We remove car odors at the source — smoke, pets, spilled milk, moisture. Proven results in Casa Grande & Maricopa AZ (read the reviews). From $75. ☎ (520) 840-2452",
        "Odor removal that treats the source — not perfume over the problem",
        "A smell lives somewhere: in carpet padding, seat foam, vents. We find it, extract it, and treat it. One customer's review: “they were able to remove a smell I had in my car.”",
        75,
        225,
        [
            (
                "prose",
                {
                    "title": "How we kill odors for good",
                    "html": """
<p>Air fresheners lose to biology every time. Our process: identify the source (spill, smoke residue,
pet accidents, monsoon moisture), <strong>extract</strong> it with hot water from carpet and upholstery,
<strong>steam</strong> hard surfaces and vents where residue films cling, then apply an odor
<strong>treatment</strong> that neutralizes what's left instead of masking it.</p>
<p>Typical wins: cigarette and smoke residue, pet smells, spilled milk and food, gym gear, and the
mildew note cars pick up after monsoon season. Severe cases (long-term smoking, biohazard) can take a
second treatment — you'll get an honest read from the photos and a firm price before we start.</p>
""",
                },
            ),
            price_block(
                "Odor removal pricing",
                "Added to any interior service, or booked standalone.",
                [
                    {"name": "Odor Treatment", "tagline": "With any interior deep clean", "popular": True, "prices": [("Add-on", "from $75")], "includes": ["Source extraction", "Steam + neutralizer treatment", "Vents treated"]},
                    {"name": "Standalone", "tagline": "Odor treatment + targeted extraction", "prices": [("Car / Truck / SUV", "from $125")], "includes": ["Targeted shampoo of affected areas", "Full odor treatment", "Honest severity assessment first"]},
                    {"name": "Severe / Smoke-out", "tagline": "Long-term smoke, heavy pet", "prices": [("Quoted from photos", "$150–225")], "includes": ["Full interior deep clean advised", "Multi-stage treatment", "Follow-up if needed"]},
                ],
            ),
            (
                "reviews",
                {
                    "title": "The review that says it all",
                    "items": [
                        ("They left my car smelling fresh new & deep detailed. Also they were able to remove a smell I had in my car. I had such an amazing experience with them!", "Kimberly García", "Google review"),
                        ("Recently had my two trucks detailed… smelled new and looked even newer.", "Jase Archer", "Google review"),
                        ("My car came back looking beautiful. I trust him implicitly.", "Suanne Dunn", "Google review · Local Guide"),
                    ],
                    "all_link": "/reviews/",
                },
            ),
            (
                "faq",
                {
                    "title": "Odor FAQ",
                    "items": [
                        ("Can you remove cigarette smell completely?", "<p>Light-to-moderate smoke: usually yes in one visit. Years of heavy smoking: expect major improvement first visit and a straight answer about whether a second treatment is worth it.</p>"),
                        ("Something spilled and now it's baking in the heat…", f"<p>Classic Arizona. Don't wait — the longer it cooks, the deeper it goes. <a href=\"sms:{TEL}\">Text {PHONE}</a> today; spill extractions are often same-week.</p>"),
                        ("Do you just ozone-bomb the car?", "<p>No — treatment without extraction is perfume with extra steps. We physically remove the source first; that's why it works.</p>"),
                    ],
                },
            ),
        ],
    ),
    # ------------------------------------------------------- pet hair removal
    svc(
        "pet-hair-removal",
        "Pet Hair Removal",
        "Pet Hair Removal for Cars — Casa Grande, AZ from $40 | Supreme Clean Detailing",
        "Embedded dog & cat hair removed from car carpet and seats with a proper two-step process. From $40 with any detail in Casa Grande & Maricopa AZ. ☎ (520) 840-2452",
        "Pet hair removal that actually gets it all",
        "A regular vacuum leaves woven-in fur behind. Our two-step process lifts embedded hair out of carpet and upholstery — the difference between “vacuumed” and “no dog in this truck, ever.”",
        40,
        120,
        [
            (
                "prose",
                {
                    "title": "Why pet hair defeats normal vacuums",
                    "html": """
<p>Dog and cat hair barbs into carpet fibers like Velcro. Our process: specialized rubber-edge tooling
that rakes hair out of the weave, then high-suction extraction — repeated seat by seat, panel by panel.
Combined with an interior deep clean, the cabin also stops <em>smelling</em> like the dog park
(see <a href="/services/odor-removal/">odor removal</a>).</p>
<p>Great before selling a vehicle, after a road trip with the pups, or for allergy-sensitive passengers.</p>
""",
                },
            ),
            price_block(
                "Pet hair pricing",
                "Honest tiering by how furry we're talking.",
                [
                    {"name": "Light", "tagline": "Occasional passenger pup", "prices": [("With any interior service", "$40")], "includes": ["Affected seats &amp; carpet", "Two-step tooling + extraction"]},
                    {"name": "Moderate", "tagline": "Daily co-pilot", "popular": True, "prices": [("With any interior service", "$60–80")], "includes": ["All carpet + upholstery", "Cargo area included"]},
                    {"name": "Heavy / Working dogs", "tagline": "Ranch trucks, breeders, rescues", "prices": [("Quoted from photos", "$100–120")], "includes": ["Full-cabin multi-pass process", "Paired with deep clean advised"]},
                ],
            ),
            (
                "faq",
                {
                    "title": "Pet hair FAQ",
                    "items": [
                        ("Can you get hair out of the headliner and seat seams?", "<p>Yes — seams, rails, vents, the works. That's what the tooling pass is for.</p>"),
                        ("Cat hair too?", "<p>Cat hair is the finer, meaner cousin — same process, a little more patience. Yes.</p>"),
                        ("Will the smell go too?", '<p>Pair it with <a href="/services/odor-removal/">odor treatment</a> and yes — hair carries dander and oils; removing both is the fix.</p>'),
                    ],
                },
            ),
            (
                "reviews",
                {
                    "title": "Detail-obsessed, per the reviews",
                    "items": [
                        ("Very thorough and much respect on his work ethic.", "Mike Touby", "Google review"),
                        ("He truly goes above and beyond with his work.", "Anahi Sanchez", "Google review"),
                        ("Every time I get my detail from here, it looks brand new!", "Bella Tristan", "Google review"),
                    ],
                    "all_link": "/reviews/",
                },
            ),
        ],
    ),
    # -------------------------------------------------- headlight restoration
    svc(
        "headlight-restoration",
        "Headlight Restoration",
        "Headlight Restoration — Casa Grande, AZ $60/pair | Supreme Clean Detailing",
        "Cloudy yellow headlights restored & UV-sealed for $60/pair at your driveway in Casa Grande & Maricopa AZ. See clearly, look newer, drive safer. ☎ (520) 840-2452",
        "Headlight restoration: see clearly again for $60",
        "Arizona UV turns polycarbonate lenses yellow and blind. We wet-sand, polish and seal them back to clear — at your driveway, in about an hour.",
        60,
        60,
        [
            (
                "prose",
                {
                    "title": "Cloudy lenses are a safety problem, not just ugly",
                    "html": """
<p>Oxidized headlights can cut usable light output dramatically — exactly what you don't want on an
unlit farm road or I-8 at night. Replacement housings run hundreds per side at a dealer. Restoration
is $60 <em>for the pair</em>: progressive wet-sanding to remove the dead UV-burned layer, machine polish
back to optical clarity, then a UV sealant so it lasts instead of hazing back in a month.</p>
<p>It's also the single highest-impact $60 you can spend before selling a vehicle — yellowed lights
read as “old car” from across the lot.</p>
""",
                },
            ),
            price_block(
                "Headlight pricing",
                "Flat and simple.",
                [
                    {"name": "Headlight Restoration", "tagline": "Both lenses, restored + sealed", "popular": True, "prices": [("Per pair", "$60")], "time": "About 1 hour", "includes": ["Wet-sand oxidation removal", "Machine polish to clarity", "UV sealant applied", "Standalone or with any detail"]},
                ],
            ),
            (
                "faq",
                {
                    "title": "Headlight FAQ",
                    "items": [
                        ("How long does it last?", "<p>With the UV sealant, expect years — not the weeks you get from toothpaste tricks or kit wipes that skip protection.</p>"),
                        ("Can every lens be saved?", "<p>Almost all. Lenses cracked or hazed on the <em>inside</em> can't be fixed from outside — Anthony will tell you honestly from a photo.</p>"),
                        ("Standalone or add-on?", "<p>Either. It's the most popular add-on to the <a href='/services/full-detail/'>full detail</a>, and a common quick standalone visit.</p>"),
                    ],
                },
            ),
        ],
    ),
    # -------------------------------------------------------- fleet detailing
    svc(
        "fleet-detailing",
        "Fleet & Business",
        "Fleet Detailing & Work Truck Washing — Casa Grande, AZ | Supreme Clean Detailing",
        "Mobile fleet washing & detailing for Pinal County businesses: work trucks, vans & crew vehicles cleaned at your yard on a schedule. Custom quotes. ☎ (520) 840-2452",
        "Your trucks are your brand. We keep them spotless.",
        "Scheduled washing and detailing for work trucks, vans and small fleets — at your yard, before or after crew hours, with one simple invoice.",
        99,
        999,
        [
            (
                "prose",
                {
                    "title": "How fleet service works",
                    "html": """
<p>Dusty, bug-plastered trucks tell your customers a story — the wrong one. Supreme Clean comes to your
yard in Casa Grande, Maricopa, Coolidge, Eloy or Florence on a schedule that doesn't interrupt work:
weekly or bi-weekly exterior washes to keep the fleet presentable, monthly or quarterly interior cleans
for crew vehicles, and full details when a unit rotates, sells, or comes off lease.</p>
<ul>
<li><strong>Volume pricing</strong> — 3+ vehicles saves on every unit</li>
<li><strong>Off-hours scheduling</strong> — early mornings, evenings, weekends</li>
<li><strong>One monthly invoice</strong>, photos of completed units on request</li>
<li>Pickups, vans, box trucks and equipment washdowns welcome</li>
</ul>
<p>Farm and ag operators: yes, we understand what a Pinal County harvest season does to a truck.
Bring us your worst.</p>
""",
                },
            ),
            (
                "cards",
                {
                    "title": "Typical fleet programs",
                    "items": [
                        {"icon": "drop", "title": "Presence wash", "text": "Bi-weekly exterior wash & shine for customer-facing trucks.", "price": "volume-priced per unit"},
                        {"icon": "seat", "title": "Crew cab care", "text": "Monthly interior cleans for shared vehicles — because nobody claims the mess.", "price": "volume-priced per unit"},
                        {"icon": "sparkle", "title": "Turnover details", "text": "Full detail when a unit sells, rotates or comes off lease.", "price": "from $199/unit"},
                    ],
                },
            ),
            (
                "faq",
                {
                    "title": "Fleet FAQ",
                    "items": [
                        ("What's the minimum fleet size?", "<p>Three vehicles unlocks volume pricing, but even a two-truck outfit can set a standing schedule.</p>"),
                        ("Can you work weekends or before 6 AM?", "<p>Yes — fleet slots are scheduled around your crew's hours, not ours.</p>"),
                        ("How do we start?", f"<p>Text or call {PHONE} with fleet size and location; Anthony will walk the yard with you and put a simple program + price in writing.</p>"),
                    ],
                },
            ),
            (
                "reviews",
                {
                    "title": "Trucks are the specialty",
                    "items": [
                        ("Recently had my two trucks detailed — amazing job, literally came back brand new.", "Jase Archer", "Google review"),
                        ("Anthony did an amazing job with my truck. I don't think it's been this clean since I bought it.", "Carolyn Miller", "Google review"),
                        ("Arrived on time, did an excellent job detailing both my cars. Pricing was half of the quotes I received!", "Ron McClure", "Google review"),
                    ],
                    "all_link": "/reviews/",
                },
            ),
        ],
    ),
]
