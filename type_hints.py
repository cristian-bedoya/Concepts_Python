def addition(num1: int, num2: int) -> int:
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError(f'Both parameters have to be integers')
    return num1 + num2


# def headline(text, align=True):
#     if align:
#         return f"{text.title()}\n{'-' * len(text)}"
#     else:
#         return f" {text.title()} ".center(50, "o")

def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


headline

if __name__ == '__main__':
    print(addition(1, 2))
    print('========_____========')
    print(headline("python type checking", align=False))
    print(headline("python type checking"))
