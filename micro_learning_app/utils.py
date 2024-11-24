from openai import OpenAI
import os

# Set OpenAI API key
os.getenv('OPENAI_API_KEY')
client = OpenAI()
def get_recommendation(prompt):
    try:
        response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an assistant that provides hobby recommendations based on user details. You are striclty providing the answer related to that"},
            {"role": "user", "content": prompt}
        ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Log the error if necessary
        print(f"OpenAI API error: {e}")
        return "Sorry, there was an error processing your request. Please try again later."
   
