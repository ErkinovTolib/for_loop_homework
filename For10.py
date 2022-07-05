def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    x = []
    for i in list1:
        x.append(i.title())
    return x
print(main(["tolibjon","erkinov","botir"]))