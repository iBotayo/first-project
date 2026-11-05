def collatz(n):
    """Compute the Collatz sequence starting from n.

    The Collatz sequence is defined as follows:
    - If n is even, the next number is n / 2.
    - If n is odd, the next number is 3n + 1.
    - The sequence ends when it reaches 1.

    Parameters:
    n (int): A positive integer to start the sequence.

    Returns:
    list: A list containing the Collatz sequence starting from n.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    sequence = [n]
    
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    
    return sequence

number = int(input("Enter a positive integer: "))
try:
    result = collatz(number)
    print("Collatz sequence:", result)
except ValueError as e:
    print(e)