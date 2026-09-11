"""Real owner-shot before/after + showcase photos.

Optimized web copies live in site/assets/gallery/ (shipped); full-res originals
stay in site/assets/gallery/_staging/ (committed, not shipped). Before/after
direction and vehicle IDs were confirmed against the images when staged.
"""

G = "/assets/gallery/"


def _ba(slug, title, service, alt):
    return {
        "before": f"{G}{slug}-before.jpg",
        "after": f"{G}{slug}-after.jpg",
        "title": title,
        "service": service,
        "alt": alt,
    }


# order = strongest transformation first
BA_EXPLORER_FRONT = _ba("explorer-interior-front", "Ford Explorer", "Full interior detail",
                        "Ford Explorer driver-area interior deep clean in Casa Grande, AZ")
BA_EXPLORER_REAR = _ba("explorer-interior-rear", "Ford Explorer", "Rear floor &amp; carpet",
                       "Ford Explorer rear floor carpet shampoo and deep clean")
BA_F150 = _ba("f150-interior", "Ford F-150", "Interior deep clean",
              "Ford F-150 interior deep clean of the dashboard, console and carpets")
BA_SEATS = _ba("suv-rear-seats", "Cloth rear seats", "Seat deep clean",
               "SUV cloth rear-seat deep clean and vacuum")
BA_F350 = _ba("f350-dually-exterior", "Ford F-350 Dually", "Exterior detail",
              "Ford F-350 dually exterior hand wash and wax, Casa Grande AZ")
BA_CHALLENGER = _ba("challenger-exterior", "Dodge Challenger R/T", "Exterior + engine bay",
                    "Dodge Challenger R/T exterior detail and engine-bay clean")
BA_MUSTANG = _ba("mustang-exterior", "Ford Mustang", "Exterior detail",
                 "Black Ford Mustang exterior hand wash and paint shine")
BA_CADILLAC = _ba("cadillac-engine-bay", "Cadillac", "Engine-bay detail",
                  "Cadillac engine-bay degrease, rinse and dress")

BEFORE_AFTER = [
    BA_EXPLORER_FRONT, BA_EXPLORER_REAR, BA_F150, BA_SEATS,
    BA_F350, BA_CHALLENGER, BA_MUSTANG, BA_CADILLAC,
]
BA_INTERIOR = [BA_EXPLORER_FRONT, BA_EXPLORER_REAR, BA_F150, BA_SEATS]
BA_EXTERIOR = [BA_F350, BA_CHALLENGER, BA_MUSTANG]
BA_ENGINE = [BA_CADILLAC, BA_CHALLENGER]
BA_HOME = [BA_EXPLORER_FRONT, BA_F350, BA_CADILLAC]  # interior / exterior / engine variety


def _sc(img, title, sub, alt):
    return {"img": f"{G}showcase-{img}.jpg", "title": title, "sub": sub, "alt": alt}


SHOWCASE = [
    _sc("mustang-gt", "Ford Mustang GT", "Grabber Blue",
        "Grabber-blue Ford Mustang GT detailed by Supreme Clean Detailing, Casa Grande AZ"),
    _sc("corvette-z06", "Corvette Z06", "Show-ready gloss",
        "Orange Chevrolet Corvette Z06 detailed in Casa Grande, AZ"),
    _sc("super-duty", "Ford Super Duty", "Big-truck shine",
        "White Ford Super Duty truck detailed by Supreme Clean Detailing"),
    _sc("camaro", "Chevrolet Camaro", "Deep-gloss finish",
        "Gray Chevrolet Camaro exterior detail in Casa Grande, AZ"),
    _sc("corvette-c6", "Chevrolet Corvette", "Mirror finish",
        "Red Chevrolet Corvette detailed by Supreme Clean Detailing, Casa Grande AZ"),
]
SHOWCASE_HOME = SHOWCASE[:3]  # Mustang, Z06, Super Duty


def ba_section(title, sub, items, more_link=None):
    return ("beforeafter", {"title": title, "sub": sub, "items": items, "more_link": more_link})


def showcase_section(title, sub, items):
    return ("showcase", {"title": title, "sub": sub, "items": items})
