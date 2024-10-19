from flask import Blueprint, request, jsonify
import requests
from app.utils.pdf_converter import convert_pdf_to_images
from app.utils.text_creator import create_job_description_text, create_candidate_text
from app.utils.gemini_integration import get_gemini_response
from app.utils.response_cleaner import clean_gemini_response

# Define a blueprint for the API routes
evaluate_resume = Blueprint('evaluate_resume', __name__)

# Default route for the API
@evaluate_resume.route('/')
def home():
    return "Welcome to the AI-Powered Resume Evaluator API!"

# API route to evaluate resume and job description
@evaluate_resume.route('/evaluate_resume', methods=['POST'])
def evaluate_resume_route():
    try:
        data = request.get_json()

        # Extract job description and candidate details from the request
        job_desc_json = data.get("jobDescription")
        candidate_json = data.get("candidateDetail")
        resume_url = candidate_json.get("resume")

        # Validate required data
        if not job_desc_json or not candidate_json or not resume_url:
            return jsonify({"error": "Incomplete data provided"}), 400

        # Download and process the resume PDF
        resume_response = requests.get(resume_url)
        if resume_response.status_code != 200:
            return jsonify({"error": "Unable to download resume"}), 400

        # Convert resume PDF to images
        resume_content = convert_pdf_to_images(resume_response.content)

        # Generate text descriptions for job and candidate
        jd_text = create_job_description_text(job_desc_json)
        candidate_text = create_candidate_text(candidate_json)

        # Interact with Gemini AI to get the evaluation
        response_text = get_gemini_response(jd_text, candidate_text, [resume_content])

        # Clean the AI response and return it
        cleaned_response = clean_gemini_response(response_text)
        return jsonify({"evaluation": cleaned_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500