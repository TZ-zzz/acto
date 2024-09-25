import openai
import argparse
import os
import json

def read_missing_properties(path):
    with open(path, 'r') as f:
        missing_properties = f.read().splitlines()
    return missing_properties

def gen_values(missing_values, path, api_key):
    openai.api_key = api_key
    
    prompt = "Here are some properties that need values:\n"
    for prop in missing_values:
        prompt += f"- {prop}\n"

    response = openai.Completion.create(
        model="chat:gpt-4-1o",
        prompt=prompt,
        max_tokens=150
    )
    
    result_text = response.choices[0].text.strip()
    result_lines = result_text.split("\n")
    result_dict = {}
    
    #TODO: modify the results processing part
    for prop, value in zip(missing_values, result_lines):
        result_dict[prop] = value.strip("- ")

    output_file = os.path.join(path, "values_for_missing_properties.json")
    with open(output_file, 'w') as f:
        json.dump(result_dict, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", type=str, help="Path to the file containing the missing properties")
    parser.add_argument("--api_key", type=str, help="API key for the OpenAI API")
    args = parser.parse_args()

    missing_properties = read_missing_properties(args.path)
    
    gen_values(missing_properties, args.path, args.api_key)
