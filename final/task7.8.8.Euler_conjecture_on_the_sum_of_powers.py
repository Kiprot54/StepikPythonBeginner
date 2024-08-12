print('Гипотеза Эйлера о сумме степеней')
print()

for e in range(4, 151):
    e5 = e ** 5
    for a in range(1, 151):
        a5 = a ** 5
        if a5 >= e5:
            break
        else:
            for b in range(a, 151):
                b5 = b ** 5
                ab5 = b5 + a5
                if ab5 >= e5:
                    break
                else:
                    for c in range(b, 151):
                        c5 = c ** 5
                        abc5 = ab5 + c5
                        if abc5 > e5:
                            break
                        else:
                            for d in range(c, 151):
                                d5 = d ** 5
                                abcd5 = abc5 + d5
                                if abcd5 == e5:
                                    print(a + b + c + d + e)
                                    break
                                elif abcd5 > e5:
                                    break
