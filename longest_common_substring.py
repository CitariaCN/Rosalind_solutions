def find_longest_common_substring(sequences):
    """Find A longest common substring (any one is fine)."""
    if not sequences:
        return None
    
    if len(sequences) == 1:
        return sequences[0]
    
    shortest = min(sequences, key=len)
    
    # Try from longest to shortest
    for length in range(len(shortest), 0, -1):
        for start in range(len(shortest) - length + 1):
            motif = shortest[start:start + length]
            
            if all(motif in seq for seq in sequences):
                return motif  # Return first one found 
    
    return None


def solve_lcsm(fasta_file):
    """Solve Rosalind LCSM problem."""
    sequences = []
    current_seq = ""
    
    try:
        with open(fasta_file, "r") as f:
            for line in f:
                line = line.strip()
                
                if not line:
                    continue
                
                if line.startswith(">"):
                    if current_seq:
                        sequences.append(current_seq)
                        current_seq = ""
                else:
                    current_seq += line
            
            if current_seq:
                sequences.append(current_seq)
        
        sequences = [seq.upper() for seq in sequences]
        
        if len(sequences) < 2:
            print("Error: Need at least 2 sequences")
            return None
        
        # Find ONE longest common substring
        result = find_longest_common_substring(sequences)
        
        return result
                
    except FileNotFoundError:
        print(f"Error: File not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    fasta_path = "/home/cfneira1/bioinfo/rosalind_lcsm.txt"
    result = solve_lcsm(fasta_path)
    
    if result:
        print(result) 
    else:
        print("No common substring found")
