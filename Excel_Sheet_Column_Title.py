class Solution:
    column_mapper = {
        1: "A", 2: "B", 3: "C", 4: "D", 5: "E",
        6: "F", 7: "G", 8: "H", 9: "I", 10: "J",
        11: "K", 12: "L", 13: "M", 14: "N", 15: "O",
        16: "P", 17: "Q", 18: "R", 19: "S", 20: "T",
        21: "U", 22: "V", 23: "W", 24: "X", 25: "Y", 26: "Z",
    }

    """
    아래와 같은 방식으로 column title이 column number로 변환된다.
    - AZ = 1*26^1 + 26*26^0
    - ZY = 26*26^1 + 25*26^0
    - CZG = 3*26^2 + 26*26^1 + 7*26^0
    
    문제 풀이 방법은 modulo를 통해 역순으로 column title을 추적한다.
    단 modulo를 사용할 때 그 결과가 0인 경우(Z일 때)는 특수 처리가 필요하다.
    """
    def convertToTitle(self, columnNumber: int) -> str:
        column_title = ""

        while 0 < columnNumber:
            digit_for_column = columnNumber % 26
            columnNumber = columnNumber // 26

            # if it is `Z` when columnNumber is more than 26
            if digit_for_column == 0:
                digit_for_column = 26
                columnNumber -= 1

            column_title = self.column_mapper[digit_for_column] + column_title

        return column_title


if __name__ == '__main__':
    assert Solution().convertToTitle(columnNumber=702) == "ZZ"
    assert Solution().convertToTitle(columnNumber=701) == "ZY"
    assert Solution().convertToTitle(columnNumber=16980) == "YCB"
    assert Solution().convertToTitle(columnNumber=1) == "A"
    assert Solution().convertToTitle(columnNumber=28) == "AB"
