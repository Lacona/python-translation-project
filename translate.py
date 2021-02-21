#! /usr/bin/env python3

import sys

def translate_sequence(rna_sequence, genetic_code):
    """Translates a sequence of RNA into a sequence of amino acids.

    Translates `rna_sequence` into string of amino acids, according to the
    `genetic_code` given as a dict. Translation begins at the first position of
    the `rna_sequence` and continues until the first stop codon is encountered
    or the end of `rna_sequence` is reached.

    If `rna_sequence` is less than 3 bases long, or starts with a stop codon,
    an empty string is returned.

    Parameters
    ----------
    rna_sequence : str
        A string representing an RNA sequence (upper or lower-case).

    genetic_code : dict
        A dictionary mapping all 64 codons (strings of three RNA bases) to
        amino acids (string of single-letter amino acid abbreviation). Stop
        codons should be represented with asterisks ('*').

    Returns
    -------
    str
        A string of the translated amino acids.
    """    
    rna_sequence = rna_sequence.upper()
    #protein = []
    #for i in range(0, len(rna_sequence)-(3+len(rna_sequence)%3), 3):
        #if genetic_code[rna_sequence[i:i+3]] == "*":
            #break
        #protein += genetic_code[rna_sequence[i:i+3]]
    #return "".join(protein)

    rna_sequence = rna_sequence.upper()
    peptide = []
    print("\n\nOriginal rna_sequence: " + rna_sequence)    
#    while True:
#        if len(rna_sequence) < 3:
#            break
#    print("\n\nOriginal rna_sequence: " + rna_sequence)
#        codon, remaining_sequence = next_codon(rna_sequence)
#        rna_sequence = remaining_sequence
#        aa = genetic_code[codon]
    if len(rna_sequence) > 2:
        print("in if len(rna_sequence)%3 == 0")
        for i in range(0, len(rna_sequence),3):
            print("for i in range")
            codon = rna_sequence[i:i + 3]
            print(codon)            
            if len(codon) < 3:
                print(rna_sequence)                
                break
            elif genetic_code[codon] == "*":
                print("*")                
                break
            peptide += genetic_code[codon]    
    return "".join(peptide)
    
def get_all_translations(rna_sequence, genetic_code):
    """Get a list of all amino acid sequences encoded by an RNA sequence.

    All three reading frames of `rna_sequence` are scanned from 'left' to
    'right', and the generation of a sequence of amino acids is started
    whenever the start codon 'AUG' is found. The `rna_sequence` is assumed to
    be in the correct orientation (i.e., no reverse and/or complement of the
    sequence is explored).

    The function returns a list of all possible amino acid sequences that
    are encoded by `rna_sequence`.

    If no amino acids can be translated from `rna_sequence`, an empty list is
    returned.

    Parameters
    ----------
    rna_sequence : str
        A string representing an RNA sequence (upper or lower-case).

    genetic_code : dict
        A dictionary mapping all 64 codons (strings of three RNA bases) to
        amino acids (string of single-letter amino acid abbreviation). Stop
        codons should be represented with asterisks ('*').

    Returns
    -------
    list
        A list of strings; each string is an sequence of amino acids encoded by
        `rna_sequence`.
    """
    def gen_reading_frames(rna_sequence, genetic_code):
        """Generate the six reading frames of a DNA sequence"""
        """including reverse complement"""
    
        frames = []
        frames.append(translate_sequence(sequence, 0))
        frames.append(translate_sequence(sequence, 1))
        frames.append(translate_sequence(sequence, 2))
	frames.append(translate_sequence(reverse_and_complement(sequence), 0))
	frames.append(translate_sequence(reverse_and_complement(sequence), 1))
	frames.append(translate_sequence(reverse_and_complement(sequence), 2))
	return frames    
	print('[9] + Reading_frames:')
	rna_sequence=rna_sequence.upper()
	for frames in gen_reading_frames(rna_sequence):
	print(frames)

	def proteins_from_rf(aa_seq):
	    """Compute all possible proteins in an aminoacid"""
	    """seq and return a list of possible proteins"""
	    current_prot = []
	    proteins = []
	    for aa in aa_seq:
		if aa == "*":
		    # STOP accumulating amino acids if _ - STOP was found
		    if current_prot:
			for p in current_prot:
			    proteins.append(p)
			current_prot = []
		else:
		    # START accumulating amino acids if M - START was found
		    if aa == "M":
			current_prot.append("")
		    for i in range(len(current_prot)):
			current_prot[i] += aa
	    return proteins
	    print(proteins_from_rf(['I', 'M', 'T', 'H', 'T',
				'Q', 'G', 'N', 'V', 'A', 'Y', 'I', '_']))

	def all_proteins_from_orfs(seq, startReadPos=0, endReadPos=0, ordered=False:
	    """Compute all possible proteins for all open reading frames"""
	    """Protine Search DB: https://www.ncbi.nlm.nih.gov/nuccore/NM_001185097.2"""
	    """API can be used to pull protein info"""
	    if endReadPos > startReadPos:
		rfs = gen_reading_frames(seq[startReadPos: endReadPos])
	    else:
		rfs = gen_reading_frames(seq)

	    res = []
	    for rf in rfs:
		prots = proteins_from_rf(rf)
		for p in prots:
		    res.append(p)

	    if ordered:
		return sorted(res, key=len, reverse=True)
	    return res

	print('\n[10] + All prots in 6 open reading frames:')
	for prot in all_proteins_from_orfs(rna_sequence, 0, 0, True):
	    print(f'{prot}')

def get_reverse(sequence):
    """Reverse orientation of `sequence`.

    Returns a string with `sequence` in the reverse order.

    If `sequence` is empty, an empty string is returned.

    Examples
    --------
    >>> get_reverse('AUGC')
    'CGUA'
    """
    sequence=sequence.upper()    
    return sequence [::-1]

def get_complement(sequence):
    """Get the complement of a `sequence` of nucleotides.

    Returns a string with the complementary sequence of `sequence`.

    If `sequence` is empty, an empty string is returned.

    Examples
    --------
    >>> get_complement('AUGC')
    'UACG'
    """
    sequence=sequence.upper()
    complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
    return "".join(complement[n] for n in sequence)
    

def reverse_and_complement(sequence):
    """Get the reversed and complemented form of a `sequence` of nucleotides.

    Returns a string that is the reversed and complemented sequence
    of `sequence`.

    If `sequence` is empty, an empty string is returned.

    Examples
    --------
    >>> reverse_and_complement('AUGC')
    'GCAU'
    """
    return get_complement(sequence[::-1])

def get_longest_peptide(rna_sequence, genetic_code):
    """Get the longest peptide encoded by an RNA sequence.

    Explore six reading frames of `rna_sequence` (the three reading frames of
    `rna_sequence`, and the three reading frames of the reverse and complement
    of `rna_sequence`) and return (as a string) the longest sequence of amino
    acids that it encodes, according to the `genetic_code`.

    If no amino acids can be translated from `rna_sequence` nor its reverse and
    complement, an empty string is returned.

    Parameters
    ----------
    rna_sequence : str
        A string representing an RNA sequence (upper or lower-case).

    genetic_code : dict
        A dictionary mapping all 64 codons (strings of three RNA bases) to
        amino acids (string of single-letter amino acid abbreviation). Stop
        codons should be represented with asterisks ('*').

    Returns
    -------
    str
        A string of the longest sequence of amino acids encoded by
        `rna_sequence`.
    """
    pass


if __name__ == '__main__':
    genetic_code = {'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'GUU': 'V', 'CAC': 'H', 'ACG': 'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': '*', 'GGA': 'G', 'UAC': 'Y', 'GAC': 'D', 'UAG': '*', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'GCU': 'A', 'GAA': 'E', 'AUU': 'I', 'UUG': 'L', 'UUA': 'L', 'UGA': '*', 'UUC': 'F'}
    rna_seq = ("AUG"
            "UAC"
            "UGG"
            "CAC"
            "GCU"
            "ACU"
            "GCU"
            "CCA"
            "UAU"
            "ACU"
            "CAC"
            "CAG"
            "AAU"
            "AUC"
            "AGU"
            "ACA"
            "GCG")
    longest_peptide = get_longest_peptide(rna_sequence = rna_seq,
            genetic_code = genetic_code)
    assert isinstance(longest_peptide, str), "Oops: the longest peptide is {0}, not a string".format(longest_peptide)
    message = "The longest peptide encoded by\n\t'{0}'\nis\n\t'{1}'\n".format(
            rna_seq,
            longest_peptide)
    sys.stdout.write(message)
    if longest_peptide == "MYWHATAPYTHQNISTA":
        sys.stdout.write("Indeed.\n")
