# Step 1: Import necessary libraries
import json  # Built-in library for parsing JSON data
import ollama  # Library to interact with local LLM

# Step 2: Define model and prompt
MODEL = "llama3"  # Using local Llama 3 model
# Explicitly instruct the model to return ONLY JSON with specific fields
PROMPT_TEXT = "Generate 10 fictional user profiles. Return ONLY valid JSON with a 'users' array. Keys: id (int), username (str), email (str), is_active (bool)."


# Step 3: Define the function header
def fetch_json_from_ollama(model_name, prompt_text):
    print(f"Querying {model_name} for JSON data...")
    # (We will add the API call code here in the next step)
    # Step 4: Call Ollama with format='json' to enforce structure
    response = ollama.chat(
        model=model_name,
        messages=[{"role": "user", "content": prompt_text}],
        format="json",
    )
    return response["message"]["content"]  # Return the raw JSON string


# Step 5: Main Execution Block
if __name__ == "__main__":
    raw_json = fetch_json_from_ollama(MODEL, PROMPT_TEXT)  # Get the raw string
    data = json.loads(raw_json)  # Parse the string into a Python Dictionary
    # Access the list inside the dictionary and print details
    print(f"\nSuccessfully parsed {len(data['users'])} users:")
    for user in data["users"]:
        print(f"- {user['username']} ({user['email']}) | Active: {user['is_active']}")

    # Step 6: Save the data to a JSON file
    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)  # indent=4 makes it pretty and readable
    print("Data successfully saved to 'users.json'")
