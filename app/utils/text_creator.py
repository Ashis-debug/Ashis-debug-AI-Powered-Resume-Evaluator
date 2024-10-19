# Create a textual description from the job description JSON
def create_job_description_text(job_desc):
    jd_text = f"""
    Job Title: {job_desc.get('job_name', 'N/A')}
    Designation: {job_desc.get('designation', 'N/A')}
    Company: {job_desc.get('comp_name', 'N/A')}
    Company Website: {job_desc.get('company_website_url', 'N/A')}
    Location: {', '.join(job_desc.get('job_location', [])) or 'N/A'}
    Diversity Preference: {job_desc.get('diversity', 'N/A')}

    Job Description: {job_desc.get('job_description', 'N/A')}

    Experience Required:
    - Minimum: {job_desc.get('min_work_exp', 'N/A')} years
    - Maximum: {job_desc.get('max_work_exp', 'N/A')} years

    Compensation:
    - Minimum: {job_desc.get('min_compensation', 'N/A')} {job_desc.get('compensation_type', 'N/A')}
    - Maximum: {job_desc.get('max_compensation', 'N/A')} {job_desc.get('compensation_type', 'N/A')}
    (Compensation visible: {'No' if job_desc.get('hide_compensation') else 'Yes'})

    Must-Have Skills: {', '.join(job_desc.get('must_have_skills', [])) or 'N/A'}
    Good-to-Have Skills: {', '.join(job_desc.get('good_to_have_skills', [])) or 'N/A'}

    Educational Qualifications: {', '.join(job_desc.get('educational_qualification', [])) or 'N/A'}
    Industry: {', '.join(job_desc.get('industry', [])) or 'N/A'}

    Perks and Benefits: {', '.join(job_desc.get('perk_and_benefits', [])) or 'N/A'}

    Application Process:
    - Interview Steps: {', '.join(job_desc.get('interview_steps', [])) or 'N/A'}
    - Screening Questions: {', '.join(job_desc.get('screeing_questions', [])) or 'N/A'}

    Job Status:
    - Approved: {'Yes' if job_desc.get('is_approved') else 'No'}
    - Urgent: {'Yes' if job_desc.get('is_urgent') else 'No'}
    - Hired Count: {job_desc.get('hired_count', 0)}
    - Number of Openings: {job_desc.get('no_of_opening', 0)}
    """
    return jd_text


# Create a textual description from the candidate details JSON
def create_candidate_text(candidate):
    candidate_text = f"""
    Candidate Name: {candidate.get('fname', '')} {candidate.get('lname', '')}
    Location: {candidate.get('city', 'N/A')}, {candidate.get('state', 'N/A')}, {candidate.get('country', 'N/A')}
    Total Experience: {candidate.get('total_experience', 'N/A')} years
    Relevant Experience: {candidate.get('relevant_experience', 'N/A')} years
    Current CTC: {candidate.get('current_CTC', 'N/A')} LPA
    Expected CTC: {candidate.get('expected_CTC', 'N/A')} LPA
    Skills: {', '.join(candidate.get('skills', [])) or 'N/A'}
    """
    return candidate_text
