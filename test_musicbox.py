import datetime
import requests
import re

# Configuración de prueba
# Carpeta en la URL : ID que viene dentro del XML
mb_config = {
    "classic": "MUSIC BOX CLASSIC",
    "dance": "MUSIC BOX DANCE",
    "hits": "MUSIC BOX HITS",
    "sexy": "MUSIC BOX SEXY"
}
URL_MB_BASE = "https://epg.musicboxtv.net/xml"

def prueba_musicbox():
    now = datetime.datetime.now()
    fecha_hoy = now.strftime("%Y-%m-%d")
    
    lines = []
    lines.append('<?xml version="1.0" encoding="utf-8"?>')
    lines.append('<tv generator-info="Prueba Music Box">')
    
    # Crear canales
    for _, official_id in mb_config.items():
        lines.append(f'  <channel id="{official_id}">')
        lines.append(f'    <display-name>{official_id}</display-name>')
        lines.append(f'  </channel>')

    print(f"Iniciando descarga para la fecha: {fecha_hoy}...")

    for folder, official_id in mb_config.items():
        url = f"{URL_MB_BASE}/{fecha_hoy}/{folder}.xml"
        print(f"Probando: {url}")
        
        try:
            r = requests.get(url, timeout=15)
            if r.status_code == 200:
                # Buscamos todos los bloques <programme> ... </programme>
                programas = re.findall(r'<programme.*?>.*?</programme>', r.text, re.DOTALL)
                
                print(f"  ✓ Encontrados {len(programas)} programas para {official_id}")
                
                for p in programas:
                    # 1. Quitamos los namespaces ns0: si existen
                    p_clean = p.replace('ns0:', '').replace(':ns0', '')
                    
                    # 2. Forzamos el ID oficial del canal para que no haya dudas
                    # Esto reemplaza cualquier channel="LO_QUE_SEA" por channel="MUSIC BOX XXXX"
                    p_final = re.sub(r'channel=".*?"', f'channel="{official_id}"', p_clean)
                    
                    lines.append("  " + p_final)
            else:
                print(f"  ✗ Error {r.status_code}: No se encontró archivo para {folder}")
        
        except Exception as e:
            print(f"  ✗ Error de conexión en {folder}: {e}")

    lines.append('</tv>')

    # Guardar resultado
    with open("test_musicbox.xml", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    print("\nPrueba finalizada. Revisa el archivo 'test_musicbox.xml'")

if __name__ == "__main__":
    prueba_musicbox()
