#######################################################################################################################
# n!(n >= 0)을 반복 방식과 재귀 방식으로 각각 계산 후, 메뉴를 통해 실행 방식을 선택/비교할 수 있는 인터랙티브 콘솔 프로그램
# 작성자 : 20220803 백창륜
# 작성일 : 2025-09-26
# 최종 수정일 : 2025-10-02
#######################################################################################################################

import time

TEST = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]

# ValueError 예외 처리 아니었으면 그냥 if-return 문이 더 짧고 간결함

def factorial_iter(n):                                                  # 반복문(for문)을 이용한 n! 계산
    try:
        if n < 0:
            raise ValueError("0 이상의 숫자를 입력해야 합니다.")
        result = 1
        for x in range(2, n + 1):
            result *= x
        return result
    except ValueError:
        return -1                                                       # 올바르지 않은 값(예외) 리턴

def factorial_rec(n):                                                   # 재귀문(함수 재호출)을 이용한 n! 계산
    try:
        if n < 0:
            raise ValueError("0 이상의 숫자를 입력해야 합니다.")
        if n == 0 or n == 1:
            return 1
        return n * factorial_rec(n - 1)
    except ValueError:
        return -1                                                       # 올바르지 않은 값(예외) 리턴

def run_with_time(func, n):                                             # 함수(func)의 값(n)과 걸린 시간을 계산
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    if result == -1:
        return -1, end - start
    return result, end - start

def when_1_to_3():                                                      # 1 ~ 3번) 정수(0 이상) 입력용 함수
    try:
        n = int(input("n 값(정수, 0 이상)을 입력하세요 : "))
    except:
        return -1
    return n

def menu():                                                             # 메뉴 출력 및 선택값 리턴용
    print("================ Factorial Tester ================")
    print("1) 반복법으로 n! 계산")
    print("2) 재귀로 n! 계산")
    print("3) 두 방식 모두 계산 후 결과/시간 비교")
    print("4) 준비된 테스트 데이터 일괄 실행")
    print("q) 종료")
    print("--------------------------------------------------")
    n = input("선택: ")
    return n

if __name__ == "__main__":
    print("팩토리얼 계산기 (반복/재귀) - 정수 n>=0 를 입력하세요.")
    while True:
        m = menu()
        
        if m in ["1", "2", "3"]:                                        # (메뉴) 1, 2, 3을 입력했을 경우
            n = when_1_to_3()
            if n < 0:
                print("정수(0 이상의 숫자)만 입력하세요.\n")
                continue
            if m == "1":
                result = factorial_iter(n)
                if result == -1:
                    continue
                print(f"[반복] : {n}! = {result}\n")
            if m == "2":
                result = factorial_rec(n)
                if result == -1:
                    continue
                print(f"[재귀] : {n}! = {result}\n")
            if m == "3":
                result_iter, time_iter = run_with_time(factorial_iter, n)
                result_rec, time_rec = run_with_time(factorial_rec, n)
                if result_iter == -1 or result_rec == -1:
                    continue
                print(f"[반복] : {n}! = {result_iter}")
                print(f"[재귀] : {n}! = {result_rec}")
                if result_iter == result_rec:
                    print("결과 일치 여부 : 일치")
                else:
                    print("결과 일치 여부 : 불일치")
                print(f"[반복] 시간 : {time_iter:.6f} s   |   [재귀] 시간 : {time_rec:.6f} s\n")

        elif m == "4":                                                  # (메뉴) 4를 입력했을 경우
            print("테스트 데이터 실행")
            for n in TEST:
                result_iter, time_iter = run_with_time(factorial_iter, n)
                result_rec, time_rec = run_with_time(factorial_rec, n)
                if result_iter == -1 or result_rec == -1:
                    print("처리 불가능한 데이터가 감지되어 처리를 중단합니다.")
                    print(f"처리 불가 데이터 : {n}")
                    break
                if result_iter == result_rec:
                    TF = True
                else:
                    TF = False
                print(f"n = {n}\t|  same = {TF}\t|  iter = {time_iter:.6f} s, rec = {time_rec:.6f} s")
                print(f"  {n}! = {result_iter}")
            print()
        elif m.lower() == "q":                                          # (메뉴) "Q" 혹은 "q"를 입력했을 경우
            break
        else:                                                           # (메뉴) 기타 값
            print("잘못된 선택입니다. 다시 입력하세요.\n")
            continue
