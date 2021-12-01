import os


def lag_fibb(a = 17, b = 5):
    n = a + 1
    k = [1, 1]
    while True:
        for i in range(2, a + 1):
            temp = k[i - 1] + k[i - 2]
            k.append(temp)
        #k = [0.1, 0.7, 0.3, 0.9, 0.5]
        if k[n - a] >= k[n - b]:
            k_i = k[n - a] - k[n - b]
        else:
            k_i = k[n - a] - k[n - b] + 1
        k.insert(n, abs(k_i))
        n += 1
        yield k[-1]

def fibb(a = 17, b = 5):
    while True:
        r = (a + b) % 253
        a, b = b, r
        yield r


numbers = []
fibbon_num = fibb()

for _ in range(4):
    numbers.append(next(fibbon_num))

numbers += [0x55, 0xAA, [0x92, 0x49, 0x24], [0x49, 0x24, 0x92], [0x24, 0x92, 0x49], 0x00, 0x11, 0x22, 0x33, 0x44, 0x55,
            0x66, 0x77, 0x88, 0x99, 0xAA, 0xBB, 0xCC, 0xDD, 0xEE, 0xFF, [0x92, 0x49, 0x24], [0x49, 0x24, 0x92], [0x24, 0x92, 0x49],
            [0x6D, 0xB6, 0xDB], [0xB6, 0xDB, 0x6D], [0xDB, 0x6D, 0xB6]]

for _ in range(4):
    numbers.append(next(fibbon_num))

for i in range(35):
    if isinstance(numbers[i], list):
        numbers[i] = bytes(numbers[i])
    else:
        numbers[i] = numbers[i].to_bytes(2, 'big')

print(numbers)
print('Enter file path:')
file_path = input()
file_path = r'{}'.format(file_path)

print('Choice type of recording for your hard drive disk: 1 - RLL(1,7), 2 - RLL(2,7), 3 - MFM')
type_record = int(input())
while type_record < 1 or type_record > 3:
    print('Choice type of recording for your hard drive disk: 1 - RLL(1,7), 2 - RLL(2,7), 3 - MFM')
    type_record = int(input())

with open(file_path, 'rb+') as file:
    file.seek(0, os.SEEK_END)
    leng = file.tell()

for i in range(35):
    file = open(file_path, 'rb+')
    file.seek(0)
    if type_record == 1:
        if (5 < i < 9) or (24 < i < 31):
            pass
        else:
            for j in range(leng):
                file.write(numbers[i])
    elif type_record == 2:
        if (2 < i < 6) or (9 < i < 12) or (12 < i < 15) or (15 < i < 18) or (18 < i < 21) or (21 < i < 24):
            pass
        else:
            for j in range(leng):
                file.write(numbers[i])
    elif type_record == 3:
        if (8 < i < 14) or (14 < i < 19) or (19 < i < 25) or (27 < i < 31):
            pass
        else:
            for j in range(leng):
                file.write(numbers[i])
    file.close()





