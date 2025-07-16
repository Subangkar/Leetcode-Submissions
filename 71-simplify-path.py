class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        tokens = path.split("/")
        for i in range(len(tokens)):
            if tokens[i] in ('', '.'):
                continue
            elif tokens[i] == '..':
                if len(stack)>0:
                    stack.pop()
            else:
                stack.append(tokens[i])
        return '/' + '/'.join(stack)