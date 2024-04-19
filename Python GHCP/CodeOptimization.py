def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_dynamic(n):
    fib = [0] * (n+1)
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
#can you please optimize the below selected code for better performance
def find_duplicates(nums):
    duplicates = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                duplicates.append(nums[i])
    return duplicates

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def main():
    n = 35
    print("Calculating Fibonacci number using recursive approach:")
    print(fibonacci_recursive(n))
    
    print("\nCalculating Fibonacci number using dynamic programming:")
    print(fibonacci_dynamic(n))
    
    nums = [3, 2, 1, 5, 4, 2, 3, 1]
    print("\nFinding duplicates in a list using brute-force method:")
    print(find_duplicates(nums))
    
    nums = [5, 3, 8, 4, 2]
    print("\nSorting a list using bubble sort:")
    print(bubble_sort(nums))

if __name__ == "__main__":
    main()
