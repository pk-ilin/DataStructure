from stack import Stack


def main():
    s = input()
    stack = Stack()

    for i in range(len(s)):
        if s[i] in ["(", "[", "{"]:
            stack.push((s[i], i))
        else:
            if s[i] in [")", "]", "}"]:
                if not stack.is_empty():
                    bracket = stack.pop()[0]
                    if (bracket + s[i]) not in ["()", "[]", "{}"]:
                        return i + 1
                else:
                    return i + 1
            else:
                continue

    if stack.is_empty():
        return "Success"
    else:
        return stack.peek()[1] + 1


if __name__ == "__main__":
    print(main())
