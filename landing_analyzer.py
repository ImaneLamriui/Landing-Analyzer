#!/usr/bin/env python3
"""
Landing Analyzer - Laboratorio educativo
Analiza URLs de prueba / acortadores y extrae:
- URL final tras redirecciones
- Código HTTP
- Título de la página
- Tracking parameters (utm_)
Genera CSV y gráfico de frecuencia de dominios finales.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

results = []

# Leer URLs desde archivo
with open("urls.txt") as f:
    urls = [line.strip() for line in f if line.strip()]

print(f"[INFO] Analizando {len(urls)} URLs...\n")

# Analizar cada URL
for url in urls:
    try:
        r = requests.get(url, timeout=5, allow_redirects=True)
        final_url = r.url
        status_code = r.status_code
        title = BeautifulSoup(r.text, 'html.parser').title.string if r.text else ''
        tracking = [p for p in final_url.split('?')[-1].split('&') if 'utm_' in p] if '?' in final_url else []
        results.append({
            'original_url': url,
            'final_url': final_url,
            'status': status_code,
            'title': title,
            'tracking_params': ','.join(tracking)
        })
        print(f"[OK] {url} -> {final_url} ({status_code})")
    except Exception as e:
        results.append({
            'original_url': url,
            'final_url': '',
            'status': 'ERROR',
            'title': '',
            'tracking_params': ''
        })
        print(f"[ERROR] {url} -> {e}")

# Guardar resultados en CSV
df = pd.DataFrame(results)
df.to_csv("landing_results.csv", index=False)
print("\n[INFO] CSV generado: landing_results.csv")

# Gráfico de frecuencia de dominios finales
df['domain'] = df['final_url'].apply(lambda x: x.split('/')[2] if x else 'ERROR')
df['domain'].value_counts().plot(kind='bar', figsize=(10,5))
plt.title("Frecuencia de dominios finales")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.savefig("landing_graph.png")
plt.show()
print("[INFO] Gráfico generado: landing_graph.png")
