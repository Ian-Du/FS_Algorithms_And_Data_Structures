romansDict = {
    1000: "M",
    500: "D",
    100: "C",
    50: "L",
    10: "X",
    5: "V",
    1: "I",
}


def Int_To_Roman(val_to_convert):
    result = ""
    divider = 1
    while val_to_convert >= divider:
        divider *= 10
    divider /= 10

    while val_to_convert > 0:
        multiplier = int(val_to_convert // divider)
        #print(f"{val_to_convert} {divider} {multiplier}")
        if multiplier <= 3:
            result += (romansDict[divider] * multiplier)
        elif multiplier == 4:
            result += romansDict[divider] + romansDict[divider * 5]
        elif 5 <= multiplier <= 8:
            result += romansDict[divider * 5] + (romansDict[divider] * (multiplier - 5))
        if multiplier == 9:
            result += romansDict[divider] + romansDict[divider * 10]

        val_to_convert %= divider
        divider /= 10

    return result


def Int_To_Roman_Rec(val_to_convert):
    divider = 1
    while val_to_convert >= divider:
        divider *= 10
    divider /= 10
    return Convert_Roman(val_to_convert=val_to_convert, divider=divider)


def Convert_Roman(val_to_convert, divider):
    result = ""

    if val_to_convert == 0:
        return result

    multiplier = int(val_to_convert // divider)
    #print(f"{val_to_convert} {divider} {multiplier}")
    if multiplier <= 3:
        result += (romansDict[divider] * multiplier)
    elif multiplier == 4:
        result += romansDict[divider] + romansDict[divider * 5]
    elif 5 <= multiplier <= 8:
        result += romansDict[divider * 5] + (romansDict[divider] * (multiplier - 5))
    if multiplier == 9:
        result += romansDict[divider] + romansDict[divider * 10]

    val_to_convert %= divider
    divider /= 10
    result += Convert_Roman(val_to_convert=val_to_convert, divider=divider)

    return result


print(Int_To_Roman(1999))
print(Int_To_Roman_Rec(1999))

print(Int_To_Roman(1444))
print(Int_To_Roman_Rec(1444))

print(Int_To_Roman(1786))
print(Int_To_Roman_Rec(1786))
