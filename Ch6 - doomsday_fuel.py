from fractions import Fraction
import fractions


def lcm(a, b):
    return (a * b) // fractions.gcd(a, b)


def transposeMatrix(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t


def getMatrixMinor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def getMatrixDeterminant(m):
    # base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * m[0][c] * getMatrixDeterminant(getMatrixMinor(m, 0, c))
    return determinant


def getMatrixInverse(m):
    determinant = getMatrixDeterminant(m)
    # special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1] / determinant, -1 * m[0][1] / determinant],
                [-1 * m[1][0] / determinant, m[0][0] / determinant]]

    # find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m, r, c)
            cofactorRow.append(((-1) ** (r + c)) * getMatrixDeterminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors


def answer(m):
    initialIsTerm = False
    if sum(m[0]) == 0:  # if initial state is a terminal state
        initialIsTerm = True

    # find which rows are terminals
    terms = []
    for row in m:
        terms.append(sum(row) == 0)
    print("initial terminals: " + str(terms))

    # move all terminal rows to the bottom, and swap columns to account for row swaps
    for i in range(len(m)):
        try:
            if terms[i] and terms[i:].index(
                    False):  # if the current state is terminal, and a non-terminal state exists after it
                # swap the rows
                swapWith = terms[i:].index(False) + i
                terms[i], terms[swapWith] = terms[swapWith], terms[i]
                m[i], m[swapWith] = m[swapWith], m[i]
                # swap the corresponding columns
                for row in m:
                    row[i], row[swapWith] = row[swapWith], row[i]
        except ValueError as e:
            pass

    print("after sorting: " + str(terms))
    numTerms = len(terms) - terms.index(True)
    print("number of terminal states:", numTerms)

    if initialIsTerm:
        ans = []
        ans.append(1)
        for i in range(numTerms - 1):
            ans.append(0)
        ans.append(1)
        return ans

    # normalize rows
    for i in range(len(m)):
        if not terms[i]:
            total = sum(m[i])
            for j in range(len(m[0])):
                m[i][j] = Fraction(m[i][j], total)
    print("m after sorting and normalizing:")
    for row in m:
        print(row)

    # isolate Q from m
    Q = []
    for row in m[:len(m) - numTerms]:
        temp = []
        for element in row[:len(m) - numTerms]:
            temp.append(element)
        Q.append(temp)

    # isolate R from m
    R = []
    for row in m[:len(m) - numTerms]:
        temp = []
        for element in row[len(m) - numTerms:]:
            temp.append(element)
        R.append(temp)

    # calculate N, which is (Q - I)^-1
    # first, produce identity matrix
    I = []
    for i in range(len(Q)):
        temp = []
        for j in range(len(Q)):
            temp.append(int(i == j))
        I.append(temp)

    # I becomes I - Q
    for i in range(len(I)):
        for j in range(len(I)):
            I[i][j] -= Q[i][j]

    # calculate inverse of I - Q and assign it to N
    N = getMatrixInverse(I)

    B = []
    for i in range(len(N)):
        temp = []
        for j in range(len(R[0])):
            result = 0
            for k in range(len(R)):
                result += N[i][k] * R[k][j]
            temp.append(result)
        B.append(temp)
    print("B[0]: " + str(B[0]))

    # take only first row of B, calculate and apply denominator
    ans = B[0]
    denom = 1
    # calculate lowest common denominator
    for fraction in ans:
        denom = lcm(fraction.denominator, denom)
    # change ans to only numerators and multiply them appropriately to match denominator
    for i in range(numTerms):
        ans[i] = ans[i].numerator * int(denom / ans[i].denominator)
    ans.append(denom)
    print("answer: " + str(ans))
    return ans


#inputMatrix = [[1, 2, 1], [3, 1, 1], [5, 2, 1]]
# inputMatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# inputMatrix = [[0, 2, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0]]
# inputMatrix = [[0, 0, 1, 2, 0], [0, 3, 0, 0, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
inputMatrix = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# inputMatrix = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
answer(inputMatrix)
