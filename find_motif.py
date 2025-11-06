#Finding a motif in DNA 

### Find all positions where motif occurs in sequence.
###      
def identify_motif_positions(sequence,motif):
    positions = []
    motif_len = len(motif)

    # Search through the sequence
    for i in range(len(sequence) - motif_len + 1):
        # Check if motif matches at this position
        if sequence[i:i + motif_len] == motif:
            positions.append(i + 1)  # 1-based indexing
    
    return positions

def find_motif(fasta_file):
    """
    Read FASTA file and find motif positions.
    Expected format:
    - First sequence is the main DNA string
    - Second sequence is the motif to search for
    """
    lines = []
    
    try:
        with open(fasta_file, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                    
                if line and not line.startswith(">"):
                    lines.append(line)
            
        
        if len(lines) < 2:
            print("Error: File must contain at least 2 sequences (main sequence and motif)")
            return []
        
        main_sequence = lines[0].upper()
        motif = lines[1].upper()
        
        # Find all positions
        positions = identify_motif_positions(main_sequence, motif)
        
        return positions
                
    except FileNotFoundError:
        print(f"Error: The file '{fasta_file}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    # Example usage with file
    fasta_path = "/home/cfneira1/bioinfo/rosalind_subs.txt"
    result = find_motif(fasta_path)
    
    if result:
        print("Motif found at positions:", ' '.join(map(str, result)))
    else:
        print("Motif not found")
