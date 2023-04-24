def find_outlier(integers):
    odd_numbers = [odd for odd in integers if odd % 2 == 1]
    even_numbers = [even for even in integers if even % 2 == 0]
    return odd_numbers[0] if len(odd_numbers) < len(even_numbers) else even_numbers[0]