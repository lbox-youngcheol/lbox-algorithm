# https://school.programmers.co.kr/learn/courses/30/lessons/140108?language=python3
def solution(s):
    answer = 0

    first_letter = None
    first_count = 0
    others_count = 0

    for c in s:
        # 분리된 뒤 다음 문자열을 시작하는 경우
        if first_letter is None:
            first_letter = c
            first_count = 0
            others_count = 0

        if c == first_letter:
            first_count += 1
        else:
            others_count += 1

        # 분리 되어야하는지 여부 확인
        if first_count == others_count:
            answer += 1
            first_letter = None
            first_count = 0
            others_count = 0

    # 마지막에 문자열이 분리가 되지 않은 경우: ab - ra - ca - da - br - `a`
    if first_count != others_count:
        answer += 1

    return answer


if __name__ == '__main__':
    assert solution("banana") == 3
    assert solution("abracadabra") == 6
    assert solution("aaabbaccccabba") == 3
