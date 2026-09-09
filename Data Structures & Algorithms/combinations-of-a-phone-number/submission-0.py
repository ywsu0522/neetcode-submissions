class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        def combination(digits, s):
            if not digits:
                if s:
                    result.append(s)
                return

            for letter in letter_dict[digits[0]]:
                s = s + letter
                combination(digits[1:], s)
                s = s[:-1]

        combination(digits, "")

        return result
