list = ['a', 'b', 'c', 'd', 'e']
import random                    #이게 있어야지 랜덤이 실행됨
print(random.random())           #0~1사이의 난수
print(random.randrange(1,6))     #1~5사이 랜덤값 발생
menu = ['짜장면','짬뽕','육개장','칼국수']
print(random.choice(menu))       #list중에서 한개 그냥 고름
random.shuffle(list)             #먼저 셔플로 리스를 섞어야함
print(list)                      #그리고나서 출력함
print(random.choice([True, False])) # 트루 펄스중 한개 랜덤으로 고름
                                    # 그런데 트루, 펄스를 소문자로 쓰면 안됨. 반드시 앞에 t, f가 대문자여야 함
