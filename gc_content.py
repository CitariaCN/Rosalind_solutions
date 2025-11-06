#Computing GC Content
def calculate_gc_manual(fasta_file):
    gc_percentages = {}
    current_seq_id = None
    current_seq = ""
    
    try:
        with open(fasta_file, "r") as f:
            for line in f :
                line = line.strip()
                if not line:
                    continue
                if line.startswith (">"):
                    if current_seq_id and current_seq:
                        gc_percentages[current_seq_id] = calculate_single_gc(current_seq)
                    current_seq_id = line[1:]
                    current_seq = ""
                else:
                        current_seq += line

                     
            if current_seq_id and current_seq:
                gc_percentages[current_seq_id] = calculate_single_gc(current_seq)   
                
    except FileNotFoundError:
         print(f"Error: The file '{fasta_file}' was not found.")
    except Exception as e:
         print(f"An error occurred: {e}")


    return gc_percentages
      
def calculate_single_gc(sequence):
   
    sequence = sequence.upper()     
    C = sequence.count('C')
    G = sequence.count('G')
    total_bases = len(sequence)
    if total_bases == 0:
        return 0.0

    gc_content= ((G+C)/(total_bases))* 100
    
    
    return gc_content
 
if __name__ == "__main__":
    fasta_path = "/home/cfneira1/bioinfo/rosalind_gc (2).txt"
    results = calculate_gc_manual(fasta_path)
    print (results)
