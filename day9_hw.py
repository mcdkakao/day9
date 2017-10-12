import turtle as t

t.shape("arrow")                # 화살표 모양으로 설정
t.bgcolor("black")              # 배경을 검으색으로 설정
t.speed(0)                      # 그리기 속도 최고로 설정

for x in range(450):            # for 반복 블록 450번 반복 설정
    if x%4 == 0:                # 450/4를 계산해 남은 나머지가 0이면 빨강색으로 설정
        t.color("red")       
    if x%4 == 1:                # 450/4를 계산해 남은 나머지가 1이면 초록색으로 설정
        t.color("green")
    if x%4 == 2:
        t.color("blue")         # 450/4를 계산해 남은 나머지가 2이면 파랑색으로 설정
    if x%4 == 3:
        t.color("white")        # 450/4를 계산해 남은 나머지가 3이면 흰색으로 설정

    t.forward(1.5 * x)          # x * 1.5 만큼 앞으로 이동

    t.left(145)                 # 왼쪽으로 145도 회전

t.hideturtle()                  # 화살표 모양 숨기


