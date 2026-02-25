import datetime

canales = [
    {"id": "GH.MULTI", "n": "Multicámara", "t": "GH - Experiencia Multicámara", "d": "La casa más famosa del país vuelve a abrir sus puertas.", "m": "https://i.postimg.cc/hjxWkfMf/image.png"},
    {"id": "GH.24HS", "n": "Gran Hermano 24 hs.", "t": "Gran Hermano 24 hs.", "d": "La casa más famosa del país en vivo.", "m": "https://i.postimg.cc/hjxWkfMf/image.png"},
    {"id": "GH.CAM1", "n": "Cámara 1", "t": "Gran Hermano - Cámara 1", "d": "Cámara exclusiva de la casa.", "m": "https://i.postimg.cc/hjxWkfMf/image.png"},
    {"id": "GH.CAM2", "n": "Cámara 2", "t": "Gran Hermano - Cámara 2", "d": "Cámara exclusiva de la casa.", "m": "https://i.postimg.cc/hjxWkfMf/image.png"},
    {"id": "GH.CAM3", "n": "Cámara 3", "t": "Gran Hermano - Cámara 3", "d": "Cámara exclusiva de la casa.", "m": "https://i.postimg.cc/hjxWkfMf/image.png"},
    {"id": "Simpson", "n": "Los Simpson", "t": "Los Simpson", "d": "Narra las vivencias de una peculiar familia norteamericana.", "m": "https://static.flow.com.ar/images/10105665361/BROWSE/600/600/0/0/10105665361.jpg"},
    {"id": "TRACE.UK", "n": "TRACE UK", "t": "TRACE UK", "d": "The best of national and international artists.", "m": ""},
    {"id": "INFO.FLOW", "n": "FLOW", "t": "Comenzá a usar FLOW", "d": "TV en vivo, películas, series y más.", "m": ""},
    {"id": "Diputados.TV.ARG", "n": "Diputados TV", "t": "Diputados TV", "d": "Información de los Diputados de la Nación.", "m": ""},
    {"id": "Mix.TV", "n": "Mix TV", "t": "Mix TV", "d": "Entretenimiento sin pausa con realities.", "m": ""},
    {"id": "Lapacho.TV", "n": "Lapacho TV", "t": "Lapacho TV", "d": "La pantalla que refleja la identidad formoseña.", "m": ""},
    {"id": "Telesol.San.Juan", "n": "Telesol", "t": "Telesol", "d": "Toda la actualidad sanjuanina.", "m": ""},
    {"id": "Claro.Sports.2", "n": "Claro Sports 2", "t": "Claro Sports 2", "d": "Más acción y más deporte en vivo.", "m": ""},
    {"id": "HBO.Boxing", "n": "HBO Boxing", "t": "HBO Boxing by WBTV", "d": "The home of elite boxing.", "m": ""},
    {"id": "Cazé.TV", "n": "Cazé TV", "t": "Cazé TV", "d": "Esporte com leveza e muita resenha.", "m": ""},
    {"id": "Tigo.Sports.2.PY", "n": "Tigo Sports 2", "t": "Tigo Sports 2", "d": "Viví la emoción del deporte en Tigo Sports.", "m": ""},
    {"id": "Flow.Sports.1", "n": "Flow Sports", "t": "Flow Sports", "d": "La pasión del deporte en Flow.", "m": ""},
    {"id": "Flow.Sports.2", "n": "Flow Sports 2", "t": "Flow Sports 2", "d": "La pasión del deporte en Flow.", "m": ""},
    {"id": "Flow.Sports.3", "n": "Flow Sports 3", "t": "Flow Sports 3", "d": "La pasión del deporte en Flow.", "m": ""},
    {"id": "DM.Kids.TV", "n": "DM Kids TV", "t": "DM Kids TV", "d": "Diversión, imaginación y aventuras.", "m": ""},
    {"id": "ENTFamily.40mediaGroup", "n": "ENT Family", "t": "ENT Family", "d": "Contenido familiar para toda la familia.", "m": ""},
    {"id": "ENTMain.40mediaGroup", "n": "ENT Channel", "t": "ENT Channel", "d": "El equilibrio perfecto de películas.", "m": ""},
    {"id": "TMC.40mediaGroup", "n": "Totalmusic", "t": "Totalmusic", "d": "Ofrecemos la más amplia selección de videoclips.", "m": ""},
    {"id": "TMC80s.40mediaGroup", "n": "Totalmusic 80s", "t": "Totalmusic 80s", "d": "Videoclips de la década dorada.", "m": ""},
    {"id": "TMC2000s.40mediaGroup", "n": "Totalmusic 2000s", "t": "Totalmusic 2000s", "d": "Selección de videoclips de los años 2000.", "m": ""},
    {"id": "TMCConcerts.40mediaGroup", "n": "Totalmusic Concerts", "t": "Totalmusic Concerts", "d": "Conciertos en vivo inolvidables.", "m": ""},
    {"id": "TMCDance.40mediaGroup", "n": "Totalmusic Dance", "t": "Totalmusic Dance", "d": "Música electrónica y dance.", "m": ""},
    {"id": "West.TV.PE", "n": "West TV", "t": "West TV", "d": "Cine del Lejano Oeste.", "m": ""},
    {"id": "Caras.TV", "n": "Caras TV", "t": "Caras TV", "d": "La vida de los famosos y el glamour.", "m": ""},
    {"id": "El.Mueble", "n": "El Mueble", "t": "El Mueble", "d": "Inspiración, diseño y decoración.", "m": ""},
    {"id": "Aunar", "n": "Aunar", "t": "Aunar", "d": "Cultura y contenidos que inspiran.", "m": ""},
    {"id": "Horizons.Wild", "n": "Horizons.Wild", "t": "Horizons.Wild", "d": "Explorá la naturaleza salvaje.", "m": ""},
    {"id": "Viajar", "n": "Viajar", "t": "Viajar", "d": "Descubrí destinos y aventuras.", "m": ""},
    {"id": "Flow.Music.1", "n": "Flow Music", "t": "Flow Music", "d": "La música la vivís en Flow.", "m": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg"},
    {"id": "Flow.Music.2", "n": "Flow Music 2", "t": "Flow Music 2", "d": "La música la vivís en Flow.", "m": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg"},
    {"id": "Flow.Music.3", "n": "Flow Music 3", "t": "Flow Music 3", "d": "La música la vivís en Flow.", "m": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg"},
    {"id": "Flow.Music.4", "n": "Flow Music 4", "t": "Flow Music 4", "d": "La música la vivís en Flow.", "m": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg"}
]

def generar_xml():
    inicio_fijo = datetime.datetime(2026, 2, 23, 0, 0, 0)
    
    lines = []
    lines.append('<?xml version="1.0" encoding="utf-8"?>')
    lines.append('<tv generator-info="EPGCL">')
    
    for c in canales:
        lines.append(f'  <channel id="{c["id"]}">')
        lines.append(f'    <display-name>{c["n"]}</display-name>')
        lines.append('  </channel>')

    for c in canales:
        for d in range(6):
            for h in range(0, 24, 4):
                start_dt = inicio_fijo + datetime.timedelta(days=d, hours=h)
                stop_dt = start_dt + datetime.timedelta(hours=4)
                
                s = start_dt.strftime("%Y%m%d%H%M%S -0300")
                e = stop_dt.strftime("%Y%m%d%H%M%S -0300")
                
                lines.append(f'  <programme start="{s}" stop="{e}" channel="{c["id"]}">')
                lines.append(f'    <title>{c["t"]}</title>')
                lines.append(f'    <desc>{c["d"]}</desc>')
                lines.append(f'    <icon src="{c.get("m")} "/>')
                lines.append('  </programme>')

    lines.append('</tv>')
    
    with open("data_v10.xml", "wb") as f:
        f.write("\r\n".join(lines).encode("utf-8"))
    
    print("Archivo data_v10.xml generado correctamente.")

if __name__ == "__main__":
    generar_xml()
