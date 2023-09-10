from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Get the current day of the week
    current_day = datetime.datetime.now().strftime("%A")

    # Get the current UTC time
    current_utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Construct the JSON response
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": "https://github.com/MERCY12-champ/HNG_Internship_2023/blob/main/app.py",
        "github_repo_url": "https://github.com/MERCY12-champ/HNG_Internship_2023.git",
        "status_code": 200
    }

    # Convert the response data to JSON format
    response_json = jsonify(response_data)

    # Return the JSON response with a 200 status code
    return response_json, 200

if __name__ == '__main__':
    app.run(debug=True)
