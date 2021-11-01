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
#라운드 돌리는 함수(1 바이트씩 돌림)
def round(var, rnd):
    rndv = list(var)#쪼갬
    rnc = len(rndv)#쪼갠 바이트 수

    i = 0
    res = []
    while i < len(rndv):#바이트값 맞을때까지 반복

        i2 = 0
        rnd_var = rndv[i:i+8]

        while i2 < rnd%8:

            i2 = i2 + 1
            popv = rnd_var.pop()
            rnd_var.insert(0,popv)#섞음


        res = res + rnd_var#값을 더함

        i = i+8

    i=0
    res2=''
    lent = len(res)
    while i < lent:#결과값

        res2 = res2+res.pop(0)

        i=i+1


    return res2
#인코딩 함수
def enc(var, key):
    varv = list(var)
    keyv = list(key)

    i=0
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

    return res
#문자열, 키 변환
def baseenc(var, key):
    var = var.encode('utf-8')#문자열
    key = key.encode('utf-8')#키값

    hex_var = binascii.hexlify(var).decode('utf-8')  # 암호화 할 문자열(16진수)

    hex_key = binascii.hexlify(key).decode('utf-8')  # 키값(역시 16진수)

    return hex_var, hex_key

var = input('어떤 내용을 암호화 하실건가요?')
key = input('키는 무엇인가요?')

var, key = baseenc(var, key)#키값, 문자열 인코딩

clzkey = clz(int(key, 16))#콜라츠값
var = enc(var, key)#인코딩

var = round(var, clzkey)#라운드


print('암호화된 값은', var, '입니다')