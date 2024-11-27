import requests
from config import CVE_API_URL

def fetch_cve_by_criteria(criteria):
    response = requests.get(f"{CVE_API_URL}last?{criteria}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erreur HTTP {response.status_code}: {response.text}")

# Test de la fonction avec critères
if __name__ == "__main__":
    criteria = "date=2024-11-27&type=network&system=linux"  # Exemple de critères supplémentaires
    try:
        cve_data = fetch_cve_by_criteria(criteria)
        if cve_data:
            for cve in cve_data:
                print(f"CVE ID: {cve['id']}, Description: {cve['summary']}")
        else:
            print("Aucun CVE trouvé.")
    except Exception as e:
        print(e)