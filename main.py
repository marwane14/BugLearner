import cve_scraper
import summarizer
import ai_explainer

def main():
    # Récupérer les CVE
    cve_data = cve_scraper.get_cve_data()

    # Résumer les CVE récupérées
    summaries = summarizer.summarize_cves(cve_data)

    # Utiliser l'IA pour expliquer les CVE
    explanations = ai_explainer.explain_with_ai(summaries)

    # Afficher ou retourner les résultats
    for cve, explanation in zip(summaries, explanations):
        print(f"CVE: {cve['id']}\nExplication: {explanation}\n")

if __name__ == '__main__':
    main()
