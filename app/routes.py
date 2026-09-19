from flask import Blueprint, request, jsonify, render_template
from app.database import lead_ekle, tum_leadler
from app.services.ai_service import ai_service, AIServiceError

api = Blueprint('api', __name__)
pages = Blueprint('pages', __name__)


@pages.route('/')
def anasayfa():
    return render_template('index.html')


@pages.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@api.route('/sohbet', methods=['POST'])
def sohbet():
    data = request.get_json(silent=True) or {}
    mesaj = data.get('mesaj')
    gecmis = data.get('gecmis', [])

    if not mesaj:
        return jsonify({"basari": False, "hata": "mesaj alanı zorunludur"}), 400

    try:
        cevap = ai_service.yanit_uret(mesaj, gecmis)
        return jsonify({"basari": True, "cevap": cevap}), 200
    except AIServiceError as e:
        return jsonify({"basari": False, "hata": str(e)}), 503


@api.route('/leads', methods=['POST'])
def yeni_lead():
    data = request.get_json(silent=True) or {}
    isim = data.get('isim')
    telefon = data.get('telefon')
    mesaj = data.get('mesaj')
    ilgi_alani = data.get('ilgi_alani')

    if not isim or not telefon:
        return jsonify({"basari": False, "hata": "isim ve telefon zorunludur"}), 400

    try:
        yeni_id = lead_ekle(isim, telefon, mesaj, ilgi_alani)
        return jsonify({"basari": True, "id": yeni_id}), 201
    except Exception as e:
        return jsonify({"basari": False, "hata": str(e)}), 500


@api.route('/leads', methods=['GET'])
def leadleri_getir():
    try:
        leadler = tum_leadler()
        return jsonify({"basari": True, "leadler": leadler}), 200
    except Exception as e:
        return jsonify({"basari": False, "hata": str(e)}), 500
    
    