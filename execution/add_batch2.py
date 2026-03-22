#!/usr/bin/env python3
"""Adds remaining 18 pages to page_data.json"""
import json, os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'page_data.json')
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    pages = json.load(f)

# --- Batch 2: 9 more pages ---
pages['parkett-schleifen.html'] = {
    "title": "Parkett schleifen", "hero_desc": "Staubarmes Schleifen für perfekte Oberflächen – Ihr Parkettboden wie am ersten Tag.",
    "intro": "Das Schleifen ist der wichtigste Schritt bei der Parkettrenovierung. Wir setzen modernste, staubarme Schleiftechnik ein.",
    "info_box": "Unsere Staubabsaugung entfernt bis zu 99% des Schleifstaubs – so bleibt Ihre Wohnung sauber.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "fan", "title": "Staubarmes Arbeiten", "text": "99% Staubabsaugung."},
      {"icon": "hammer", "title": "Perfekte Oberfläche", "text": "Mehrstufiges Schleifen für makelloses Ergebnis."},
      {"icon": "clock", "title": "Schnell fertig", "text": "In der Regel 1 Tag pro Raum."},
      {"icon": "leaf", "title": "Nachhaltig", "text": "Renovieren statt Wegwerfen."}],
    "process_title": "Unser Schleif-Ablauf", "process": [
      {"title": "Analyse", "text": "Prüfung des Holzzustands und der Schichtstärke."},
      {"title": "Grobschliff", "text": "Entfernung der alten Oberfläche."},
      {"title": "Feinschliff", "text": "Mehrere Durchgänge für perfekte Glätte."},
      {"title": "Behandlung", "text": "Ölen, Wachsen oder Versiegeln."}],
    "table": None, "faqs": [
      {"q": "Wie oft kann Parkett geschliffen werden?", "a": "Massivparkett 5-8 Mal, Fertigparkett 1-2 Mal."},
      {"q": "Entstehen Gerüche?", "a": "Beim Schleifen kaum. Bei Versiegelung je nach Produkt leichte Gerüche."}]
}
pages['fussboeden-entfernen.html'] = {
    "title": "Fußböden entfernen", "hero_desc": "Professioneller Rückbau alter Bodenbeläge – sauber, schnell und fachgerecht.",
    "intro": "Bevor ein neuer Boden kommt, muss der alte fachgerecht entfernt werden. Ob Teppich, PVC, Fliesen oder Parkett – wir entfernen jeden Belag.",
    "info_box": "Wir entsorgen alle Materialien fachgerecht und umweltkonform. Die Entsorgungskosten sind im Angebot enthalten.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "trash", "title": "Komplettservice", "text": "Entfernung und Entsorgung aus einer Hand."},
      {"icon": "broom", "title": "Sauber", "text": "Besenreine Übergabe."},
      {"icon": "tools", "title": "Alle Beläge", "text": "Parkett, Fliesen, Teppich, PVC."},
      {"icon": "clock", "title": "Schnell", "text": "Effizient dank Profi-Maschinen."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Begutachtung", "text": "Beurteilung des vorhandenen Belags."},
      {"title": "Schutz", "text": "Abdeckung empfindlicher Bereiche."},
      {"title": "Rückbau", "text": "Maschinelle oder manuelle Entfernung."},
      {"title": "Entsorgung", "text": "Fachgerechte Entsorgung aller Materialien."}],
    "table": None, "faqs": [
      {"q": "Was kostet Bodenentfernung?", "a": "8-25 €/m² inkl. Entsorgung je nach Belagsart."},
      {"q": "Können Asbest-haltige Böden entfernt werden?", "a": "Ja, wir arbeiten mit zertifizierten Fachbetrieben zusammen."}]
}
pages['designbeschichtungen.html'] = {
    "title": "Designbeschichtungen", "hero_desc": "Fugenlose Böden mit Charakter – moderne Designbeschichtungen für individuelle Raumgestaltung.",
    "intro": "Designbeschichtungen bieten eine fugenlose, moderne Alternative zu klassischen Bodenbelägen. Ob Beton-Optik, Terrazzo-Look oder individuelle Farbgestaltung.",
    "info_box": "Fugenlose Beschichtungen sind extrem hygienisch – ideal für Allergiker und pflegesensible Bereiche.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "paint-roller", "title": "Fugenlos", "text": "Keine Fugen, keine Schmutzfänger."},
      {"icon": "palette", "title": "Individuell", "text": "Jede Farbe und Textur realisierbar."},
      {"icon": "shield-alt", "title": "Strapazierfähig", "text": "Ideal für stark beanspruchte Flächen."},
      {"icon": "home", "title": "Modern", "text": "Trend für hochwertige Innenarchitektur."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Design", "text": "Farb- und Texturberatung vor Ort."},
      {"title": "Grundierung", "text": "Professionelle Untergrundvorbereitung."},
      {"title": "Beschichtung", "text": "Mehrschichtiger Auftrag."},
      {"title": "Versiegelung", "text": "Abschließende Schutzversiegelung."}],
    "table": None, "faqs": [
      {"q": "Wo können Designbeschichtungen eingesetzt werden?", "a": "Wohnräume, Bäder, Küchen, Treppen und Wände."},
      {"q": "Wie lange hält eine Designbeschichtung?", "a": "Bei fachgerechter Ausführung 15-25 Jahre und länger."}]
}
pages['terrassen-bauen.html'] = {
    "title": "Terrassen bauen", "hero_desc": "Ihre Outdoor-Oase – professionell geplante und gebaute Holzterrassen.",
    "intro": "Eine Holzterrasse erweitert Ihren Wohnraum nach draußen. Wir planen und bauen aus Bangkirai, Douglasie oder Thermoesche.",
    "info_box": "Hochwertige Terrassenhölzer wie Bangkirai können ohne Holzschutz über 25 Jahre im Außenbereich bestehen.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "umbrella-beach", "title": "Outdoor-Wohnraum", "text": "Stilvolle Außenfläche für Ihr Zuhause."},
      {"icon": "tree", "title": "Naturmaterial", "text": "Echtes Holz für warmes Gefühl."},
      {"icon": "ruler-combined", "title": "Maßarbeit", "text": "Individuelle Planung."},
      {"icon": "shield-alt", "title": "Langlebig", "text": "Witterungsbeständige Hölzer."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Planung", "text": "Aufmaß, Holzauswahl und Entwurf."},
      {"title": "Unterbau", "text": "Fundament und Unterkonstruktion."},
      {"title": "Verlegung", "text": "Präzise Montage der Dielen."},
      {"title": "Finish", "text": "Erste Behandlung mit Terrassenöl."}],
    "table": None, "faqs": [
      {"q": "Welches Holz eignet sich?", "a": "Bangkirai und Cumaru für höchste Beständigkeit. Douglasie als günstigere Alternative."},
      {"q": "Was kostet eine Terrasse?", "a": "90-200 €/m² inkl. Montage je nach Holzart."}]
}
pages['terrassenreinigung.html'] = {
    "title": "Terrassenreinigung", "hero_desc": "Professionelle Reinigung und Pflege für Ihre Holzterrasse.",
    "intro": "Witterung, Moos und Schmutz setzen jeder Terrasse zu. Unsere Reinigung bringt Ihr Holz wieder zum Strahlen.",
    "info_box": "Regelmäßige Reinigung und Ölung verlängert die Lebensdauer um 10-15 Jahre.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "shower", "title": "Tiefenreinigung", "text": "Entfernung von Moos, Algen und Schmutz."},
      {"icon": "sync-alt", "title": "Wie Neu", "text": "Erstrahlt im ursprünglichen Ton."},
      {"icon": "shield-alt", "title": "Schutz", "text": "Ölung schützt langfristig."},
      {"icon": "leaf", "title": "Umweltfreundlich", "text": "Biologisch abbaubare Reiniger."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Inspektion", "text": "Begutachtung des Zustands."},
      {"title": "Vorreinigung", "text": "Entfernung grober Verschmutzungen."},
      {"title": "Reinigung", "text": "Schonende Tiefenreinigung."},
      {"title": "Pflege", "text": "Auftragen von Terrassenöl."}],
    "table": None, "faqs": [
      {"q": "Wie oft reinigen?", "a": "Wir empfehlen alle 1-2 Jahre je nach Witterung."},
      {"q": "Hochdruckreiniger?", "a": "Nein, wir nutzen schonende Spezialgeräte statt Hochdruck."}]
}
pages['objektbau-gewerbebau.html'] = {
    "title": "Objektbau & Gewerbebau", "hero_desc": "Bodenbeläge für Gewerbe, Büros und öffentliche Gebäude – termingerecht und zuverlässig.",
    "intro": "Im gewerblichen Bereich müssen Böden besonderen Anforderungen standhalten. Wir sind Ihr Partner für Großprojekte.",
    "info_box": "Über 50 gewerbliche Projekte erfolgreich umgesetzt – von Arztpraxen bis Hotels.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "building", "title": "Großprojekte", "text": "Erfahrung von 100 bis über 5.000 m²."},
      {"icon": "calendar-check", "title": "Termintreu", "text": "Einhaltung aller Fristen."},
      {"icon": "hard-hat", "title": "Koordination", "text": "Abstimmung mit anderen Gewerken."},
      {"icon": "file-contract", "title": "VOB-konform", "text": "Alle Arbeiten nach VOB-Standard."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Ausschreibung", "text": "Detailliertes Angebot nach LV."},
      {"title": "Planung", "text": "Bauablaufplanung mit Bauleitung."},
      {"title": "Ausführung", "text": "Termingerechte Verlegung."},
      {"title": "Abnahme", "text": "Protokollierte Abnahme nach VOB."}],
    "table": None, "faqs": [
      {"q": "Welche Beläge für Gewerbe?", "a": "Vinyl, Kautschuk und NK 33/34 Laminat sind besonders beliebt."},
      {"q": "Arbeiten am Wochenende?", "a": "Ja, auch außerhalb Ihrer Geschäftszeiten möglich."}]
}
pages['tischlerarbeiten.html'] = {
    "title": "Tischlerarbeiten", "hero_desc": "Maßgefertigte Holzarbeiten vom Meisterbetrieb.",
    "intro": "Neben Bodenbelägen bieten wir individuelle Tischlerarbeiten – von Einbauschränken bis Sonderanfertigungen.",
    "info_box": "Unsere Tischlerarbeiten werden exakt auf Ihre Raummaße gefertigt – für perfekte Passgenauigkeit.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "ruler-combined", "title": "Maßanfertigung", "text": "Millimetergenaue Fertigung."},
      {"icon": "tree", "title": "Echtes Holz", "text": "Hochwertige Massivhölzer und Furniere."},
      {"icon": "palette", "title": "Individuell", "text": "Design ganz nach Ihren Wünschen."},
      {"icon": "check-circle", "title": "Aus einer Hand", "text": "Boden und Möbel perfekt abgestimmt."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Beratung", "text": "Entwurfsgespräch und Aufmaß."},
      {"title": "Planung", "text": "Detaillierte Zeichnung und Materialauswahl."},
      {"title": "Fertigung", "text": "Handwerkliche Fertigung in unserer Werkstatt."},
      {"title": "Montage", "text": "Professionelle Montage vor Ort."}],
    "table": None, "faqs": [
      {"q": "Welche Arbeiten bieten Sie an?", "a": "Einbauschränke, Regale, Wandverkleidungen, Türrahmen und mehr."},
      {"q": "Wie lange dauert eine Maßanfertigung?", "a": "2-6 Wochen von Bestellung bis Montage."}]
}
pages['tuerenbau.html'] = {
    "title": "Türenbau", "hero_desc": "Maßgefertigte Türen und professioneller Einbau.",
    "intro": "Türen prägen den Charakter eines Raumes. Wir liefern und montieren Innentüren, Schiebetüren und Sonderanfertigungen.",
    "info_box": "Passende Türen zum Parkettboden schaffen ein harmonisches Gesamtbild.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "door-open", "title": "Passgenau", "text": "Exakter Einbau auch bei schwierigen Maßen."},
      {"icon": "palette", "title": "Harmonisch", "text": "Tür und Boden aus einem Guss."},
      {"icon": "drafting-compass", "title": "Sonderlösungen", "text": "Schiebetüren und Spezialmaße."},
      {"icon": "volume-mute", "title": "Schallschutz", "text": "Türen mit Schalldämm-Werten."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Aufmaß", "text": "Vermessung der Türöffnungen."},
      {"title": "Auswahl", "text": "Design, Holzart und Beschläge."},
      {"title": "Bestellung", "text": "Bestellung nach Maß."},
      {"title": "Montage", "text": "Einbau inkl. Zargen und Beschläge."}],
    "table": None, "faqs": [
      {"q": "Welche Türarten?", "a": "Innentüren, Schiebetüren, Glastüren mit Holzrahmen."},
      {"q": "Kann die Tür zum Parkett passen?", "a": "Ja! Holzart und Oberfläche stimmen wir aufeinander ab."}]
}
pages['individuelle-beratung.html'] = {
    "title": "Individuelle Beratung", "hero_desc": "Persönliche Beratung für Ihr Bodenprojekt – kompetent und unverbindlich.",
    "intro": "Jeder Raum ist anders. Unsere kostenlose Beratung ist der erste Schritt zu Ihrem Traumboden.",
    "info_box": "Wir bringen Originalmuster zu Ihnen – so sehen Sie das Material bei Ihrem Licht und neben Ihren Möbeln.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "comments", "title": "Persönlich", "text": "Beratung vor Ort oder in unserer Ausstellung."},
      {"icon": "euro-sign", "title": "Kostenlos", "text": "Beratung und Erstangebot unverbindlich."},
      {"icon": "swatchbook", "title": "Musterservice", "text": "Originalmuster für Ihre Räume."},
      {"icon": "file-alt", "title": "Transparenz", "text": "Angebot ohne versteckte Kosten."}],
    "process_title": "So läuft unsere Beratung ab", "process": [
      {"title": "Kontakt", "text": "Rufen Sie an oder schreiben Sie uns."},
      {"title": "Termin", "text": "Wir kommen zu Ihnen."},
      {"title": "Beratung", "text": "Aufmaß, Musterauswahl und Prüfung."},
      {"title": "Angebot", "text": "Transparentes, unverbindliches Angebot."}],
    "table": None, "faqs": [
      {"q": "Ist die Beratung kostenlos?", "a": "Ja, Erstberatung inkl. Aufmaß ist immer kostenlos."},
      {"q": "Wie schnell bekomme ich einen Termin?", "a": "In 3-5 Werktagen, bei Dringlichkeit auch kurzfristiger."}]
}

with open(DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump(pages, f, ensure_ascii=False, indent=2)
print(f'Total pages after batch 2: {len(pages)}')
