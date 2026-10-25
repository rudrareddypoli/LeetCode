class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current_str, open_count, close_count):
            # Base case: reached the required length of 2 * n
            if len(current_str) == 2 * n:
                result.append(current_str)
                return

            # Can add '(' if we haven't used all n open parentheses
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)

            # Can add ')' only if there is an unmatched '(' waiting to be closed
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result