"""Tiny static-site builder: wraps each page body in the shared header/footer.

Run:  python3 src/build.py
Edit the CONTACT dict below once to update phone/address/email/hours on every page.
"""

CONTACT = {
    "phone": "(479) 751-2322",
    "phone_href": "+14797512322",
    "fax": "(479) 239-4855",
    "email": "buenavida479@gmail.com",
    "street": "7260 Village Park Ave, Ste A",
    "city": "Springdale, AR 72762",
    "map_query": "7260+Village+Park+Ave+Ste+A,+Springdale,+AR+72762",
}

NAV = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("staff.html", "Our Team"),
    ("new-patients.html", "New Patients"),
    ("contact.html", "Contact"),
]


def header(active):
    items = "\n".join(
        f'        <li><a href="{href}"{" aria-current=\"page\"" if href == active else ""}>{label}</a></li>'
        for href, label in NAV
    )
    c = CONTACT
    return f"""  <div class="topbar">
    <div class="container">
      <span>Minority-owned · Se habla español · All insurance accepted</span>
      <span>Call <a href="tel:{c['phone_href']}">{c['phone']}</a></span>
    </div>
  </div>
  <header class="nav">
    <div class="container">
      <a class="brand" href="index.html" aria-label="Buena Vida Chiropractic home">
        <img class="brand-logo" src="assets/img/logo-mark.png" alt="" width="36" height="52">
        <span class="brand-text">Buena Vida<small>Chiropractic · Springdale</small></span>
      </a>
      <button class="nav-toggle" aria-label="Open menu" aria-expanded="false">&#9776;</button>
      <ul class="nav-links">
{items}
        <li><a class="btn btn--primary" href="contact.html#book">Book a Visit</a></li>
      </ul>
    </div>
  </header>
"""


def footer():
    c = CONTACT
    return f"""  <footer class="footer">
    <div class="container">
      <div class="grid">
        <div>
          <a href="index.html" aria-label="Buena Vida Chiropractic home">
            <img class="footer-logo" src="assets/img/logo-light.png" alt="Buena Vida Chiropractic" width="190" height="155">
          </a>
          <p style="margin-top:18px">Live life naturally, optimally, and fully. Get back to living the Buena Vida &mdash; the good life.</p>
        </div>
        <div>
          <h4>Care</h4>
          <ul>
            <li><a href="services.html#adjustments">Chiropractic Adjustments</a></li>
            <li><a href="services.html#sports-massage">Sports Massage</a></li>
            <li><a href="services.html#acupuncture">Acupuncture</a></li>
            <li><a href="services.html#rehab">Corrective Exercise</a></li>
          </ul>
        </div>
        <div>
          <h4>Practice</h4>
          <ul>
            <li><a href="staff.html">Our Team</a></li>
            <li><a href="new-patients.html">New Patients</a></li>
            <li><a href="new-patients.html#faq">FAQ</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>
        <div>
          <h4>Visit</h4>
          <ul>
            <li>{c['street']}</li>
            <li>{c['city']}</li>
            <li><a href="tel:{c['phone_href']}">{c['phone']}</a></li>
            <li>Fax: {c['fax']}</li>
            <li><a href="mailto:{c['email']}">{c['email']}</a></li>
            <li style="margin-top:12px">Mon&ndash;Thu 9am&ndash;6pm<br>Fri 9am&ndash;1pm</li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; <span data-year></span> Buena Vida Chiropractic. All rights reserved.</span>
        <span>This site is for general information and is not a substitute for a professional diagnosis.</span>
      </div>
    </div>
  </footer>
"""


def page(filename, title, description, body):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/styles.css">
  <link rel="icon" type="image/png" href="assets/img/favicon.png">
  <link rel="apple-touch-icon" href="assets/img/favicon.png">
</head>
<body>
{header(filename)}
  <main>
{body}
  </main>
{footer()}
  <script src="assets/main.js"></script>
</body>
</html>
"""
