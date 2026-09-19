# SmartLead AI - İç Mimarlık Asistanı

Bu proje, iç mimarlık hizmetleri sunan bir firma için geliştirilmiş, yapay zekâ destekli bir müşteri iletişimi ve "lead" (müşteri adayı) toplama sistemidir. Yönergede belirtilen "Sorumlulukların Ayrılığı" (Separation of Concerns) ilkesine sadık kalınarak modüler bir mimariyle inşa edilmiştir.

## Projenin Amacı
Ziyaretçiler, web sitesindeki yapay zekâ asistanı ile iç mimarlık hizmetleri, tasarım süreçleri ve proje detayları hakkında sohbet edebilir. Sistem, danışmanlık veya projelendirme teklifi almak isteyen ziyaretçilerin iletişim bilgilerini (isim, telefon, mail) toplayarak veritabanına kaydeder ve bu kayıtları firma sahibine özel bir yönetim panelinde listeler.

## Kullanılan Teknolojiler
* **Backend:** Python, Flask
* **Yapay Zekâ:** Groq API (Llama-3.1-8b-instant)
* **Veritabanı:** SQLite
* **Frontend:** Wix Studio (Velo API & wix-fetch)
* **Deployment:** Render (Backend) & GitHub[cite: 2]

## Kurulum ve Çalıştırma (Yerel Geliştirme)
Projeyi kendi bilgisayarınızda test etmek ve çalıştırmak için aşağıdaki adımları izleyin:[cite: 2]

1. **Depoyu Klonlayın:**
   ```bash
   git clone [https://github.com/aysegulari306-del/smartlead-ai.git](https://github.com/aysegulari306-del/smartlead-ai.git)
   cd smartlead-ai
   
