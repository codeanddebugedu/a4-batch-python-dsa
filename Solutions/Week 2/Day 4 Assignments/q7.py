def harmonic_series(n: int) -> float:
    sum_harmonic = 0.0
    i = 1
    while i <= n:
        sum_harmonic += 1 / i
        i += 1
    # Round is a new function I have not taught yet, google it
    return round(sum_harmonic, 2)


print(harmonic_series(14))
