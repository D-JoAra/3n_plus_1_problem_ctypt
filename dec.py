import binascii

#콜라츠 함수
def clz(inp):
    res = 0
    while True:
        if inp == 1:
            break
        if inp%2 == 1:
            inp = 3*inp + 1
            res = res + 1
        else:
            inp = int(inp/2)
            res = res + 1

    return res
#디코딩 함수
def dec(var, key):
    varv = list(var)
    keyv = list(key)
    i = 0
    i2 = 0
    res = ''

    while i < len(varv):

        if len(varv) == i:
            break
        a = int(varv[i], 16)


        if len(keyv) == i2:
            i2 = 0

        b = int(keyv[i2], 16)

        c = a^b
        res = res + str(format(c, 'x'))
        i = i + 1
        i2 = i2 + 1
    res = int(res, 16)
    return res
#역 라운드 함수
def decr(var, rnd):
    rndv = list(var)#쪼갬
    rnc = len(rndv)#쪼갠 바이트 수


    i = 0
    res = []
    while i < len(rndv):#바이트값 맞을때까지 반복

        i2 = 0
        rnd_var = rndv[i:i+8]

        while i2 < len(rndv[1:i+8]) - rnd%8 + 1:

            i2 = i2 + 1
            popv = rnd_var.pop()
            rnd_var.insert(0,popv)#다시


        res = res + rnd_var#값을 더함

        i = i+8


    i=0
    res2=''
    lent = len(res)
    while i < lent:#결과값

        res2 = res2+res.pop(0)

        i=i+1


    return res2
#키 16진수화
def tohex(key):

    key = key.encode('utf-8')
    hex_key = binascii.hexlify(key).decode('utf-8')  # 키값(16진수)

    return hex_key

var = input('무엇을 디코딩 하시겠어요?')
key = input('키는 무엇인가요?')

key = tohex(key)

clzkey = clz(int(key, 16))#콜라츠 키

var = decr(var, clzkey)
var = dec(var, key)
var = binascii.unhexlify(format(var, 'x')).decode('utf-8')


print("복호화된 값은 '", var, "' 입니다")
