import itertools

def answer(M, F):
    m = int(M)
    f = int(F)
    gen = 0
    mult = 0;
    # if they are multiples/factors or both even, then it's impossible
    if (m != 1 and f != 1) and (m % f == 0 or f % m == 0 or (m % 2 == 0 and f % 2 == 0)):
        return "impossible"

    while m > 1 or f > 1:
        if m < 1 or f < 1:
            break
        if m > f:
            if f == 1:
                mult = m - 1
            else:
                mult = m // f
            m -= f * mult
        else:
            if m == 1:
                mult = f - 1
            else:
                mult = f // m
            f -= m * mult
        gen += mult
        print("gen: " + str(gen) + "   m: " + str(m) + " f: " + str(f))

    if m == 1 and f == 1:
        return gen
    else:
        return "impossible"
