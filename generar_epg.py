from datetime import datetime, timedelta

# Canales de Gran Hermano
canales_gh = [
    {"id": "GH.MULTI", "n": "Multicámara", "t": "GH - Experiencia Multicámara"},
    {"id": "GH.24HS", "n": "Gran Hermano 24 hs.", "t": "Gran Hermano 24 hs."},
    {"id": "GH.CAM1", "n": "Cámara 1", "t": "Gran Hermano - Cámara 1"},
    {"id": "GH.CAM2", "n": "Cámara 2", "t": "Gran Hermano - Cámara 2"},
    {"id": "GH.CAM3", "n": "Cámara 3", "t": "Gran Hermano - Cámara 3"},
]

# Configuración del canal de Los Simpsons
canal_simpsons = {"id": "Simpsons", "n": "Los Simpsons 24/7", "t": "Los Simpsons"}
desc_simpsons = "Narra las vivencias de una peculiar familia norteamericana conformada por Homero, Marge, Bart, Lisa y Maggie Simpson, junto a otros divertidos personajes de la localidad de Springfield. Elenco: Julie Kavner, Yeardley Smith, Hank Azaria. Director: Jim Reardon."
img_simpsons = "https://static.flow.com.ar/images/10105665361/BROWSE/600/600/0/0/10105665361.jpg"

desc_gh = "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada."
img_gh = "https://i.postimg.cc/hjxWkfMf/image.png"

def generar():
    now = datetime.now()
    inicio = now.replace(hour=0, minute=0, second=0, microsecond=0)
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<tv>\n'
    
    # Declaramos todos los canales (GH + Simpsons)
    for c in canales_gh:
        xml += f'  <channel id="{c["id"]}"><display-name>{c["n"]}</display-name></channel>\n'
    xml += f'  <channel id="{canal_simpsons["id"]}"><display-name>{canal_simpsons["n"]}</display-name></channel>\n'
    
    # Bloques para Gran Hermano
    for c in canales_gh:
        for d in range(3):
            for h in range(0, 24, 3):
                s = (inicio + timedelta(days=d, hours=h)).strftime("%Y%m%d%H%M%S +0000")
                e = (inicio + timedelta(days=d, hours=h+3)).strftime("%Y%m%d%H%M%S +0000")
                xml += f'  <programme start="{s}" stop="{e}" channel="{c["id"]}">\n'
                xml += f'    <title lang="es">{c["t"]}</title>\n<desc lang="es">{desc_gh}</desc>\n'
                xml += f'    <category>Reality</category>\n<icon src="{img_gh}" />\n  </programme>\n'

    # Bloques para Los Simpsons (3 horas, 24/7, renovación automática)
    for d in range(3):
        for h in range(0, 24, 3):
            s = (inicio + timedelta(days=d, hours=h)).strftime("%Y%m%d%H%M%S +0000")
            e = (inicio + timedelta(days=d, hours=h+3)).strftime("%Y%m%d%H%M%S +0000")
            xml += f'  <programme start="{s}" stop="{e}" channel="{canal_simpsons["id"]}">\n'
            xml += f'    <title lang="es">{canal_simpsons["t"]}</title>\n'
            xml += f'    <desc lang="es">{desc_simpsons}</desc>\n'
            xml += f'    <category>Comedia, Animación</category>\n'
            xml += f'    <icon src="{img_simpsons}" />\n'
            xml += f'  </programme>\n'

    xml += '</tv>'
    with open("data_v9.xml", "w", encoding="utf-8") as f:
        f.write(xml)

if __name__ == "__main__":
    generar()
