class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2==1:
            return False

        dic ={ '(':')', '[':']', '{':'}'}     # 创建字典，表示左右括号的对应关系

        stack = []
        for c in s:
            if c in dic:
                stack.append(c)
            else:
                if len(stack)==0:     #判断栈为空？
                    return False
                else:
                    top = stack.pop()     #栈顶元素
                    if c != dic[top]:     #进来的括号不等于栈顶左括号对应
                        return False
                  
        return not stack
