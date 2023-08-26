def busca_binaria(ar, x):
    
    left = 0
    right = len(ar) - 1

    while left <= right:
        
        mid = left + (right - left) // 2
        
        if ar[mid] == x:
            return mid
        
        if ar[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


if __name__ == '__main__':
    import random
    ar = sorted(random.sample(range(1000), 100))
    x = ar[random.randint(0,100)]
    res = busca_binaria(ar, x)
    print(ar)
    print(x, res)