def ask():
    print(c.red + question + c.reset)
    answer = input("> ").lower().strip()
    print(c.reset)
    return answer

