from datetime import datetime, timedelta

# Canales de Gran Hermano
canales_gh = [
    {"id": "GH.MULTI", "n": "Multicámara", "t": "GH - Experiencia Multicámara"},
    {"id": "GH.24HS", "n": "Gran Hermano 24 hs.", "t": "Gran Hermano 24 hs."},
    {"id": "GH.CAM1", "n": "Cámara 1", "t": "Gran Hermano - Cámara 1"},
    {"id": "GH.CAM2", "n": "Cámara 2", "t": "Gran Hermano - Cámara 2"},
    {"id": "GH.CAM3", "n": "Cámara 3", "t": "Gran Hermano - Cámara 3"},
]

# Configuración del canal de Los Simpson (ID corregido a Simpson)
canal_simpson = {"id": "Simpson", "n": "Los Simpson", "t": "Los Simpson"}
desc_simpson = "Narra las vivencias de una peculiar familia norteamericana conformada por Homero, Marge, Bart, Lisa y Maggie Simpson, junto a otros divertidos personajes de la localidad de Springfield. Elenco: Julie Kavner, Yeardley Smith, Hank Azaria. Director: Jim Reardon."
img_simpson = "https://static.flow.com.ar/images/10105665361/BROWSE/600/600/0/0/10105665361.jpg"

desc_gh = "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada, donde los participantes deberán sobreponerse al encierro y la convivencia."
img_gh = "https://i.postimg.cc/hjxWkfMf/image.png"

def generar():
    now = datetime.now()
    inicio = now.replace(hour=0, minute=0, second=0, microsecond=0)
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<tv>\n'
    
    # 1. Declaramos los canales de GH
    for c in canales_gh:
        xml += f'  <channel id="{c["id"]}"><display-name>{c["n"]}</display-name></channel>\n'
    
    # 2. Declaramos el canal de Los Simpson con ID Simpson
    xml += f'  <channel id="{canal_simpson["id"]}"><display-name>{canal_simpson["n"]}</display-name></channel>\n'
    
    # 3. Generamos programas para Gran Hermano
    for c in canales_gh:
        for d in range(3):
            for h in range(0, 24, 3):
                s = (inicio + timedelta(days=d, hours=h)).strftime("%Y%m%d%H%M%S +0000")
                e = (inicio + timedelta(days=d, hours=h+3)).strftime("%Y%m%d%H%M%S +0000")
                xml += f'  <programme start="{s}" stop="{e}" channel="{c["id"]}">\n'
                xml += f'    <title lang="es">{c["t"]}</title>\n<desc lang="es">{desc_gh}</desc>\n'
                xml += f'    <category>Reality</category>\n<icon src="{img_gh}" />\n  </programme>\n'

    # 4. Generamos programas para Los Simpson (ID: Simpson)
    for d in range(3):
        for h in range(0, 24, 3):
            s = (inicio + timedelta(days=d, hours=h)).strftime("%Y%m%d%H%M%S +0000")
            e = (inicio + timedelta(days=d, hours=h+3)).strftime("%Y%m%d%H%M%S +0000")
            xml += f'  <programme start="{s}" stop="{e}" channel="{canal_simpson["id"]}">\n'
            xml += f'    <title lang="es">{canal_simpson["t"]}</title>\n'
            xml += f'    <desc lang="es">{desc_simpson}</desc>\n'
            xml += f'    <category>Comedia, Animación</category>\n'
            xml += f'    <icon src="{img_simpson}" />\n'
            xml += f'  </programme>\n'

    xml += '</tv>'
    with open("data_v9.xml", "w", encoding="utf-8") as f:
        f.write(xml)

if __name__ == "__main__":
    generar()
