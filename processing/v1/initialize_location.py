import json
import os
import requests

total_store = 0;
delete_store = 0;


def fetch_location_info(name):
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')

    headers = {
        'X-Naver-Client-Id': client_id,
        'X-Naver-Client-Secret': client_secret
    }
    params = {
        'query': name
    }

    try:
        response = requests.get('https://openapi.naver.com/v1/search/local.json', headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        if data['items']:
            # Take the first result
            first_result = data['items'][0]
            return {
                'mapx': first_result.get('mapx'),
                'mapy': first_result.get('mapy')
            }
        else:
            return None
    except Exception as e:
        print(f"Error fetching location info for {name}: {e}")
        return None


# JSON 파일을 읽어들이고 전처리하는 함수
def preprocess_json(file_path):
    global total_store, delete_store
    filtered_data = []
    error_data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

        for restaurant in data:
            total_store += 1
            # Fetch location info and update the restaurant data
            location_info = fetch_location_info(restaurant.get('name', ''))
            if location_info:
                restaurant.update(location_info)
                restaurant['success'] = True
                filtered_data.append(restaurant)
            else:
                delete_store += 1
                restaurant['success'] = False
                error_data.append(restaurant)

        return filtered_data, error_data


input_directory_path = 'data'
output_directory_path = '../v2/data'
error_directory='../v2/error'

if not os.path.exists(output_directory_path):
    os.makedirs(output_directory_path)

for filename in os.listdir(input_directory_path):
    if filename.endswith('.json'):
        file_path = os.path.join(input_directory_path, filename)
        print(f"Processing file: {file_path}")
        processed_data,error_data = preprocess_json(file_path)

        new_filename = os.path.splitext(filename)[0] + '_processed.json'
        output_file_path = os.path.join(output_directory_path, new_filename)
        print(f"Saving processed file to: {output_file_path}")

        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            json.dump(processed_data, output_file, ensure_ascii=False, indent=4)

        print(f"Processed data saved to {output_file_path}")

        ## 에러 json를 저장한다.
        error_filename = os.path.splitext(os.path.basename(file_path))[0] + '_error.json'
        error_file_path = os.path.join(error_directory, error_filename)
        with open(error_file_path, 'w', encoding='utf-8') as error_file:
            json.dump(error_data, error_file, ensure_ascii=False, indent=4)
        print(f"Error data saved to {error_file_path}")
print(f"Total store: {total_store}")
print(f"Delete store: {delete_store}")