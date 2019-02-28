# That optimization problem involves matrices multiplication. That is, considering and array chain
# <A1, A2, ..., An>, which of the order of multiplications of this chain will return the least number
# of scalar multiplications?

# That dynamic implementation has a O(n^3) time complexity class when the recursive has a O(2^n).
from numpy import zeros


# Helper class to store the information of the read matrices.
class Matrix:
    def __init__(self, lines, columns):
        self.lines = int(lines)
        self.columns = int(columns)


# Method that prints the optimal matrices chain.
def print_chain(brackets, i, j):
    if i == j:
        print("A" + str(i), end=' ')
        return None

    print("( ", end='')

    print_chain(brackets, i, brackets[i][j])
    print_chain(brackets, brackets[i][j] + 1, j)

    print(") ", end='')


# p = <p0, p1, p2, p3..., pn>, where the dimension of the Ai matrix is pi-1,pi. That is,
# p is actually the dimensions array of our matrices on the chain.
# For instance, dimension of A3 is p2,p3.
def matrix_chain_order(dimensions, dim_size):
    # The 'm' array stores the minimum number of scalar multiplications needed.
    # We initialize it with zeros to simplify the code.
    m = zeros((dim_size, dim_size), dtype=int)
    # 'brackets' array stores the chain position that contains parentheses.
    brackets = zeros((dim_size, dim_size), dtype=int)

    # Cost is zero when multiplying one matrix.
    if dim_size == 1:
        raise RuntimeError

    if dim_size == 2:
        m[1][-1] = dimensions[0]*dimensions[1]

    # 'l' variable used to run through the p array
    for l in range(2, dim_size):
        for i in range(1, dim_size - l + 1):
            j = i+l-1

            for k in range(i, j):
                m[i][j] = m[i][k] + m[k+1][j] + dimensions[i - 1] * dimensions[k] * dimensions[j]
                # 'k' is the optimal break point of the multiplication interval <Ai...j>
                brackets[i][j] = k

    # Returns the minimum number of scalar multiplications needed and the brackets indexes array.
    return m[1][-1], brackets


if __name__ == "__main__":
    matrices = []
    dimensions = []

    try:
        i = 0
        chain_size = int(input("Number of matrices in the chain\n> "))
        while i < chain_size:
            print("\nMatrix " + str(i))
            matrices.append(Matrix(input("Lines\n> "), input("Columns\n> ")))
            # Remember that to a matrices multiplication be possible the lines number of the 1st matrix
            # should be equal to the columns number of the 2nd.
            # Thus, we just need to store in 'p' array the matrices lines.
            if i != 0 and matrices[i-1].columns != matrices[i].lines:
                print("\nERROR!\nThe number of lines of this matrix should be equal to the previous columns.")
                matrices.pop(-1)
                # Repeat the insertion on the index i
                continue

            dimensions.append(matrices[i].lines)
            i += 1

        dim_size = len(dimensions)
        min_mult, brackets_array = matrix_chain_order(dimensions, dim_size)

        print("\nOptimal parenthesization\n> ", end='')
        print_chain(brackets_array, 0, dim_size-1)
        print("\n%i scalars multiplications needed." % min_mult)
    except ValueError:
        print("\nJust integers, please. Try again.")
    except RuntimeError:
        print("\nYou cannot multiply just one matrix.")
    finally:
        exit(0)
