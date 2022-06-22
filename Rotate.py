def rotate(list_to_rotate: list[int], rotate_by: int) -> list[int]:
    rotate_by = rotate_by % len(list_to_rotate)
    return list_to_rotate[rotate_by:] + list_to_rotate[:rotate_by]

print(rotate([7, -3, 2, 4, 9], 3))


def bracket_pair(brackets: str) -> bool:
    if len(brackets) < 2 or len(brackets) % 2 != 0:
        return False


    stack = []

    for bracket in brackets:
        if bracket in "{[(":
            stack.append(bracket)
        elif bracket in "]})":
            if bracket == ")" and stack[-1] == "(":
                stack.pop()
            elif bracket == "}" and stack[-1] == "{":
                stack.pop()
            elif bracket == "]" and stack[-1] == "[":
                stack.pop()
            else:
                return False

        else:
            return False

    return True

print(bracket_pair("{}({[]})"))
