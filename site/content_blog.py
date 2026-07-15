"""Blog hub + two launch posts targeting the highest-value question queries
(the pattern that works for the market leaders: cost guides + local climate)."""

from build import BIZ, blogposting_schema
from content_core import TRUSTBAR, CTA

TEL = BIZ["phone_e164"]
PHONE = BIZ["phone_display"]

BLOG_PAGES = [
    {
        "slug": "blog",
        "nav_active": "",
        "priority": "0.6",
        "title": "Car Care Blog — Detailing Tips for Casa Grande & Pinal County | Supreme Clean Detailing",
        "desc": "Straight answers about car detailing in Casa Grande & Pinal County AZ: how pricing works, monsoon dust survival, interior care in desert heat and more.",
        "h1": "The Pinal County car care blog",
        "hero_sub": "No fluff — straight pricing answers, desert-specific advice, and the questions customers actually text us.",
        "crumbs": [("Blog", None)],
        "sections": [
            (
                "cards",
                {
                    "title": "Latest posts",
                    "items": [
                        {
                            "icon": "cash",
                            "title": "How much does mobile detailing cost in Casa Grande? (2026 guide)",
                            "text": "What actually sets the price of a detail — and how to have your exact quote before you book.",
                            "href": "/blog/mobile-detailing-cost-casa-grande/",
                        },
                        {
                            "icon": "drop",
                            "title": "Monsoon dust storms vs. your car: a survival guide",
                            "text": "What haboob dust really does to paint and interiors, and the post-storm routine that saves both.",
                            "href": "/blog/monsoon-dust-car-care-pinal-county/",
                        },
                    ],
                },
            ),
            CTA,
        ],
    },
    {
        "slug": "blog/mobile-detailing-cost-casa-grande",
        "nav_active": "",
        "priority": "0.7",
        "og_type": "article",
        "title": "How Much Does Mobile Car Detailing Cost in Casa Grande, AZ? (2026 Guide)",
        "desc": "How mobile detailing is priced in Casa Grande AZ in 2026 — what drives the number up or down, and how to get your exact quote before you book.",
        "h1": "How much does mobile car detailing cost in Casa Grande, AZ?",
        "hero_sub": "The straight answer on what drives the number — and how to have your exact price in hand before you book.",
        "crumbs": [("Blog", "/blog/"), ("Detailing cost guide", None)],
        "schema_extra": [
            blogposting_schema(
                "How Much Does Mobile Car Detailing Cost in Casa Grande, AZ? (2026 Guide)",
                "How mobile detailing is priced in Casa Grande AZ and how to get an exact quote upfront.",
                "/blog/mobile-detailing-cost-casa-grande/",
                "2026-07-13",
            )
        ],
        "sections": [
            TRUSTBAR,
            (
                "prose",
                {
                    "html": f"""
<p><strong>Short answer for Casa Grande in 2026:</strong> it depends on two things — vehicle size and
honest condition — which is why any detailer quoting one number before seeing your vehicle is guessing.
Our approach instead: text a photo, get your <strong>exact price before you book</strong>, and that's
the number you pay. (Full package details are on the <a href="/pricing/">pricing page</a>.)</p>
<h3>What the market does</h3>
<p>Phoenix-metro mobile companies price comparable details at big-city rates — before any travel
consideration for Pinal County addresses. Tucson shops are an hour the other way. Casa Grande sits in
the gap between both metros, which historically meant paying city prices <em>plus</em> the “we had to
drive out there” premium.</p>
<p>Being based in Casa Grande is our structural advantage — no commute cost to pass on, no shop
overhead — and it shows up in reviews: <em>“Pricing was half of the quotes I received from several
others.”</em></p>
<h3>What actually changes the price of a detail</h3>
<ul>
<li><strong>Vehicle size.</strong> A Tahoe has nearly twice the interior surface of a Civic. That's why
every price is listed by size class.</li>
<li><strong>Condition.</strong> Average dirty is the listed price. Heavy pet hair, sand infiltration,
spilled milk in July, or years of skipped cleanings add labor hours — quoted upfront from your photos,
never sprung on you afterward.</li>
<li><strong>Extras.</strong> Odor treatment, pet hair removal, headlight restoration, engine bay —
each quoted upfront with your detail. Add what you need, skip what you don't.</li>
</ul>
<h3>How to keep the cost down (honestly)</h3>
<ol>
<li><strong>Don't wait for “bad enough.”</strong> A monthly wash &amp; shine keeps you out of
condition-surcharge territory forever.</li>
<li><strong>Bundle vehicles.</strong> Two cars, one visit is the most efficient appointment on our board.</li>
<li><strong>Ask about the maintenance rotation.</strong> Monthly and every-other-month regulars save on
every visit and get priority scheduling.</li>
</ol>
<h3>The real question: what does a cheap wash cost?</h3>
<p>Tunnel brushes grind desert grit into clear coat (that's what swirl marks are). Baked-in stains and
smells tank trade-in offers. The cheap tunnel wash is often the most expensive option on a long enough
timeline — appraisers see everything.</p>
<p><strong>Want your exact number?</strong> Text a photo of your vehicle to
<a href="sms:{TEL}">{PHONE}</a> — Anthony replies the same day with a firm price. No prepayment,
and you approve the work before paying.</p>
""",
                },
            ),
            (
                "faq",
                {
                    "title": "Cost questions, quick-fire",
                    "items": [
                        ("Is mobile detailing more expensive than a shop?", "<p>Not here — you skip the shop's rent in the price and the two drop-off trips. Same professional result, at your driveway, quoted upfront.</p>"),
                        ("Do you charge more for Maricopa / Eloy / Coolidge?", "<p>No. Everything inside the <a href='/service-areas/'>service area</a> is standard rate — no travel fees.</p>"),
                        ("Deposits?", "<p>Never. You pay after the walk-around, when you're happy.</p>"),
                    ],
                },
            ),
            CTA,
        ],
    },
    {
        "slug": "blog/monsoon-dust-car-care-pinal-county",
        "nav_active": "",
        "priority": "0.7",
        "og_type": "article",
        "title": "Monsoon Dust Storms vs. Your Car: A Pinal County Survival Guide | Supreme Clean Detailing",
        "desc": "What haboob dust actually does to paint, interiors and AC systems — and the post-storm care routine Casa Grande & Maricopa drivers should follow.",
        "h1": "Monsoon dust storms vs. your car: a Pinal County survival guide",
        "hero_sub": "We detail the aftermath every summer. Here's what the dust actually does — and the routine that beats it.",
        "crumbs": [("Blog", "/blog/"), ("Monsoon dust guide", None)],
        "schema_extra": [
            blogposting_schema(
                "Monsoon Dust Storms vs. Your Car: A Pinal County Survival Guide",
                "What haboob dust does to paint, interiors and AC — and the post-storm routine that saves them.",
                "/blog/monsoon-dust-car-care-pinal-county/",
                "2026-07-13",
            )
        ],
        "sections": [
            TRUSTBAR,
            (
                "prose",
                {
                    "html": f"""
<p>If you've lived a summer between Casa Grande and Eloy, you've watched a wall of brown swallow I-10.
Here's what that haboob leaves behind on your vehicle — and what to do about it, in order.</p>
<h3>1. The dust is not dirt — it's abrasive rock flour</h3>
<p>Monsoon dust is pulverized silica fine enough to hang in the air for hours. On paint it acts like
600-grit sandpaper the moment anything drags across it: a sleeve, a duster, or — worst of all — a
tunnel-wash brush that just scrubbed forty other dusty cars. <strong>Rule one: never dry-wipe a dusty
car.</strong> Rinse first, always; better, get a proper two-bucket hand wash where the media is rinsed
clean after every panel.</p>
<h3>2. Then the rain arrives and makes cement</h3>
<p>Dust + a light monsoon sprinkle = mineral-rich mud spots that bake onto glass and clear coat by the
next afternoon's 110°. That's how hard-water etching happens without a sprinkler in sight. Getting the
vehicle washed <em>within a day or two</em> of a dust-rain one-two punch is the difference between an
easy wash and a spot-removal job.</p>
<h3>3. Inside, the dust wins by infiltration</h3>
<p>Door seals, vents, window channels — after a good haboob you'll find silt in the cupholders of a
closed, parked car. It settles into carpet, seat seams and the HVAC intake, which is why cabin air
starts smelling like a dirt road (our <a href="/services/odor-removal/">odor service</a> treats vents
for exactly this). A seasonal <a href="/services/interior-detailing/">interior deep clean</a> —
steam on hard surfaces, extraction in carpet — pulls the desert back out of the cabin.</p>
<h3>The Pinal County monsoon routine</h3>
<ol>
<li><strong>After every major dust event:</strong> rinse or hand wash within 48 h. No dry wiping. Ever.</li>
<li><strong>Monthly June–September:</strong> <a href="/services/exterior-detailing/">wash &amp; shine</a>
with sealant — the sealant is what makes next month's dust rinse off instead of stick.</li>
<li><strong>Each fall:</strong> one <a href="/services/full-detail/">full detail</a> to reset interior
and exterior after the season.</li>
<li><strong>Parked outside?</strong> Nose the car out of the prevailing storm direction (storms here
mostly roll in from the southeast) and skip the cheap car cover — a cover over dust <em>is</em>
the sandpaper.</li>
</ol>
<p>Or skip the memorizing: our maintenance-plan customers get priority rebooking after every big storm.
Text <a href="sms:{TEL}">{PHONE}</a> and we'll keep your vehicle on the right side of the dust.</p>
""",
                },
            ),
            (
                "faq",
                {
                    "title": "Monsoon quick answers",
                    "items": [
                        ("A haboob hit yesterday — tunnel wash today?", "<p>Please don't. The brushes are loaded with everyone else's grit. Rinse-only touchless is acceptable triage; a hand wash is the fix.</p>"),
                        ("Are water spots after monsoon rain permanent?", "<p>Fresh ones, no — wash promptly. Baked in for weeks, they can etch; we offer dedicated spot treatment when that's happened — send a photo for a straight quote.</p>"),
                        ("Does sealant actually help with dust?", "<p>Noticeably. Sealed paint is slick, so dust has less to grab — it rinses instead of bonding. That's why it's included in our wash &amp; shine.</p>"),
                    ],
                },
            ),
            CTA,
        ],
    },
]
