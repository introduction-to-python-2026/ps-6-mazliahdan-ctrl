def create_codon_dict(file_path):
    codon_to_amino_acid = {}
    rows = read_file(file_path)

    for row in rows:
        parts = row.strip().split()  
        if len(parts) < 3:
            continue

        codon = parts[0]
        amino_acid = parts[2]  

        codon_to_amino_acid[codon] = amino_acid

    return codon_to_amino_acid
