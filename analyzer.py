import openai
from cve_search import fetch_cve_by_criteria

# Configuration
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your API key

BASE_PROMPT = """
You are a professional cybersecurity analyst. Your task is to provide detailed insights into software vulnerabilities and cybersecurity threats.
When given a description of a bug or vulnerability:
1. Explain the vulnerability in detail, including its impact and technical root cause.
2. Provide mitigation strategies or steps to secure systems against this vulnerability.
3. Respond as a cybersecurity expert, using technical but accessible language.
"""

def ask_ai(prompt):
    """Send a prompt to OpenAI and get the response."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": BASE_PROMPT}, {"role": "user", "content": prompt}],
            temperature=0.7,  # Adjust creativity
            max_tokens=1500   # Limit the length of the response
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error communicating with the AI: {e}"

def get_vulnerability_insights(criteria):
    """Fetch CVE data and get AI-generated insights."""
    try:
        # Fetch CVE data
        cve_data_list = fetch_cve_by_criteria(criteria)
        if not cve_data_list:
            return "No vulnerabilities found for the given criteria."

        insights = []
        for cve in cve_data_list[:5]:  # Limit to 5 results for brevity
            prompt = f"Here is a vulnerability: {cve['summary']}. Please provide insights."
            ai_response = ask_ai(prompt)
            insights.append(f"CVE ID: {cve['id']}\nSummary: {cve['summary']}\nAI Insights:\n{ai_response}\n{'-'*80}")

        return "\n".join(insights)

    except Exception as e:
        return f"Error fetching insights: {e}"

if __name__ == "__main__":
    # Example usage
    criteria = "date=2024-11-27&type=network&system=linux"  # Modify as needed
    print(get_vulnerability_insights(criteria))

