import requests
from datetime import datetime, timedelta
import html

# API configuration
def get_stackoverflow_questions():
    api_url = "https://api.stackexchange.com/2.3/questions"
    params = {
        "order": "desc",
        "sort": "creation",
        "tagged": "python",
        "site": "stackoverflow",
        "fromdate": int((datetime.now() - timedelta(days=2)).timestamp()),
    }

    # Sending HTTP request on API
    response = requests.get(api_url, params=params)
    
    # Response processing
    if response.status_code == 200:
        questions = response.json()["items"]
        return questions
    else:
        print(f"Chyba při komunikaci se stackoverflow API: {response.status_code}")
        return None

# Formatting and printing of questions
def format_print_questions(questions):
    for i, question in enumerate(questions, start=1):
        title = html.unescape(question["title"])
        print(f"Otázka číslo: {i}; {datetime.utcfromtimestamp(question['creation_date']).strftime('%Y-%m-%d %H:%M:%S')}")
        print(question["tags"])
        print(title)
        print(question["link"])
        print("...")


# Direct script launch instead of modul
if __name__ == "__main__":
    questions = get_stackoverflow_questions()

    if questions:
        format_print_questions(questions)

