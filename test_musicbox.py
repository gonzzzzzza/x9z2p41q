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

def prueba_musicbox():
    now = datetime.datetime.now()
    # Probamos un rango de 3 días para asegurar que encuentre algo
    rango_fechas = [
        (now - datetime.timedelta(days=1)).strftime("%Y-%m-%d"), # Ayer
        now.strftime("%Y-%m-%d"),                               # Hoy
        (now + datetime.timedelta(days=1)).strftime("%Y-%m-%d")  # Mañana
    ]
    
    lines = []
    lines.append('<?xml version="1.0" encoding="utf-8"?>')
    lines.append('<tv generator-info="Prueba Music Box Mejorada">')
    
    for _, official_id in mb_config.items():
        lines.append(f'  <channel id="{official_id}"><display-name>{official_id}</display-name></channel>')

    print(f"Iniciando búsqueda en fechas: {rango_fechas}")

    for fecha in rango_fechas:
        print(f"\n--- Probando fecha: {fecha} ---")
        for folder, official_id in mb_config.items():
            url = f"{URL_MB_BASE}/{fecha}/{folder}.xml"
            try:
                r = requests.get(url, timeout=10)
                if r.status_code == 200:
                    programas = re.findall(r'<programme.*?>.*?</programme>', r.text, re.DOTALL)
                    if programas:
                        print(f"  [OK] {official_id}: {len(programas)} programas encontrados.")
                        for p in programas:
                            p_clean = p.replace('ns0:', '').replace(':ns0', '')
                            p_final = re.sub(r'channel=".*?"', f'channel="{official_id}"', p_clean)
                            lines.append("  " + p_final)
                    else:
                        print(f"  [!] {official_id}: Archivo vacío o sin etiquetas 'programme'.")
                else:
                    print(f"  [Error {r.status_code}] No existe: {url}")
            except Exception as e:
                print(f"  [Fallo] Error de conexión: {e}")

    lines.append('</tv>')

    with open("test_musicbox.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("\nProceso terminado. Revisa el archivo 'test_musicbox.xml' nuevamente.")

if __name__ == "__main__":
    prueba_musicbox()
