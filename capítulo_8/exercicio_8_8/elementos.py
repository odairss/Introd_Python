def calc_primos(a,b):
    div = 2
    primos = list()
    while a > 1 or b > 1:
        if a%div == 0 or b%div == 0:
            if a%div == 0:
                a /= div
            if b%div == 0:
                b /= div
            primos.append(div)            
        else:
            div += 1
    return primos


def calc_mmc(primos):
    mmc = 1
    for primo in primos:
        mmc *= primo
    return mmc
