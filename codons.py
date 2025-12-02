def read_file(path):
    file = open(path)
    rows = file.readlines()
    file.close()
    return rows path = "data/codons.txt"
rows = read_file(path)
rows[0]
def create_codon_dict(file_path):
    codon_to_amino_acid = {}
    rows = read_file(file_path)

    for row in rows:
        row_list = row.strip().split('\t')
        codon = row_list[0]
        amino_acid = row_list[2] # Third cell is the amino acid abbreviation
        codon_to_amino_acid[codon] = amino_acid
    return codon_to_amino_acid
