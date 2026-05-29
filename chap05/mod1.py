def sum(a,b):
    return a + b    

def safe_sum(a,b):
    if type(a) != type(b):
        print("더할 수 있는 값이 아닙니다.")
        return
    else:
        return a + b    
        