# 🧬 Analizador de Secuencias Biológicas

Un programa en Python para analizar secuencias biológicas (ADN, ARN y proteínas) desarrollado para el Laboratorio 01 de Bioinformática.

## 📋 Características

* **Identificación de tipo de secuencia**: Determina si una secuencia es ADN, ARN, Proteína o Desconocida.
* **Transcripción de ADN a ARN**: Transcribe secuencias de ADN válidas a ARN.
* **Procesamiento de archivos FASTA**: Lee secuencias desde archivos en formato FASTA estándar para su análisis.
* **Pruebas automatizadas**: Pruebas completas para todas las funcionalidades usando `pytest`.

## 🔎 Criterios de Identificación de Secuencias

- **DNA**: Contiene solo A, T, G, C
- **RNA**: Contiene solo A, U, G, C
- **Proteína**: Contiene solo los 20 aminoácidos estándar (A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y)
- **Desconocido**: Cualquier secuencia que no encaje en las categorías anteriores

## 💻 Instalación

1. Crea y activa un entorno virtual (recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate    # En Windows
   ```

2. Clona el repositorio:
   ```bash
   git clone <url-del-repositorio>
   cd repositorio
   ```

3. Instala las dependencias (si es necesario):
   ```bash
   pip install pytest
   ```

## 🚀 Uso

### Interfaz de Línea de Comandos

El programa puede usarse desde la terminal de la siguiente manera:

```bash
python bio_sequence_analyzer.py ATGCATGC           # Analiza una secuencia directamente
python bio_sequence_analyzer.py archivo.fasta      # Analiza una secuencia desde un archivo FASTA
```

- Si se proporciona una secuencia, la identifica y, si es ADN, la transcribe a ARN.
- Si se proporciona un archivo `.fasta` o `.fa`, lee la secuencia y realiza el análisis.

### Ejemplo de Uso

```bash
# Identificar una secuencia de ADN
python bio_sequence_analyzer.py "ATGCATGC"

# Analizar una secuencia desde un archivo FASTA
python bio_sequence_analyzer.py "crab_fasta_examples/crab_human.fasta"
```

## 🧪 Ejecución de Pruebas

Las pruebas están implementadas con `pytest` y utilizan archivos `.fasta` temporales. Para ejecutarlas:

```bash
pytest test_bio_sequence_analyzer.py
```

## 🔄 Funcionalidad

### Funciones principales

1. **identify_sequence_type(sequence)**: 
   - Identifica si una secuencia es ADN, ARN, Proteína o Desconocida.

2. **transcribe_dna_to_rna(sequence)**:
   - Convierte una secuencia de ADN válida a ARN reemplazando T por U.
   - Devuelve un mensaje de error si la secuencia no es ADN válido.

3. **read_sequence_from_file(file_path)**:
   - Lee una secuencia desde un archivo de texto o FASTA e identifica su tipo.
   - Devuelve la secuencia y su tipo, o un mensaje de error si falla la lectura.

4. **extract_fasta_sequence(file_path)**:
   - Extrae la secuencia de un archivo FASTA (desde la segunda línea en adelante, sin espacios ni tabs).

