#!/usr/bin/env python3
"""Adds final 9 pages to page_data.json"""
import json, os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'page_data.json')
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    pages = json.load(f)

pages['energetische-sanierung.html'] = {
    "title": "Energetische Sanierung", "hero_desc": "Böden als Teil der energetischen Modernisierung – Dämmung und Verlegung aus einer Hand.",
    "intro": "Bei energetischer Sanierung spielt der Fußbodenaufbau eine zentrale Rolle. Wir verbinden Dämmung, Estrich und Bodenbelag zu einem optimalen System.",
    "info_box": "Ein gut gedämmter Fußboden kann die Heizkosten um bis zu 15% senken und den Wohnkomfort erheblich steigern.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "leaf", "title": "Energieeinsparung", "text": "Bis zu 15% weniger Heizkosten."},
      {"icon": "temperature-low", "title": "Warme Füße", "text": "Spürbar wärmer dank professioneller Dämmung."},
      {"icon": "award", "title": "Förderfähig", "text": "Beratung zu KfW- und BAFA-Fördermitteln."},
      {"icon": "check-circle", "title": "Alles aus einer Hand", "text": "Dämmung und Boden in einem Durchgang."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Analyse", "text": "Energetische Bewertung des Fußbodenaufbaus."},
      {"title": "Planung", "text": "Auswahl der Dämmmaterialien und des Bodenbelags."},
      {"title": "Einbau", "text": "Fachmännischer Einbau von Dämmung und Boden."},
      {"title": "Dokumentation", "text": "Nachweis für Fördermittelanträge."}],
    "table": None, "faqs": [
      {"q": "Welche Förderungen gibt es?", "a": "KfW und BAFA fördern energetische Sanierungen. Wir beraten Sie zu den Möglichkeiten."},
      {"q": "Muss der alte Boden raus?", "a": "Nicht immer. In manchen Fällen kann über dem bestehenden Aufbau gedämmt werden."}]
}
pages['raumlange-massivholzdielen.html'] = {
    "title": "Raumlange Massivholzdielen", "hero_desc": "Exklusive raumfüllende Dielen aus einem Stück – für königliches Wohnen.",
    "intro": "Raumlange Massivholzdielen sind die Königsklasse der Bodenbau. Ein Brett, ein Raum – keine Stöße, keine Unterbrechungen.",
    "info_box": "Raumlange Dielen werden individuell nach Ihren Raummaßen gefertigt – jedes Brett ist ein Unikat aus der Natur.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "arrows-alt-h", "title": "Keine Stöße", "text": "Durchgehende Dielen ohne Unterbrechung."},
      {"icon": "gem", "title": "Exklusiv", "text": "Individuelle Maßanfertigung für Ihren Raum."},
      {"icon": "tree", "title": "Premium-Holz", "text": "Nur ausgesuchte Stämme werden verwendet."},
      {"icon": "home", "title": "Wertsteigerung", "text": "Maximale Aufwertung Ihrer Immobilie."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Aufmaß", "text": "Exaktes Aufmaß jedes Raumes."},
      {"title": "Fertigung", "text": "Individuelle Maßanfertigung der Dielen."},
      {"title": "Verlegung", "text": "Fachgerechte Montage mit spezieller Technik."},
      {"title": "Finish", "text": "Oberflächenbehandlung nach Ihren Wünschen."}],
    "table": None, "faqs": [
      {"q": "Welche Längen sind möglich?", "a": "Standardmäßig bis 6 m, auf Wunsch auch darüber hinaus."},
      {"q": "Was kosten raumlange Dielen?", "a": "Je nach Holzart und Breite ab ca. 120 €/m² aufwärts."}]
}
pages['treppenverkleidungen.html'] = {
    "title": "Treppenverkleidungen", "hero_desc": "Ihre Treppe im passenden Holzdesign – nahtloser Übergang vom Boden zur Treppe.",
    "intro": "Eine Treppenverkleidung mit dem gleichen Holz wie Ihr Parkettboden schafft ein stimmiges Gesamtbild im ganzen Haus.",
    "info_box": "Treppenverkleidungen aus Parkett sind nicht nur optisch schön, sondern bieten auch einen besseren Trittschall als Stein oder Fliesen.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "shoe-prints", "title": "Einheitlich", "text": "Treppe und Boden aus dem gleichen Holz."},
      {"icon": "volume-mute", "title": "Leise", "text": "Deutlich besserer Trittschall als Stein."},
      {"icon": "palette", "title": "Vielfalt", "text": "Alle Holzarten und Oberflächen möglich."},
      {"icon": "shield-alt", "title": "Rutschhemmend", "text": "Spezielle Kantenprofile für Sicherheit."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Aufmaß", "text": "Präzise Vermessung jeder Stufe."},
      {"title": "Fertigung", "text": "Maßanfertigung der Stufenplatten."},
      {"title": "Montage", "text": "Fachgerechte Verklebung und Anpassung."},
      {"title": "Finish", "text": "Montage von Kantenprofilen."}],
    "table": None, "faqs": [
      {"q": "Kann jede Treppe verkleidet werden?", "a": "Ja – Beton, Stein und vorhandene Holztreppen können mit Parkett verkleidet werden."},
      {"q": "Wie lange dauert die Montage?", "a": "In der Regel 1-2 Tage für eine Standard-Treppe."}]
}
pages['handlaeufe-parkett.html'] = {
    "title": "Handläufe aus Parkett", "hero_desc": "Individuelle Handläufe passend zu Ihrem Parkettboden – für ein stimmiges Gesamtbild.",
    "intro": "Handläufe aus dem gleichen Holz wie Ihr Parkettboden schaffen eine durchgängige Designlinie vom Boden bis zum Geländer.",
    "info_box": "Holzhandläufe fühlen sich angenehm warm an und bieten im Vergleich zu Metall einen natürlichen Grip.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "hand-holding", "title": "Passend", "text": "Gleiches Holz wie Ihr Boden."},
      {"icon": "thermometer-half", "title": "Warm", "text": "Angenehme Haptik statt kaltem Metall."},
      {"icon": "ruler-combined", "title": "Maßarbeit", "text": "Exakt an Ihre Treppe angepasst."},
      {"icon": "shield-alt", "title": "Sicher", "text": "Natürlicher Grip für sicheren Halt."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Aufmaß", "text": "Vermessung des Treppenlaufs."},
      {"title": "Holzauswahl", "text": "Abstimmung mit Ihrem Parkettboden."},
      {"title": "Fertigung", "text": "Handwerkliche Fertigung nach Maß."},
      {"title": "Montage", "text": "Professionelle Montage und Finish."}],
    "table": None, "faqs": [
      {"q": "Welche Profile gibt es?", "a": "Rund, oval und eckig – wir beraten Sie zur passenden Form."},
      {"q": "Kann der Handlauf zum Parkett passen?", "a": "Ja, wir verwenden exakt die gleiche Holzart und Oberfläche."}]
}
pages['einlassungen-sauberlaeufe.html'] = {
    "title": "Einlassungen & Sauberläufe", "hero_desc": "Professionell eingelassene Fußmatten und Sauberläufe – für saubere Eingangsbereiche.",
    "intro": "Eingelassene Sauberläufe schützen Ihre hochwertigen Böden vor Schmutz und Feuchtigkeit direkt am Eingang.",
    "info_box": "Ein professioneller Sauberlauf fängt bis zu 90% des eingetragenen Schmutzes ab und verlängert die Lebensdauer Ihres Bodens.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "door-closed", "title": "Schutz", "text": "Schmutz und Nässe bleiben am Eingang."},
      {"icon": "ruler-combined", "title": "Bündig", "text": "Flächenbündig eingelassen – keine Stolperfallen."},
      {"icon": "palette", "title": "Passend", "text": "Farblich abgestimmt auf Ihren Boden."},
      {"icon": "sync-alt", "title": "Austauschbar", "text": "Matten können einfach gewechselt werden."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Planung", "text": "Festlegung von Position und Größe."},
      {"title": "Einbau", "text": "Fräsung der Vertiefung im Bodenaufbau."},
      {"title": "Rahmen", "text": "Montage eines Edelstahl- oder Alurahmes."},
      {"title": "Fertig", "text": "Einlegen des passenden Sauberlaufs."}],
    "table": None, "faqs": [
      {"q": "Kann das nachträglich eingebaut werden?", "a": "Ja, ein nachträglicher Einbau ist bei den meisten Bodenaufbauten möglich."},
      {"q": "Welche Matten-Arten gibt es?", "a": "Bürsten, Textil, Gummi oder Kombinationsmatten – je nach Beanspruchung."}]
}
pages['funkenschutzplatten.html'] = {
    "title": "Funkenschutzplatten", "hero_desc": "Schutz für Ihren Boden vor Kaminöfen – stilvolle Funkenschutzplatten nach Maß.",
    "intro": "Ein Kaminofen bringt Wärme und Gemütlichkeit. Damit Ihr Parkettboden dabei geschützt bleibt, liefern und montieren wir passende Funkenschutzplatten.",
    "info_box": "Funkenschutzplatten sind bei Kaminöfen gesetzlich vorgeschrieben und müssen bestimmte Mindestmaße erfüllen.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "fire", "title": "Hitze-Schutz", "text": "Zuverlässiger Schutz vor Funkenflug und Strahlungswärme."},
      {"icon": "gavel", "title": "Normgerecht", "text": "Konform mit allen baurechtlichen Vorgaben."},
      {"icon": "gem", "title": "Edel", "text": "Glas, Stahl oder Naturstein – passend zum Interieur."},
      {"icon": "ruler-combined", "title": "Maßanfertigung", "text": "Exakt zugeschnitten auf Ihren Ofen und Raum."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Beratung", "text": "Aufmaß und Materialauswahl."},
      {"title": "Fertigung", "text": "Maßanfertigung der Platte."},
      {"title": "Lieferung", "text": "Transport und Einbringung."},
      {"title": "Montage", "text": "Fachgerechte Platzierung."}],
    "table": None, "faqs": [
      {"q": "Welche Materialien gibt es?", "a": "Sicherheitsglas, Edelstahl, Schiefer und Granit sind die gängigsten Optionen."},
      {"q": "Welche Mindestmaße gelten?", "a": "Seitlich 30 cm und vorne 50 cm über den Kaminofen hinaus (länderabhängig)."}]
}
pages['kuechenarbeitsplatten.html'] = {
    "title": "Küchenarbeitsplatten", "hero_desc": "Massivholz-Arbeitsplatten für Ihre Küche – natürlich, robust und individuell.",
    "intro": "Eine Massivholz-Arbeitsplatte bringt Wärme und Natürlichkeit in Ihre Küche. Wir fertigen und montieren Arbeitsplatten aus Eiche, Buche, Nussbaum und mehr.",
    "info_box": "Holz-Arbeitsplatten sind antibakteriell – Studien zeigen, dass Holz Keime schneller abtötet als Kunststoff.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "utensils", "title": "Natürlich", "text": "Echtes Massivholz für eine warme Küchenatmosphäre."},
      {"icon": "shield-alt", "title": "Robust", "text": "Richtig behandelt extrem langlebig und belastbar."},
      {"icon": "ruler-combined", "title": "Nach Maß", "text": "Exakte Maßanfertigung inkl. Ausschnitten für Spüle und Herd."},
      {"icon": "sync-alt", "title": "Renovierbar", "text": "Kann bei Bedarf abgeschliffen und neu behandelt werden."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Aufmaß", "text": "Exakte Vermessung Ihrer Küche."},
      {"title": "Holzwahl", "text": "Auswahl von Holzart und Kantenform."},
      {"title": "Fertigung", "text": "Zuschnitt und Ausschnitte für Einbauten."},
      {"title": "Montage", "text": "Einbau und Ölung der Oberfläche."}],
    "table": None, "faqs": [
      {"q": "Welches Holz eignet sich am besten?", "a": "Eiche ist der Klassiker – hart und wasserbeständig. Buche und Nussbaum sind edle Alternativen."},
      {"q": "Wie pflege ich eine Holzarbeitsplatte?", "a": "Regelmäßiges Nachölen alle 3-6 Monate. Keine aggressiven Reiniger verwenden."}]
}
pages['wandverkleidungen-parkett.html'] = {
    "title": "Wandverkleidungen aus Parkett", "hero_desc": "Holz an der Wand – exklusive Akzente mit Parkettverkleidungen.",
    "intro": "Parkett ist nicht nur für den Boden. Wandverkleidungen aus Parkett setzen markante Designakzente und schaffen eine warme, einladende Raumatmosphäre.",
    "info_box": "Parkett an der Wand ist ein Mega-Trend im Interior Design und eignet sich perfekt als Akzentwand im Wohn- oder Schlafzimmer.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "home", "title": "Design-Statement", "text": "Holzwand als eindrucksvoller Blickfang."},
      {"icon": "volume-mute", "title": "Akustik", "text": "Holz an der Wand verbessert die Raumakustik."},
      {"icon": "thermometer-half", "title": "Wärmedämmung", "text": "Zusätzliche Isolierung an Außenwänden."},
      {"icon": "palette", "title": "Vielfalt", "text": "Alle Holzarten und Verlegemuster möglich."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Design", "text": "Planung der Akzentwand und Holzauswahl."},
      {"title": "Unterkonstruktion", "text": "Montage einer Tragstruktur."},
      {"title": "Verkleidung", "text": "Fachgerechte Montage des Parketts."},
      {"title": "Finish", "text": "Abschlussleisten und finale Kontrolle."}],
    "table": None, "faqs": [
      {"q": "Welches Parkett eignet sich für die Wand?", "a": "Leichte Varianten wie Fertigparkett oder dünnes Massivholz eignen sich besonders gut."},
      {"q": "Kann man das gleiche Parkett wie am Boden verwenden?", "a": "Ja, für ein durchgängiges Design verwenden wir oft das identische Parkett."}]
}
pages['vinyl-nassbereich.html'] = {
    "title": "Vinyl im Nassbereich", "hero_desc": "Wasserfester Designboden für Bad und Wellnessbereiche – stylisch und pflegeleicht.",
    "intro": "Vinyl im Nassbereich bietet die perfekte Kombination: die warme Optik von Holz mit der Wasserresistenz einer Fliese.",
    "info_box": "Modernes Vinyl für Nassbereiche ist zu 100% wasserdicht, rutschfest und fußwarm – ganz ohne die Kälte von Fliesen.",
    "benefits_title": "Ihre Vorteile", "benefits": [
      {"icon": "tint", "title": "100% Wasserdicht", "text": "Kein Aufquellen, kein Wasserschaden."},
      {"icon": "shoe-prints", "title": "Rutschfest", "text": "Spezielle Oberflächen für nasse Bereiche."},
      {"icon": "thermometer-half", "title": "Fußwarm", "text": "Deutlich wärmer als Fliesen."},
      {"icon": "broom", "title": "Pflegeleicht", "text": "Einfache Reinigung, keine Fugen."}],
    "process_title": "Unser Ablauf", "process": [
      {"title": "Beratung", "text": "Auswahl des passenden Nassraum-Vinyls."},
      {"title": "Abdichtung", "text": "Professionelle Untergrundabdichtung."},
      {"title": "Verlegung", "text": "Vollflächige Verklebung mit Nahtversiegelung."},
      {"title": "Finish", "text": "Silikonfugen und Übergangsprofile."}],
    "table": None, "faqs": [
      {"q": "Ist Vinyl im Bad wirklich wasserdicht?", "a": "Ja! Vollflächig verklebtes Vinyl mit versiegelten Nähten ist zu 100% wasserdicht."},
      {"q": "Kann Vinyl auf Fliesen im Bad verlegt werden?", "a": "Ja, nach fachgerechter Vorbereitung kann Vinyl direkt auf vorhandene Fliesen geklebt werden."}]
}

with open(DATA_FILE, 'w', encoding='utf-8') as f:
    json.dump(pages, f, ensure_ascii=False, indent=2)
print(f'Total pages after batch 3: {len(pages)}')
