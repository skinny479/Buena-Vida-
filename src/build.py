"""Build the static site: python3 src/build.py  -> writes *.html at repo root."""
from pathlib import Path

from layout import CONTACT, page

ROOT = Path(__file__).resolve().parent.parent
PAGES = {
    "index.html": ("Buena Vida Chiropractic | Springdale, AR Chiropractor",
                   "Minority-owned chiropractic in Springdale, AR: adjustments, sports massage and corrective care."),
    "services.html": ("Services | Buena Vida Chiropractic",
                      "Chiropractic adjustments, sports massage, rehab, auto injury and wellness care in Springdale, AR."),
    "staff.html": ("Our Team | Buena Vida Chiropractic",
                   "Meet Dr. Anthony Le and the Buena Vida Chiropractic team in Springdale, Arkansas."),
    "new-patients.html": ("New Patients | Buena Vida Chiropractic",
                          "What to expect on your first visit, what to bring, and answers to common questions."),
    "contact.html": ("Contact & Book | Buena Vida Chiropractic",
                     "Book an appointment with Buena Vida Chiropractic in Springdale, AR."),
}

for name, (title, desc) in PAGES.items():
    body = (ROOT / "src" / "pages" / name).read_text()
    for key, val in CONTACT.items():
        body = body.replace("{" + key + "}", val)
    (ROOT / name).write_text(page(name, title, desc, body))
    print("built", name)
