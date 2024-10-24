#!/usr/bin/env python3

#Figuring out the number of contigs in the file named: ecoli_0.25.contigs.fasta

def count_configs_in_fasta(file_path):
    with open(file_path,'r') as fasta_file:
        count = 0
        for line in fasta_file:
            if line.startswith('>'):
                count +=1
    return count

if __name__ == "__main__":
    fasta_file_path = 'ecoli_0.25.contigs.fasta'
    num_configs = count_configs_in_fasta(fasta_file_path)
    print(f"Number of configurations in the FASTA file: {num_configs}")

#Finding the shortest contig

def count_configs_and_find_extreme_contigs(file_path):
    with open(file_path, 'r') as fasta_file:
        count = 0
        shortest_contig = None
        longest_contig = None
        shortest_length = float('inf')
        longest_length = 0
        total_length = 0
        contig_lengths =[]
        current_sequence = []

        for line in fasta_file:
            line = line.strip()
            if line.startswith('>'):
                if current_sequence:
                    sequence = ''.join(current_sequence)
                    seq_length = len(sequence)
                    total_length += seq_length
                    contig_lengths.append(seq_length)
                    count += 1

                    if seq_length < shortest_length:
                        shortest_length, shortest_contig = seq_length, sequence
                    if seq_length > longest_length:
                        longest_length, longest_contig = seq_length, sequence
                
                current_sequence = []
            else:
                current_sequence.append(line)

        # Process the last sequence if it exists
        if current_sequence:
            sequence = ''.join(current_sequence)
            seq_length = len(sequence)
            total_length += seq_length
            contig_lengths.append(seq_length)
            count += 1
            if seq_length < shortest_length:
                shortest_length, shortest_contig = seq_length, sequence
            if seq_length > longest_length:
                longest_length, longest_contig = seq_length, sequence

    # Calculate N50
    contig_lengths.sort(reverse=True)
    cumulative_length = 0
    half_total_length = total_length / 2

    for length in contig_lengths:
        cumulative_length += length
        if cumulative_length >= half_total_length:
            n50 = length
            break

    # Calculate L50
    l50 = next((length for length in contig_lengths if length >= n50), None)

    return (count, shortest_contig, shortest_length, longest_contig, longest_length,
            total_length, n50, l50)

if __name__ == "__main__":
    fasta_file_path = 'ecoli_0.25.contigs.fasta'
    (num_configs, shortest_contig, shortest_length, longest_contig, longest_length,
     total_length, n50, l50) = count_configs_and_find_extreme_contigs(fasta_file_path)

    print(f"Number of configurations: {num_configs}")
    if shortest_contig:
        print(f"Shortest contig: {shortest_contig} (Length: {shortest_length})")
    if longest_contig:
        print(f"Longest contig: {longest_contig} (Length: {longest_length})")
    print(f"Total contig length: {total_length}")
    print(f"N50: {n50}")
    print(f"L50: {l50}")
