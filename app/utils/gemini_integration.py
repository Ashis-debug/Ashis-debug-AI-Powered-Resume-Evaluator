import google.generativeai as genai
from app.config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)


# Interact with Gemini AI using job and resume data to get evaluation response
def get_gemini_response(jd_text, candidate_text, resume_content):
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Flatten the list of resume content (base64 images)
    flat_resume_content = [part for content_list in resume_content for part in content_list]

    # Combine the job description and candidate details into the prompt
    input_prompt = f"""
        You are an ATS system. Evaluate the following resume against the job description.

        Job Description:
        {jd_text}

        Candidate Information:
        {candidate_text}

        Compare the two and return a JSON response with the following fields:

        1. 'Work Experience Match Percentage': Percentage of work experience match.
        2. 'Location Match': Yes or No.
        3. 'Skills Match': List of matching skills.
        4. 'Overall Match Percentage': Overall match percentage between the resume and the job description.
        5. 'Skills Percentage': Percentage of skills match.
        6. 'Diversity Match': Yes or No, based on the company's diversity requirement.
        7. 'Reason': Provide reasons for the evaluation, explaining why the percentages were calculated as they were.

        Return the response as a JSON.
    """

    # Send the input prompt and resume images to Gemini
    response = model.generate_content([input_prompt] + flat_resume_content)
    return response.text
