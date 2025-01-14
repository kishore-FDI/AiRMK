import requests

# Base URL for your local Flask app
base_url = "http://localhost:10000"

# Test the health check endpoint
response = requests.get(f"{base_url}/")
print("Health check response:", response.json())

# Test questions
test_questions = [
    "What is R.M.K?",
    "Who is the Chairmain and Vice Chairman of R.M.K?",
    "Where is R.M.K Located?"
]

# Test each question
for question in test_questions:
    print(f"\nAsking: {question}")
    response = requests.post(
        f"{base_url}/query", 
        json={"question": question}
    )
    result = response.json()
    if 'error' in result:
        print("Error:", result['error'])
    else:
        print("Answer:", result['answer'])
        # print("\nContext used:", result['context']) 