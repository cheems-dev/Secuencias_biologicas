"""
Módulo de pruebas para bio_sequence_analyzer
-------------------------------------
Contiene pruebas para todas las funciones del módulo bio_sequence_analyzer.
"""

import os
import tempfile
import pytest
from bio_sequence_analyzer import identify_sequence_type, transcribe_dna_to_rna, read_sequence_from_file

def test_identificacion_dna():
    """Prueba la identificación correcta de secuencias de ADN."""
    # Secuencias de ADN válidas
    assert identify_sequence_type("ATGC") == "DNA"
    assert identify_sequence_type("AAAGTCGTA") == "DNA"
    assert identify_sequence_type("GCAT") == "DNA"
    assert identify_sequence_type("atgc") == "DNA"  # Prueba insensibilidad a mayúsculas
    assert identify_sequence_type("ATGC ATGC") == "DNA"  # Prueba con espacios

def test_identificacion_dna_invalido():
    """Prueba la identificación de secuencias de ADN inválidas."""
    # Secuencias de ADN inválidas
    assert identify_sequence_type("AUUGC") != "DNA"  # Contiene U
    assert identify_sequence_type("ATGCx") != "DNA"  # Contiene carácter inválido
    assert identify_sequence_type("ATGCN") != "DNA"  # Contiene N
    assert identify_sequence_type("ATGC123") != "DNA"  # Contiene números
    assert identify_sequence_type("ATGCY") != "DNA"  # Contiene Y

def test_identificacion_rna():
    """Prueba la identificación correcta de secuencias de ARN."""
    # Secuencias de ARN válidas
    assert identify_sequence_type("AUGC") == "RNA"
    assert identify_sequence_type("AAAGUUGUA") == "RNA"
    assert identify_sequence_type("GCAU") == "RNA"
    assert identify_sequence_type("augc") == "RNA"  # Prueba insensibilidad a mayúsculas
    assert identify_sequence_type("AUGC AUGC") == "RNA"  # Prueba con espacios

def test_identificacion_rna_invalido():
    """Prueba la identificación de secuencias de ARN inválidas."""
    # Secuencias de ARN inválidas
    assert identify_sequence_type("ATTGC") != "RNA"  # Contiene T
    assert identify_sequence_type("AUGCx") != "RNA"  # Contiene carácter inválido
    assert identify_sequence_type("AUGCN") != "RNA"  # Contiene N
    assert identify_sequence_type("AUGC123") != "RNA"  # Contiene números
    assert identify_sequence_type("AUGCY") != "RNA"  # Contiene Y

def test_identificacion_proteina():
    """Prueba la identificación correcta de secuencias de proteína."""
    # Secuencias de proteína válidas
    assert identify_sequence_type("ACDEFGHIKLMNPQRSTVWY") == "Proteína"  # Los 20 aminoácidos
    assert identify_sequence_type("ARNDCQEGHILKMFPSTWYV") == "Proteína"  # Reordenado
    assert identify_sequence_type("MSKSPPK") == "Proteína"  # Proteína corta
    assert identify_sequence_type("acdefghiklmnpqrstvwy") == "Proteína"  # Prueba insensibilidad a mayúsculas
    assert identify_sequence_type("ACDEP GHIKL MNPQR STVWY") == "Proteína"  # Con espacios

def test_identificacion_proteina_invalida():
    """Prueba la identificación de secuencias de proteína inválidas."""
    # Secuencias de proteína inválidas
    assert identify_sequence_type("ACDXEFG") != "Proteína"  # X no es aminoácido estándar
    assert identify_sequence_type("ACDEFB") != "Proteína"  # B no es aminoácido estándar
    assert identify_sequence_type("ACDEF1") != "Proteína"  # Contiene número
    assert identify_sequence_type("ACDEF*") != "Proteína"  # Contiene carácter especial
    assert identify_sequence_type("ACDEFO") != "Proteína"  # O no es aminoácido estándar

def test_secuencias_desconocidas():
    """Prueba la identificación de secuencias desconocidas."""
    # Secuencias desconocidas
    assert identify_sequence_type("") == "Desconocido"  # Cadena vacía
    assert identify_sequence_type("123456") == "Desconocido"  # Solo números
    assert identify_sequence_type("ACGTN") == "Desconocido"  # ADN con N
    assert identify_sequence_type("ATGCX") == "Desconocido"  # ADN con carácter inválido
    assert identify_sequence_type("!@#$%^") == "Desconocido"  # Caracteres especiales

def test_transcripcion_dna_a_rna():
    """Prueba la transcripción de ADN a ARN."""
    # Transcripciones válidas
    assert transcribe_dna_to_rna("ATGC") == "AUGC"
    assert transcribe_dna_to_rna("TTTT") == "UUUU"
    assert transcribe_dna_to_rna("GCAT") == "GCAU"
    assert transcribe_dna_to_rna("atgc") == "AUGC"  # Prueba insensibilidad a mayúsculas
    assert transcribe_dna_to_rna("ATGC ATGC") == "AUGC AUGC"  # Con espacios

def test_transcripcion_dna_invalida():
    """Prueba la transcripción de secuencias de ADN inválidas."""
    # Transcripciones inválidas
    assert transcribe_dna_to_rna("AUGC").startswith("Error")  # ARN, no ADN
    assert transcribe_dna_to_rna("ATGCx").startswith("Error")  # ADN inválido
    assert transcribe_dna_to_rna("ATGCN").startswith("Error")  # ADN con N
    assert transcribe_dna_to_rna("").startswith("Error")  # Cadena vacía
    assert transcribe_dna_to_rna("ACDEFGHIKLMNPQRSTVWY").startswith("Error")  # Proteína
