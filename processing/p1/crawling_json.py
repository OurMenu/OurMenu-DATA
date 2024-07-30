import json
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

# 크롬 드라이버 사용
#service = Service(ChromeDriverManager().install())

#검색이 되지 않는경우
no_places=0
#사진이 없는 경우
no_photos=0
#메뉴가 없는 경우
no_menus=0;
#영업시간 정보가 없는경우
no_times=0;

def crawl_restaurant_info(json):
    global no_places, no_photos, no_menus, no_times
    data = {
        "name": json['bplcnm'],
        "address": json['sitewhladdr'],
        "type": json['uptaenm'],
        "images": [],
        "menu": None,
        "time":None
    }
    webDriver = webdriver.Chrome()

    url = "https://map.naver.com/p/search/"+json['bplcnm']+" 광진구"
    webDriver.get(url)  # 해당 URL로 접속
    wait = WebDriverWait(webDriver, 5)  # 1
    # 검색 실패한경우
    try:
        iframe_element = wait.until(EC.visibility_of_element_located((By.ID, "entryIframe")))

    # iframe 으로 변경
        webDriver.switch_to.frame(iframe_element)
    except Exception as e:
        no_places+=1;
        return data

    # 1. 가게 메뉴를 조회한다.
    try:
        body_element1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".place_section >.place_section_content>ul")))
        data["menu"] = body_element1.text
        print("가게 메뉴:", body_element1.text)
    except Exception as e:
        no_menus+=1
        print("가게 메뉴 크롤링 실패:", e)

    # 2. 가게 사진을 조회한다.
    try:
        body_element2 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#app-root > div > div > div > div.CB8aP > div")))
        img_elements = body_element2.find_elements(By.TAG_NAME, "img")
        data["images"] = [img.get_attribute("src") for img in img_elements if img.get_attribute("src")]
        # 각 <img> 태그의 src 속성에서 URL 추출
        for img in img_elements:
            img_url = img.get_attribute("src")
            print("가게 사진:", img_url)

    except Exception as e:
        no_photos+=1
        print("가게 사진 크롤링 실패:", e)

    # 3. 영업시간을 조회한다.
    try:
        button_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".gKP9i.RMgN0")))
        button_element.click()

        # 영업시간을 조회한다.
        body_element3 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#app-root > div > div > div > div:nth-child(5) > div > div:nth-child(2) > div.place_section_content > div > div.O8qbU.pSavy > div > a")))
        data["time"] = body_element3.text
        print("가게 영업 시간:", body_element3.text)
    except Exception as e:
        no_times+=1
        print("가게 영업 시간 크롤링 실패:", e)

    webDriver.close()
    return data

# JSON 파일 로드 함수
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def main(input_file, output_file):
    data = load_json(input_file)
    results = []

    for restaurant in data:
        info = crawl_restaurant_info(restaurant)
        results.append(info)

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(results, file, ensure_ascii=False, indent=4)
def print_result():
    global no_places, no_photos, no_menus, no_times
    print("검색이 되지 않는경우: ", no_places)
    print("사진이 없는 경우: ", no_photos)
    print("메뉴가 없는 경우: ", no_menus)
    print("영업시간 정보가 없는경우: ", no_times)


def process_json_files(input_dir, output_dir):
    global no_places, no_photos, no_menus, no_times  # 전역 변수 사용 선언

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file_name in os.listdir(input_dir):
        if file_name.endswith('.json'):
            file_path = os.path.join(input_dir, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                restaurants = json.load(file)

            file_results = []

            for restaurant in restaurants:
                info = crawl_restaurant_info(restaurant)
                file_results.append(info)

            # 파일별 결과 저장
            output_file = os.path.join(output_dir, f'{os.path.splitext(file_name)[0]}_crawled_data.json')
            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(file_results, file, ensure_ascii=False, indent=4)



if __name__ == "__main__":
    # JSON 파일 경로와 결과 파일 경로 설정
    input_dir = 'data'
    output_dir = '../p2/data'

    process_json_files(input_dir, output_dir)
    print_result();