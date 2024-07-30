import json
import os


def transform_menu(menu_string):
    # 메뉴 문자열을 줄바꿈 문자 기준으로 나누기
    menu_items = menu_string.split('\n')

    # 새로운 메뉴 리스트 생성
    new_menu = []

    # 임시 저장 리스트
    temp_menu = []

    # 메뉴 이름과 가격을 2개씩 묶기
    for item in menu_items:
        # "대표" 또는 "사진"이 포함된 항목은 건너뛰기
        if "대표" in item or "사진" in item:
            continue

        # 임시 리스트에 추가
        temp_menu.append(item.strip())

        # 2개씩 묶어서 새로운 리스트에 추가
        if len(temp_menu) == 2:
            new_menu.append({
                "name": temp_menu[0],
                "price": temp_menu[1]
            })
            temp_menu = []

    return new_menu


def process_json_files_in_directory(directory,output_directory):
    # 디렉토리 내의 모든 파일 목록
    for filename in os.listdir(directory):
        # JSON 파일만 처리
        if filename.endswith('.json'):
            input_file = os.path.join(directory, filename)
            output_file = os.path.join(output_directory, f'transformed_{filename}')

            # 입력 파일에서 데이터 읽기
            with open(input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 데이터의 각 항목에 대해 menu 항목 변환
            for item in data:
                if 'menu' in item and item['menu']:
                    item['menu'] = transform_menu(item['menu'])

            # 변환된 데이터를 출력 파일에 저장
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)



# 입력 파일과 출력 파일 경로 지정
input_directory = 'data'
# 입력 파일과 출력 파일 경로 지정
output_directory = '../v3/data'

# JSON 파일 처리 함수 호출
process_json_files_in_directory(input_directory,output_directory)
# import json
#
# # 주어진 JSON 데이터
# data = {
#     "name": "마더락 건대점",
#     "address": "서울특별시 광진구 구의동 67-3 더 하이스트.ck",
#     "type": "한식",
#     "images": [
#         "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20231204_282%2F1701680908824DIgyP_PNG%2F%25C0%25FA%25BF%25EB%25B7%25AE.png",
#         "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20231204_230%2F1701680901532SuDP4_PNG%2FBRO07502%2528%25C0%25FA%25BF%25EB%25B7%25AE%2529.png",
#         "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20231203_9%2F17015324170853ynQK_JPEG%2FIMG_20231130_001601_246.jpg"
#     ],
#     "menu": "사 히비\n사진\n대표\n6,900원\n고급음료\n사진\n대표\n6,900원",
#     "time": "영업 종료\n09:30에 영업 시작\n9시 30분에 영업 시작\n금\n09:30 - 14:00\n토\n10:30 - 13:00\n일\n정기휴무 (매주 일요일)\n월\n09:30 - 14:00\n화\n09:30 - 14:00\n수\n09:30 - 14:00\n목\n09:30 - 14:00\n- 영업시간 이외에도 전화,카톡채널@마더락건대점 상담 가능\n접기"
# }
#
# # 메뉴 문자열을 줄바꿈 문자 기준으로 나누기
# menu_items = data['menu'].split('\n')
#
# # 새로운 메뉴 리스트 생성
# new_menu = []
#
# # 임시 저장 리스트
# temp_menu = []
#
# # 메뉴 이름과 가격을 2개씩 묶기
# for item in menu_items:
#     # "대표" 또는 "사진"이 포함된 항목은 건너뛰기
#     if "대표" in item or "사진" in item:
#         continue
#
#     # 임시 리스트에 추가
#     temp_menu.append(item.strip())
#
#     # 2개씩 묶어서 새로운 리스트에 추가
#     if len(temp_menu) == 2:
#         new_menu.append({
#             "name": temp_menu[0],
#             "price": temp_menu[1]
#         })
#         temp_menu = []
#
# # 기존 데이터를 새 메뉴로 대체
# data['menu'] = new_menu
#
# # 결과 출력 (JSON 형식으로)
# print(json.dumps(data, ensure_ascii=False, indent=4))