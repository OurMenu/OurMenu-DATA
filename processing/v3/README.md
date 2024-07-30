## v0

## data
- 가게 정보(image의 개수가 0개 이상)
- 메뉴 정보가 정제되지 않았다
  - 데이터가 잘못 들어간 경우가 있다.
  - 가격이 int가 아니다(싯가, 1000원~2000)
- 

```json
{
        "name": "샤브댁",
        "address": "서울특별시 광진구 화양동 32-32 1층",
        "type": "일식",
        "images": [
            "https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240508_165%2F17151510161946gdV9_JPEG%2FKakaoTalk_20240508_153223135_06.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240508_155%2F1715151016132CWA3c_JPEG%2FKakaoTalk_20240508_153223135_05.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240508_28%2F17151510161584A1Ws_JPEG%2FKakaoTalk_20240508_153809372.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240508_251%2F17151510161561A2FF_JPEG%2F%25BD%25B4%25C1%25AB.jpg",
            "https://search.pstatic.net/common/?autoRotate=true&type=w278_sharpen&src=https%3A%2F%2Fldb-phinf.pstatic.net%2F20240508_297%2F1715151016207X8NGN_JPEG%2FKakaoTalk_20240508_153456090.jpg"
        ],
        "menu": [
            {
                "name": "샤브댁 샤브샤브 (우삼겹)",
                "price": "9,800원"
            },
            {
                "name": "우삼겹 런치세트 (우삼겹+야채+사리)",
                "price": "10,000원"
            },
            {
                "name": "샤브댁 샤브샤브 (목심)",
                "price": "10,800원"
            },
            {
                "name": "목심 런치세트 (목심+야채+사리)",
                "price": "11,000원"
            }
        ],
        "time": "오늘 휴무\n07/26 휴무\n07/26 휴무\n금(7/26)\n휴무\n토(7/27)\n휴무\n일(7/28)\n휴무\n월(7/29)\n휴무\n화(7/30)\n휴무\n수(7/31)\n휴무\n목(8/1)\n휴무\n07/15-08/30 휴무\n접기"
    }
```
### 전처리
- 이미지는 최대 3개로 제한한다.
- x,xxx원을 int로 변환하고 그렇지 않은 경우는 모두 제외한다.

### 결과 
- (광진구 기준)
- 전체 음식점수 4259
- 메뉴룰 가지고 있는 음식점 수 1964
- 메뉴를 가지고 있지 않은 음식점 수(전처리 전) 2295
- 전체 메뉴수(전처리 전) 7970
- 전처리중 유실된 메뉴 수 1564