import os
import json

# 특정 디렉토리 경로 설정
input_directory_path = 'data'
output_directory_path = '../v4/data'

total_menu_count = 0
cancel_count = 0
store_not_have_menu = 0
total_store = 0


# 함수: JSON 파일을 읽어들이고 전처리하는 함수
def preprocess_json(file_path):
    global cancel_count, total_menu_count, store_not_have_menu, total_store
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

        # 전처리 작업 수행
        for restaurant in data:
            # Limit images to 3
            total_store += 1
            restaurant['images'] = restaurant['images'][:3]

            # Convert prices to int if menu exists and is not None

            if 'menu' in restaurant and restaurant['menu'] is not None:
                processed_menu = []
                for item in restaurant['menu']:
                    total_menu_count += 1;
                    try:
                        item['price'] = int(item['price'].replace('원', '').replace(',', ''))
                        processed_menu.append(item)
                    except ValueError:
                        cancel_count += 1
                        # If there is an error converting the price, skip this item
                        print(f"Error converting price for item: {item.get('name', 'Unknown')}. Skipping this item.")

                restaurant['menu'] = processed_menu
            else:
                # Increment global counter for null menu
                store_not_have_menu += 1

        return data


# 모든 JSON 파일을 읽고 전처리
for filename in os.listdir(input_directory_path):
    if filename.endswith('.json'):
        file_path = os.path.join(input_directory_path, filename)
        processed_data = preprocess_json(file_path)

        # 새로운 파일 이름 설정 (예: 원래 이름에 '_processed' 추가)
        new_filename = os.path.splitext(filename)[0] + '_processed.json'
        output_file_path = os.path.join(output_directory_path, new_filename)
        print(f'Writing processed data to {output_directory_path}')
        # 전처리된 데이터를 새로운 파일에 저장
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            json.dump(processed_data, output_file, ensure_ascii=False, indent=4)

        print(f"Processed data saved to {output_file_path}")

print(f"전체 음식점수 {total_store}")
print(f"메뉴룰 가지고 있는 음식점 수 {total_store-store_not_have_menu}")
print(f"메뉴를 가지고 있지 않은 음식점 수(전처리 전) {store_not_have_menu}")
print(f"전체 메뉴수(전처리 전) {total_menu_count}")
print(f"전처리중 유실된 메뉴 수 {cancel_count}")
# print(cancel_count)
# total_menu_count = 0
# cancel_count = 0
# store_not_have_menu = 0
# total_store = 0
