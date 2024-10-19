### README.md


# AI-Powered Resume Evaluator API

This project is a Flask-based API that uses AI to evaluate the suitability of a candidate's resume for a given job description. The system processes the resume (in PDF format) and compares it against the job description using Google Gemini AI to provide a detailed evaluation.

## Features

- Converts resume PDFs to images for processing.
- Extracts and compares job description details with the candidate's information.
- Provides an AI-based evaluation with insights on work experience, skills match, and location.
- Returns an overall match percentage along with other evaluation metrics.
  
## Technologies Used

- Python 3.12.4
- Flask
- Google Gemini AI
- Poppler-utils (for PDF processing)
- Docker

## Project Structure

```bash
AI-Powered-Resume-Evaluator/
├── app/
│   ├── __init__.py                 # Initializes the Flask app
│   ├── routes.py                   # Contains the API route for evaluation
│   ├── utils/
│   │   ├── pdf_converter.py        # Converts PDFs to images
│   │   ├── text_creator.py         # Generates text for job and candidate details
│   │   ├── gemini_integration.py   # Handles integration with Google Gemini AI
│   │   ├── response_cleaner.py     # Cleans and formats the AI response
│   └── config.py                   # Configuration for API keys and services
├── run.py                          # Entry point to start the Flask app
├── Dockerfile                      # Docker configuration
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

## API Endpoints

### 1. `/evaluate_resume` (POST)

This endpoint accepts a job description and candidate details (including a resume URL) and returns an AI-powered evaluation of the resume against the job description.

#### Request Example

```json
{
    "jobDescription": {
        "job_name": "Web Developer",
        "min_work_exp": "3",
        "max_work_exp": "7",
        "must_have_skills": ["HTML", "CSS", "JavaScript", "React"],
        "good_to_have_skills": ["Node.js", "TypeScript", "GraphQL"],
        "job_location": ["Bangalore"],
        "industry": ["Information Technology"],
        "perk_and_benefits": ["Health Insurance", "Remote Work"],
        "compensation_type": "lpa",
        "min_compensation": "8",
        "max_compensation": "15"
    },
    "candidateDetail": {
        "fname": "John",
        "lname": "Doe",
        "email": "john.doe@example.com",
        "resume": "https://example.com/path/to/resume.pdf",
        "linkedin_url": "https://linkedin.com/in/johndoe",
        "total_experience": "5",
        "relevant_experience": "4",
        "current_CTC": "6",
        "expected_CTC": "10",
        "notice_period": "30"
    }
}
```

#### Response Example

```json
{
    "evaluation": {
        "Overall Match Percentage": "80%",
        "Skills Match": ["HTML", "CSS", "JavaScript", "React"],
        "Skills Percentage": "75%",
        "Work Experience Match Percentage": "100%",
        "Location Match": "Yes",
        "Diversity Match": "Yes",
        "Reason": "The candidate has relevant skills and experience matching the job description."
    }
}
```

## Running the Project Locally

### Prerequisites

- [Python 3.12.4](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/)

### Step-by-Step Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-repo/AI-Powered-Resume-Evaluator.git
   cd AI-Powered-Resume-Evaluator
   ```

2. **Install the required dependencies**:

   Create and activate a virtual environment, then install the dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Run the Flask application**:

   ```bash
   python run.py
   ```

4. **Access the API**:

   The API will be running at `http://127.0.0.1:5000/`. You can use tools like Postman or `curl` to interact with it.

### Running with Docker

1. **Build the Docker image**:

   ```bash
   docker build -t ai-powered-resume-evaluator .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -d -p 5000:5000 ai-powered-resume-evaluator
   ```

3. **Access the API**:

   The API will be accessible at `http://localhost:5000/`.

## Example Input and Output

### Input (JSON):

```json
{
    "jobDescription": {
        "job_name": "Web Developer",
        "min_work_exp": "3",
        "max_work_exp": "7",
        "must_have_skills": ["HTML", "CSS", "JavaScript", "React"],
        "good_to_have_skills": ["Node.js", "TypeScript", "GraphQL"]
    },
    "candidateDetail": {
        "fname": "John",
        "lname": "Doe",
        "email": "john.doe@example.com",
        "resume": "https://example.com/path/to/resume.pdf"
    }
}
```

### Output (JSON):

```json
{
    "evaluation": {
        "Overall Match Percentage": "80%",
        "Skills Match": ["HTML", "CSS", "JavaScript", "React"],
        "Skills Percentage": "75%",
        "Work Experience Match Percentage": "100%",
        "Location Match": "Yes",
        "Reason": "The candidate has relevant skills and experience matching the job description."
    }
}
```

## License

