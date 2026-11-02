def intersection (l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with integer numbers existing in both input lists
    Examples: intersection([1, 2, 3], [4, 3, 1])=> [1, 3]
    intersection([1, 2, 3], [4, 5, 6])=> [];
    """
    return [num for num in l1 if num in l2]

def union (l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with  integer numbers existing  in either list or both
    Result list shouldn't contain repeated numbers
    Examples: union([1, 2, 3], [4, 3, 1])=> [1, 2, 3, 4]
    union([1, 2, 3], [4, 5, 6])=> [1, 2, 3, 4, 5, 6]
    """
    base = l1 if len(l1) >= len(l2) else l2
    addition = l2 if len(l1) >= len(l2) else l1
    result = base[:]
    for num in addition:
        if num not in base:
            result.append(num)
    return result

def difference (l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with  integer numbers existing  in l1
    but non-existing  l2
    Examples: difference([1, 2, 3], [4, 3, 1])=> [2]
    difference([1, 2, 3], [4, 5, 6])=> [1, 2, 3]
    """
    return [num for num in l1 if num not in l2]

def symmetric_difference (l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with  integer numbers existing  in either list but not in both
    Examples: symmetric_difference([1, 2, 3], [4, 3, 1])=> [2, 4]
    symmetric_difference([1, 2, 3], [4, 5, 6])=> [1, 2, 3, 4, 5, 6]
    """
    common = intersection(l1, l2)
    return union(difference(l1, common), difference(l2, common))

def remove_positive_greater_or_negative_less(numbers: list[int],\
        positive_lim: int, negative_lim: int) -> list[int]:
    """
    numbers - list with integer numbers
    returns new list containing all numbers from the input list
    except the positive ones greater than 'positive_lim' and the negative ones
    less than 'negative_lim'
    Example: remove_positive_greater_or_negative_less([1, 2, 11, -3, 10, 15], 10, -3)
    => [1, 2, -3, 10]
    """
    positive_lim = positive_lim if positive_lim > 0 else 0
    negative_lim = negative_lim if negative_lim < 0 else 0
    return [num for num in numbers\
        if negative_lim <= num <= positive_lim]

def max_with_negative_duplicate(numbers: list[int]) -> int:
    """
    numbers - list with integer numbers
    returns the maximal element of "numbers" with existing negative duplicate 
    (example of a number with negative duplicate: number 100, negative duplicate -100)
    If no such number exists, returns -1
    Examples: max_with_negative_duplicate([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100]) => 100
    max_with_negative_duplicate([10, 20, -15, -11, 20]) => -1
    """
    negatives = [num for num in numbers if num < 0]
    max_value = -1
    for num in numbers:
        if num <= max_value or num <= 0 or -num not in negatives:
            continue
        max_value = num
    return max_value