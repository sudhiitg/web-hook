from flask import Flask, request, jsonify,json
from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv() 

app = Flask(__name__)

# # Set up MongoDB connection
mongo_uri = os.getenv('MONGO_URI')
client = MongoClient(mongo_uri)
db = client['github_events']  # Create a database called "github_events"
collection = db['events']  # Collection to store GitHub events

# Serve plain text on the home route
@app.route('/')

def home():
    return "Welcome to the GitHub Events Tracker! Use the /events endpoint to see recent events."


# # Webhook endpoint to receive GitHub actions
@app.route('/github', methods=['POST'])
def handle_webhook():
     if request.headers['content-type'] == 'application/json':
        event_type = request.headers.get('X-GitHub-Event')
        print("Received event type:", event_type)
        data = request.json

    # Convert back to JSON string (for logging or sending somewhere)
        json_string = json.dumps(data)

        # print("As Python dict:", data)
        # print("As JSON string:", json_string)
        if event_type == 'push':
         entry = {
            "type": "push",
            "author": data['pusher']['name'],
            "to_branch": data['ref'].split('/')[-1],
            "timestamp": data['commits'][0]['timestamp']
         }
        elif event_type == 'pull_request':
         pr = data['pull_request']
         entry = {
            "type": "merge" if pr.get('merged', False) and data['action'] == 'closed' else "pull_request",
            "author": pr['user']['login'],
            "from_branch": pr['head']['ref'],
            "to_branch": pr['base']['ref'],
            "timestamp": pr['updated_at']
             }
        else:
         return jsonify({"msg": "Unhandled event"}), 200
        collection.insert_one(entry)
        return jsonify({"msg": "Event stored"}), 201
        #  print("Entry to be saved:", entry)
@app.route('/api/events', methods=['GET'])
def get_events():
    events = list(collection.find({}, {'_id': 0}).sort("timestamp", -1).limit(20))
   
    # return render_template("index.html",events=events)
    return jsonify(events)



if __name__ == "__main__":
    app.run(debug=True, port=5000)
    