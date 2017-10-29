import turtle as t         # 거북이 불러옴
import random              # random 불러옴

t.bgcolor("black")         # 배경색을 검정으로 설정
t.pencolor("white")        # 펜 색깔 흰색으로 설정

t.shape("circle")          # 거북이 모양 원으로 변경
t.speed(3)                 # 거북이 속도 7로 설정
t.up()                     # 펜 올린다.

t.goto(250,250)            # 250,250으로 이동
t.down()                   # 펜 내린다.
t.goto(250,-250)           # 250,-250으로 이동
t.goto(-250,-250)          # -250,-250으로 이동
t.goto(-250,250)           # -250,250 으로 이동
t.goto(250,250)            # 250,250으로 이동

t.up()                     # 펜 올린다.

#이쪽 벽면은 속도 빨라짐

t.goto(265,250)            # 265,250으로 이동(이쪽 벽면은 속도 빨라짐)
t.fillcolor("blue")        # 도형 채우기 파란색으로 설정
t.begin_fill()             # 도형 색채울 준비
t.down()                   # 펜 내린다
t.goto(265,-250)           # 265,-250으로 이동
t.goto(255,-250)           # 255,-250으로 이동
t.goto(255,250)            # 255,250으로 이동
t.goto(265,250)            # 265,250으로 이동
t.end_fill()               # 도형 색 채우기

t.up()                     # 펜 올린다.

#이쪽 벽면은 속도 느려짐

t.goto(-255,250)           # -255,250으로 이동(이쪽 벽면은 속도 느려짐)
t.fillcolor("yellow")      # 도형 채우기 노란색으로 설정
t.begin_fill()             # 도형 색채울 준비
t.down()                   # 펜 내린다.
t.goto(-255,-250)          # -255,-250으로 이동 
t.goto(-265,-250)          # -265,-250으로 이동
t.goto(-265,250)           # -265,250으로 이동
t.goto(-255,250)           # -255,250으로 이동
t.end_fill()               # 도형 색 채우기

t.up()                     # 펜 올린다.
t.home()                   # 사각형 가운데로 이동
t.down()                   # 펜 내린다.


angle = random.randint(1,360) # 랜덤으로 각도 1~360사이로 설정

t.setheading(angle)     # 거북이 방향 무작위로 변경

for x in range(100):
    while -250<= t.xcor() <= 250 and -250 <= t.ycor() <= 250:   # x와 y의 각도가 사각형에 맞닿으면 멈추도록 설정

         t.forward(1)           # 거북이 앞으로 1만큼 감
         a = t.heading()         # a에 현재 각도 저장


         if t.xcor() >= 250:            # 만약 오른쪽 벽면에 부딪쳤을 때
            if 270 <= a <= 360:         # 만약 오른쪽 벽면에 부딪쳤는데 각도가 270 ~ 360사이 일때
                t.setheading(180-a)     # 각도를 180-a로 변경
                t.forward(10)            # 앞으로 이동
            else:                       # 만약 오른쪽 벽면에 부딪쳤는데 각도가 270~  360사이가 아닐 때
                t.setheading(180-a)     # 각도를 180-a로 변경
                t.forward(10)            # 앞으로 이동
                
         if t.ycor() >= 250:            # 만약 위쪽 벽면에 부딪쳤을 때
             if 0 <= a <= 180:           
                t.setheading(360-a)     # 각도를 360-a로 변경
                t.forward(3)            # 앞으로 이동

         if t.xcor() <= -250:           # 만약 왼쪽 벽면에 부딪쳤는을 때
            if 180 <= a <= 270:         # 만약 왼쪽 벽면에 부딪쳤는데 각도가 180 ~ 270사이 일때
                t.speed(1)
                t.setheading(180-a)     # 각도를 180-a로 변경
                t.forward(1)            # 앞으로 이동
            else:                       # 만약 왼쪽 벽면에 부딪쳤는데 각도가 180 ~ 270사이가 아닐 때
                t.setheading(180-a)     # 각도를 180-a로 변경
                t.forward(1)            # 앞으로 이동

         if t.ycor() <= -250:           # 만약 아래쪽 벽면에 부딪쳤을 때
            if 180 <= a <= 360:
                t.setheading(360-a)     # 각도를 360-a로 변경
                t.forward(3)            # 앞으로 이동

            

