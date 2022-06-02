bo = ['A','I','U','E','O']
shi = ['K','M','N','R','W']
f = open('result.txt', 'a')
for s1 in range(0, len(shi)):
    for s2 in range(0, len(shi)):
        if (s1 == s2):
            continue
        for s3 in range(0, len(shi)):
            if (s1 == s3 or s2 == s3):
                continue
            for s4 in range(0, len(shi)):
                if (s1 == s4 or s2 ==s4 or s3 == s4):
                    continue
                for b1 in range(0, len(bo)):
                    for b2 in range(0, len(bo)):
                        if (b1 == b2):
                            continue
                        if (((s1 == 4 or s2 == 4 or s4 == 4) and (b1 != 0 and b1 != 4)) or ((s3 == 4) and (b2 != 0 and b2 != 4))):
                            continue
                        f.write(f'{shi[s1]}{bo[b1]}{shi[s2]}{bo[b1]}{shi[s3]}{bo[b2]}{shi[s4]}{bo[b1]}\n')
f.close()