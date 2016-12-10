

def function_builder(n):
    l = []
    for i in range(n):
        l.append(lambda x: x + i)
    return l

