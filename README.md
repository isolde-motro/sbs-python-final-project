# sbs-python-final-project
# AI-Powered Meal & Workout Planner

This is a Streamlit web application that uses AI to generate personalized meal plans, grocery lists, and workout routines based on user input. The app tracks your gym progress and adapts your plans accordingly, helping you stay on track with your fitness goals.

---

## Features

- New User Mode: Generate a personalized meal and workout plan based on your fitness goal, dietary preferences, budget, weight, and height.
- Existing User Mode: Update your weekly workout progress and notes to receive updated plans.
- AI-generated weekly meal plans and grocery lists tailored to your preferences and budget.
- AI-generated workout plans adjusted to your progress.
- Clean and intuitive UI using Streamlit tabs for input, meal/grocery plan, and workout plan.
- Integration with an n8n workflow via webhook for backend AI processing.

---

## How It Works

1. **User Input:** You enter your details and goals or update your weekly progress.
2. **Data Submission:** The app sends your data to an n8n webhook endpoint.
3. **AI Processing:** The backend (managed by n8n) generates personalized meal, grocery, and workout plans.
4. **Display Results:** The plans are parsed and displayed in the app under separate tabs.

---

## Tech Stack

- Frontend: Streamlit
- Backend Automation: n8n (workflow automation and AI integration)
- Communication: REST API calls (POST requests to n8n webhook)
- Data Format: JSON

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Streamlit
- Requests library

### Installation

1. Clone this repository:

   git clone https://github.com/yourusername/ai-meal-workout-planner.git
   cd ai-meal-workout-planner

2. Create and activate a Python virtual environment (optional but recommended):

   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. Install dependencies:

   pip install -r requirements.txt

4. Run the app:

   streamlit run app.py

5. Open your browser and go to http://localhost:8501

---

## Configuration

- Replace the placeholder webhook URL below with your own n8n webhook URL in the app.py file:

  webhook_url = "https://your-n8n-instance.com/webhook/your-webhook-id"

---

## Usage

- Select whether you are a "New User" or "Existing User".
- Fill in the required fields and submit your data.
- Your personalized meal plan, grocery list, and workout plan will be generated and displayed in separate tabs.
- For new users, fill in your fitness goal, diet preferences, budget, weight, and height.
- Existing users can update lifted weight and notes to adjust plans.

---

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- Built with Streamlit
- Workflow automation powered by n8n
