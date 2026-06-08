import ast


def memUpdate():
    # 먼저 전체 회원 데이터를 불러옵니다.
    try:
        with open('./members.dat', 'r', encoding="utf-8") as f:
            members = [ast.literal_eval(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print("\n[안내] 등록된 회원 데이터 파일이 없습니다.")
        return

    # 흐름 1. 수정할 회원의 이름을 입력받는다.
    print("\n----------------------------")
    print(" 수정할 회원의 이름을 입력하세요.")
    print("----------------------------")
    search_name = input("이름 : ").strip()
    if not search_name:
        print("❌ 이름을 입력해야 합니다. 메뉴로 돌아갑니다.")
        return

    # 흐름 2. 해당 이름의 회원을 검색한다. (원본 인덱스와 함께 저장)
    search_results = [(idx, m) for idx, m in enumerate(members) if m['name'] == search_name]
    search_count = len(search_results)

    target_idx = -1  # 수정 대상이 될 원본 리스트의 인덱스 번호

    # 🛑 0명일 때 예외 처리
    if search_count == 0:
        print("\n❌ 해당하는 회원 정보가 없습니다.")
        return

    # 🟢 1명일 때 즉시 수정 이동
    elif search_count == 1:
        target_idx = search_results[0][0]

    # 🟡 2명 이상(동명이인)일 때 번호 선택
    else:
        print(f"\n총 {search_count}개의 목록이 검색되었습니다.")
        print("아래 목록 중 수정할 회원의 번호를 입력하세요.")
        for i, (idx, m) in enumerate(search_results, 1):
            print(f"{i}. 이름 = {m['name']}, 전화번호 : {m['phone']}, 주소 : {m['addr']}, 종류 : {m['div']}")
        
        while True:
            try:
                choice = int(input("번호 입력: "))
                if 1 <= choice <= search_count:
                    target_idx = search_results[choice - 1][0]
                    break
                else:
                    print(f"❌ 1번부터 {search_count}번 사이의 숫자를 입력해 주세요.")
            except ValueError:
                print("❌ 올바른 숫자를 입력해 주세요.")

    # 흐름 3. 새 정보를 입력받는다.
    print("\n----------------------------")
    print(" 수정할 정보를 입력하세요.")
    print("----------------------------")
    new_name = input("이름: ").strip()
    new_phone = input("전화번호(ex: 01012345678): ").strip()
    new_addr = input("주소: ").strip()
    new_div = input("종류(ex. 가족, 친구, 기타): ").strip()

    # 유효성 검사 (이름과 전화번호 필수)
    if not new_name or not new_phone:
        print("\n❌ 에러: 이름과 전화번호는 필수 입력 항목입니다. 수정이 취소되었습니다.")
        return

    # 메모리에서 해당 인덱스의 회원 데이터 교체
    members[target_idx] = {
        "name": new_name,
        "phone": new_phone,
        "addr": new_addr,
        "div": new_div
    }

    # 수정한 전체 데이터를 파일에 덮어쓰기('w')로 저장합니다.
    with open('./members.dat', 'w', encoding="utf-8") as f:
        for m in members:
            f.write(f"{m}\n")
            
    # 흐름 4. 완료 출력
    print("\n✨ 수정이 완료되었습니다.")

def memAdd(name, phone, addr, div):
    # 파일에 새로운 내용을 이어붙이기 위해 'a' (Append) 모드로 엽니다.
    with open('./members.dat', 'a', encoding="utf-8") as f:
        # 입력받은 파라미터들로 예쁜 딕셔너리 생성
        new_member = {
            "name": name,
            "phone": phone,
            "addr": addr,
            "div": div
        }
        # 파일에 한 줄로 쓰고 줄바꿈('\n') 처리
        f.write(f"{new_member}\n")
    
    print(f"\n [완료] {name} 회원의 정보가 성공적으로 추가되었습니다!")

# 2. 회원 목록 보기
def memList():
    try:
        with open('./members.dat', 'r', encoding="utf-8") as f:
            lines_to_print = [ast.literal_eval(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print("\n[안내] 등록된 회원 데이터 파일이 없습니다.")
        return

    print(f"\n총 {len(lines_to_print)}명의 회원이 저장되어 있습니다.") 
    for member in lines_to_print:
        print("회원정보 : 이름 =", member['name'],",","전화번호 =", member['phone'],",","주소 =", member['addr'],",","구분 =", member['div'])   

# 화면 메뉴 로딩
def init():
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
        
        # 💡 [버그 수정] 기능을 실행하기도 전에 작동하던 무분별한 break들을 정리했습니다.
        if menu == '1':
            print("\n----------------------------")
            print(" 등록할 회원의 정보를 입력하세요.")
            print("----------------------------")
            name = input("이름: ").strip()
            phone = input("전화번호(ex: 01012345678): ").strip()
            addr = input("주소: ").strip()
            div = input("종류(ex. 가족, 친구, 기타): ").strip()

            if not name or not phone:
                print("\n에러: 이름과 전화번호는 필수 입력 항목입니다. 처음부터 다시 시도하세요.")
                continue

            memAdd(name, phone, addr, div)

        elif menu == '2':
            memList()
        elif menu == '3':
            memUpdate()
        elif menu == '4':
            print("\n[4. 회원 삭제] 기능을 실행합니다.")
            # delete_member()
        elif menu == '5':
            print("\n👋 프로그램을 종료합니다.")
            break  # 5번을 눌렀을 때만 안전하게 종료되도록 탈출구 일원화!
        else:
            print("\n❌ 잘못된 메뉴입니다. 다시 선택하세요.")

# 화면 메뉴 로딩 실행
init()




