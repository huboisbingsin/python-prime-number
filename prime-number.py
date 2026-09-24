# prime-number.py -소수구하기기본로직완성
print("1부터100 사이의소수를구합니다.")
for num in range(2, 101):
    is_prime= True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")