#!/usr/bin/env python3
"""
Build-time injector: replace <!-- contact-form --> in FAQ index.html
with content from contact.html.
"""
import os
import sys
import shutil

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    faq_file = os.path.join(base, "faqs", "index.html")
    contact_file = os.path.join(base, "contact.html")
    bak_file = os.path.join(base, "index.html.bak")
    out_marker = "<!-- contact-form -->"

    if not os.path.exists(contact_file):
        print(f"ERROR: contact.html not found at {contact_file}")
        sys.exit(1)
    if not os.path.exists(faq_file):
        print(f"ERROR: faq index not found at {faq_file}")
        sys.exit(1)

    # Backup if not already done
    if not os.path.exists(bak_file):
        shutil.copy2(faq_file, bak_file)
        print(f"Backup created: {bak_file}")

    with open(contact_file, "r", encoding="utf-8") as f:
        contact_html = f.read()

    with open(faq_file, "r", encoding="utf-8") as f:
        content = f.read()

    if out_marker not in content:
        print(f"WARNING: marker '{out_marker}' not found in {faq_file}")
        # Try to insert before closing </body> as fallback
        if "</body>" in content:
            content = content.replace("</body>", contact_html + "\n</body>")
            print("Injected before </body> as fallback.")
        else:
            print("No fallback injection point found; skipping.")
            sys.exit(0)
        replaced = True
    else:
        content = content.replace(out_marker, contact_html)
        replaced = True

    if replaced:
        # Basic sanity checks
        checks = [
            ('action=', 'form action'),
            ('novalidate', 'form novalidate'),
            ('Full Name', 'full name field'),
            ('Company Name', 'company field'),
        ]
        ok = True
        for key, desc in checks:
            if key not in content:
                print(f"ERROR: Missing expected content '{key}' ({desc})")
                ok = False
        if ok:
            with open(faq_file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Successfully injected contact form into {faq_file}")
        else:
            # restore from backup
            shutil.copy2(bak_file, faq_file)
            print("Restored from backup due to validation failure.")
            sys.exit(1)
    else:
        print("No changes made.")

if __name__ == "__main__":
    main()
