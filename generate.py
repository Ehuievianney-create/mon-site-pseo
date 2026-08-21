import os
import json
import xml.etree.ElementTree as ET

# 🌐 URL officielle de production
BASE_URL = "https://mon-site-pseo.vercel.app"

# Configuration : Génération directement à la racine
OUTPUT_DIR = "."

# 1. Base de données des sujets avec offres d'affiliation ciblées
TOPICS = [
    {
        "slug": "mp4-to-mp3", 
        "title": "Convertir MP4 en MP3", 
        "category": "Audio/Video", 
        "bitrate": "320 kbps", 
        "codec": "AAC/MPEG",
        "aff_title": "🎬 Logiciel Recommandé : Movavi Video Converter",
        "aff_desc": "Convertissez vos fichiers MP4 en MP3 à grande vitesse sans perte de qualité audio. Supporte le traitement par lot.",
        "aff_link": "https://www.movavi.com/fr/",
        "aff_cta": "Essayer gratuitement Movavi"
    },
    {
        "slug": "youtube-4k-bitrate", 
        "title": "Bitrate Recommandé YouTube 4K", 
        "category": "Video Render", 
        "bitrate": "45-68 Mbps", 
        "codec": "H.264 / HEVC",
        "aff_title": "🚀 Optimisez vos rendus 4K avec Wondershare Filmora",
        "aff_desc": "Exportez des vidéos 4K fluides aux profils de bitrate idéaux pour YouTube Shorts et vidéos longues.",
        "aff_link": "https://filmora.wondershare.fr/",
        "aff_cta": "Télécharger Filmora Pro"
    },
    {
        "slug": "flac-vs-wav", 
        "title": "FLAC vs WAV : Comparatif Qualité", 
        "category": "Audio Formats", 
        "bitrate": "1411 kbps", 
        "codec": "Lossless",
        "aff_title": "🎧 Traitement Audio Studio avec Adobe Audition",
        "aff_desc": "Nettoyez, éditez et convertissez vos pistes Lossless (FLAC, WAV) avec les outils standard de l'industrie.",
        "aff_link": "https://www.adobe.com/fr/products/audition.html",
        "aff_cta": "Découvrir Adobe Audition"
    },
    {
        "slug": "mkv-to-mp4", 
        "title": "Convertir MKV en MP4 sans Perte", 
        "category": "Video Conversion", 
        "bitrate": "Variable", 
        "codec": "H.264",
        "aff_title": "⚡ EaseUS Video Converter : Conversion Ultra Rapide",
        "aff_desc": "Convertissez vos fichiers MKV lourds en MP4 universel en gardant toutes les pistes sous-titres et audio.",
        "aff_link": "https://fr.easeus.com/multimedia/video-converter.html",
        "aff_cta": "Obtenir EaseUS Converter"
    },
    {
        "slug": "png-vs-jpeg", 
        "title": "PNG vs JPEG : Compression et Transparence", 
        "category": "Image Formats", 
        "bitrate": "Lossless/Lossy", 
        "codec": "PNG/JPG",
        "aff_title": "🎨 Canva Pro : Optimisation d'Images Web & Transparence",
        "aff_desc": "Créez et exportez des visuels PNG haute résolution ou JPEG compressés en un clic.",
        "aff_link": "https://www.canva.com/fr_fr/",
        "aff_cta": "Tester Canva Pro Gratuitement"
    },
    {
        "slug": "webp-converter", 
        "title": "Optimisation WebP pour Sites Web", 
        "category": "Web Performance", 
        "bitrate": "75% Compression", 
        "codec": "WebP",
        "aff_title": "⚡ Boostez la vitesse de votre site avec WP Rocket",
        "aff_desc": "Servez automatiquement vos images au format WebP et améliorez votre score Google Core Web Vitals.",
        "aff_link": "https://wp-rocket.me/fr/",
        "aff_cta": "Booster mon site avec WP Rocket"
    },
    {
        "slug": "mov-to-mp4", 
        "title": "Exporter MOV en MP4 pour Premiere Pro", 
        "category": "Editing", 
        "bitrate": "Auto", 
        "codec": "ProRes/H.264",
        "aff_title": "🎬 Suite Adobe Creative Cloud pour Monteurs",
        "aff_desc": "Profitez de Premiere Pro et Media Encoder pour gérer tous vos exports MOV/MP4 sans aucun bug de codec.",
        "aff_link": "https://www.adobe.com/fr/creativecloud.html",
        "aff_cta": "Voir les offres Creative Cloud"
    },
    {
        "slug": "pdf-to-docx", 
        "title": "Convertir PDF en Word Éditable", 
        "category": "Document Conversion", 
        "bitrate": "N/A", 
        "codec": "PDF/DOCX",
        "aff_title": "📄 PDFelement : L'alternative puissante à Adobe Acrobat",
        "aff_desc": "Editez, convertissez et OCRisez tous vos documents PDF en fichiers Word modifiables en quelques secondes.",
        "aff_link": "https://pdf.wondershare.fr/",
        "aff_cta": "Télécharger PDFelement"
    },
    {
        "slug": "heic-to-jpg", 
        "title": "Convertir Photo HEIC iOS en JPG", 
        "category": "Image Formats", 
        "bitrate": "Haute Qualité", 
        "codec": "HEIC/JPG",
        "aff_title": "📱 CopyTrans Manager : Gérez vos Photos iPhone facilement",
        "aff_desc": "Transférez et convertissez automatiquement vos photos iPhone HEIC vers Windows au format JPG.",
        "aff_link": "https://www.copytrans.fr/",
        "aff_cta": "Découvrir CopyTrans"
    },
    {
        "slug": "audio-transcription", 
        "title": "Transcription Audio en Texte", 
        "category": "Audio AI", 
        "bitrate": "128 kbps", 
        "codec": "WAV/TXT",
        "aff_title": "🤖 Descript : Transcription IA et Édition Audio Automatique",
        "aff_desc": "Transcrivez vos fichiers audio en texte avec une précision de 95% et éditez le son en modifiant directement le texte.",
        "aff_link": "https://www.descript.com/",
        "aff_cta": "Essayer Descript IA"
    },
    {
        "slug": "compress-pdf", 
        "title": "Compresser Fichier PDF pour Email", 
        "category": "Document Optimization", 
        "bitrate": "Medium DPI", 
        "codec": "PDF",
        "aff_title": "💼 Smallpdf Pro : Compressez et Organisez vos Fichiers",
        "aff_desc": "Réduisez la taille de vos documents PDF jusqu'à 80% tout en conservant la netteté du texte et des images.",
        "aff_link": "https://smallpdf.com/fr",
        "aff_cta": "Essayer Smallpdf Pro"
    },
    {
        "slug": "srt-subtitle-extractor", 
        "title": "Extraire Sous-Titres SRT de Vidéo", 
        "category": "Video Subtitles", 
        "bitrate": "N/A", 
        "codec": "SRT/UTF-8",
        "aff_title": "🎥 Kapwing : Sous-titrage Automatique par IA",
        "aff_desc": "Générez, extrayez et traduisez des fichiers de sous-titres SRT pour TikTok, Reels et YouTube en un clic.",
        "aff_link": "https://www.kapwing.com/",
        "aff_cta": "Créer des sous-titres avec Kapwing"
    }
]

# 2. Cas d'usage
USES = [
    {"slug": "gratuit-en-ligne", "name": "Gratuit en Ligne"},
    {"slug": "pour-montage-pro", "name": "pour Montage Vidéo Pro"},
    {"slug": "pour-tiktok-et-reels", "name": "pour TikTok et Reels"},
    {"slug": "pour-youtube-shorts", "name": "pour YouTube Shorts"},
    {"slug": "pour-wordpress", "name": "pour Site WordPress"},
    {"slug": "pour-shopify", "name": "pour Boutique Shopify"},
    {"slug": "sur-mac-et-ios", "name": "sur Mac et iPhone"},
    {"slug": "sur-windows-11", "name": "sur Windows 11"},
    {"slug": "sans-perte-de-qualite", "name": "Sans Perte de Qualité"},
    {"slug": "pour-envoi-email", "name": "pour Envoi par Email"},
    {"slug": "pour-archivage", "name": "pour Archivage Web"},
    {"slug": "pour-etudiants", "name": "pour Étudiants & Cours"},
    {"slug": "traitement-par-lot", "name": "par Lot (Batch)"},
    {"slug": "pour-developpeurs", "name": "pour Développeurs"},
    {"slug": "pour-reseaux-sociaux", "name": "pour Réseaux Sociaux"}
]

# 3. Formats de révision
TARGETS = [
    {"slug": "guide-2026", "name": "Guide 2026"},
    {"slug": "methode-facile", "name": "Méthode Facile"},
    {"slug": "meilleurs-outils", "name": "Meilleurs Outils"},
    {"slug": "tutoriel-complet", "name": "Tutoriel Pas à Pas"},
    {"slug": "sans-logiciel", "name": "Sans Logiciel"},
    {"slug": "outil-gratuit", "name": "Outil Gratuit"},
    {"slug": "methode-securisee", "name": "Méthode Sécurisée"},
    {"slug": "en-1-minute", "name": "En 1 Minute"},
    {"slug": "haute-performance", "name": "Haute Performance"},
    {"slug": "sans-installation", "name": "Sans Installation"},
    {"slug": "qualite-maximale", "name": "Qualité Maximale"},
    {"slug": "parametres-recommandes", "name": "Paramètres Recommandés"}
]

# Template HTML avec bloc d'affiliation stylisé
html_template = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Hw5HcXkd5TKh4zwp_48lZS02Vbcq26puFir5GiVd_dY" />
    <title>{full_title} | Spécifications & Guides</title>
    <meta name="description" content="Guide complet et fiches techniques : {full_title}. Spécifications, codecs et paramètres recommandés.">
    <link rel="canonical" href="{canonical_url}" />
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 0; background-color: #f8f9fa; color: #212529; line-height: 1.6; }}
        header {{ background: #007bff; color: white; padding: 20px; text-align: center; }}
        .container {{ max-width: 800px; margin: 30px auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }}
        
        /* Style du bloc d'affiliation */
        .affiliate-box {{ background-color: #f0f7ff; border: 2px solid #007bff; border-radius: 8px; padding: 20px; margin: 25px 0; }}
        .affiliate-box h3 {{ margin-top: 0; color: #0056b3; font-size: 1.2rem; }}
        .affiliate-box p {{ font-size: 0.95rem; color: #333; margin-bottom: 15px; }}
        .aff-btn {{ display: inline-block; background-color: #28a745; color: white !important; font-weight: bold; padding: 12px 20px; border-radius: 5px; text-decoration: none; transition: background 0.2s; }}
        .aff-btn:hover {{ background-color: #218838; text-decoration: none; }}

        .ad-slot {{ background: #e9ecef; border: 2px dashed #ced4da; text-align: center; padding: 15px; margin: 20px 0; font-weight: bold; color: #6c757d; border-radius: 4px; font-size: 0.85rem; }}
        table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
        th, td {{ border: 1px solid #dee2e6; padding: 12px; text-align: left; }}
        th {{ background-color: #f1f3f5; }}
        a {{ color: #007bff; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        .links-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 10px; list-style: none; padding: 0; margin-top: 20px; }}
        .links-grid li {{ background: #f8f9fa; padding: 10px; border-radius: 4px; font-size: 0.9rem; border: 1px solid #e9ecef; }}
    </style>
</head>
<body>
    <header>
        <h1>Centre de Spécifications Tech & Média</h1>
    </header>
    <div class="container">
        <h1>{full_title}</h1>
        
        <!-- EMPLACEMENT PUB HAUT (AdSense / Ezoic) -->
        <div class="ad-slot">[ EMPLACEMENT PUB HIGH RPM ]</div>

        <p>Catégorie : <strong>{category}</strong> | Usage : <strong>{use_name}</strong></p>
        
        <h2>Fiche Technique & Configuration</h2>
        <table>
            <tr><th>Paramètre</th><th>Valeur Standard</th></tr>
            <tr><td>Débit / Bitrate</td><td>{bitrate}</td></tr>
            <tr><td>Codec / Format</td><td>{codec}</td></tr>
            <tr><td>Usage Cible</td><td>{use_name}</td></tr>
            <tr><td>Format du Guide</td><td>{target_name}</td></tr>
        </table>

        <!-- BLOC D'AFFILIATION DYNAMIQUE CIBLÉ -->
        <div class="affiliate-box">
            <h3>{aff_title}</h3>
            <p>{aff_desc}</p>
            <a href="{aff_link}" target="_blank" rel="nofollow sponsored" class="aff-btn">{aff_cta} →</a>
        </div>

        <!-- EMPLACEMENT PUB MILIEU -->
        <div class="ad-slot">[ EMPLACEMENT PUB MILIEU ]</div>

        <h2>Recommandations d'Optimisation</h2>
        <p>Pour obtenir les meilleures performances dans la catégorie <strong>{category}</strong> ({use_name}), assurez-vous de configurer vos exportations selon les valeurs indiquées ci-dessus.</p>

        <h2>Foire Aux Questions</h2>
        <p><strong>Est-ce adapté pour un usage professionnel ?</strong><br>Oui, cette méthode ({target_name}) est optimisée pour garantir la compatibilité maximale et un rendu rapide.</p>

        <p><a href="/index.html">← Retour à l'accueil</a></p>

        <h2>Autres fiches techniques suggérées</h2>
        <ul class="links-grid">
            {related_links}
        </ul>

        <!-- EMPLACEMENT PUB BAS -->
        <div class="ad-slot">[ EMPLACEMENT PUB BAS ]</div>
    </div>
</body>
</html>
"""

# Template Page d'accueil (Index)
index_template = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="google-site-verification" content="Hw5HcXkd5TKh4zwp_48lZS02Vbcq26puFir5GiVd_dY" />
    <title>Base de Données Tech & Conversion Média</title>
    <link rel="canonical" href="{base_url}/" />
    <style>
        body {{ font-family: sans-serif; max-width: 900px; margin: 40px auto; padding: 0 20px; line-height: 1.6; }}
        ul {{ list-style-type: none; padding: 0; display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 10px; }}
        li {{ background: #f8f9fa; padding: 12px; border-radius: 4px; border: 1px solid #e9ecef; font-size: 0.9rem; }}
        a {{ color: #007bff; text-decoration: none; font-weight: bold; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>Répertoire Complet des Fiches Techniques (2000+ Guides)</h1>
    <p>Sélectionnez un guide ci-dessous pour voir les spécifications d'encodage :</p>
    <ul>
        {links}
    </ul>
</body>
</html>
"""

# 1. Génération de la matrice complète des pages
all_pages = []
for topic in TOPICS:
    for use in USES:
        for tgt in TARGETS:
            slug = f"{topic['slug']}-{use['slug']}-{tgt['slug']}"
            title = f"{topic['title']} {use['name']} ({tgt['name']})"
            all_pages.append({
                "slug": slug,
                "title": title,
                "topic": topic,
                "use": use,
                "tgt": tgt
            })

total_pages = len(all_pages)
print(f"🚀 Début de la génération de {total_pages} pages pSEO optimisées pour l'affiliation...")

generated_files = []
links_html = ""

# 2. Écriture des fichiers HTML à la racine du projet
for idx, page in enumerate(all_pages):
    file_name = f"{page['slug']}.html"
    file_path = os.path.join(OUTPUT_DIR, file_name)
    canonical_url = f"{BASE_URL}/{file_name}"

    # Maillage interne
    related_items = [all_pages[(idx + i * 43) % total_pages] for i in range(1, 6)]
    related_links_html = "".join([f'<li><a href="/{r["slug"]}.html">{r["title"]}</a></li>' for r in related_items])

    content = html_template.format(
        full_title=page['title'],
        category=page['topic']['category'],
        use_name=page['use']['name'],
        target_name=page['tgt']['name'],
        bitrate=page['topic']['bitrate'],
        codec=page['topic']['codec'],
        aff_title=page['topic']['aff_title'],
        aff_desc=page['topic']['aff_desc'],
        aff_link=page['topic']['aff_link'],
        aff_cta=page['topic']['aff_cta'],
        canonical_url=canonical_url,
        related_links=related_links_html
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    generated_files.append(file_name)
    
    if idx < 150:
        links_html += f'<li><a href="/{file_name}">{page["title"]}</a></li>\n'

# 3. Génération de index.html
with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_template.format(links=links_html, base_url=BASE_URL))

# 4. Génération du sitemap.xml
urlset = ET.Element("urlset", {
    "xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9"
})

url_elem = ET.SubElement(urlset, "url")
loc = ET.SubElement(url_elem, "loc")
loc.text = f"{BASE_URL}/"

for file_name in generated_files:
    url_elem = ET.SubElement(urlset, "url")
    loc = ET.SubElement(url_elem, "loc")
    loc.text = f"{BASE_URL}/{file_name}"

tree = ET.ElementTree(urlset)
ET.indent(tree, space="  ", level=0)
tree.write(os.path.join(OUTPUT_DIR, "sitemap.xml"), encoding="utf-8", xml_declaration=True)

# 5. Génération du robots.txt
robots_content = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_content)

print(f"✨ SUCCÈS : {len(generated_files)} pages HTML avec blocs d'affiliation régénérées avec succès !")