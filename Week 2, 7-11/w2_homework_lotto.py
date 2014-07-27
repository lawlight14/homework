#	-*- coding: utf-8 -*-
#
#	< 로또 숫자 6개 조합을 10만 개 출력하는 프로그램 >
#	
#	lotto_print() 함수는 "lotto_list"라는 리스트를 
#	"lotto_result.txt" 라는 텍스트 파일에 쓰는 역할을 합니다.
#	
#	"건드리지 마세요!" 라고 되어있는 부분은 반드시 그대로 두세요!
#	모르셔도 아무 상관없는 부분입니다.
#
#	================	여러분이 구현하실 내용	====================
#	"1 ~ 35 " 숫자 중에서 6개를 랜덤으로 만들어내는데 총 10만 번 반복해주세요.
#	(로또는 45까지이지만 우리는 35까지! - 그 이유는 당첨확률을 높여드리기 위함입니다^^)
#	반드시 "lotto_list" 에 총 10만 쌍의 로또 번호를 모두 넣어주세요!
#	올바른 방법으로 6개를 랜덤으로 만들어낸다면 6개 숫자들끼리 중복은 없습니다.
#
#	그리고 반드시 6개의 숫자는 오름차순으로 정렬이 되어야합니다! 예를 들면,
#	[33, 2, 24, 11, 9, 16]	이렇게 되어있는 리스트를
#	[2, 9, 11, 16, 24, 33]	이렇게 오름차순으로 정렬해주어야 합니다.
#
#	아마도 [2, 9, 11, 16, 24, 33] 이런 리스트를 총 10만 번 만들어주셔야 할겁니다.
#	
#	성공적으로 완성했다면 같은 폴더에 있는 "lotto_result.txt" 파일을 열어보세요.
#	아래처럼 랜덤한 6개의 숫자가 10만 줄 보이신다면 성공입니다.
#
#	[2, 9, 11, 16, 24, 33]
#	[5, 6, 15, 22, 28, 31]
#	.....(생략)
#	[1, 15, 20, 21, 30, 35]
#
import random

#	33~42줄 건드리지 마세요!
def lotto_print(list_x):
	for index, item in enumerate(list_x):
		f.write(str(item))
		if index != len(list_x)-1:
			f.write("\n")

f = open("lotto_result.txt", "w")

lotto_list = [ ]
#	위의 "lotto_list" 리스트에 총 10만 쌍의 로또 번호를 모두 넣어주세요!



#	이 공간에 코드를 작성 
for i in range(100000):
    single_list = []
    for j in range(6):
        while(True):
            num = random.randint(1,35)
            if(num not in single_list):
                single_list.append(num)
                break
    single_list.sort()
    lotto_list.append(single_list)

#	아래 두 줄 건드리지 마세요!
lotto_print(lotto_list)
f.close()
#	코드 끝 
