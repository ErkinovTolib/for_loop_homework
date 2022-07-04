def main(N):
    """
    The number N is given. Calculate the sum below: 1 + 1/2 + 1/3 + … + 1/N.
    Args:
        N: int
    Returns:
        float: return  answer
    """
    sum = 0
    for i in range(1,N):
        sum += 1+i/N
    return sum
print(main(6))