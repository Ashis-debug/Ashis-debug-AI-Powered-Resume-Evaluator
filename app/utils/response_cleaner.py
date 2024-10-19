import re
import json


# Clean the Gemini AI response by extracting the JSON part
def clean_gemini_response(response):
    # Extract the JSON part from the response string
    json_match = re.search(r'```json\n({.*?})\n```', response, re.DOTALL)

    if json_match:
        raw_json = json_match.group(1)

        # Clean up the raw_json to remove escaped characters like \"
        cleaned_raw_json = raw_json.replace('\\"', '"').replace('\\n', '').strip()

        # Convert the cleaned JSON string to a Python dictionary
        cleaned_json = json.loads(cleaned_raw_json)

        # Now, extract the reason part (after the JSON in the response)
        reason_match = re.search(r'\*\*Reason:\*\*\n\n(.+)', response, re.DOTALL)
        if reason_match:
            reason_text = reason_match.group(1)

            # Split reasons by the bullet points (*) and clean them
            reasons = [line.strip("* ").strip() for line in reason_text.split('\n') if line]

            # Add the cleaned reasons back to the JSON
            cleaned_json["Reason"] = reasons

        return cleaned_json
    else:
        return {"error": "Failed to extract JSON from the response"}
