import turtle as t

t.shape("arrow")            # 화살표 모양으로 설정

t.bgcolor("black")          # 배경 화면색을 검정색으로 설정
t.color("red")              # 펜 색상을 노란색으로 설정
t.speed(0)                  # 속도 최고로 설정
t.pensize(2)                # 펜 크기 2로 설정

n=110                       # n을 110으로 설정
for x in range(n):          # n번 반복
    t.forward(100)          # 앞으로 100만큼 이동
    t.left(n+1)             # 왼쪽으로 n+1만큼 회전
    t.color("white")        # 펜 색상을 흰색으로 설정
    t.circle(100)           # 반지름이 100인 원 그리기
    t.left(10)              # 왼쪽으로 10만큼 회전
    t.color("blue")         # 펜 색상 파랑색으로 설정
    t.forward(70)           # 앞으로 70만큼 이동
    t.left(90)              # 왼쪽으로 90만큼 회전
    t.color("yellow")       # 펜 색상 노랑색으로 설정



