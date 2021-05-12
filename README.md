# Korea-Subway ![Python versions](https://img.shields.io/badge/Language-Python3-blue) ![License](https://img.shields.io/badge/License-MIT-green) ![Release](https://img.shields.io/badge/Last_Update-2021.05.12-red)
Korea subway location and connection information <br>
대한민국 지하철 GPS 좌표 및 노선도 연결 그래프 <br>
~~코리아 샌드위치 아닙니다~~<br>

## Overview

대한민국 지하철 노선도를 그래프화시키기 위한 오픈소스 프로젝트입니다! 

대한민국의 지하철/도시철도의 GPS 좌표 및 연결된 역 정보들을 관리합니다.

현재는 수도권만 구현되어 있어요!



현재까지 구현된 지역은 다음과 같습니다.

- **수도권: 2021.05.12 업데이트**



## Usage

해당 Repo를 다운받으셔서 dataset에 있는 각 지역별 노선도 정보 파일을 자유롭게 사용하시면 됩니다.

assets에는 각 호선에 매칭되는 Icon 이미지가 들어있어요. 혹시 필요하시다면 사용해주세요!

### dataset

- `captialStations.json`: 수도권

### assets

- `capitalSubwayIcon/`: 수도권 호선별 아이콘



모든 json 파일은 `UTF-8-SIG` 인코딩으로 되어 있습니다. 

따라서, Python3 기준으로 Json 파일을 불러오기 위해서 아래와 같이 코드를 작성하여 사용하시면 됩니다.

```python
FILE_PATH = '~/data.json'
with open(FILE_PATH, "r", encoding='UTF-8-sig') as f:
    result = json.load(f) # Json data load
```





## Contributing





## 도움을 주신 분들

- [@NB](https://github.com/altmshfkgudtjr)

