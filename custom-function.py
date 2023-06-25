def summation(arg1, arg2):
    total = arg1 + arg2
    return total


out = summation(2, 8)
print(out)


def summ(arg1):
    x = 0
    for i in arg1:
        x += i

    return x


print(summ([1, 2, 3, 4, 5, 5, 6]))
print(summ((1, 2, 3, 4, 5, 5, 6)))
print(summ((1, 2, 3, 4, 5, 5, 6)))


def order_food(min_order, *arg):
    print(f"you have ordered: {min_order}")
    for i in arg:
        print(f"you have ordered: {i}")


order_food("sugar")
order_food("sugar", 12, 13, 45)
