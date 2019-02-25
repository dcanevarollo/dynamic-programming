# The DNA chain longest common sequence problem consists in determinate one of the possibles
# common subsequences between two DNA sequences (X and Y, for instance). If we tried to
# compare all genotypes in each sequence, we would have a time complexity O(2^n) (!).
# Thus, we run through the sequences filling an array. That array stores, practically,
# the indexes that contains a common genotype.


from numpy import zeros  # To easily manipulate the indexes array.


# Main method called that returns one common sequence and the size of it.
def lcs(dna_x, dna_y):
    seq = []  # List of genotypes on our common sequence.

    size_x = len(dna_x)
    size_y = len(dna_y)

    # First we create an array of zeros.
    # The first line and column of it will always be 0. So we
    # need an array that can store all DNA sequences.
    common_array = zeros((size_x+1, size_y+1), dtype=int)

    for i in range(1, size_x+1):
        for j in range(1, size_y+1):
            if dna_x[i-1] == dna_y[j-1]:
                common_array[i][j] = common_array[i-1][j-1] + 1
            else:
                common_array[i][j] = max(common_array[i][j-1], common_array[i-1][j])

        # Considering the last column of the array, when an increments is noticed, that is,
        # the last element of the current line is one unit larger than the last element
        # of the previous line, my common sequence receives the genotype on that DNA X index.
        if common_array[i][-1] > common_array[i-1][-1]:
            seq.append(dna_x[i-1])

    return common_array[-1][-1], seq  # The last element of the array stores the size of the common sequence.


if __name__ == "__main__":
    dnas = []

    print("<DNAs separated with blank spaces>")
    for i in range(2):
        dnas.append(input("\nDNA " + str(i+1) + "\n> ").split(" "))

    seq_size, seq = lcs(dnas[0], dnas[1])

    print("\nFound %i common genotypes in this possible subsequence:\n<" % seq_size, end=' ')
    print(*seq, end=' ')
    print(">")
