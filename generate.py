import os
import xml.etree.ElementTree as ET

# 🌐 URL officielle de production avec https://
BASE_URL = "https://mon-site-pseo.vercel.app"

# Base de données d'exemples de formats, outils et specs tech
topics = [
    ("mp4-to-mp3", "Convertir MP4 en MP3", "Audio/Video", "320 kbps", "AAC/MPEG"),
    ("youtube-4k-bitrate", "Bitrate Recommandé YouTube 4K", "Video Render", "45-68 Mbps", "H.264 / HEVC"),
    ("flac-vs-wav", "FLAC vs WAV : Comparatif Qualité", "Audio Formats", "1411 kbps", "Lossless"),
    ("mkv-to-mp4", "Convertir MKV en MP4 sans Perte", "Video Conversion", "Variable", "H.264"),
    ("png-vs-jpeg", "PNG vs JPEG : Compression et Transparence", "Image Formats", "Lossless/Lossy", "PNG/JPG"),
    ("webp-converter", "Optimisation WebP pour Sites Web", "Web Performance", "75% Compression", "WebP"),
    ("mov-to-mp4", "Exporter MOV en MP4 pour Premiere Pro", "Editing", "Auto", "ProRes/H.264"),
]

# Template HTML pour les sous-pages
html_template = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Hw5HcXkd5TKh4zwp_48lZS02Vbcq26puFir5GiVd_dY" />
    <title>{title} - Guide & Spécifications</title>
    <meta name="description" content="Guide complet et fiches techniques : {title}. Spécifications, codecs et paramètres recommandés.">
    <link rel="canonical" href="{canonical_url}" />
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 0; background-color: #f8f9fa; color: #212529; }}
        header {{ background: #007bff; color: white; padding: 20px; text-align: center; }}
        .container {{ max-width: 800px; margin: 30px auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }}
        .ad-slot {{ background: #e9ecef; border: 2px dashed #ced4da; text-align: center; padding: 25px; margin: 25px 0; font-weight: bold; color: #6c757d; border-radius: 4px; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ border: 1px solid #dee2e6; padding: 12px; text-align: left; }}
        th {{ background-color: #f1f3f5; }}
        a {{ color: #007bff; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <header>
        <h1>Centre de Spécifications Tech & Média</h1>
    </header>
    <div class="container">
        <h1>{title}</h1>
        
        <!-- ESPACE PUB HAUT -->
        <div class="ad-slot">[ EMPLACEMENT PUB HIGH RPM ]</div>

        <p>Catégorie : <strong>{category}</strong></p>
        
        <h2>Fiche Technique</h2>
        <table>
            <tr><th>Paramètre</th><th>Valeur Standard</th></tr>
            <tr><td>Débit / Bitrate</td><td>{bitrate}</td></tr>
            <tr><td>Codec / Format</td><td>{codec}</td></tr>
        </table>

        <!-- ESPACE PUB MILIEU -->
        <div class="ad-slot">[ EMPLACEMENT PUB MILIEU ]</div>

        <h2>Recommandations d'Optimisation</h2>
        <p>Pour obtenir les meilleures performances dans la catégorie <strong>{category}</strong>, assurez-vous de configurer vos exportations selon les valeurs indiquées ci-dessus.</p>
        
        <p><a href="index.html">← Retour à l'accueil</a></p>

        <!-- ESPACE PUB BAS -->
        <div class="ad-slot">[ EMPLACEMENT PUB BAS ]</div>
    </div>
</body>
</html>
"""

# Template Page d'accueil (Index) - Ajout de la balise de vérification Google
index_template = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Hw5HcXkd5TKh4zwp_48lZS02Vbcq26puFir5GiVd_dY" />
    <title>Base de Données Tech & Conversion Média</title>
    <link rel="canonical" href="{base_url}/" />
    <style>
        body {{ font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 0 20px; line-height: 1.6; }}
        ul {{ list-style-type: none; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 10px; }}
        li {{ background: #f8f9fa; padding: 12px; border-radius: 4px; border: 1px solid #e9ecef; }}
        a {{ color: #007bff; text-decoration: none; font-weight: bold; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>Répertoire Complet des Fiches Techniques</h1>
    <p>Sélectionnez un guide ci-dessous pour voir les spécifications d'encodage :</p>
    <ul>
        {links}
    </ul>
</body>
</html>
"""

# 1. Génération des pages HTML
links_html = ""
generated_files = []
count = 0

for i in range(1, 75):
    for slug, title, category, bitrate, codec in topics:
        full_slug = f"{slug}-v{i}.html"
        full_title = f"{title} (Option #{i})"
        canonical_url = f"{BASE_URL}/{full_slug}"
        
        content = html_template.format(
            title=full_title,
            category=category,
            bitrate=bitrate,
            codec=codec,
            canonical_url=canonical_url
        )
        
        with open(full_slug, "w", encoding="utf-8") as f:
            f.write(content)
        
        generated_files.append(full_slug)
        links_html += f'<li><a href="{full_slug}">{full_title}</a></li>\n'
        count += 1

# 2. Génération de la page d'accueil (index.html)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_template.format(links=links_html, base_url=BASE_URL))

# 3. Génération automatique du sitemap.xml
urlset = ET.Element("urlset", xmlns="http://www.sitemap.org/schemas/sitemap/0.9")

# Ajouter l'index
url_elem = ET.SubElement(urlset, "url")
loc = ET.SubElement(url_elem, "loc")
loc.text = f"{BASE_URL}/"

# Ajouter toutes les pages
for file_name in generated_files:
    url_elem = ET.SubElement(urlset, "url")
    loc = ET.SubElement(url_elem, "loc")
    loc.text = f"{BASE_URL}/{file_name}"

tree = ET.ElementTree(urlset)
ET.indent(tree, space="  ", level=0)
tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)

# 4. Génération automatique du robots.txt
robots_content = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)

print(f" SUCCÈS :")
print(f" - {count} pages HTML générées")
print(f" - index.html généré (avec balise de vérification Google)")
print(f" - sitemap.xml généré avec {count + 1} URLs sous https://")
print(f" - robots.txt généré")