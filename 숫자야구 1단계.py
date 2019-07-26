import random

start= 'Y'

while start == 'Y' :
    num=[]      #답 리스트 초기화
    while len(num)<3:       #길이가 3가 될 때까지
        ran = random.randrange(0,10)        #0~10사이 숫자중 랜덤수
        if ran in num :     #예외처리
            continue       #중복되면 돌아가시오
        else :
            num.append(ran)  #중복 없으면 리스트에 삽입
    print('답이 결정되었습니다')
    print(list(num))
    
    while True :
        answer=[]
        ballcnt = 0
        strkcnt = 0         #사용자 제출 답 리스트와 ball count, strike count 초기화
        answer.append(int(input('첫번째 숫자를 입력하세요 : ')))
        answer.append(int(input('두번째 숫자를 입력하세요 : ')))
        answer.append(int(input('세번째 숫자를 입력하세요 : ')))
        
        for i in range(3):      #3개의 랜덤수를 비교
            if num[i]==answer[i] :      #위치와 값이 같으면
                strkcnt += 1        #strike count를 1 증가
            else :
                if num[i] in answer :       #strike가 아니고 값만 같다면
                    ballcnt += 1    #ball count를 1 증가
        
        print('strike가 ',strkcnt,'개 입니다')   #strike 갯수 출력
        print('ball이 ',ballcnt, '개 입니다')    #ball 갯수 출력
        if strkcnt == 3 :       #strike가 3개이면
            print('정답입니당')
            break               #r게임 끝
        if strkcnt==0 and ballcnt==0 :      #stike와 ball이 한개도 없으면
            print('아웃입니다.')     #아웃
            continue                #다시 답을 제출하도록
        
    start = input('계속 하시겠습니까?')     #게임이 반복 되도록
