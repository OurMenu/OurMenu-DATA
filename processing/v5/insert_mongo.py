import json
import os

from pymongo import MongoClient, errors

# MongoDB Atlas 연결 함수
def connect_to_mongo(uri, db_name):
    client = MongoClient(uri)
    db = client[db_name]
    return db

# JSON 데이터 삽입 함수
def insert_json_list_to_mongo(db, collection_name, json_list):
    collection = db[collection_name]

    try:
        # Bulk insert for list of documents
        if isinstance(json_list, list):
            result = collection.insert_many(json_list)
            print(f"Inserted {len(result.inserted_ids)} documents into {collection_name}")
        else:
            print("Provided data is not a list.")
    except errors.BulkWriteError as bwe:
        print(f"Bulk write error: {bwe.details}")
    except Exception as e:
        print(f"An error occurred: {e}")

# 사용 예제
def main():
    url = os.getenv('MONGO_URL')
    mongo_uri = url  # MongoDB Atlas URI
    db_name = 'ourmenu'      # 데이터베이스 이름
    collection_name = 'store'  # MongoDB 컬렉션 이름

    # MongoDB에 연결
    db = connect_to_mongo(mongo_uri, db_name)

    # JSON 파일 읽기
    input_directory_path= 'data'

    for filename in os.listdir(input_directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(input_directory_path, filename)
            print(f"Processing file: {file_path}")
            with open(file_path, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                insert_json_list_to_mongo(db, collection_name, json_data)


if __name__ == "__main__":
    main()