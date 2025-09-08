def isPalinArray(arr):
    for element in arr:
        if str(element)!=str(element)[::-1]:
            return False
    return True
