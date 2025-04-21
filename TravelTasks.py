from crewai import Task

def location_task(agent, from_city, destination_city, date_from, date_to):
    return Task(
        description=f"""Provide travel logistics (visa, transport) from {from_city} to {destination_city} ({date_from} - {date_to}).""",
        expected_output="A detailed markdown report with relevant travel data.",
        agent=agent,
        output_file='city_report.md',
    )

def guide_task(agent, destination_city, interests, date_from, date_to):
    return Task(
        description=f"""Create a travel guide for {destination_city} ({date_from} - {date_to}), recommending top 5 attractions and food based on {interests}.""",
        expected_output="A markdown itinerary including attractions, food, and activities.",
        agent=agent,
        output_file='guide_report.md',
    )

def planner_task(context, agent, destination_city, interests, date_from, date_to):
    return Task(
        description=f"""Create a structured travel itinerary for {destination_city} ({date_from} - {date_to}) based on {interests}, including city introduction, daily plan, expenses, and tips.""",
        expected_output="A structured markdown travel itinerary.",
        context=context,
        agent=agent,
        output_file='travel_plan.md',
    )
