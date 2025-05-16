"""
Bio Sequence Analyzer - Main Interface
-------------------------------------
A command-line interface for the bio sequence analyzer.
"""

import argparse
from bio_sequence_analyzer import identify_sequence_type, transcribe_dna_to_rna, read_sequence_from_file

def main():
    parser = argparse.ArgumentParser(
        description="Bio Sequence Analyzer - Identify and process biological sequences",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py -s ATGCATGC
  python main.py -f sequence.txt
  python main.py -s ATGCATGC -t
"""
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-s", "--sequence", help="Biological sequence to analyze")
    group.add_argument("-f", "--file", help="File containing a biological sequence")
    
    parser.add_argument("-t", "--transcribe", action="store_true", 
                        help="Transcribe DNA to RNA (if the sequence is valid DNA)")
    
    args = parser.parse_args()
    
    # Process sequence from direct input
    if args.sequence:
        sequence = args.sequence.strip()
        sequence_type = identify_sequence_type(sequence)
        
        print(f"Sequence: {sequence}")
        print(f"Type: {sequence_type}")
        
        if args.transcribe and sequence_type == "DNA":
            rna = transcribe_dna_to_rna(sequence)
            print(f"Transcribed RNA: {rna}")
        elif args.transcribe and sequence_type != "DNA":
            print("Transcription failed: Input is not a valid DNA sequence")
    
    # Process sequence from file
    elif args.file:
        sequence, sequence_type = read_sequence_from_file(args.file)
        
        if isinstance(sequence_type, str) and "Error" in sequence_type:
            print(sequence_type)
            return
            
        print(f"Sequence from file: {args.file}")
        print(f"Sequence type: {sequence_type}")
        
        if args.transcribe and sequence_type == "DNA":
            rna = transcribe_dna_to_rna(sequence)
            print(f"Transcribed RNA: {rna}")
        elif args.transcribe and sequence_type != "DNA":
            print("Transcription failed: Input is not a valid DNA sequence")

if __name__ == "__main__":
    main() 