n1, n2, n3, n4 = [int(i) for i in input().split('.')]
m1, m2, m3, m4 = [int(i) for i in input().split('.')]

def mask_is_correct(m1, m2, m3, m4):
    if m1 == m2 == m3 == m4 == 255 or m1 == m2 == m3 == m4 == 0:
        return True 
    elif m1 == m2 == m3 == 255 and m4 in [254, 252, 248, 240, 224, 192, 128, 0]:
        return True
    elif m1 == m2 == 255 and m3 in [254, 252, 248, 240, 224, 192, 128, 0] and m4 == 0:
        return True
    elif m1 == 255 and m2 in [254, 252, 248, 240, 224, 192, 128, 0] and m3 == m4 == 0:
        return True
    else:
        return False

def IP_address_is_correct(n1, n2, n3, n4):
    if (n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0) or (n1 == 255 and n2 == 255 and n3 == 255 and n4 == 255):
        return False
    elif 0 <= n1 <= 255 and 0 <= n2 <= 255 and 0 <= n3 <= 255 and 0 <= n4 <= 255:
        return True
    else:
        return False

if IP_address_is_correct(n1, n2, n3, n4) and mask_is_correct(m1, m2, m3, m4):
    print(n1 & m1, n2 & m2, n3 & m3, n4 & m4, sep = '.')
else:
    print('Валидация не пройдена')