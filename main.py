from utils import run_llama

def roadmap(goal):
    prompt = f"Create a 12-month strategic roadmap to achieve this goal:\n{goal}"
    return run_llama(prompt)

if __name__ == "__main__":
    goal = input("Business goal: ")
    print(roadmap(goal))
