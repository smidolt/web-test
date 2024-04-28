import json

def load_questions_from_json(file_path):
    try:
        with open(file_path, 'r') as f:
            questions = json.load(f)['questions']
        return questions
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON file '{file_path}'.")
        return []

def filter_questions(questions, role, experience_level):
    filtered_questions = [
        {"question": q['question']}
        for q in questions
        if q['role'] == role and q['experience_level'] == experience_level
    ]
    return filtered_questions

def save_filtered_questions_to_json(filtered_questions, output_file_path):
    try:
        with open(output_file_path, 'w') as f:
            json.dump(filtered_questions, f, indent=2)
        print(f"Filtered questions saved to '{output_file_path}'.")
    except FileNotFoundError:
        print(f"Output directory not found.")
    except PermissionError:
        print(f"Permission denied to write to '{output_file_path}'.")

if __name__ == "__main__":
    # Load questions from the JSON file (questions.json)
    questions = load_questions_from_json("questions.json")

    # Candidate attributes (role and experience level)
    candidate_role = "FrontEnd Developer"
    candidate_experience = "Senior"

    # Filter questions based on candidate attributes
    relevant_questions = filter_questions(questions, candidate_role, candidate_experience)

    # Save filtered questions to a new JSON file (filtered_questions.json)
    save_filtered_questions_to_json(relevant_questions, "filtered_questions.json")