from datetime import datetime, timedelta

# IDs actualizados según tu pedido
canales = [
    {"id": "GH.MULTI", "nombre": "Multicámara", "titulo": "GH - Experiencia Multicámara"},
    {"id": "GH.24HS", "nombre": "Gran Hermano 24 hs.", "titulo": "Gran Hermano 24 hs."},
    {"id": "GH.CAM1", "nombre": "Cámara 1", "titulo": "Gran Hermano - Cámara 1"},
    {"id": "GH.CAM2", "nombre": "Cámara 2", "titulo": "Gran Hermano - Cámara 2"},
    {"id": "GH.CAM3", "nombre": "Cámara 3", "titulo": "Gran Hermano - Cámara 3"},
]

desc = "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada, donde los participantes deberán sobreponerse al encierro y la convivencia para avanzar y quedarse con el tan anhelado premio."
img = "https://i.postimg.cc/hjxWkfMf/image.png"

def generar():
    now = datetime.now()
    # Iniciamos desde el comienzo del día actual
    inicio = now.replace(hour=0, minute=0, second=0, microsecond=0)
    
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<tv generator-info-name="D-SYS">\n'
    
    # 1. Definir TODOS los canales en la cabecera
    for c in canales:
        xml += f'  <channel id="{c["id"]}"><display-name>{c["nombre"]}</display-name></channel>\n'
    
    # 2. Generar programas para cada uno de los 5 canales
    for d in range(3): # 3 días de cobertura
        for h in range(0, 24, 3): # Bloques de 3 horas
            s = (inicio + timedelta(days=d, hours=h)).strftime("%Y%m%d%H%M%S +0000")
            e = (inicio + timedelta(days=d, hours=h+3)).strftime("%Y%m%d%H%M%S +0000")
            
            # ESTA PARTE ES CLAVE: debe iterar por cada canal del array
            for c in canales:
                xml += f'  <programme start="{s}" stop="{e}" channel="{c["id"]}">\n'
                xml += f'    <title>{c["titulo"]}</title>\n'
                xml += f'    <desc>{desc}</desc>\n'
                xml += f'    <category>Reality</category>\n'
                xml += f'    <rating><value>+16</value></rating>\n'
                xml += f'    <icon src="{img}" />\n'
                xml += f'  </programme>\n'
                
    xml += '</tv>'
    with open("data_v9.xml", "w", encoding="utf-8") as f:
        f.write(xml)

if __name__ == "__main__":
    generar()
