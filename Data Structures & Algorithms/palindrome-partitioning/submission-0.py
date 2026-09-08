class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        result = []

        def substrs(string, rec):
            if len(string) == 0:
                result.append(rec)
                return

            for end in range(1, len(string) + 1):
                if not self.isPalindrome(string[:end]):
                    continue

                rec.append(string[:end])
                substrs(string[end:], rec[:])
                rec.pop()

        substrs(s, [])

        return result