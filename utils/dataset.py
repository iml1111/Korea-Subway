"""
dataset/ 내의 각 지역 노선도 json 파일 경로를 관리합니다.
"""
BASE_DIR = "./dataset/%s.json"
DATA_PATH = {
    # 수도권 노선도 정보
    'capital': BASE_DIR % "capitalStations",
}