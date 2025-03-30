from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

NOTION_API_KEY = os.environ.get("NOTION_API_KEY")
NOTION_DATABASE_ID = "1c5d76d4935c80d1886fee13ae9443b9"
NOTION_VERSION = "2022-06-28" 

@app.route('/create-eap-entry', methods=['POST'])
def create_eap_entry():
    notion_url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json"
    }

    data = request.get_json()

    if 'parent' not in data:
        data['parent'] = { "database_id": NOTION_DATABASE_ID }

    response = requests.post(notion_url, headers=headers, json=data)

    return jsonify(response.json()), response.status_code

app.run(host='0.0.0.0', port=3000)


