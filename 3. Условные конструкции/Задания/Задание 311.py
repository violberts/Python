n=int(input())
a = n//100
b = n//10%10
c = n%10
match a:
    case 1: print("сто")
    case 2: print("двести")
    case 3: print("триста")
    case 4: print("четыреста")
    case 5: print("пятьсот")
    case 6: print("шестьсот")
    case 7: print("семьсот")
    case 8: print("восемьсот")
    case 9: print("девятьсот")
if b == 1:
    match c:
        case 0: print("десять")
        case 1: print("одиннадцать")
        case 2: print("двенадцать")
        case 3: print("тринадцать")
        case 4: print("четырнадцать")
        case 5: print("пятнадцать")
        case 6: print("шестнадцать")
        case 7: print("семнадцать")
        case 8: print("восемнадцать")
        case 9: print("девятнадцать")
if c>0:
    match c:
        case 1: print("один")
        case 2: print("два")
        case 3: print("три")
        case 4: print("четыре")
        case 5: print("пять")
        case 6: print("шесть")
        case 7: print("семь")
        case 8: print("восемь")
        case 9: print("девять")
else:
    match b:
        case 2: print("двадцать")
        case 3: print("тридцать")
        case 4: print("сорок")
        case 5: print("пятьдесят")
        case 6: print("шестьдесят")
        case 7: print("семьдесят")
        case 8: print("восемьдесят")
        case 9: print("девяносто")
