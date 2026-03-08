import google.generativeai as genai

genai.configure(api_key="api_key")

model = genai.GenerativeModel("models/gemini-2.0-flash")

def get_ai_diagnosis(severity):

    prompt = f"""
    A plant leaf analysis detected severity level: {severity}.
    Suggest possible plant disease and treatment.
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception:
        # fallback if API fails
        if severity == "Healthy":
            return "The plant leaf appears healthy. Maintain proper watering and sunlight."
        elif severity == "Mild":
            return "Possible early nutrient deficiency. Monitor the plant and adjust fertilizer."
        elif severity == "Moderate":
            return "Possible leaf spot disease. Remove infected leaves and improve airflow."
        elif severity == "Severe":
            return "Possible fungal infection. Apply fungicide and isolate the plant."
        else:
            return "Severe plant damage detected. Consider replacing the plant and improving soil quality."




