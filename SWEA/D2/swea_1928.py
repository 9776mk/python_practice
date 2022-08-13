base_64= { 'A' : 0, 'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25,
         'a':26,'b':27,'c':28,'d':29,'e':30,'f':31,'g':32,'h':33,'i':34,'j':35,'k':36,'l':37,'m':38,'n':39,'o':40,'p':41,'q':42,'r':43,'s':44,'t':45,'u':46,'v':47,'w':48,'x':49,'y':50,'z':51,
         '0':52,'1':53,'2':54,'3':55,'4':56,'5':57,'6':58,'7':59,'8':60,'9':61,'+':62,'/':63}

T = int(input())

for test_case in range(1,T+1):
    byte_1 = ""
    decoded_text = ""
    encoded_text = list(input())
    
    # 각 알파벳을 base_64 딕셔너리를 이용해 숫자로 바꾸고, 바꾼 숫자를 2진수로 변경후 0을 채워 6글자 만들기
    # ex) 'A' -> 0 -> 000000, 'T' -> 19 -> 010011
    # format(str, 'b')는 str을 2진수로 바꿈. a.zfill(n)은 n자리가 되도록 a 앞에 0 추가
    for text in encoded_text:
        byte_1 += str(format(base_64[text],'b').zfill(6)) 

    # 원래의 1byte 글자의 길이가 되도록 decode할 횟수를 위해 8로 나눔.
    len_decode = int(len(byte_1)/8)

    # 2진수를 8자리씩 끊은 후, 10진수로 바꾸고, 해당하는 아스키 코드값의 글자로 변환
    # int(a,n) n진수 a를 10진수로 변환
    for j in range(1, len_decode+1):
        decoded_text += chr(int(byte_1[(j-1)*8:((8*j))],2))
    print(f'#{test_case} {decoded_text}')