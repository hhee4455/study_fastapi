import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

class Settings:
    """ 환경 설정 클래스 """
    MONGO_URI: str = os.getenv("MONGO_URI")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")

settings = Settings()
