# utils.py

import openai

def enhance_internship_description(description):
    # Set your OpenAI API key here
    openai.api_key = 'api-key-here'

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Transform the following internship experience into three technical, recruiter-appealing bullet points:\n\n{description}"},
            ],
            max_tokens=150
        )
        enhanced_description = response['choices'][0]['message']['content'].strip()
        return enhanced_description
    except Exception as e:
        print(f"Error in OpenAI API call: {e}")
        return description  # Return the original description in case of an error
    
def enhance_project_description(description2):
    # Set your OpenAI API key here
    openai.api_key = 'api-key-here'

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Transform the following project description into recruiter-appealing bullet points. Make two bullet points with:\n\n{description2}"},
            ],
            max_tokens=150
        )
        enhanced_description2 = response['choices'][0]['message']['content'].strip()
        return enhanced_description2
    except Exception as e:
        print(f"Error in OpenAI API call: {e}")
        return description2  # Return the original description in case of an error
    


