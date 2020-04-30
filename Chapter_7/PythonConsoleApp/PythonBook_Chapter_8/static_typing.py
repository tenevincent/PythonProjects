

def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")

def calling_main():
    print(headline("python type checking"))
    print(headline("use mypy", align="center"))
