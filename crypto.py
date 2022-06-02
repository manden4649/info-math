n = 26 #文字数
s = 'WVSPJL' #暗号文
l = len(s) #文字列の長さを求める
for k in range(26): #鍵を１～２５試す
    print("key = ",k)
    for i in range(l):
        ## print(s[i],"¥n")
        p = ord(s[i]) - 65
        c = (p - k) % 26
        print(chr(c+65),end="")
    print()
print("Finish¥n")