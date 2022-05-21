print('一次合同方程式\n\n')
while True:

    a: int = []
    b: int = []
    r: int = []
    q: int = []

    print('[a]x ≡ 1 (mod [N])\n')
    #input
    a.append(int(input('>[a]: ')))
    b.append(int(input('>[N]: ')))

    #preview
    print(f'\n{a[0]}x ≡ 1 (mod {b[0]})')

    if 0 < a[0] or 0 < b[0]: #Check suitability
        i = 0
        print('\n--- ユークリッドの互除法 ---')

        #Euclid
        while True:
            q.append(a[i] // b[i])
            r.append(a[i] % b[i])
            print(f'  {a[i]} = {b[i]} × {q[i]} + {r[i]}')

            if r[i] == 0:
                break
            a.append(b[i])
            b.append(r[i])
            i += 1
        print('\n  最大公約数 = ', b[i],'\n\n')

        #Hute-Ho-Te-Shiki
        print('--- 不定方程式 ---')
        P = [''] * (i+1)
        P[i] = 1
        while i != 0:
            P[i-1] =  -int(((P[i] * a[i-1])-1) / a[i])
            print(f'  1 = {P[i]} × {a[i-1]} + {P[i-1]} × {a[i]}')
            i -= 1

        #Output
        print('\n')
        print(f'  x ≡ {P[i+1]}')
        print(f'  y ≡ {P[i]}')
        print(f'  y ≡ {P[i+1]} (mod {a[i+1]})')

        if str(input('\n>exit?(y or n): ')) == 'y': #loop break
            break
    else:
        print('0むりです') #ERROR msg

