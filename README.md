# Rosalind_solutions
A collection of Python solutions for [Rosalind](http://rosalind.info/) bioinformatics problems, focusing on DNA sequence analysis, pattern matching, and computational biology algorithms.

This repository contains my solutions to various Rosalind problems, implemented in Python. Each script is designed to be readable, efficient, and well-documented for learning purposes.

##Problems Solved

### String Algorithms
- **GC Content** (`gc_content.py`) - Calculate GC percentage in DNA sequences
- **Finding a Motif** (`find_motif.py`) - Locate all occurrences of a motif in DNA
- **Hamming Distance** (`hamming_distance.py`) - Count point mutations between sequences
- **Longest Common Substring** (`longest_common_substring.py`) - Find shared motifs across multiple sequences

### Combinatorics & Recursion
- **Fibonacci Rabbits** (`rabbit_pairs.py`) - Model rabbit population growth with recurrence relations.

## Installation

### Prerequisites
- Python 3.7 or higher
- No external libraries required (uses only Python standard library)

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/rosalind-solutions.git

# Navigate to the directory
cd rosalind-solutions

# Run any script
python3 gc_content.py
```

## Usage

### General Pattern

All scripts follow a similar structure:
```python
# Read input from FASTA file
python3 script_name.py

# Or modify the file path in the script:
fasta_path = "/path/to/your/input.txt"
```

