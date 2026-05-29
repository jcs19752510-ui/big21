def sum(a,b):
    return a + b    

def safe_sum(a,b):
    if type(a) != type(b):
        print("더할 수 있는 값이 아닙니다.")
        return
    else:
        return a + b     

# python에서 인터프리터로 직접 실행할때만 __name__ --> '__main__'
# import 하면
# __name__ --> 'mod1' (파일명이거나 as 엘리어스 명이 넘어온다)
if __name__ == "__main__":
    print(safe_sum('a', 1))
    print(safe_sum(1, 4))
    print(sum(10,10.4))