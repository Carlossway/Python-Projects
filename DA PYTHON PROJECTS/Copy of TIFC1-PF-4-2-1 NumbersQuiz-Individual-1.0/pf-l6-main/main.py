def main():
  print("Hello learners!")
import requests

def trivia_fetch(num):
    """Fetches trivia about a given number using the Numbers API."""
    url = f"http://numbersapi.com/{num}?json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {"number": num, "text": data.get("text", "No trivia available.")}
    else:
        return {"number": num, "text": "No trivia available for this number."}

def main():
    print("Welcome to the Number Trivia Quiz!")
    score = 0
    for _ in range(3):  # 3 trivia questions
        num = int(input("Enter a number: "))
        trivia = trivia_fetch(num)
        print(f"Trivia: {trivia['text']}")
        user_input = input(f"What number do you think this trivia is about? ")
        if user_input.isdigit() and int(user_input) == num:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {num}.")
    print(f"Quiz Over! Your score: {score}/3")
40
if __name__=="__main__":
  main()