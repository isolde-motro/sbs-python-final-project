import streamlit as st
import requests
import json

st.set_page_config(page_title="AI Meal & Workout Planner", layout="centered")

def send_data_to_n8n(data):
    webhook_url = "https://isoldemotro.app.n8n.cloud/webhook/49a65ba0-529e-4a65-bb1f-60f164e6416a"
    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code >= 200 and response.status_code < 300:
            response_json = response.json()
            output_text = response_json.get('output')

            if not output_text:
                st.error("No 'output' field found in the response.")
                return None

            st.success("✅ Your plan has been generated! Check the next tabs.")
            return output_text
        else:
            st.error(f"❌ Error: Received status code {response.status_code}")
            return None
    except Exception as e:
        st.error(f"❌ Error submitting data: {e}")
    return None

def display_and_store_result(name, output_text):

    # parse the JSON string into a Python dict
    parsed_data = json.loads(output_text)

    # Now you can access the fields directly:
    st.session_state["user_name"] = name
    st.session_state["meal_plan"] = parsed_data['meal_plan']
    st.session_state["grocery_list"] = parsed_data['grocery_list']
    st.session_state["workout_plan"] = parsed_data['workout_plan']

    # meal_plan = parsed_data['meal_plan']
    # grocery_list = parsed_data['grocery_list']
    # workout_plan = parsed_data['workout_plan']

    # st.session_state["user_name"] = name
    # st.session_state["plan_text"] = output_text

# -------------- Main Streamlit UI below --------------

st.title("🥗 AI-Powered Meal & Workout Planner")

user_type = st.radio("Select user type:", ["New User", "Existing User"])

tab1, tab2, tab3 = st.tabs(["📝 Fill Your Info", "🥦 Diet & Grocery List", "🏋️ Workout Plan"])

with tab1:
    st.header("Step 1: Tell us about yourself")

    name = st.text_input("🧑 Your name (required)")
    if not name:
        st.warning("You must enter a name — this is how we track your data.")

    if user_type == "New User":
        goal = st.selectbox("🎯 Your fitness goal", ["", "Lose weight", "Gain muscle", "Maintain"])
        way_of_eating = st.selectbox("🍽️ Dietary preference", ["", "Balanced", "Vegetarian", "Vegan", "Keto", "No preference"])
        budget = st.number_input("💰 Weekly grocery budget (€)", min_value=0.0, format="%.2f")
        weight = st.number_input("⚖️ Your current weight (kg)", min_value=0.0, format="%.1f")
        height = st.number_input("📏 Your height (cm)", min_value=0.0, format="%.1f")

        required_filled = all([
            name.strip(),
            goal.strip(),
            way_of_eating.strip(),
            budget > 0,
            weight > 0,
            height > 0
        ])

        if st.button("🚀 Generate My Plan"):
            if not required_filled:
                st.error("Please fill in all required fields for a new user.")
            else:
                data = {
                    "name": name,
                    "goal": goal,
                    "way_of_eating": way_of_eating,
                    "budget": budget,
                    "weight": weight,
                    "height": height,
                }
                response_result = send_data_to_n8n(data)
                if response_result:
                    display_and_store_result(name, response_result)

    else:  # Existing User
        lifted_weight = st.text_input("🏋️ Weight lifted this week (required)")
        notes = st.text_area("📝 Any additional notes or progress (required)")

        if st.button("🚀 Generate My Plan"):
            if not name.strip():
                st.error("Please enter your name.")
            elif not lifted_weight.strip():
                st.error("Please enter lifted weight for existing user.")
            elif not notes.strip():
                st.error("Please enter notes for existing user.")
            else:
                data = {
                    "name": name,
                    "lifted_weight": lifted_weight,
                    "notes": notes
                }
                response_result = send_data_to_n8n(data)
                if response_result:
                    display_and_store_result(name, response_result)

with tab2:
    st.header("Your AI-Generated Meal Plan & Grocery List")

    if "user_name" not in st.session_state:
        st.info("Please fill in your info first in the first tab.")
    else:
        st.subheader(f"Hello, {st.session_state['user_name']} 👋")
        st.markdown("### 🍽️ Meal Plan")
        st.markdown(st.session_state.get("meal_plan", "No meal plan found."))

        st.markdown("### 🛒 Grocery List")
        grocery_list = st.session_state.get("grocery_list", [])
        if isinstance(grocery_list, list):
            for item in grocery_list:
                st.write("- " + item)
        else:
            st.write(grocery_list)

with tab3:
    st.header("Your AI-Generated Workout Plan")

    if "user_name" not in st.session_state:
        st.info("Please fill in your info first in the first tab.")
    else:
        st.subheader(f"Let's get moving, {st.session_state['user_name']}!")

        workout_plan = st.session_state.get("workout_plan", "")

        if workout_plan:
            if isinstance(workout_plan, list):
                # workout_plan is a list of daily plans, just print each line
                for day in workout_plan:
                    st.write(day)
            elif isinstance(workout_plan, str):
                # workout_plan is a string, split by new lines or periods
                days = [d.strip() for d in workout_plan.replace('\n', ' ').split('. ') if d.strip()]
                for day in days:
                    st.write(day + ".")
            else:
                st.write("Workout plan format not recognized.")
        else:
            st.write("No workout plan found.")



