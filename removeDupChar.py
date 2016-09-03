Time complexity: o(n)
space complexity: o(k) k is size of string

def removeDuplicateLetters(s):
        """
        :type s: str
        :rtype: str
        """
        remaining = collections.defaultdict(int)
        for c in s:
            remaining[c] += 1
        print remaining
        in_stack, stk = set(), []
        for c in s:
            if c not in in_stack:
                while stk and stk[-1] > c and remaining[stk[-1]]:
                    in_stack.remove(stk.pop())
                stk += c
                in_stack.add(c)
            remaining[c] -= 1
        return "".join(stk)