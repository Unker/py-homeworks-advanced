from stack import Stack

closes = ')]}'
mirror = {
    '{': '}',
    '[': ']',
    '(': ')',
}


def is_balanced(elements: Stack) -> bool:
    elements = Stack(elements)
    if elements.size() % 2 != 0 or elements.size() == 0:
        return False
    else:
        ret = True
        left = elements
        right = Stack([])
        while not left.is_empty():
            el = left.pop()
            if el in closes:
                right.push(el)
            elif not right.is_empty():
                if right.pop() != mirror[el]:
                    ret = False
                    break
            else:
                ret = False
                break

        return ret


