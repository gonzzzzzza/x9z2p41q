import datetime

canales = [
    {"id": "GH.MULTI", "n": "Multicámara", "t": "GH - Experiencia Multicámara", "g": "Reality", "i": "https://i.postimg.cc/hjxWkfMf/image.png", "d": "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada."},
    {"id": "GH.24HS", "n": "Gran Hermano 24 hs.", "t": "Gran Hermano 24 hs.", "g": "Reality", "i": "https://i.postimg.cc/hjxWkfMf/image.png", "d": "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada."},
    {"id": "GH.CAM1", "n": "Cámara 1", "t": "Gran Hermano - Cámara 1", "g": "Reality", "i": "https://i.postimg.cc/hjxWkfMf/image.png", "d": "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada."},
    {"id": "GH.CAM2", "n": "Cámara 2", "t": "Gran Hermano - Cámara 2", "g": "Reality", "i": "https://i.postimg.cc/hjxWkfMf/image.png", "d": "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada."},
    {"id": "GH.CAM3", "n": "Cámara 3", "t": "Gran Hermano - Cámara 3", "g": "Reality", "i": "https://i.postimg.cc/hjxWkfMf/image.png", "d": "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada."},
    {"id": "Simpson", "n": "Los Simpson", "t": "Los Simpson", "g": "Comedia, Animación", "i": "https://static.flow.com.ar/images/10105665361/BROWSE/600/600/0/0/10105665361.jpg", "d": "Narra las vivencias de una peculiar familia norteamericana conformada por Homero, Marge, Bart, Lisa y Maggie Simpson."},
    {"id": "TRACE.UK", "n": "TRACE UK", "t": "TRACE UK", "g": "Música", "i": "https://cdn.broadbandtvnews.com/wp-content/uploads/2024/07/02103920/Trace-UK.jpg", "d": "TRACE UK brings viewers the very best of national and international artists, playing the hottest music videos."},
    {"id": "INFO.FLOW", "n": "FLOW", "t": "Comenzá a usar FLOW", "g": "Interés general", "i": "https://www.personal.com.py/img/logos/files/flow-color/flow-color.jpg", "d": "En Flow podés disfrutar de TV en vivo, películas, series, deportes, música y mucho más."},
    {"id": "Diputados.TV.ARG", "n": "Diputados TV", "t": "Diputados TV", "g": "Periodístico", "i": "https://static.flow.com.ar/images/10109930827/BROWSE/600/600/0/0/10109930827.jpg", "d": "Toda la información que concierte al trabajo de los Diputados de la Nación."},
    {"id": "Mix.TV", "n": "Mix TV", "t": "Mix TV", "g": "Interés general", "i": "", "d": "Entretenimiento sin pausa con realities, espectáculos, actualidad y contenidos que marcan tendencia."},
    {"id": "Lapacho.TV", "n": "Lapacho TV", "t": "Lapacho TV", "g": "Interés general", "i": "", "d": "La pantalla que refleja la identidad formoseña. Información local, cultura y actualidad."},
    {"id": "Telesol.San.Juan", "n": "Telesol", "t": "Telesol", "g": "Interés general", "i": "https://i.ytimg.cc/vi/BbJo6A888a4/maxresdefault.jpg", "d": "Toda la actualidad sanjuanina en un solo lugar. Noticias y producción local."},
    {"id": "Claro.Sports.2", "n": "Claro Sports 2", "t": "Claro Sports 2", "g": "Deportes", "i": "https://cdn.amxinfra.com/clarosports/images/2024/08/paralimpicos-cs2-133315.jpg", "d": "Más acción, más competencia y más deporte en vivo."},
    {"id": "HBO.Boxing", "n": "HBO Boxing", "t": "HBO Boxing by WBTV", "g": "Boxeo", "i": "https://canvas-lb.tubitv.com/opts/lweaVPhEK4ZaUw==/c68711a9-7ca5-4153-a288-00b76afc4372/CPwDEJ0COgUxLjEuOA==", "d": "The home of elite boxing. World-class fighters."},
    {"id": "Cazé.TV", "n": "Cazé TV", "t": "Cazé TV", "g": "Deportes", "i": "https://mir-s3-cdn-cf.behance.net/projects/404/f02c5b206996309.Y3JvcCw4MTAsNjMzLDAsMA.png", "d": "Esporte com leveza, informação e muita resenha."},
    {"id": "Tigo.Sports.2.PY", "n": "Tigo Sports 2", "t": "Tigo Sports 2", "g": "Deportes", "i": "https://i.postimg.cc/fWrLGTmL/image.png", "d": "Viví la emoción del deporte en Tigo Sports."},
    {"id": "Flow.Sports.1", "n": "Flow Sports", "t": "Flow Sports", "g": "Deportes", "i": "https://static.flow.com.ar/images/10114132674/BROWSE/600/600/0/0/10114132674.jpg", "d": "Viví la pasión del deporte como si estuvieras ahí."},
    {"id": "Flow.Sports.2", "n": "Flow Sports 2", "t": "Flow Sports 2", "g": "Deportes", "i": "https://static.flow.com.ar/images/10114151657/BROWSE/600/600/0/0/10114151657.jpg", "d": "Viví la pasión del deporte como si estuvieras ahí."},
    {"id": "Flow.Sports.3", "n": "Flow Sports 3", "t": "Flow Sports 3", "g": "Deportes", "i": "https://i.postimg.cc/MKsrqNtf/Flow-Sports-3.png", "d": "Viví la pasión del deporte como si estuvieras ahí."},
    {"id": "DM.Kids.TV", "n": "DM Kids TV", "t": "DM Kids TV", "g": "Infantil", "i": "https://i.ytimg.cc/vi/JMbngwxZqZU/maxresdefault.jpg", "d": "Diversión, imaginación y aventuras."},
    {"id": "ENTFamily.40mediaGroup", "n": "ENT Family", "t": "ENT Family", "g": "Películas", "i": "", "d": "Contenido familiar para toda la familia."},
    {"id": "ENTMain.40mediaGroup", "n": "ENT Channel", "t": "ENT Channel", "g": "Películas", "i": "", "d": "El equilibrio perfecto de películas y series."},
    {"id": "TMC.40mediaGroup", "n": "Totalmusic", "t": "Totalmusic", "g": "Música", "i": "https://static.elektamedia.com/ch/tmc_main.png", "d": "Ofrecemos la más amplia selección de videoclips."},
    {"id": "TMC80s.40mediaGroup", "n": "Totalmusic 80s", "t": "Totalmusic 80s", "g": "Música", "i": "https://static.elektamedia.com/ch/tmc_80s.png", "d": "Videoclips de la década dorada de la música."},
    {"id": "TMC2000s.40mediaGroup", "n": "Totalmusic 2000s", "t": "Totalmusic 2000s", "g": "Música", "i": "https://static.elektamedia.com/ch/tmc_00s.png", "d": "Selección de videoclips que marcaron los años 2000."},
    {"id": "TMCConcerts.40mediaGroup", "n": "Totalmusic Concerts", "t": "Totalmusic Concerts", "g": "Música", "i": "https://i.postimg.cc/DzxpBRBC/Totalmusic-Concerts.png", "d": "Selección de conciertos en vivo inolvidables."},
    {"id": "TMCDance.40mediaGroup", "n": "Totalmusic Dance", "t": "Totalmusic Dance", "g": "Música", "i": "https://i.postimg.cc/MG93dgdg/Totalmusic-Dance.png", "d": "Selección vibrante de música electrónica y dance."},
    {"id": "West.TV.PE", "n": "West TV", "t": "West TV", "g": "Películas", "i": "https://i.postimg.cc/C5MT6DLp/West.png", "d": "Cine del Lejano Oeste. Duelos y sheriffs."},
    {"id": "Caras.TV", "n": "Caras TV", "t": "Caras TV", "g": "Interés general", "i": "https://media.canalnet.tv/2024/05/CYaZv3N-1157x720.jpg", "d": "La vida de los famosos y el glamour."},
    {"id": "El.Mueble", "n": "El Mueble", "t": "El Mueble", "g": "Interés general", "i": "", "d": "Inspiración, diseño y decoración."},
    {"id": "Aunar", "n": "Aunar", "t": "Aunar", "g": "Cultura", "i": "", "d": "Cultura, sociedad y contenidos que inspiran."},
    {"id": "Horizons.Wild", "n": "Horizons.Wild", "t": "Horizons.Wild", "g": "Naturaleza", "i": "", "d": "Explorá la naturaleza en su estado más puro."},
    {"id": "Viajar", "n": "Viajar", "t": "Viajar", "g": "Viajes", "i": "", "d": "Descubrí destinos, culturas y aventuras."},
    {"id": "Flow.Music.1", "n": "Flow Music", "t": "Flow Music", "g": "Música", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "d": "La música la vivís en Flow."},
    {"id": "Flow.Music.2", "n": "Flow Music 2", "t": "Flow Music 2", "g": "Música", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "d": "La música la vivís en Flow."},
    {"id": "Flow.Music.3", "n": "Flow Music 3", "t": "Flow Music 3", "g": "Música", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "d": "La música la vivís en Flow."},
    {"id": "Flow.Music.4", "n": "Flow Music 4", "t": "Flow Music 4", "g": "Música", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "d": "La música la vivís en Flow."},
    {"id": "Billboard.AR", "n": "Billboard", "t": "Billboard", "g": "Música", "i": "", "d": "Lo último en música, charts y artistas."},
    {"id": "Deluxe.Music.Wintertime", "n": "Deluxe Music Wintertime", "t": "Deluxe Music Wintertime", "g": "Música", "i": "", "d": "Música para disfrutar el invierno."},
    {"id": "El.Folclorico", "n": "El Folclórico", "t": "El Folclórico", "g": "Música", "i": "", "d": "Raíces y tradición del folclore."},
    {"id": "Hit.TV", "n": "Hit TV", "t": "Hit TV", "g": "Música", "i": "", "d": "Los éxitos musicales más sonados."},
    {"id": "FMH.Kizzi", "n": "FMH Kizzi", "t": "FMH Kizzi", "g": "Música", "i": "", "d": "Ritmo y lanzamientos actuales."},
    {"id": "Music.Box.Classic", "n": "Music Box Classic", "t": "Music Box Classic", "g": "Música", "i": "https://www.digitalfernsehen.de/wp-content/uploads/2025/12/Music-Box-Classic.jpg", "d": "Los clásicos que nunca pasan de moda."},
    {"id": "Music.Box.Dance", "n": "Music Box Dance", "t": "Music Box Dance", "g": "Música", "i": "https://www.digitalfernsehen.de/wp-content/uploads/2025/12/Music-Box-Dance.jpg", "d": "Ritmo, energía y beats."},
    {"id": "Music.Box.Hits", "n": "Music Box Hits", "t": "Music Box Hits", "g": "Música", "i": "https://www.digitalfernsehen.de/wp-content/uploads/2025/12/Music-Box-Hits.jpg", "d": "Temas más escuchados del momento."},
    {"id": "Music.Box.Sexy", "n": "Music Box Sexy", "t": "Music Box Sexy", "g": "Música", "i": "https://www.parabola.cz/img_magazin/2025/music-box-sexy.jpg", "d": "Vibras sensuales y lounge."},
    {"id": "Musictop", "n": "Musictop", "t": "Musictop", "g": "Música", "i": "", "d": "Top charts y éxitos globales."},
    {"id": "Vorterix", "n": "Vorterix", "t": "Vorterix", "g": "Música", "i": "https://static.flow.com.ar/images/10114219640/BROWSE/600/600/0/0/10114219640.jpg", "d": "Pionero en streaming y radio FM."},
    {"id": "Radio.Maria", "n": "Radio María", "t": "Radio María", "g": "Religión", "i": "", "d": "Espiritualidad y oración."},
    {"id": "Santa.Maria", "n": "Santa María", "t": "Santa María", "g": "Religión", "i": "", "d": "Contenido religioso y formación."},
    {"id": "Solidaria.TV", "n": "Solidaria TV", "t": "Solidaria TV", "g": "Religión", "i": "", "d": "Ayuda y compromiso social."},
    {"id": "Latam.Rural", "n": "Latam Rural", "t": "Latam Rural", "g": "Agro", "i": "", "d": "Todo el mundo agro."},
    {"id": "BBB.MULTI", "n": "BBB Multicâmera", "t": "BBB Multicâmera", "g": "Reality", "i": "https://dominiopop.com.br/wp-content/uploads/2025/12/logo-bbb.jpg", "d": "Acompanhe tudo em tempo real."},
    {"id": "BBB.CAM1", "n": "BBB Câmera 1", "t": "BBB Câmera 1", "g": "Reality", "i": "https://dominiopop.com.br/wp-content/uploads/2025/12/logo-bbb.jpg", "d": "Acompanhe tudo em tempo real."},
    {"id": "BBB.CAM2", "n": "BBB Câmera 2", "t": "BBB Câmera 2", "g": "Reality", "i": "https://dominiopop.com.br/wp-content/uploads/2025/12/logo-bbb.jpg", "d": "Acompanhe tudo em tempo real."},
    {"id": "VTV.URUGUAY", "n": "VTV", "t": "VTV Uruguay", "g": "Interés general", "i": "https://i.postimg.cc/Y0Sncxc9/vtv.jpg", "d": "Noticias y actualidad de Uruguay."},
    {"id": "Noticias.Caracol", "n": "Noticias Caracol", "t": "Noticias Caracol", "g": "Noticias", "i": "https://i.postimg.cc/HxLYNfLz/image.png", "d": "La información con análisis."},
    {"id": "Radio.Cosquin.Rock", "n": "Radio Cosquín Rock", "t": "Cosquín Rock", "g": "Radios", "i": "https://static.mytuner.mobi/media/tvos_radios/053/cosquin-rock-fm.71fd78e3.png", "d": "El rock argentino suena fuerte."},
    {"id": "Radio.Del.Plata", "n": "Radio Del Plata", "t": "Radio Del Plata", "g": "Radios", "i": "", "d": "Música y noticias."},
    {"id": "Radio.Disney", "n": "Radio Disney", "t": "Radio Disney", "g": "Radios", "i": "", "d": "Hits para la familia."},
    {"id": "Radio.La.Red", "n": "Radio La Red", "t": "Radio La Red", "g": "Radios", "i": "", "d": "Actualidad y noticias."},
    {"id": "Radio.Latina", "n": "Radio Latina", "t": "Radio Latina", "g": "Radios", "i": "", "d": "Éxitos en español."},
    {"id": "Radio.Los.40", "n": "Radio Los 40", "t": "Radio Los 40", "g": "Radios", "i": "", "d": "Hits del momento pop."},
    {"id": "Radio.Mega", "n": "Radio Mega", "t": "Radio Mega", "g": "Radios", "i": "", "d": "Música y diversión."},
    {"id": "Radio.Nacional.Clasica", "n": "Radio Nacional Clásica", "t": "Nacional Clásica", "g": "Radios", "i": "", "d": "Música clásica."},
    {"id": "Radio.Nacional.Folclorica", "n": "Radio Nacional Folclórica", "t": "Nacional Folclórica", "g": "Radios", "i": "", "d": "Tradición argentina."},
    {"id": "Radio.Nacional.Rock", "n": "Radio Nacional Rock", "t": "Nacional Rock", "g": "Radios", "i": "", "d": "Rock nacional e internacional."},
    {"id": "Radio.La.Popu", "n": "Radio La Popu", "t": "La Popu", "g": "Radios", "i": "", "d": "Música popular."},
    {"id": "Radio.Rivadavia", "n": "Radio Rivadavia", "t": "Radio Rivadavia", "g": "Radios", "i": "", "d": "Noticias y opinión."},
    {"id": "Radio.Rock.and.Pop", "n": "Radio Rock & Pop", "t": "Rock & Pop", "g": "Radios", "i": "", "d": "Todo el rock y pop."},
    {"id": "Radio.Vida", "n": "Radio Vida", "t": "Radio Vida", "g": "Radios", "i": "", "d": "Música variada."}
]

def generar_xml():
    now = datetime.datetime.now()
    inicio = now.replace(minute=0, second=0, microsecond=0)

    lines = []
    lines.append('<?xml version="1.0" encoding="utf-8"?>')
    lines.append('<tv generator-info="EPGCL">')

    # Canales (sin iconos)
    for c in canales:
        lines.append(f'  <channel id="{c["id"]}">')
        lines.append(f'    <display-name>{c["n"]}</display-name>')
        lines.append('  </channel>')

    # Programación 3h
    horas_total = 72

    for c in canales:
        t = inicio
        for _ in range(int(horas_total / 3)):
            stop = t + datetime.timedelta(hours=3)

            s = t.strftime("%Y%m%d%H%M%S -0300")
            e = stop.strftime("%Y%m%d%H%M%S -0300")

            lines.append(f'  <programme start="{s}" stop="{e}" channel="{c["id"]}">')
            lines.append(f'    <title>{c["t"]}</title>')
            lines.append(f'    <desc>{c["d"]}</desc>')
            lines.append(f'    <category>{c["g"]}</category>')
            if c["i"]:
                lines.append(f'    <icon src="{c["i"]}" />')
            lines.append('  </programme>')

            t = stop

    lines.append('</tv>')

    with open("data.xml", "wb") as f:
        f.write("\n".join(lines).encode("utf-8"))

    print("data.xml generado correctamente")

if __name__ == "__main__":
    generar_xml()
