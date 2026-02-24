from datetime import datetime, timedelta

# Diccionario de canales con los IDs CORTOS que pediste
canales = [
    {"id": "GH.MULTI", "n": "Multicámara", "t": "GH - Experiencia Multicámara"},
    {"id": "GH.24HS", "n": "Gran Hermano 24 hs.", "t": "Gran Hermano 24 hs."},
    {"id": "GH.CAM1", "n": "Cámara 1", "t": "Gran Hermano - Cámara 1"},
    {"id": "GH.CAM2", "n": "Cámara 2", "t": "Gran Hermano - Cámara 2"},
    {"id": "GH.CAM3", "n": "Cámara 3", "t": "Gran Hermano - Cámara 3"},
]

desc = "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada, donde los participantes deberán sobreponerse al encierro y la convivencia para avanzar y quedarse con el tan anhelado premio."
img = "https://i.postimg.cc/hjxWkfMf/image.png"

def generar():
    now = datetime.now()
    inicio = now.replace(hour=0, minute=0, second=0, microsecond=0)
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<tv>\n'
    
    # Declaramos los 5 canales
    for c in canales:
        xml += f'  <channel id="{c["id"]}"><display-name>{c["n"]}</display-name></channel>\n'
    
    # Generamos los programas para los 5 canales
    for c in canales:
        for d in range(3):
            for h in range(0, 24, 3):
                s = (inicio + timedelta(days=d, hours=h)).strftime("%Y%m%d%H%M%S +0000")
                e = (inicio + timedelta(days=d, hours=h+3)).strftime("%Y%m%d%H%M%S +0000")
                xml += f'  <programme start="{s}" stop="{e}" channel="{c["id"]}">\n'
                xml += f'    <title lang="es">{c["t"]}</title>\n'
                xml += f'    <desc lang="es">{desc}</desc>\n'
                xml += f'    <icon src="{img}" />\n'
                xml += f'  </programme>\n'
    xml += '</tv>'
    with open("data_v9.xml", "w", encoding="utf-8") as f:
        f.write(xml)

if __name__ == "__main__":
    generar()
