def create_codon_dict(file_path):
    file = open(file_path)
    rows = file.readlines()
    file.close()

    row = rows[0]
    clean = row.strip()
    parts = clean.split('\t')
    print(clean)
    print(parts)

    codon_dict = {}
    for row in rows:
        parts = row.strip().split('\t')
        codon = parts[0]
        aa = parts[2]
        codon_dict[codon] = aa

    return codon_dict
