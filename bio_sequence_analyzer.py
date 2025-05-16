"""
Analizador de Secuencias Biológicas
---------------------
Módulo para analizar y procesar secuencias biológicas.
"""

def identify_sequence_type(sequence):
    """
    Identifica el tipo de secuencia biológica.
    
    Args:
        sequence (str): La secuencia a analizar
        
    Returns:
        str: 'DNA', 'RNA', 'Proteína' o 'Desconocido'
    """
    # Elimina cualquier espacio en blanco de la secuencia
    sequence = sequence.strip().upper()
    
    if not sequence:
        return "Desconocido"
    
    # Verifica si es ADN (contiene solo A, T, G, C)
    if all(nucleotide in "ATGC" for nucleotide in sequence):
        return "DNA"
    
    # Verifica si es ARN (contiene solo A, U, G, C)
    if all(nucleotide in "AUGC" for nucleotide in sequence):
        return "RNA"
    
    # Verifica si es proteína (contiene solo los 20 aminoácidos estándar)
    amino_acids = {"A", "C", "D", "E", "F", "G", "H", "I", "K", "L", 
                   "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"}
    if all(aa in amino_acids for aa in sequence):
        return "Proteína"
    
    # Si no es ninguno de los anteriores
    return "Desconocido"

def transcribe_dna_to_rna(sequence):
    """
    Transcribe una secuencia de ADN a ARN reemplazando T por U.
    
    Args:
        sequence (str): La secuencia de ADN a transcribir
        
    Returns:
        str: La secuencia de ARN transcrita o un mensaje de error
    """
    # Elimina espacios en blanco y convierte a mayúsculas
    sequence = sequence.strip().upper()
    
    # Verifica que sea una secuencia de ADN válida
    if identify_sequence_type(sequence) != "DNA":
        return "Error: La secuencia proporcionada no es un ADN válido"
    
    # Transcribe ADN a ARN (reemplaza T por U)
    return sequence.replace("T", "U")

def extract_fasta_sequence(file_path):
    """
    Extrae la secuencia de un archivo FASTA (desde la segunda línea en adelante).
    Args:
        file_path (str): Ruta al archivo FASTA
    Returns:
        str: Secuencia concatenada sin espacios ni tabs
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        # Ignora la primera línea (cabecera) y concatena el resto
        sequence = ''.join(line.strip() for line in lines[1:])
        sequence = sequence.replace(' ', '').replace('\t', '')
        return sequence

def read_sequence_from_file(file_path):
    """
    Lee una secuencia desde un archivo de texto (incluyendo formato FASTA) e identifica su tipo.
    Args:
        file_path (str): Ruta al archivo que contiene la secuencia
    Returns:
        tuple: (secuencia, tipo_de_secuencia)
    """
    try:
        if file_path.lower().endswith(('.fasta', '.fa')):
            sequence = extract_fasta_sequence(file_path)
        else:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
                sequence = sequence.replace(' ', '').replace('\t', '')
        seq_type = identify_sequence_type(sequence)
        return sequence, seq_type
    except Exception as e:
        return None, f"Error al leer el archivo: {str(e)}"

def get_aminoacid_names(sequence):
    """
    Devuelve una lista con el nombre completo de cada aminoácido en la secuencia.
    Args:
        sequence (str): Secuencia de proteína
    Returns:
        list: Lista de nombres de aminoácidos
    """
    aminoacid_dict = {
        'A': 'Alanina', 'C': 'Cisteína', 'D': 'Ácido aspártico', 'E': 'Ácido glutámico',
        'F': 'Fenilalanina', 'G': 'Glicina', 'H': 'Histidina', 'I': 'Isoleucina',
        'K': 'Lisina', 'L': 'Leucina', 'M': 'Metionina', 'N': 'Asparagina',
        'P': 'Prolina', 'Q': 'Glutamina', 'R': 'Arginina', 'S': 'Serina',
        'T': 'Treonina', 'V': 'Valina', 'W': 'Triptófano', 'Y': 'Tirosina'
    }
    return [aminoacid_dict.get(aa.upper(), 'Desconocido') for aa in sequence if aa.upper() in aminoacid_dict]

if __name__ == "__main__":
    # Interfaz simple de línea de comandos
    import sys
    
    if len(sys.argv) > 1:
        # Verifica si se proporciona una ruta de archivo
        if sys.argv[1].endswith(('.txt', '.fasta', '.fa')):
            sequence, seq_type = read_sequence_from_file(sys.argv[1])
            if sequence:
                print(f"Secuencia: {sequence}")
                print(f"Tipo: {seq_type}")
                
                if seq_type == "DNA":
                    rna = transcribe_dna_to_rna(sequence)
                    print(f"ARN transcrito: {rna}")
                elif seq_type == "Proteína":
                    nombres = get_aminoacid_names(sequence)
                    print("Aminoácidos:")
                    for letra, nombre in zip(sequence, nombres):
                        print(f"  {letra}: {nombre}")
            else:
                print(seq_type)  # Mensaje de error
        else:
            # Trata el argumento como secuencia
            sequence = sys.argv[1]
            seq_type = identify_sequence_type(sequence)
            print(f"Secuencia: {sequence}")
            print(f"Tipo: {seq_type}")
            
            if seq_type == "DNA":
                rna = transcribe_dna_to_rna(sequence)
                print(f"ARN transcrito: {rna}")
            elif seq_type == "Proteína":
                nombres = get_aminoacid_names(sequence)
                print("Aminoácidos:")
                for letra, nombre in zip(sequence, nombres):
                    print(f"  {letra}: {nombre}")
    else:
        print("Por favor proporciona una secuencia o la ruta a un archivo.")
        print("Uso: python bio_sequence_analyzer.py <secuencia o archivo.txt>") 