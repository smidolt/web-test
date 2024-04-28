import json
import logging

def filter_questions(data, difficulty_level=None, tags=None):
    filtered_questions = []
    for question in data['questions']:
        if (difficulty_level is None or question['difficulty_level'] == difficulty_level) and \
           (tags is None or set(tags).issubset(question['tags'])):
            filtered_questions.append(question)
    return filtered_questions

def process_json_file(input_file, output_file, difficulty_level=None, tags=None):
    try:
        with open(input_file, 'r') as file:
            data = json.load(file)
            filtered_questions = filter_questions(data, difficulty_level, tags)
            output_data = {'questions': filtered_questions}
            with open(output_file, 'w') as output:
                json.dump(output_data, output, indent=4)
            logging.info(f"Filtered questions saved to {output_file}")
    except FileNotFoundError:
        logging.error(f"Input file {input_file} not found")
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON format in {input_file}")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

# Example usage
input_file = 'interview_questions.json'
output_file = 'filtered_questions.json'
difficulty_level = "Beginner"
tags = ["Programming"]
process_json_file(input_file, output_file, difficulty_level, tags)