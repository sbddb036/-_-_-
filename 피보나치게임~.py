import random

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
        
def play_game():
    print("피보나치 수열 게임에 온걸 환영해~!^^")
    score = 0

    while True:
        n = random.randint(1, 10)
        correct_answer = fibonacci(n)
        user_answer = input(f"피보나치 수열에서 {n}번째 숫자는 무엇일까요? (종료하려면 'q'입력)")

        if user_answer.lower() == 'q':
            break

        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("정답 축하해^^")
            score += 1
        else:
            print(f"아쉽다 틀렸어..정답은{correct_answer}이거야!!")
        
        
        print(f"현재 점수:{score}")
        
    print(f"게임 종료! 수고햇어 최종 점수: {score}")

if __name__ == "__main__":
    play_game()
    