# Buena Vida Chiropractic — Website

A redesigned static site for Buena Vida Chiropractic (Springdale, AR). It has no framework and no build dependencies beyond Python 3.

## Pages
- `index.html`: home (hero, mission, services overview, why us, first visit, reviews CTA)
- `services.html`: adjustments, sports massage, acupuncture, rehab, auto/work injury, wellness
- `staff.html`: Dr. Anthony Le, the care team and values
- `new-patients.html`: what to expect, what to bring, insurance, FAQ
- `contact.html`: appointment request form, contact info, hours, map

## Editing
Page content lives in `src/pages/*.html`. The shared header, footer and contact details live in `src/layout.py`.
After you edit, rebuild:

```
python3 src/build.py
```

Preview: open `index.html` in a browser.

## Before launch: fill in placeholders
Search for `TODO(owner)`:
- Care team names, bios and photos (`src/pages/staff.html`)

Online booking works by email: the appointment form opens the visitor's email app with the request filled in, addressed to the practice inbox.
