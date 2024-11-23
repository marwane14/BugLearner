import requests

def get_cve_data():
    # Exemple de récupération des CVE depuis l'API du NVD
    url = "url a mettre"
    response = requests.get(url)
    cve_data = response.json()
    return cve_data['CVE_Items'][:10]  # Récupère les 10 dernières CVE par exemple
