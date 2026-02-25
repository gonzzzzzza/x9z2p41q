import datetime

# CONFIGURACIÓN DE LOS 71 CANALES
# 'i' es el logo del canal, 'm' es la miniatura del programa
canales = [
    {"id": "GH.MULTI", "n": "Multicámara", "t": "GH - Experiencia Multicámara", "d": "La casa más famosa del país vuelve a abrir sus puertas.", "m": "https://i.postimg.cc/hjxWkfMf/image.png"},
    {"id": "GH.24HS", "n": "Gran Hermano 24 hs.", "t": "Gran Hermano 24 hs.", "d": "La casa más famosa del país en vivo.", "m": "https://i.postimg.cc/hjxWkfMf/image.png"},
    {"id": "GH.CAM1", "n": "Cámara 1", "t": "Gran Hermano - Cámara 1", "d": "Cámara exclusiva de la casa.", "m": "https://i.postimg.cc/hjxWkfMf/image.png"},
    {"id": "GH.CAM2", "n": "Cámara 2", "t": "Gran Hermano - Cámara 2", "d": "Cámara exclusiva de la casa.", "m": "https://i.postimg.cc/hjxWkfMf/image.png"},
    {"id": "GH.CAM3", "n": "Cámara 3", "t": "Gran Hermano - Cámara 3", "d": "Cámara exclusiva de la casa.", "m": "https://i.postimg.cc/hjxWkfMf/image.png"},
    {"id": "Simpson", "n": "Los Simpson", "t": "Los Simpson", "d": "Narra las vivencias de una peculiar familia norteamericana.", "m": "https://static.flow.com.ar/images/10105665361/BROWSE/600/600/0/0/10105665361.jpg"},
    {"id": "TRACE.UK", "n": "TRACE UK", "t": "TRACE UK", "d": "The best of national and international artists.", "i": "https://cdn.broadbandtvnews.com/wp-content/uploads/2024/07/02103920/Trace-UK.jpg", "m": ""},
    {"id": "INFO.FLOW", "n": "FLOW", "t": "Comenzá a usar FLOW", "d": "TV en vivo, películas, series y más.", "i": "https://www.personal.com.py/img/logos/files/flow-color/flow-color.jpg", "m": ""},
    {"id": "Diputados.TV.ARG", "n": "Diputados TV", "t": "Diputados TV", "d": "Información de los Diputados de la Nación.", "i": "https://static.flow.com.ar/images/10109930827/BROWSE/600/600/0/0/10109930827.jpg", "m": ""},
    {"id": "Mix.TV", "n": "Mix TV", "t": "Mix TV", "d": "Entretenimiento sin pausa con realities.", "i": "", "m": ""},
    {"id": "Lapacho.TV", "n": "Lapacho TV", "t": "Lapacho TV", "d": "La pantalla que refleja la identidad formoseña.", "i": "", "m": ""},
    {"id": "Telesol.San.Juan", "n": "Telesol", "t": "Telesol", "d": "Toda la actualidad sanjuanina.", "i": "https://i.ytimg.cc/vi/BbJo6A888a4/maxresdefault.jpg", "m": ""},
    {"id": "Claro.Sports.2", "n": "Claro Sports 2", "t": "Claro Sports 2", "d": "Más acción y más deporte en vivo.", "i": "https://cdn.amxinfra.com/clarosports/images/2024/08/paralimpicos-cs2-133315.jpg", "m": ""},
    {"id": "HBO.Boxing", "n": "HBO Boxing", "t": "HBO Boxing by WBTV", "d": "The home of elite boxing.", "i": "https://canvas-lb.tubitv.com/opts/lweaVPhEK4ZaUw==/c68711a9-7ca5-4153-a288-00b76afc4372/CPwDEJ0COgUxLjEuOA==", "m": ""},
    {"id": "Cazé.TV", "n": "Cazé TV", "t": "Cazé TV", "d": "Esporte com leveza e muita resenha.", "i": "https://mir-s3-cdn-cf.behance.net/projects/404/f02c5b206996309.Y3JvcCw4MTAsNjMzLDAsMA.png", "m": ""},
    {"id": "Tigo.Sports.2.PY", "n": "Tigo Sports 2", "t": "Tigo Sports 2", "d": "Viví la emoción del deporte en Tigo Sports.", "i": "https://i.postimg.cc/fWrLGTmL/image.png", "m": ""},
    {"id": "Flow.Sports.1", "n": "Flow Sports", "t": "Flow Sports", "d": "La pasión del deporte en Flow.", "i": "https://static.flow.com.ar/images/10114132674/BROWSE/600/600/0/0/10114132674.jpg", "m": ""},
    {"id": "Flow.Sports.2", "n": "Flow Sports 2", "t": "Flow Sports 2", "d": "La pasión del deporte en Flow.", "i": "https://static.flow.com.ar/images/10114151657/BROWSE/600/600/0/0/10114151657.jpg", "m": ""},
    {"id": "Flow.Sports.3", "n": "Flow Sports 3", "t": "Flow Sports 3", "d": "La pasión del deporte en Flow.", "i": "https://i.postimg.cc/MKsrqNtf/Flow-Sports-3.png", "m": ""},
    {"id": "DM.Kids.TV", "n": "DM Kids TV", "t": "DM Kids TV", "d": "Diversión, imaginación y aventuras.", "i": "https://i.ytimg.cc/vi/JMbngwxZqZU/maxresdefault.jpg", "m": ""},
    {"id": "ENTFamily.40mediaGroup", "n": "ENT Family", "t": "ENT Family", "d": "Contenido familiar para toda la familia.", "i": "", "m": ""},
    {"id": "ENTMain.40mediaGroup", "n": "ENT Channel", "t": "ENT Channel", "d": "El equilibrio perfecto de películas.", "i": "", "m": ""},
    {"id": "TMC.40mediaGroup", "n": "Totalmusic", "t": "Totalmusic", "d": "Ofrecemos la más amplia selección de videoclips.", "i": "https://static.elektamedia.com/ch/tmc_main.png", "m": ""},
    {"id": "TMC80s.40mediaGroup", "n": "Totalmusic 80s", "t": "Totalmusic 80s", "d": "Videoclips de la década dorada.", "i": "https://static.elektamedia.com/ch/tmc_80s.png", "m": ""},
    {"id": "TMC2000s.40mediaGroup", "n": "Totalmusic 2000s", "t": "Totalmusic 2000s", "d": "Selección de videoclips de los años 2000.", "i": "https://static.elektamedia.com/ch/tmc_00s.png", "m": ""},
    {"id": "TMCConcerts.40mediaGroup", "n": "Totalmusic Concerts", "t": "Totalmusic Concerts", "d": "Conciertos en vivo inolvidables.", "i": "https://i.postimg.cc/DzxpBRBC/Totalmusic-Concerts.png", "m": ""},
    {"id": "TMCDance.40mediaGroup", "n": "Totalmusic Dance", "t": "Totalmusic Dance", "d": "Música electrónica y dance.", "i": "https://i.postimg.cc/MG93dgdg/Totalmusic-Dance.png", "m": ""},
    {"id": "West.TV.PE", "n": "West TV", "t": "West TV", "d": "Cine del Lejano Oeste.", "i": "https://i.postimg.cc/C5MT6DLp/West.png", "m": ""},
    {"id": "Caras.TV", "n": "Caras TV", "t": "Caras TV", "d": "La vida de los famosos y el glamour.", "i": "https://media.canalnet.tv/2024/05/CYaZv3N-1157x720.jpg", "m": ""},
    {"id": "El.Mueble", "n": "El Mueble", "t": "El Mueble", "d": "Inspiración, diseño y decoración.", "i": "", "m": ""},
    {"id": "Aunar", "n": "Aunar", "t": "Aunar", "d": "Cultura y contenidos que inspiran.", "i": "", "m": ""},
    {"id": "Horizons.Wild", "n": "Horizons.Wild", "t": "Horizons.Wild", "d": "Explorá la naturaleza salvaje.", "i": "", "m": ""},
    {"id": "Viajar", "n": "Viajar", "t": "Viajar", "d": "Descubrí destinos y aventuras.", "i": "", "m": ""},
    {"id": "Flow.Music.1", "n": "Flow Music", "t": "Flow Music", "d": "La música la vivís en Flow.", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "m": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg"},
    {"id": "Flow.Music.2", "n": "Flow Music 2", "t": "Flow Music 2", "d": "La música la vivís en Flow.", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "m": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg"},
    {"id": "Flow.Music.3", "n": "Flow Music 3", "t": "Flow Music 3", "d": "La música la vivís en Flow.", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "m": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg"},
    {"id": "Flow.Music.4", "n": "Flow Music 4", "t": "Flow Music 4", "d": "La música la vivís en Flow.", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "m": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg"},
    {"id": "Billboard.AR", "n": "Billboard", "t": "Billboard", "d": "Lo último en música y charts.", "i": "", "m": ""},
    {"id": "Deluxe.Music.Wintertime", "n": "Deluxe Music Wintertime", "t": "Deluxe Music Wintertime", "d": "Música para el invierno.", "i": "", "m": ""},
    {"id": "El.Folclorico", "n": "El Folclórico", "t": "El Folclórico", "d": "Raíces y tradición del folclore.", "i": "", "m": ""},
    {"id": "Hit.TV", "n": "Hit TV", "t": "Hit TV", "d": "Los éxitos musicales más sonados.", "i": "", "m": ""},
    {"id": "FMH.Kizzi", "n": "FMH Kizzi", "t": "FMH Kizzi", "d": "Ritmo y lanzamientos actuales.", "i": "", "m": ""},
    {"id": "Music.Box.Classic", "n": "Music Box Classic", "t": "Music Box Classic", "d": "Los clásicos que nunca pasan de moda.", "i": "https://www.digitalfernsehen.de/wp-content/uploads/2025/12/Music-Box-Classic.jpg", "m": ""},
    {"id": "Music.Box.Dance", "n": "Music Box Dance", "t": "Music Box Dance", "d": "Ritmo, energía y beats.", "i": "https://www.digitalfernsehen.de/wp-content/uploads/2025/12/Music-Box-Dance.jpg", "m": ""},
    {"id": "Music.Box.Hits", "n": "Music Box Hits", "t": "Music Box Hits", "d": "Temas más escuchados del momento.", "i": "https://www.digitalfernsehen.de/wp-content/uploads/2025/12/Music-Box-Hits.jpg", "m": ""},
    {"id": "Music.Box.Sexy", "n": "Music Box Sexy", "t": "Music Box Sexy", "d": "Vibras sensuales y lounge.", "i": "https://www.parabola.cz/img_magazin/2025/music-box-sexy.jpg", "m": ""},
    {"id": "Musictop", "n": "Musictop", "t": "Musictop", "d": "Top charts e éxitos globais.", "i": "", "m": ""},
    {"id": "Vorterix", "n": "Vorterix", "t": "Vorterix", "d": "Pionero en streaming y radio FM.", "i": "https://static.flow.com.ar/images/10114219640/BROWSE/600/600/0/0/10114219640.jpg", "m": ""},
    {"id": "Radio.Maria", "n": "Radio María", "t": "Radio María", "d": "Espiritualidad y oración.", "i": "", "m": ""},
    {"id": "Santa.Maria", "n": "Santa María", "t": "Santa María", "d": "Contenido religioso y formación.", "i": "", "m": ""},
    {"id": "Solidaria.TV", "n": "Solidaria TV", "t": "Solidaria TV", "d": "Ayuda y compromiso social.", "i": "", "m": ""},
    {"id": "Latam.Rural", "n": "Latam Rural", "t": "Latam Rural", "d": "Todo el mundo agro.", "i": "", "m": ""},
    {"id": "BBB.MULTI", "n": "BBB Multicâmera", "t": "BBB Multicâmera", "d": "Acompanhe tudo em tempo real.", "i": "https://dominiopop.com.br/wp-content/uploads/2025/12/logo-bbb.jpg", "m": ""},
    {"id": "BBB.CAM1", "n": "BBB Câmera 1", "t": "BBB Câmera 1", "d": "Acompanhe tudo em tempo real.", "i": "https://dominiopop.com.br/wp-content/uploads/2025/12/logo-bbb.jpg", "m": ""},
    {"id": "BBB.CAM2", "n": "BBB Câmera 2", "t": "BBB Câmera 2", "d": "Acompanhe tudo em tempo real.", "i": "https://dominiopop.com.br/wp-content/uploads/2025/12/logo-bbb.jpg", "m": ""},
    {"id": "VTV.URUGUAY", "n": "VTV", "t": "VTV Uruguay", "d": "Noticias y actualidad de Uruguay.", "i": "https://i.postimg.cc/Y0Sncxc9/vtv.jpg", "m": ""},
    {"id": "Noticias.Caracol", "n": "Noticias Caracol", "t": "Noticias Caracol", "d": "La información con análisis.", "i": "https://i.postimg.cc/HxLYNfLz/image.png", "m": ""},
    {"id": "Radio.Cosquin.Rock", "n": "Radio Cosquín Rock", "t": "Cosquín Rock", "d": "El rock argentino suena fuerte.", "i": "https://static.mytuner.mobi/media/tvos_radios/053/cosquin-rock-fm.71fd78e3.png", "m": ""},
    {"id": "Radio.Del.Plata", "n": "Radio Del Plata", "t": "Radio Del Plata", "d": "Música y noticias.", "i": "", "m": ""},
    {"id": "Radio.Disney", "n": "Radio Disney", "t": "Radio Disney", "d": "Hits para la familia.", "i": "", "m": ""},
    {"id": "Radio.La.Red", "n": "Radio La Red", "t": "Radio La Red", "d": "Actualidad y noticias.", "i": "", "m": ""},
    {"id": "Radio.Latina", "n": "Radio Latina", "t": "Radio Latina", "d": "Éxitos en español.", "i": "", "m": ""},
    {"id": "Radio.Los.40", "n": "Radio Los 40", "t": "Radio Los 40", "d": "Hits del momento pop.", "i": "", "m": ""},
    {"id": "Radio.Mega", "n": "Radio Mega", "t": "Radio Mega", "d": "Música y diversión.", "i": "", "m": ""},
    {"id": "Radio.Nacional.Clasica", "n": "Radio Nacional Clásica", "t": "Nacional Clásica", "d": "Música clásica.", "i": "", "m": ""},
    {"id": "Radio.Nacional.Folclorica", "n": "Radio Nacional Folclórica", "t": "Nacional Folclórica", "d": "Tradición argentina.", "i": "", "m": ""},
    {"id": "Radio.Nacional.Rock", "n": "Radio Nacional Rock", "t": "Nacional Rock", "d": "Rock nacional e internacional.", "i": "", "m": ""},
    {"id": "Radio.La.Popu", "n": "Radio La Popu", "t": "La Popu", "d": "Música popular.", "i": "", "m": ""},
    {"id": "Radio.Rivadavia", "n": "Radio Rivadavia", "t": "Radio Rivadavia", "d": "Noticias y opinión.", "i": "", "m": ""},
    {"id": "Radio.Rock.and.Pop", "n": "Radio Rock & Pop", "t": "Rock & Pop", "d": "Todo el rock y pop.", "i": "", "m": ""},
    {"id": "Radio.Vida", "n": "Radio Vida", "t": "Radio Vida", "d": "Música variada.", "i": "", "m": ""},
]

def generar_xml():
    # INICIO: 23 DE FEBRERO
    inicio_fijo = datetime.datetime(2026, 2, 23, 0, 0, 0)
    
    lines = []
    lines.append('<?xml version="1.0" encoding="utf-8"?>')
    lines.append('<tv generator-info="EPGCL">')
    
    # SECCIÓN CHANNEL
    for c in canales:
        lines.append(f'  <channel id="{c["id"]}">')
        lines.append(f'    <display-name>{c["n"]}</display-name>')
        lines.append('  </channel>')

    # SECCIÓN PROGRAMME (Miniatura siempre incluida)
    # Orden exacto: start -> stop -> channel
    for c in canales:
        for d in range(6): # 6 días
            for h in range(0, 24, 4): # Bloques de 4 horas
                start_dt = inicio_fijo + datetime.timedelta(days=d, hours=h)
                stop_dt = start_dt + datetime.timedelta(hours=4)
                
                s = start_dt.strftime("%Y%m%d%H%M%S -0300")
                e = stop_dt.strftime("%Y%m%d%H%M%S -0300")
                
                lines.append(f'  <programme start="{s}" stop="{e}" channel="{c["id"]}">')
                lines.append(f'    <title>{c["t"]}</title>')
                lines.append(f'    <desc>{c["d"]}</desc>')
                # FORZADO: La línea de icon siempre se escribe
                lines.append(f'    <icon src="{c.get("m")}" />')
                lines.append('  </programme>')

    lines.append('</tv>')
    
    # Escribir el archivo
    with open("data_v10.xml", "wb") as f:
        f.write("\r\n".join(lines).encode("utf-8"))
    
    print("Archivo data_v10.xml generado correctamente con miniaturas forzadas.")

if __name__ == "__main__":
    generar_xml()
