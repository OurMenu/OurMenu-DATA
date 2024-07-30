import json
import os

input_file = 'data/서울시 일반음식점 인허가 정보.json'  # 대용량 JSON 파일이 저장된 디렉토리
output_dir = '../v1/data'  # 결과 JSON 디렉토리 경로
BATCH_SIZE = 1
LOCAL="광진구"

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def task_load_and_split_json(input_file, output_dir):
    all_data = []
    data = load_json(input_file)
    # 조건에 맞는 데이터만 추출 및 병합
    filtered_data = [item for item in data.get("DATA", [])]
    all_data.extend(filtered_data)

    # 조건에 맞는 데이터 필터링
    #filtered_data = [item for item in all_data if
    #                 "광진구" in item.get("sitewhladdr", "") and item.get("dtlstatenm") == "영업"]
    count=0
    err_count = 0
    result=[]
    for item in all_data:

        try:
        #print(item)
        #print(json.dumps(item, ensure_ascii=False, indent=3))

            if LOCAL in item["sitewhladdr"] and "영업" in item["dtlstatenm"]:
                #print(item)
                count += 1
                result.append(item)
        except Exception as e:
            err_count += 1
    chunk_size = 1000  # 병렬 처리할 청크 크기 설정
    chunks = [result[i:i + chunk_size] for i in range(0, len(result), chunk_size)]
    os.makedirs(output_dir, exist_ok=True)

    for idx, chunk in enumerate(chunks):
        chunk_file = os.path.join(output_dir, f'chunk_{idx}.json')
        with open(chunk_file, 'w', encoding='utf-8') as file:
            json.dump(chunk, file, ensure_ascii=False, indent=4)

    print("count: ",count)
    print("err_count: ", err_count)
task_load_and_split_json(input_file,output_dir)