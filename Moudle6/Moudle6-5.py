def remove_odds(nums):
    evens = []
    for n in nums:
        if n % 2 != 0:
            continue
    else:
        evens.append(n)
        return evens


def main()  :
    nums = [1,2,3,4,5,6,7,8,9]
    evens = remove_odds(nums)

    print("Original:", nums)
    print("Without odds:", evens)

main()