from TravelAgents import guide_expert, location_expert, planner_expert
from TravelTasks import location_task, guide_task, planner_task
from crewai import Crew, Process
import time
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/recommendations', methods=['POST'])
def get_recommendations():
    data = request.get_json()
    from_city = data.get('from_city', 'India')
    destination_city = data.get('destination_city', 'Rome')
    date_from = data.get('date_from')
    date_to = data.get('date_to')
    interests = data.get('interests', 'sightseeing and good food')

    # Initialize Tasks
    loc_task = location_task(location_expert, from_city, destination_city, date_from, date_to)
    guid_task = guide_task(guide_expert, destination_city, interests, date_from, date_to)
    plan_task = planner_task([loc_task, guid_task], planner_expert, destination_city, interests, date_from, date_to)

    # Define Crew
    crew = Crew(
        agents=[location_expert, guide_expert, planner_expert],
        tasks=[loc_task, guid_task, plan_task],
        process=Process.sequential,
        full_output=True,
        verbose=True,
        token_usage=True,
        planning_llm=True
    )

    # Run Crew AI
    result = crew.kickoff()
    time.sleep(10)

    return jsonify({'recommendations': str(result)})

if __name__ == '__main__':
    app.run(port=5000)
