from stack import Stack

good1 = '(((([{}]))))'
good2 = '[([])((([[[]]])))]{()}'
good3 = '{{[()]}}'
bad1 = '}{}'
bad2 = '{{[(])]}}'
bad3 = '[[{())}]'

bad4 = '{[([])((([[[]]])))]{()}]'


lefts = '([{'
rights = ')]}'
mirror = {
    '{': '}',
    '[': ']',
    '(': ')',
    '}': '{',
    ']': '[',
    ')': '(',
}


def is_balanced(elements: Stack) -> bool:
    if elements.size() % 2 != 0:
        return False
    else:
        ret = True
        left = elements
        right = Stack([])
        while not left.is_empty():
            el = left.pop()
            if el in rights:
                right.push(el)
            elif not right.is_empty():
                if right.pop() != mirror[el]:
                    ret = False
                    break

        return ret


print(is_balanced(Stack(bad1)))
print(is_balanced(Stack(bad2)))
print(is_balanced(Stack(bad3)))
print(is_balanced(Stack(bad4)))
print('*****')
print(is_balanced(Stack(good1)))
print(is_balanced(Stack(good2)))
print(is_balanced(Stack(good3)))
