def create_codon_dict(file_path):
    codon_to_amino_acid = {}
    rows = read_file(file_path)

    for row in rows:
        row_list = row.strip().split('\t')
        if len(row_list) < 3:
            continue
        codon = row_list[0]
        amino_acid = row_list[2]
        codon_to_amino_acid[codon] = amino_acid

    return codon_to_amino_acid
