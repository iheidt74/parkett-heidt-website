#!/usr/bin/env python3
"""
Generates premium-structured service subpages for Parkett Heidt.
Reads page data from page_data.json, reads existing HTML files to preserve
header/footer, and replaces the <main> block with new premium content.
"""
import json
import os
import re

LEISTUNGEN_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'leistungen')
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'page_data.json')

def generate_benefits_html(benefits):
    items = []
    for b in benefits:
        items.append(f'            <div class="benefit-item"><i class="fas fa-{b["icon"]}"></i><div><h4>{b["title"]}</h4><p>{b["text"]}</p></div></div>')
    return '\n'.join(items)

def generate_process_html(steps):
    items = []
    for i, s in enumerate(steps, 1):
        items.append(f'            <div class="process-step"><div class="step-number">{i}</div><h4>{s["title"]}</h4><p>{s["text"]}</p></div>')
    return '\n'.join(items)

def generate_table_html(table):
    if not table:
        return ''
    cols = table['columns']
    rows = table['rows']
    header = ''.join(f'<th>{c}</th>' for c in cols)
    body_rows = []
    for row in rows:
        cells = []
        for cell in row:
            if isinstance(cell, dict):
                cells.append(f'<td class="{cell.get("cls","")}">{cell["val"]}</td>')
            else:
                cells.append(f'<td>{cell}</td>')
        body_rows.append(f'              <tr>{"".join(cells)}</tr>')
    return f'''
          <h2><i class="fas fa-table"></i> {table.get("title","Vergleich")}</h2>
          <table class="comparison-table">
            <thead><tr>{header}</tr></thead>
            <tbody>
{chr(10).join(body_rows)}
            </tbody>
          </table>'''

def generate_faq_html(faqs):
    items = []
    for f in faqs:
        items.append(f'''            <div class="faq-item">
              <button class="faq-question">{f["q"]} <i class="fas fa-chevron-down"></i></button>
              <div class="faq-answer"><p>{f["a"]}</p></div>
            </div>''')
    return '\n'.join(items)

def generate_main(page):
    info_box = ''
    if page.get('info_box'):
        info_box = f'''
          <div class="info-box">
            <h4><i class="fas fa-info-circle"></i> Wussten Sie?</h4>
            <p>{page["info_box"]}</p>
          </div>
'''
    second_para = ''
    if page.get('intro2'):
        second_para = f'\n          <p>{page["intro2"]}</p>\n'

    table_html = generate_table_html(page.get('table'))

    return f'''    <main>
      <section class="service-hero">
        <div class="container">
          <p class="breadcrumb"><a href="/">Startseite</a> &raquo; <a href="/leistungen.html">Leistungen</a> &raquo; {page["title"]}</p>
          <h1>{page["title"]}</h1>
          <p class="hero-desc">{page["hero_desc"]}</p>
        </div>
      </section>

      <section class="service-detail">
        <div class="container">
          <p>{page["intro"]}</p>
{info_box}{second_para}
          <h2><i class="fas fa-star"></i> {page.get("benefits_title", "Ihre Vorteile")}</h2>
          <div class="benefits-grid">
{generate_benefits_html(page["benefits"])}
          </div>

          <h2><i class="fas fa-clipboard-list"></i> {page.get("process_title", "Unser Ablauf")}</h2>
          <div class="process-steps">
{generate_process_html(page["process"])}
          </div>
{table_html}

          <h2><i class="fas fa-question-circle"></i> Häufig gestellte Fragen (FAQ)</h2>
          <div class="faq-list">
{generate_faq_html(page["faqs"])}
          </div>

          <div class="service-cta">
            <h2>{page.get("cta_title", "Jetzt kostenlose Beratung anfragen")}</h2>
            <p>{page.get("cta_text", "Kontaktieren Sie uns für ein unverbindliches Angebot.")}</p>
            <a href="/kontakt.html" class="btn">Kostenlose Beratung anfordern</a>
          </div>
        </div>
      </section>
    </main>'''

def process_file(filename, page_data):
    filepath = os.path.join(LEISTUNGEN_DIR, filename)
    if not os.path.exists(filepath):
        print(f'  SKIP: {filename} not found')
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract everything before <main> and after </main>
    before = re.split(r'<main\b[^>]*>', content, maxsplit=1)
    if len(before) < 2:
        print(f'  SKIP: no <main> tag in {filename}')
        return False
    
    header_part = before[0]
    after_main = content.split('</main>', 1)
    if len(after_main) < 2:
        print(f'  SKIP: no </main> tag in {filename}')
        return False
    footer_part = after_main[1]

    new_main = generate_main(page_data)
    new_content = header_part + new_main + '\n' + footer_part

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f'  OK: {filename}')
    return True

def main():
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        pages = json.load(f)
    
    success = 0
    for filename, data in pages.items():
        if process_file(filename, data):
            success += 1
    
    print(f'\nDone: {success}/{len(pages)} pages updated.')

if __name__ == '__main__':
    main()
