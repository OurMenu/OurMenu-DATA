## v2

## data
- 음식점의 위치 
- 음식점의 이름
- 음식점의 타입

```json
    {
        "name": "뒤안길",
        "address": "서울특별시 광진구 자양동 51-32 1층 101호",
        "type": "기타",
        "images": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240504_76%2F1714757976028L9EgI_JPEG%2FIMG_5201.jpeg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240504_130%2F1714757974462g7A7q_JPEG%2FIMG_7935.jpeg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240504_23%2F1714757969401aE6Nt_JPEG%2FIMG_5220.jpeg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240504_245%2F17147579673896ihRo_JPEG%2FIMG_5222.jpeg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240504_48%2F1714757975851WdUn7_JPEG%2FIMG_5245.jpeg"
        ],
        "menu": "사 히비\n사진\n대표\n6,900원\n고급음료\n사진\n대표\n6,900원",
        "time": "영업 종료\n00:00에 영업 시작\n0시 0분에 영업 시작\n펼쳐보기"
    }
```
### 전처리
- 해당 음식점 이름에 대해 "음식점이름+지역명" 네이버지도에 검색
- 영업시간, 메뉴, 가게 사진 크롤링

### 결과 
- 측정중