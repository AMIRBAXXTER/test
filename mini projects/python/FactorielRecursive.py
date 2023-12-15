def factoriel(x):              # 15
    if x == 0 or x == 1:       # false
        return 1               # <--- if line 2 true
    return x * factoriel(x-1)  # 15 * factoriel (15 - 1)


print(factoriel(16))
