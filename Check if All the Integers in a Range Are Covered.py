for num in range(left, right+1):
    if not any(starti <= num <= endi for starti, endi in ranges):
        return False
return True
