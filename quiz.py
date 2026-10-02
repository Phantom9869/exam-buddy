import json, urllib.request, re

URL = "http://localhost:11434/api/chat"
MODEL = "gemma3:4b"

def ask(prompt, as_json=False):
    body = {"model": MODEL, "stream": False,
            "messages": [{"role": "user", "content": prompt}]}
    if as_json:
        body["format"] = "json"
    req = urllib.request.Request(URL, json.dumps(body).encode(),
                                 {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read())["message"]["content"]

def clean_json(text):
    # Strip markdown fences like ```json ... ```
    text = re.sub(r'```(?:json)?\s*', '', text).strip()
    # Pull out the first { ... } block as a fallback
    match = re.search(r'\{.*\}', text, re.DOTALL)
    return match.group(0) if match else text

def get_answer():
    while True:
        raw = input("Your answer (1-4): ").strip()
        if raw in ("1", "2", "3", "4"):
            return int(raw) - 1
        print("  Please type 1, 2, 3, or 4.")

def load_questions(notes):
    # Trim to 3000 chars so the 4B model isn't overwhelmed
    notes = notes[:3000]
    for attempt in range(3):
        try:
            raw = ask(f"""Using ONLY these notes, write 5 multiple-choice questions.

Return ONLY valid JSON in exactly this format:
{{"questions":[
  {{
    "q": "What is the full question text?",
    "options": [
      "First full answer sentence",
      "Second full answer sentence",
      "Third full answer sentence",
      "Fourth full answer sentence"
    ],
    "answer": 0
  }}
]}}

Rules:
- options must be complete sentences, never single letters like A/B/C/D
- answer is the index (0-3) of the correct option
- base every question strictly on the notes below

NOTES:
{notes}""", as_json=True)
            return json.loads(clean_json(raw))["questions"]
        except (json.JSONDecodeError, KeyError) as e:
            print(f"  Bad JSON on attempt {attempt+1}: {e}, retrying...")
    raise RuntimeError("Gemma returned bad JSON 3 times. Try again.")

notes = open("notes.txt", encoding="utf-8").read()
print("""
When you get a question wrong, the app will explain the correct answer
using a theme or world you're familiar with — so it actually sticks.

Examples:
  football   → explains using players, tactics, and match situations
  cooking    → uses ingredients, recipes, and kitchen steps
  minecraft  → uses blocks, crafting, and game mechanics
  movies     → uses film plots, characters, and directors
  gym        → uses workouts, muscles, and training concepts

Pick anything you enjoy — the more specific, the better.
""")
style = input("Your explanation style: ").strip()

print("\nGenerating questions, please wait...\n")
questions = load_questions(notes)

score = 0
for i, q in enumerate(questions, 1):
    print(f"Q{i}. {q['q']}")
    for j, o in enumerate(q["options"]):
        print(f"  {j+1}. {o}")
    pick = get_answer()
    if pick == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        right = q["options"][q["answer"]]
        print(f"Not quite. Right answer: {right}")
        print("Explaining, please wait...")
        print(ask(f"Using a {style} analogy, briefly explain why '{right}' "
                  f"is the answer to: {q['q']}\nNotes:\n{notes}"))
        print()

print(f"Final score: {score}/{len(questions)}")