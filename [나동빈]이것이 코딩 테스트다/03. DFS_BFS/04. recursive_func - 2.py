def recursive_func(i):
    # 출력함수를 100번 째 호출했을 때 종료하도록 명시
    if i == 100:
        return print('마지막', i, '번째 재귀함수 입니다.')
    print(i, '번째 재귀 함수에서', i + 1, '번째 재귀함수를 호출합니다.')
    recursive_func(i + 1)


recursive_func(1)