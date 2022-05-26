"""
calculations prime number

"""

def parz():
    if tiv == 1:
        return True
    if tiv > 1:
        for n in range(2, tiv):
            if (tiv % n) == 0:
                return False
        return True
    else:
        return False
    parz()
print(parz())
