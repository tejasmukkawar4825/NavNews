from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import os
import json  # Import JSON module for safe parsing

app = Flask(__name__)
CORS(app)

# Configure Gemini API (Ensure API key is correct)
genai.configure(api_key="AIzaSyA4ClpvC6Rrwj7c4WiKT7mWDhkj--Z6aNs")

# List available models
models = genai.list_models()
print("Available Models:")
for model in models:
    print(model.name)

def extract_event_links():
    url = "https://www.punekarnews.in/category/events/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = soup.find_all('h3', class_='article-title')
    hrefs = [article.find('a')['href'] for article in articles if article.find('a')]

    return hrefs

def get_event_details_from_gemini(paragraphs):
    model = genai.GenerativeModel("gemini-1.5-flash")  # Change to a working model

    prompt = f"""
    Extract structured event details from the following text. Identify the event name, date, time, venue and expected people count. 
    If any field is missing, return None.
    If the expected number of attendees is not explicitly mentioned, provide an estimated count based on the event type, venue size, and past similar events.

    Text: 
    {" ".join(paragraphs)}

    Format the response as JSON:
    {{"event_name": "...", "date": "...", "time": "...", "venue": "...", "expected_people_count": "..." }}
    """
    try:
      response = model.generate_content(prompt)
      print("Raw Response:", response.text)  # Debugging output

        # Extract only JSON data
      json_start = response.text.find("{")
      json_end = response.text.rfind("}") + 1
      event_data = json.loads(response.text[json_start:json_end])

      return event_data
    except Exception as e:
        print("Error parsing Gemini response:", e)
        return {"event_name": None, "date": None, "time": None, "venue": None,  "expected_people_count": None}

def extract_event_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    title = soup.find('h1', class_='entry-title').text.strip()
    entry_content = soup.find('div', class_='entry-content-wrap')
    image_tag = soup.find('div', class_='post-thumbnail full-width-image').find('img')
    image_url = image_tag['src'] if image_tag else "No image found" 
    paragraphs = [p.get_text(strip=True) for p in entry_content.find_all('p')]
    
    event_details = get_event_details_from_gemini(paragraphs)
    print(event_details)

    return {
        "title": title,
        "event_name": event_details["event_name"],
        "date": event_details["date"],
        "time": event_details["time"],
        "venue": event_details["venue"],
        "link": url,
        "image_url": image_url,
        "expected_people_count": event_details["expected_people_count"]
    }

def scrape_all_events():
    event_links = extract_event_links()
    events = []
    for link in event_links:
        events.append(extract_event_details(link))
    return events

@app.route('/api/data', methods=['GET'])
def get_data():
    events = scrape_all_events()
    print(events)
    return jsonify(events)

@app.route('/api/process', methods=['POST'])
def process_data():
    data = request.json
    result = {"processed_data": data["input"] * 2}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
