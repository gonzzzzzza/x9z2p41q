import datetime

canales = [
    {"id": "GH.MULTI", "n": "Multicámara", "t": "GH - Experiencia Multicámara", "d": "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada, donde los participantes deberán sobreponerse al encierro y la convivencia para avanzar y quedarse con el tan anhelado premio.", "i": "https://i.postimg.cc/hjxWkfMf/image.png", "g": "Reality"},
    {"id": "GH.24HS", "n": "Gran Hermano 24 hs.", "t": "Gran Hermano 24 hs.", "d": "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada, donde los participantes deberán sobreponerse al encierro y la convivencia para avanzar y quedarse con el tan anhelado premio.", "i": "https://i.postimg.cc/hjxWkfMf/image.png", "g": "Reality"},
    {"id": "GH.CAM1", "n": "Cámara 1", "t": "Gran Hermano - Cámara 1", "d": "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada, donde los participantes deberán sobreponerse al encierro y la convivencia para avanzar y quedarse con el tan anhelado premio.", "i": "https://i.postimg.cc/hjxWkfMf/image.png", "g": "Reality"},
    {"id": "GH.CAM2", "n": "Cámara 2", "t": "Gran Hermano - Cámara 2", "d": "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada, donde los participantes deberán sobreponerse al encierro y la convivencia para avanzar y quedarse con el tan anhelado premio.", "i": "https://i.postimg.cc/hjxWkfMf/image.png", "g": "Reality"},
    {"id": "GH.CAM3", "n": "Cámara 3", "t": "Gran Hermano - Cámara 3", "d": "La casa más famosa del país vuelve a abrir sus puertas con una ambientación totalmente renovada, donde los participantes deberán sobreponerse al encierro y la convivencia para avanzar y quedarse con el tan anhelado premio.", "i": "https://i.postimg.cc/hjxWkfMf/image.png", "g": "Reality"},
    {"id": "Simpson", "n": "Los Simpson", "t": "Los Simpson", "g": "Comedia, Animación", "i": "https://static.flow.com.ar/images/10105665361/BROWSE/600/600/0/0/10105665361.jpg", "d": "Narra las vivencias de una peculiar familia norteamericana conformada por Homero, Marge, Bart, Lisa y Maggie Simpson. Elenco: Julie Kavner, Yeardley Smith."},
    {"id": "TRACE.UK", "n": "TRACE UK", "t": "TRACE UK", "g": "Música", "i": "https://cdn.broadbandtvnews.com/wp-content/uploads/2024/07/02103920/Trace-UK.jpg", "d": "TRACE UK brings viewers the very best of national and international artists, playing the hottest hip-hop, grime, afrobeats, rap and chart topping music videos."},
    {"id": "INFO.FLOW", "n": "FLOW", "t": "Comenzá a usar FLOW", "g": "Interés general", "i": "https://www.personal.com.py/img/logos/files/flow-color/flow-color.jpg", "d": "En Flow podés disfrutar de TV en vivo, películas, series, deportes, música y mucho más."},
    {"id": "Diputados.TV.ARG", "n": "Diputados TV", "t": "Diputados TV", "g": "Periodístico", "i": "https://static.flow.com.ar/images/10109930827/BROWSE/600/600/0/0/10109930827.jpg", "d": "Toda la información que concierte al trabajo de los Diputados de la Nación."},
    {"id": "Mix.TV", "n": "Mix TV", "t": "Mix TV", "g": "Interés general", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Entretenimiento sin pausa con realities, espectáculos, actualidad y contenidos que marcan tendencia."},
    {"id": "Lapacho.TV", "n": "Lapacho TV", "t": "Lapacho TV", "g": "Interés general", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "La pantalla que refleja la identidad formoseña. Información local, cultura y actualidad."},
    {"id": "Telesol.San.Juan", "n": "Telesol", "t": "Telesol", "g": "Interés general", "i": "https://i.ytimg.cc/vi/BbJo6A888a4/maxresdefault.jpg", "d": "Toda la actualidad sanjuanina en un solo lugar. Noticias y producción local."},
    {"id": "Claro.Sports.2", "n": "Claro Sports 2", "t": "Claro Sports 2", "g": "Deportes", "i": "https://cdn.amxinfra.com/clarosports/images/2024/08/paralimpicos-cs2-133315.jpg", "d": "Más acción, más competencia y más deporte en vivo. Cobertura de torneos internacionales."},
    {"id": "HBO.Boxing", "n": "HBO Boxing", "t": "HBO Boxing by WBTV", "g": "Boxeo", "i": "https://canvas-lb.tubitv.com/opts/lweaVPhEK4ZaUw==/c68711a9-7ca5-4153-a288-00b76afc4372/CPwDEJ0COgUxLjEuOA==", "d": "The home of elite boxing. World-class fighters, iconic matchups and unforgettable championship nights."},
    {"id": "Cazé.TV", "n": "Cazé TV", "t": "Cazé TV", "g": "Deportes", "i": "https://mir-s3-cdn-cf.behance.net/projects/404/f02c5b206996309.Y3JvcCw4MTAsNjMzLDAsMA.png", "d": "Esporte com leveza, informação e muita resenha. Transmissões vibrantes e convidados especiais."},
    {"id": "Tigo.Sports.2.PY", "n": "Tigo Sports 2", "t": "Tigo Sports 2", "g": "Deportes", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Viví la emoción del deporte como si estuvieras en la cancha. Toda la pasión de los hinchas."},
    {"id": "Flow.Sports.1", "n": "Flow Sports", "t": "Flow Sports", "g": "Deportes", "i": "https://static.flow.com.ar/images/10114132674/BROWSE/600/600/0/0/10114132674.jpg", "d": "Viví la pasión del deporte como si estuvieras ahí. Adrenalina y emoción en primera fila."},
    {"id": "Flow.Sports.2", "n": "Flow Sports 2", "t": "Flow Sports 2", "g": "Deportes", "i": "https://static.flow.com.ar/images/10114151657/BROWSE/600/600/0/0/10114151657.jpg", "d": "Viví la pasión del deporte como si estuvieras ahí. Adrenalina y emoción en primera fila."},
    {"id": "Flow.Sports.3", "n": "Flow Sports 3", "t": "Flow Sports 3", "g": "Deportes", "i": "https://i.postimg.cc/MKsrqNtf/Flow-Sports-3.png", "d": "Viví la pasión del deporte como si estuvieras ahí. Adrenalina y emoción en primera fila."},
    {"id": "DM.Kids.TV", "n": "DM Kids TV", "t": "DM Kids TV", "g": "Infantil", "i": "https://i.ytimg.cc/vi/JMbngwxZqZU/maxresdefault.jpg", "d": "Diversión, imaginación y aventuras. Series animadas y contenidos para aprender jugando."},
    {"id": "ENT.Family", "n": "#ENTFamily", "t": "#ENTFamily", "g": "Películas", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Contenido familiar para toda la familia. Diversión y entretenimiento seguro las 24 horas."},
    {"id": "ENT.Channel", "n": "#ENTChannel", "t": "#ENTChannel", "g": "Películas", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "El equilibrio perfecto de las películas y las series que marcaron generaciones."},
    {"id": "Totalmusic", "n": "#Totalmusic", "t": "#Totalmusic", "g": "Música", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "La más amplia selección de videoclips de todos los géneros y épocas."},
    {"id": "Totalmusic.80", "n": "#Totalmusic80s", "t": "#Totalmusic80s", "g": "Música", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "La más variada selección de videoclips de la década dorada de la música."},
    {"id": "Totalmusic.2000", "n": "#Totalmusic2000s", "t": "#Totalmusic2000s", "g": "Música", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Una cuidada selección de videoclips que marcaron los años 2000."},
    {"id": "Totalmusic.Concerts", "n": "#TotalmusicConcerts", "t": "#TotalmusicConcerts", "g": "Música", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Selección de conciertos en vivo inolvidables de actuaciones legendarias."},
    {"id": "Totalmusic.Dance", "n": "#TotalmusicDance", "t": "#TotalmusicDance", "g": "Música", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Selección vibrante de videoclips de música electrónica y dance."},
    {"id": "West.TV.PE", "n": "West TV", "t": "West TV", "g": "Películas", "i": "https://i.postimg.cc/C5MT6DLp/West.png", "d": "Un clásico espacio dedicado al cine del Lejano Oeste. Duelos, sheriffs y forajidos."},
    {"id": "Caras.TV", "n": "Caras TV", "t": "Caras TV", "g": "Interés general", "i": "https://media.canalnet.tv/2024/05/CYaZv3N-1157x720.jpg", "d": "La vida de los famosos, el glamour y las historias que todos comentan."},
    {"id": "El.Mueble", "n": "El Mueble", "t": "El Mueble", "g": "Interés general", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Inspiración, diseño y decoración. Ideas y tendencias para transformar tu hogar."},
    {"id": "Aunar", "n": "Aunar", "t": "Aunar", "g": "Cultura", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Cultura, sociedad y contenidos que inspiran. Historias y perspectivas del mundo."},
    {"id": "Horizons.Wild", "n": "Horizons Wild", "t": "Horizons.Wild", "g": "Naturaleza", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Explorá la naturaleza en su estado más puro. Documentales de fauna y paisajes."},
    {"id": "Viajar", "n": "Viajar", "t": "Viajar", "g": "Viajes", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Descubrí destinos, culturas y aventuras sin moverte de tu sillón."},
    {"id": "Flow.Music.1", "n": "Flow Music", "t": "Flow Music", "g": "Música", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "d": "La música la vivís en Flow. Shows en vivo y mucho más."},
    {"id": "Flow.Music.2", "n": "Flow Music 2", "t": "Flow Music 2", "g": "Música", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "d": "La música la vivís en Flow. Shows en vivo y mucho más."},
    {"id": "Flow.Music.3", "n": "Flow Music 3", "t": "Flow Music 3", "g": "Música", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "d": "La música la vivís en Flow. Shows en vivo y mucho más."},
    {"id": "Flow.Music.4", "n": "Flow Music 4", "t": "Flow Music 4", "g": "Música", "i": "https://static.flow.com.ar/images/10114137124/BROWSE/600/600/0/0/10114137124.jpg", "d": "La música la vivís en Flow. Shows en vivo y mucho más."},
    {"id": "Billboard.AR", "n": "Billboard", "t": "Billboard", "g": "Música", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Lo último en música, charts y artistas que marcan tendencia."},
    {"id": "Deluxe.Music.Wintertime", "n": "Deluxe Music Wintertime", "t": "Deluxe Music Wintertime", "g": "Música", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Selección especial de música para disfrutar en invierno. Hits y baladas."},
    {"id": "El.Folclorico", "n": "El Folclórico", "t": "El Folclórico", "g": "Música", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Raíces, tradición y la esencia del folclore en cada nota. Música y danza."},
    {"id": "Hit.TV", "n": "Hit TV", "t": "Hit TV", "g": "Música", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Los éxitos musicales más sonados en un solo canal. Videos y listas."},
    {"id": "FMH.Kizzi", "n": "FMH Kizzi", "t": "FMH Kizzi", "g": "Música", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Ritmo, frescura y los mejores lanzamientos musicales actuales."},
    {"id": "Music.Box.Classic", "n": "Music Box Classic", "t": "Music Box Classic", "g": "Música", "i": "https://www.digitalfernsehen.de/wp-content/uploads/2025/12/Music-Box-Classic.jpg", "d": "Los clásicos que nunca pasan de moda. Éxitos atemporales e inolvidables."},
    {"id": "Music.Box.Dance", "n": "Music Box Dance", "t": "Music Box Dance", "g": "Música", "i": "https://www.digitalfernsehen.de/wp-content/uploads/2025/12/Music-Box-Dance.jpg", "d": "Ritmo, energía y beats que no te dejan quedarte quieto. Electrónica y dance."},
    {"id": "Music.Box.Hits", "n": "Music Box Hits", "t": "Music Box Hits", "g": "Música", "i": "https://www.digitalfernsehen.de/wp-content/uploads/2025/12/Music-Box-Hits.jpg", "d": "Los temas más escuchados del momento. Hits internacionales y nacionales."},
    {"id": "Music.Box.Sexy", "n": "Music Box Sexy", "t": "Music Box Sexy", "g": "Música", "i": "https://www.parabola.cz/img_magazin/2025/music-box-sexy.jpg", "d": "Vibras sensuales y sofisticadas. Música lounge, R&B y ritmos seductores."},
    {"id": "Musictop", "n": "Musictop", "t": "Musictop", "g": "Música", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Top charts y éxitos globales. Videos, rankings y artistas dominantes."},
    {"id": "Vorterix", "n": "Vorterix", "t": "Vorterix", "g": "Música", "i": "https://static.flow.com.ar/images/10114219640/BROWSE/600/600/0/0/10114219640.jpg", "d": "Pionero como medio de streaming sumarse a la frecuencia FM."},
    {"id": "Radio.Maria", "n": "Radio María", "t": "Radio María", "g": "Religión", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Espiritualidad, oración y música religiosa para acompañar tu fe."},
    {"id": "Santa.Maria", "n": "Santa María", "t": "Santa María", "g": "Religión", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Contenido religioso y formación espiritual con reflexiones para el hogar."},
    {"id": "Solidaria.TV", "n": "Solidaria TV", "t": "Solidaria TV", "g": "Religión", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Historias de ayuda, solidaridad y compromiso social inspirador."},
    {"id": "Latam.Rural", "n": "Latam Rural", "t": "Latam Rural", "g": "Agro", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Todo el mundo agro en un solo lugar. Noticias, producción y tecnología."},
    {"id": "BBB.MULTI", "n": "Big Brother Brasil - Multicâmera", "t": "BBB Multicâmera", "g": "Reality", "i": "https://dominiopop.com.br/wp-content/uploads/2025/12/logo-bbb.jpg", "d": "Acompanhe cada momento como se você estivesse dentro da casa em tempo real."},
    {"id": "BBB.CAM1", "n": "Big Brother Brasil - Câmera 1", "t": "BBB Câmera 1", "g": "Reality", "i": "https://dominiopop.com.br/wp-content/uploads/2025/12/logo-bbb.jpg", "d": "Acompanhe cada momento como se você estivesse dentro da casa em tempo real."},
    {"id": "BBB.CAM2", "n": "Big Brother Brasil - Câmera 2", "t": "BBB Câmera 2", "g": "Reality", "i": "https://dominiopop.com.br/wp-content/uploads/2025/12/logo-bbb.jpg", "d": "Acompanhe cada momento como se você estivesse dentro da casa em tempo real."},
    {"id": "VTV.URUGUAY", "n": "VTV", "t": "VTV", "g": "Interés general", "i": "https://i.postimg.cc/Y0Sncxc9/vtv.jpg", "d": "Noticias, actualidad y cobertura completa de Uruguay y el mundo."},
    {"id": "Noticias.Caracol", "n": "Noticias Caracol", "t": "Noticias Caracol", "g": "Noticias", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "La información que necesitás con análisis y reportajes importantes."},
    {"id": "Radio.Cosquin.Rock", "n": "Radio Cosquín Rock", "t": "Radio Cosquín Rock", "g": "Radios", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "El rock argentino suena fuerte. Conciertos y clásicos."},
    {"id": "Radio.Del.Plata", "n": "Radio Del Plata", "t": "Radio Del Plata", "g": "Radios", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Variedad musical, noticias y entretenimiento."},
    {"id": "Radio.Disney", "n": "Radio Disney", "t": "Radio Disney", "g": "Radios", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Los hits que todos aman y contenido para chicos y adolescentes."},
    {"id": "Radio.La.Red", "n": "Radio La Red", "t": "Radio La Red", "g": "Radios", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Actualidad, debate y noticias con opinión."},
    {"id": "Radio.Latina", "n": "Radio Latina", "t": "Radio Latina", "g": "Radios", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Éxitos en español y ritmos latinos para disfrutar."},
    {"id": "Radio.Los.40", "n": "Radio Los 40", "t": "Radio Los 40", "g": "Radios", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Los hits del momento y artistas que marcan tendencia pop."},
    {"id": "Radio.Mega", "n": "Radio Mega", "t": "Radio Mega", "g": "Radios", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Música, entretenimiento y diversión para todos los gustos."},
    {"id": "Radio.Nacional.Clasica", "n": "Radio Nacional Clásica", "t": "Radio Nacional Clásica", "g": "Radios", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "La música clásica y la cultura sonora a tu alcance."},
    {"id": "Radio.Nacional.Folclorica", "n": "Radio Nacional Folclórica", "t": "Radio Nacional Folclórica", "g": "Radios", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Tradición, cultura y folclore argentino en cada nota."},
    {"id": "Radio.Nacional.Rock", "n": "Radio Nacional Rock", "t": "Radio Nacional Rock", "g": "Radios", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Rock nacional e internacional las 24 horas."},
    {"id": "Radio.La.Popu", "n": "Radio La Popu", "t": "Radio La Popu", "g": "Radios", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "La música popular que mueve a la gente."},
    {"id": "Radio.Rivadavia", "n": "Radio Rivadavia", "t": "Radio Rivadavia", "g": "Radios", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Noticias, actualidad y opinión regional."},
    {"id": "Radio.Rock.and.Pop", "n": "Radio Rock & Pop", "t": "Radio Rock & Pop", "g": "Radios", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Todo el rock, pop y música alternativa."},
    {"id": "Radio.Vida", "n": "Radio Vida", "t": "Radio Vida", "g": "Radios", "i": "https://raw.githubusercontent.com/Puticastillo/EPGCL/main/zoidberg/fallback.jpg", "d": "Música variada todo el día con los hits del momento."},
]

def generar_xml():
    # Usar fecha actual como inicio
    inicio_fijo = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    
    lines = []
    lines.append('<?xml version="1.0" encoding="utf-8"?>')
    lines.append('<tv generator-info="EPG Generator">')
    
    for c in canales:
        lines.append(f'  <channel id="{c["id"]}">')
        lines.append(f'    <display-name>{c["n"]}</display-name>')
        lines.append('  </channel>')

    for c in canales:
        for d in range(6):
            for h in range(0, 24, 4):
                start_dt = inicio_fijo + datetime.timedelta(days=d, hours=h)
                stop_dt = start_dt + datetime.timedelta(hours=4)
                
                # Formato correcto sin espacio antes de la zona horaria
                s = start_dt.strftime("%Y%m%d%H%M%S") + "-0300"
                e = stop_dt.strftime("%Y%m%d%H%M%S") + "-0300"
                
                lines.append(f'  <programme start="{s}" stop="{e}" channel="{c["id"]}">')
                lines.append(f'    <title>{c["t"]}</title>')
                lines.append(f'    <desc>{c["d"]}</desc>')
                lines.append(f'    <icon src="{c.get("i")}"/>')
                lines.append(f'    <category>{c["g"]}</category>')
                lines.append(f'  </programme>')

    lines.append('</tv>')
    
    # Escribir el archivo con codificación utf-8 y saltos de línea correctos
    with open("data_v9.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    print("Archivo data_v9.xml generado correctamente.")

if __name__ == "__main__":
    generar_xml()
