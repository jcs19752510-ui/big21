import pickle
import re

FILE_PATH = './members.dat'

# 파일에서 전체 회원 리스트 로드
def load_members():
    try:
        with open(FILE_PATH, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        print(f"\n파일을 읽는 중 오류가 발생했습니다: {e}")
        return []

# 전체 회원 리스트를 파일에 통째로 저장
def save_data(members):
    try:
        with open(FILE_PATH, 'wb') as f:
            pickle.dump(members, f)
    except Exception as e:
        print(f"\n파일을 저장하는 중 오류가 발생했습니다: {e}")

# 1. 회원 추가
def add_member(name, phone, addr, div):
    new_member = {
        "name": name,
        "phone": phone,
        "addr": addr,
        "div": div
    }
    
    members = load_members()
    members.append(new_member)
    save_data(members)  

# 2. 회원 목록 보기
def list_members():
    members = load_members()
    if not members:
        print("\n[안내] 등록된 회원 데이터가 없습니다.")
        return

    print(f"\n총 {len(members)}명의 회원이 저장되어 있습니다.") 
    for i, m in enumerate(members, 1):
        print(f"회원정보 : 이름: {m['name']} , 전화번호: {m['phone']} , 주소: {m['addr']} , 구분: {m['div']}")   

# 이름검색
def find_by_name(members, action_name):
    print(f"\n----------------------------")
    print(f" {action_name}할 회원의 이름을 입력하세요.")
    print(f"----------------------------")
    search_name = input("이름 : ").strip()
    if not search_name:
        print("이름을 입력해야 합니다. 메뉴로 돌아갑니다.")
        return -1

    search_results = [(idx, m) for idx, m in enumerate(members) if m['name'] == search_name]
    search_count = len(search_results)

    if search_count == 0:
        print("\n해당하는 회원 정보가 없습니다.")
        return -1
    
    if search_count == 1:
        return search_results[0][0]

    # 동명이인 처리
    print(f"\n총 {search_count}개의 목록이 검색되었습니다.")
    print(f"아래 목록 중 {action_name}할 회원의 번호를 입력하세요.")
    for i, (idx, m) in enumerate(search_results, 1):
        print(f"{i}. 이름: {m['name']} | 전화번호: {m['phone']} | 주소: {m['addr']} | 구분: {m['div']}")
    
    while True:
        try:
            choice = int(input("번호 입력: "))
            if 1 <= choice <= search_count:
                return search_results[choice - 1][0]
            else:
                print(f"1번부터 {search_count}번 사이의 숫자를 입력해 주세요.")
        except ValueError:
            print("올바른 숫자를 입력해 주세요.")

# 3. 회원 정보 수정하기
def update_member():
    members = load_members()
    if not members:
        print("\n[안내] 등록된 회원 데이터 파일이 없습니다.")
        return

    target_idx = find_by_name(members, "수정")
    if target_idx == -1:
        return

    print("\n----------------------------")
    print(" 수정할 정보를 입력하세요.")
    print("----------------------------")
    
    # 💡 유효성 검증 루프 적용
    while True:
        new_name = input("이름: ").strip()                
        if not validate_name(new_name):
            print("\n이름은 5자 이내로 입력하세요.")                    
            continue
        break

    while True:
        new_phone = input("전화번호(ex: 01012345678): ").strip()
        if not validate_phone(new_phone):
            print("\n전화번호 형식이 올바르지 않습니다. (예: 01012345678)")                    
            continue
        break   
        
    new_addr = input("주소: ").strip()

    while True:
        new_div = input("종류(ex. 가족, 친구, 기타): ").strip()
        if not validate_type(new_div):
            print("\n종류는 가족/친구/기타 중 하나여야 합니다.")                    
            continue
        break

    members[target_idx] = {
        "name": new_name,
        "phone": new_phone,
        "addr": new_addr,  
        "div": new_div
    }

    save_data(members)
    print("\n 수정이 완료되었습니다.")

# 4. 회원 삭제
def delete_member():
    members = load_members()
    if not members:
        print("\n[안내] 등록된 회원 데이터 파일이 없습니다.")
        return

    target_idx = find_by_name(members, "삭제")
    if target_idx == -1:
        return

    members.pop(target_idx)
    save_data(members)
    print("\n 삭제가 완료되었습니다.")

def validate_name(name: str) -> bool:
    return 1 <= len(name) <= 5 

def validate_phone(phone: str) -> bool:
    return re.fullmatch(r"010\d{8}", phone) is not None

def validate_type(t: str) -> bool:
    return t in ("가족", "친구", "기타")

# 화면 메뉴 로딩
def main():
    while True:
        print("\n============================")
        print("다음 메뉴 중 하나를 선택하세요.")
        print("============================")
        print("1. 회원 추가")
        print("2. 회원 목록 보기")
        print("3. 회원 정보 수정하기")
        print("4. 회원 삭제")
        print("5. 종료")
        menu = input("메뉴를 선택하세요: ")
        
        #1. 회원 추가
        if menu == '1':
            print("\n----------------------------")
            print(" 등록할 회원의 정보를 입력하세요.")
            print("----------------------------")

            while True:
                name = input("이름: ").strip()                
                if not validate_name(name):
                    print("\n이름은 5자 이내로 입력하세요.")                    
                    continue
                break

            while True:
                phone = input("전화번호(ex: 01012345678): ").strip()
                if not validate_phone(phone):
                    print("\n전화번호 형식이 올바르지 않습니다. (예: 01012345678)")                    
                    continue
                break   
            addr = input("주소: ").strip()

            while True:
                div = input("종류(ex. 가족, 친구, 기타): ").strip()
                if not validate_type(div):
                    print("\n종류는 가족/친구/기타 중 하나여야 합니다.")                    
                    continue
                break

            add_member(name, phone, addr, div)

        #2. 회원 목록 보기
        elif menu == '2':
            list_members()
        #3. 회원 정보 수정하기    
        elif menu == '3':
            update_member()
        #4. 회원 삭제    
        elif menu == '4':
            delete_member()            
        #5. 종료    
        elif menu == '5':
            print("\n👋 프로그램을 종료합니다.")
            break
        else:
            print("\n잘못된 메뉴입니다. 다시 선택하세요.")

if __name__ == "__main__":
    main()