from datetime import datetime, timedelta

# LISTA COMPLETA DE 71 CANALES
canales = [
    {"id": "GH.MULTI", "n": "Multicámara", "t": "GH - Experiencia Multicámara", "g": "Reality", "i": "https://i.postimg.cc/hjxWkfMf/image.png", "d": "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada."},
    {"id": "GH.24HS", "n": "Gran Hermano 24 hs.", "t": "Gran Hermano 24 hs.", "g": "Reality", "i": "https://i.postimg.cc/hjxWkfMf/image.png", "d": "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada."},
    {"id": "GH.CAM1", "n": "Cámara 1", "t": "Gran Hermano - Cámara 1", "g": "Reality", "i": "https://i.postimg.cc/hjxWkfMf/image.png", "d": "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada."},
    {"id": "GH.CAM2", "n": "Cámara 2", "t": "Gran Hermano - Cámara 2", "g": "Reality", "i": "https://i.postimg.cc/hjxWkfMf/image.png", "d": "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada."},
    {"id": "GH.CAM3", "n": "Cámara 3", "t": "Gran Hermano - Cámara 3", "g": "Reality", "i": "https://i.postimg.cc/hjxWkfMf/image.png", "d": "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada."},
    {"id": "Simpson", "n": "Los Simpson", "t": "Los Simpson", "g": "Comedia, Animación", "i": "https://static.flow.com.ar/images/10105665361/BROWSE/600/600/0/0/10105665361.jpg", "d": "Narra las vivencias de una peculiar familia norteamericana."},
    {"id": "TRACE.UK", "n": "TRACE UK", "t": "TRACE UK", "g": "Música", "i": "https://cdn.broadbandtvnews.com/wp-content/uploads/2024/07/02103920/Trace-UK.jpg", "d": "TRACE UK brings viewers the very best of national and international artists."},
    {"id": "INFO.FLOW", "n": "FLOW", "t": "Comenzá a usar FLOW", "g": "Interés general", "i": "https://www.personal.com.py/img/logos/files/flow-color/flow-color.jpg", "d": "En Flow podés disfrutar de TV en vivo, películas, series y más."},
    {"id": "Diputados.TV.ARG", "n": "Diputados TV", "t": "Diputados TV", "g": "Periodístico", "i": "https://static.flow.com.ar/images/10109930827/BROWSE/600/600/0/0/10109930827.jpg", "d": "Trabajo de los Diputados de la Nación."},
    {"id": "Mix.TV", "n": "Mix TV", "t": "Mix TV", "g": "Interés general", "i": "", "d": "Entretenimiento sin pausa con realities y actualidad."},
    {"id": "Lapacho.TV", "n": "Lapacho TV", "t": "Lapacho TV", "g": "Interés general", "i": "", "d": "La pantalla que refleja la identidad formoseña."},
    {"id": "Telesol.San.Juan", "n": "Telesol", "t": "Telesol", "g": "Interés general", "i": "https://i.ytimg.cc/vi/BbJo6A888a4/maxresdefault.jpg", "d": "Toda la actualidad sanjuanina."},
    {"id": "Claro.Sports.2", "n": "Claro Sports 2", "t": "Claro Sports 2", "g": "Deportes", "i": "https://cdn.amxinfra.com/clarosports/images/2024/08/paralimpicos-cs2-133315.jpg", "d": "Más acción y deporte en vivo."},
    {"id": "HBO.Boxing", "n": "HBO Boxing", "t": "HBO Boxing by WBTV", "g": "Boxeo", "i": "https://canvas-lb.tubitv.com/opts/lweaVPhEK4ZaUw==/c68711a9-7ca5-4153-a288-00b76afc4372/CPwDEJ0COgUxLjEuOA==", "d": "The home of elite boxing."},
    {"id": "Cazé.TV", "n": "Cazé TV", "t": "Cazé TV", "g": "Deportes", "i": "https://mir-s3-cdn-cf.behance.net/projects/404/f02c5b206996309.Y3JvcCw4MTAsNjMzLDAsMA.png", "d": "Esporte com leveza e muita resenha."},
    {"id": "Tigo.Sports.2.PY", "n": "Tigo Sports 2", "t": "Tigo Sports 2", "g": "Deportes", "i": "https://i.postimg.cc/fWrLGTmL/image.png", "d": "Viví la emoción del deporte."},
    {"id": "Flow.Sports.1", "n": "Flow Sports", "t": "Flow Sports", "g": "Deportes", "i": "https://static.flow.com.ar/images/10114132674/BROWSE/600/600/0/0/10114132674.jpg", "d": "Viví la pasión del deporte."},
    {"id": "Flow.Sports.2", "n": "Flow Sports 2", "t": "Flow Sports 2", "g": "Deportes", "i": "https://static.flow.com.ar/images/10114151657/BROWSE/600/600/0/0/10114151657.jpg", "d": "Viví la pasión del deporte."},
    {"id": "Flow.Sports.3", "n": "Flow Sports 3", "t": "Flow Sports 3", "g": "Deportes", "i": "https://i.postimg.cc/MKsrqNtf/Flow-Sports-3.png", "d": "Viví la pasión del deporte."},
    {"id": "DM.Kids.TV", "n": "DM Kids TV", "t": "DM Kids TV", "g": "Infantil", "i": "https://i.ytimg.cc/vi/JMbngwxZqZU/maxresdefault.jpg", "d": "Diversión y aventuras para aprender jugando."},
    {"id": "ENTFamily.40mediaGroup", "n": "ENT Family", "t": "ENT Family", "g": "Películas", "i": "", "d": "Contenido familiar seguro las 24 horas."},
    {"id": "ENTMain.40mediaGroup", "n": "ENT Channel", "t": "ENT Channel", "g": "Películas", "i": "", "d": "Películas y series que marcaron generaciones."},
    {"id": "TMC.40mediaGroup", "n": "Totalmusic", "t": "Totalmusic", "g": "Música", "i": "https://static.elektamedia.com/ch/tmc_main.png", "d": "Videoclips de todos los géneros."},
    {"id": "TMC80s.40mediaGroup", "n": "Totalmusic 80s", "t": "Totalmusic 80s", "g": "Música", "i": "https://static.elektamedia.com/ch/tmc_80s.png", "d": "Música de la década dorada."},
    {"id": "TMC2000s.40mediaGroup", "n": "Totalmusic 2000s", "t": "Totalmusic 2000s", "g": "Música", "i": "https://static.elektamedia.com/ch/tmc_00s.png", "d": "Videoclips que marcaron los años 2000."},
    {"id": "TMCConcerts.40mediaGroup", "n": "Totalmusic Concerts", "t": "Totalmusic Concerts", "g": "Música", "i": "https://i.postimg.cc/DzxpBRBC/Totalmusic-Concerts.png", "d": "Conciertos en vivo inolvidables."},
    {"id": "TMCDance.40mediaGroup", "n": "Totalmusic Dance", "t": "Totalmusic Dance", "g": "Música", "i": "https://i.postimg.cc/MG93dgdg/Totalmusic-Dance.png", "d": "Música electrónica y dance."},
    {"id": "West.TV.PE", "n": "West TV", "t": "West TV", "g": "Películas", "i": "https://i.postimg.cc/C5MT6DLp/West.png", "d": "Cine del Lejano Oeste."},
    {"id": "Caras.TV", "n": "Caras TV", "t": "Caras TV", "g": "Interés general", "i": "https://media.canalnet.tv/2024/05/CYaZv3N-1157x720.jpg", "d": "Vida de famosos y glamour."},
    {"id": "El.Mueble", "n": "El Mueble", "t": "El Mueble", "g": "Interés general", "i": "", "d": "Inspiración y diseño para tu hogar."},
    {"id": "Aunar", "n": "Aunar", "t": "Aunar", "g": "Cultura", "i": "", "d": "Cultura y sociedad."},
    {"id": "Horizons.Wild", "n": "Horizons.Wild", "t": "Horizons.Wild", "g": "Naturaleza", "i": "", "d": "Documentales de fauna."},
    {"id": "Viajar", "n": "Viajar", "t": "Viajar", "g": "Viajes", "i": "", "d": "Descubrí destinos y culturas."},
    {"id": "Flow.Music.1", "n": "Flow Music", "t": "Flow Music", "g": "Música", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "d": "Shows en vivo y más."},
    {"id": "Flow.Music.2", "n": "Flow Music 2", "t": "Flow Music 2", "g": "Música", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "d": "Shows en vivo y más."},
    {"id": "Flow.Music.3", "n": "Flow Music 3", "t": "Flow Music 3", "g": "Música", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "d": "Shows en vivo y más."},
    {"id": "Flow.Music.4", "n": "Flow Music 4", "t": "Flow Music 4", "g": "Música", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "d": "Shows en vivo y más."},
    {"id": "Billboard.AR", "n": "Billboard", "t": "Billboard", "g": "Música", "i": "", "d": "Lo último en música y charts."},
    {"id": "Deluxe.Music.Wintertime", "n": "Deluxe Music Wintertime", "t": "Deluxe Music Wintertime", "g": "Música", "i": "", "d": "Música para disfrutar en invierno."},
    {"id": "El.Folclorico", "n": "El Folclórico", "t": "El Folclórico", "g": "Música", "i": "", "d": "Raíces y tradición del folclore."},
    {"id": "Hit.TV", "n": "Hit TV", "t": "Hit TV", "g": "Música", "i": "", "d": "Los éxitos musicales más sonados."},
    {"id": "FMH.Kizzi", "n": "FMH Kizzi", "t": "FMH Kizzi", "g": "Música", "i": "", "d": "Ritmo y frescura musical."},
    {"id": "Music.Box.Classic", "n": "Music Box Classic", "t": "Music Box Classic", "g": "Música", "i": "https://www.digitalfernsehen.de/wp-content/uploads/2025/12/Music-Box-Classic.jpg", "d": "Clásicos que nunca pasan de moda."},
    {"id": "Music.Box.Dance", "n": "Music Box Dance", "t": "Music Box Dance", "g": "Música", "i": "https://www.digitalfernsehen.de/wp-content/uploads/2025/12/Music-Box-Dance.jpg", "d": "Ritmo y beats de energía."},
    {"id": "Music.Box.Hits", "n": "Music Box Hits", "t": "Music Box Hits", "g": "Música", "i": "https://www.digitalfernsehen.de/wp-content/uploads/2025/12/Music-Box-Hits.jpg", "d": "Temas más escuchados del momento."},
    {"id": "Music.Box.Sexy", "n": "Music Box Sexy", "t": "Music Box Sexy", "g": "Música", "i": "https://www.parabola.cz/img_magazin/2025/music-box-sexy.jpg", "d": "Vibras sensuales y lounge."},
    {"id": "Musictop", "n": "Musictop", "t": "Musictop", "g": "Música", "i": "", "d": "Top charts y éxitos globales."},
    {"id": "Vorterix", "n": "Vorterix", "t": "Vorterix", "g": "Música", "i": "https://static.flow.com.ar/images/10114219640/BROWSE/600/600/0/0/10114219640.jpg", "d": "Streaming y radio FM."},
    {"id": "Radio.Maria", "n": "Radio María", "t": "Radio María", "g": "Religión", "i": "", "d": "Espiritualidad y oración."},
    {"id": "Santa.Maria", "n": "Santa María", "t": "Santa María", "g": "Religión", "i": "", "d": "Contenido religioso."},
    {"id": "Solidaria.TV", "n": "Solidaria TV", "t": "Solidaria TV", "g": "Religión", "i": "", "d": "Compromiso social inspirador."},
    {"id": "Latam.Rural", "n": "Latam Rural", "t": "Latam Rural", "g": "Agro", "i": "", "d": "Todo el mundo agro."},
    {"id": "BBB.MULTI", "n": "BBB Multicâmera", "t": "BBB Multicâmera", "g": "Reality", "i": "https://dominiopop.com.br/wp-content/uploads/2025/12/logo-bbb.jpg", "d": "Acompanhe tudo em tempo real."},
    {"id": "BBB.CAM1", "n": "BBB Câmera 1", "t": "BBB Câmera 1", "g": "Reality", "i": "https://dominiopop.com.br/wp-content/uploads/2025/12/logo-bbb.jpg", "d": "Acompanhe tudo em tempo real."},
    {"id": "BBB.CAM2", "n": "BBB Câmera 2", "t": "BBB Câmera 2", "g": "Reality", "i": "https://dominiopop.com.br/wp-content/uploads/2025/12/logo-bbb.jpg", "d": "Acompanhe tudo em tempo real."},
    {"id": "VTV.URUGUAY", "n": "VTV", "t": "VTV Uruguay", "g": "Interés general", "i": "https://i.postimg.cc/Y0Sncxc9/vtv.jpg", "d": "Noticias y actualidad de Uruguay."},
    {"id": "Noticias.Caracol", "n": "Noticias Caracol", "t": "Noticias Caracol", "g": "Noticias", "i": "https://i.postimg.cc/HxLYNfLz/image.png", "d": "Información con análisis y reportajes."},
    {"id": "Radio.Cosquin.Rock", "n": "Radio Cosquín Rock", "t": "Cosquín Rock", "g": "Radios", "i": "https://static.mytuner.mobi/media/tvos_radios/053/cosquin-rock-fm.71fd78e3.png", "d": "El rock argentino suena fuerte."},
    {"id": "Radio.Del.Plata", "n": "Radio Del Plata", "t": "Radio Del Plata", "g": "Radios", "i": "", "d": "Variedad musical y noticias."},
    {"id": "Radio.Disney", "n": "Radio Disney", "t": "Radio Disney", "g": "Radios", "i": "", "d": "Hits para toda la familia."},
    {"id": "Radio.La.Red", "n": "Radio La Red", "t": "Radio La Red", "g": "Radios", "i": "", "d": "Actualidad y noticias."},
    {"id": "Radio.Latina", "n": "Radio Latina", "t": "Radio Latina", "g": "Radios", "i": "", "d": "Éxitos en español."},
    {"id": "Radio.Los.40", "n": "Radio Los 40", "t": "Radio Los 40", "g": "Radios", "i": "", "d": "Hits del momento."},
    {"id": "Radio.Mega", "n": "Radio Mega", "t": "Radio Mega", "g": "Radios", "i": "", "d": "Música y entretenimiento."},
    {"id": "Radio.Nacional.Clasica", "n": "Radio Nacional Clásica", "t": "Nacional Clásica", "g": "Radios", "i": "", "d": "Música clásica y cultura."},
    {"id": "Radio.Nacional.Folclorica", "n": "Radio Nacional Folclórica", "t": "Nacional Folclórica", "g": "Radios", "i": "", "d": "Tradición y folclore argentino."},
    {"id": "Radio.Nacional.Rock", "n": "Radio Nacional Rock", "t": "Nacional Rock", "g": "Radios", "i": "", "d": "Rock nacional e internacional."},
    {"id": "Radio.La.Popu", "n": "Radio La Popu", "t": "La Popu", "g": "Radios", "i": "", "d": "La música popular que mueve a la gente."},
    {"id": "Radio.Rivadavia", "n": "Radio Rivadavia", "t": "Radio Rivadavia", "g": "Radios", "i": "", "d": "Noticias y actualidad regional."},
    {"id": "Radio.Rock.and.Pop", "n": "Radio Rock & Pop", "t": "Rock & Pop", "g": "Radios", "i": "", "d": "Todo el rock y pop."},
    {"id": "Radio.Vida", "n": "Radio Vida", "t": "Radio Vida", "g": "Radios", "i": "", "d": "Música variada todo el día."},
]

def generar():
    now = datetime.utcnow()
    # Generamos desde 1 día antes hasta 2 días después
    inicio_guia = now.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)
    
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<tv>\n'
    
    for c in canales:
        xml += f'  <channel id="{c["id"]}">\n'
        xml += f'    <display-name lang="es">{c["n"]}</display-name>\n'
        xml += '  </channel>\n'

    for c in canales:
        for d in range(4): # 4 días de guía total
            for h in range(0, 24, 4): # Bloques de 4 horas
                start_dt = inicio_guia + timedelta(days=d, hours=h)
                stop_dt = start_dt + timedelta(hours=4)
                s = start_dt.strftime("%Y%m%d%H%M%S +0000")
                e = stop_dt.strftime("%Y%m%d%H%M%S +0000")
                
                xml += f'  <programme start="{s}" stop="{e}" channel="{c["id"]}">\n'
                xml += f'    <title lang="es">{c["t"]}</title>\n'
                xml += f'    <desc lang="es">{c["d"]}</desc>\n'
                xml += f'    <category lang="es">{c["g"]}</category>\n'
                if c.get("i"):
                    xml += f'    <icon src="{c["i"]}" />\n'
                xml += '  </programme>\n'

    xml += '</tv>'
    with open("data_v9.xml", "w", encoding="utf-8") as f:
        f.write(xml)

if __name__ == "__main__":
    generar()
