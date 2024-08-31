import random
import json

# Step 1: Load JSON data from file
def load_prompts(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Step 2: Function to generate a random prompt
def generate_prompt(category, prompt_data):
    if category in prompt_data:
        return random.choice(prompt_data[category])
    else:
        return "Invalid category. Please choose from the following: " + ", ".join(prompt_data.keys())

# Step 3: User interaction
def main():
    prompt_data = load_prompts('prompts.json')
    
    print("Welcome to the Prompt Generator!")
    print("Please choose a category: ")
    for category in prompt_data.keys():
        print(f"- {category}")
    
    chosen_category = input("Enter your chosen category: ").strip().lower()
    prompt = generate_prompt(chosen_category, prompt_data)
    
    print("\nGenerated Prompt:")
    print(prompt)

if __name__ == "__main__":
    main()
