# Landing Analyzer 🕵️‍♂️

Herramienta educativa desarrollada en Python para analizar *landing pages* sospechosas (como links acortados o de phishing) y detectar:

<img src="images/1Project-Structure.png">

<img src="images/2graph.png">

- Redirecciones
- Estado HTTP (200, 403, 404…)
- Títulos de las páginas
- Parámetros de tracking


## 🚀 Uso
1. Clona este repositorio:
   ```
   git clone https://github.com/ImaneLamriui/Landing-Analyzer.git
   cd Landing-Analyzer
   ```
2. Crea un entorno virtual:
 ```
   python3 -m venv venv
   source venv/bin/activate
 ```
<img src="images/3venv.png">

3. Instala dependencias:
   
 ```
  pip install -r requirements.txt
 ```

<img src="images/4venv.png">

4. Añade tus URLs a urls.txt.

5. Ejecuta:
 ```
python landing_analyzer.py

```
<img src="images/5landingscript.png">  

6. Resultados:

<img src="images/6csv.png">

landing_results.csv → reporte con análisis detallado

landing_graph.png → gráfico de estados HTTP

<img src="images/finalResult.png">

⚠️ Nota: Esta herramienta es únicamente para fines educativos y de investigación en ciberseguridad.
   
