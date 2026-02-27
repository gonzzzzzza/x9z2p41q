import datetime
import requests
import re

mb_config = {
    "classic": "MUSIC BOX CLASSIC",
    "dance": "MUSIC BOX DANCE",
    "hits": "MUSIC BOX HITS",
    "sexy": "MUSIC BOX SEXY"
}
URL_MB_BASE = "https://epg.musicboxtv.net/xml"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

def prueba_musicbox():
    now = datetime.datetime.now()
    # Probamos hoy y mañana
    rango_fechas = [
        now.strftime("%Y-%m-%d"),
        (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    ]
    
    lines = []
    lines.append('<?xml version="1.0" encoding="utf-8"?>')
    lines.append('<tv generator-info="Prueba Music Box Final">')
    
    for _, official_id in mb_config.items():
        lines.append(f'  <channel id="{official_id}"><display-name>{official_id}</display-name></channel>')

    for fecha in rango_fechas:
        for folder, official_id in mb_config.items():
            url = f"{URL_MB_BASE}/{fecha}/{folder}.xml"
            print(f"Intentando: {url}")
            try:
                # Añadimos HEADERS para evitar bloqueos
                r = requests.get(url, headers=HEADERS, timeout=15)
                print(f"Respuesta: {r.status_code}")
                
                if r.status_code == 200:
                    # Usamos una técnica más agresiva para capturar los programas
                    texto = r.text
                    # Buscamos contenido entre <programme ... </programme>
                    programas = re.findall(r'(<programme.*?</programme>)', texto, re.DOTALL)
                    
                    if programas:
                        print(f"¡EXITO! {len(programas)} programas en {folder}")
                        for p in programas:
                            # Limpieza total de namespaces y fijar ID de canal
                            p_clean = re.sub(r'ns\d+:', '', p)
                            p_clean = re.sub(r':ns\d+', '', p_clean)
                            p_final = re.sub(r'channel=".*?"', f'channel="{official_id}"', p_clean)
                            lines.append("  " + p_final)
                    else:
                        print("No se encontraron etiquetas <programme> dentro del archivo.")
            except Exception as e:
                print(f"Error fatal: {e}")

    lines.append('</tv>')

    with open("test_musicbox.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

if __name__ == "__main__":
    prueba_musicbox()
