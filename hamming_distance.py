### Mismatch count

def Hdistance(seq1, seq2):

    if len(seq1) != len(seq2):
        print(f"Error: Sequences must be of equal length. seq1={len(seq1)}, seq2={len(seq2)}")
        return None
    
    mismatch_count = 0

    # Compare each position
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            mismatch_count += 1
    
    return mismatch_count


def find_mismatch(fasta_file):
    """
    Read file and calculate Hamming distance.
    Expected format:
    - First line (or sequence) is seq1
    - Second line (or sequence) is seq2
    """
    sequences = []

    try:
        with open(fasta_file, "r") as f:
            for line in f:
                line  = line.strip()
                
                if line and not line.startswith(">"):
                    sequences.append(line)

        if len(sequences) <2:
            print ("Error : file must contain at least 2 sequences")
            return None

        seq1= sequences[0].upper()
        seq2 = sequences[1].upper()

        print(f"sequence 1: {seq1}")
        print( f"sequence 2: {seq2}")
        
        Hamming_distance = Hdistance(seq1,seq2)
        
        return Hamming_distance
                
    except FileNotFoundError:
        print(f"Error: The file '{fasta_file}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Example usage with file
    fasta_path = "/home/cfneira1/bioinfo/rosalind_hamm.txt"
    result = find_mismatch(fasta_path)
    
    
    if result is not None:
        print(f"Hamming distance (mismatches): {result}")
    else:
        print("Could not calculate Hamming distance")
