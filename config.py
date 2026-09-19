import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'varsayilan-anahtar')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'aktis.db')
    GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')
    AI_PROVIDER = os.environ.get('AI_PROVIDER', 'groq')
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS', '*')

    BUSINESS_CONTEXT = """Sen AKTIS adli aydinlatma tasarim markasinin
musteri asistanisin. AKTIS, hareket eden formlarla isigi sekillendiren
ozel tasarim lambalar ve aydinlatma urunleri satar (marka felsefesi:
"Form Shapes Light"). Ziyaretcilere urun koleksiyonlari, tasarim felsefesi,
kargo ve iade politikasi hakkinda kisa ve samimi bilgi ver. Turkce konus.
Musteriyi favori tasarimini soylemeye ve iletisim bilgisi birakmaya
yonlendir ki ekibimiz kendisine ozel oneri ve fiyat teklifi ile donsun.
Kisa, sicak ve zarif bir ton kullan; asiri satis dili kullanma."""


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

