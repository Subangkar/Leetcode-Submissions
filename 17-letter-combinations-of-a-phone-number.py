class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits)==0:
            return []

        res = []
        digit_2_char = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", 
                        "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        def generate(s, pos):
            if pos == len(digits):
                res.append(s)
                return
            for i in range(len(digit_2_char[digits[pos]])):
                generate(s + digit_2_char[digits[pos]][i], pos+1)
        generate("", 0)
        return res


        