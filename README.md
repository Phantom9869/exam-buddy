# 📚 Exam Buddy

A local AI-powered quiz tool that turns your study notes into multiple-choice questions — and explains your mistakes in any analogy style you choose. Runs fully offline using [Ollama](https://ollama.com) and `gemma3:4b`.

---

## ✨ Features

- 📝 Generates MCQs directly from your own notes — choose 5, 10, or 15 questions per quiz
- 📚 Covers your entire notes file: long notes are automatically split into parts, one part per quiz, so nothing gets left out
- 🧠 Uses a local LLM (gemma3:4b via Ollama) — no API keys, no internet required
- 🎯 Explains wrong answers using a custom analogy style (football, cooking, movies — anything)
- 💬 Ask follow-up questions on any explanation that's still unclear — the chat keeps context from the original explanation
- 🔁 Retry just the questions you missed, instantly, with answer options reshuffled — no new Ollama call needed
- 🔀 Answer options are shuffled every time, so there's no position to memorize
- 📊 Score history — your last 8 quiz attempts are saved locally so you can track progress over time
- 💾 Remembers your notes, style, and question count between visits (stored only in your browser)
- 📂 Upload a `.txt` file straight into the notes box, or paste
- 📤 Export your results as a `.txt` file, or copy a summary to share with a friend
- 🌗 Web UI with light/dark theme toggle and keyboard shortcuts (A–D or 1–4 to answer, Enter for next)
- ⚡ Zero dependencies — the CLI uses only Python's built-in libraries; the web UI is a single HTML file

---

## 🛠️ Requirements

- Python 3.7+ (for the CLI version and to serve the web UI locally)
- [Ollama](https://ollama.com/download) installed and running
- `gemma3:4b` model pulled

---

## 🚀 Setup

**1. Pull the model (one-time):**
```bash
ollama pull gemma3:4b
```

**2. Clone the repo:**
```bash
git clone https://github.com/Phantom9869/exam-buddy.git
cd exam-buddy
```

**3. Add your notes:**

Replace `sample_notes.txt` with your own study notes, or use the included OS notes sample to try it out immediately. In the web UI you can also paste notes directly or upload a `.txt` file.

**4. Run it — pick CLI or web:**

**CLI:**
```bash
python quiz.py
```

**Web UI:**
```bash
python -m http.server 8000
```
Then open **http://localhost:8000** in your browser (don't open `index.html` directly — browsers block it from reaching Ollama that way).

---

## 🎮 How It Works

1. The notes file is read (CLI) or pasted/uploaded into the page (web UI)
2. You pick an explanation style (e.g. `cricket`, `cooking`, `Marvel movies`) and how many questions you want
3. Your notes are sent to `gemma3:4b` running locally via Ollama
4. You get multiple-choice questions, one at a time, with shuffled options
5. If you get one wrong, it explains the correct answer using your chosen analogy style — and you can ask follow-up questions if it's still not clicking
6. At the end you see your score, a full breakdown, and the option to retry just the questions you missed, save your results, or start a fresh quiz

```
Explain mistakes in what style? cricket

Q1. What is the kernel?
  1. A type of file system
  2. The one program running at all times on the computer
  3. A hardware component
  4. A system call interface
Your answer (1-4): 1
Not quite. Right answer: The one program running at all times on the computer
Think of it like the pitch in cricket — everything else (players, rules, equipment)
depends on it being there. Without the pitch, there's no game. Without the kernel,
there's no OS.
```

---

## 📁 Project Structure

```
exam-buddy/
├── quiz.py           # CLI quiz script
├── index.html        # Web UI (single-file, talks to Ollama directly)
├── sample_notes.txt  # Sample OS notes to test with
└── README.md
```

---

## 🗺️ Roadmap

- [x] CLI quiz from notes
- [x] Custom analogy-style explanations
- [x] Web UI (light/dark theme, keyboard shortcuts, shuffled answers)
- [x] Full notes coverage via automatic chunking
- [x] Follow-up Q&A on explanations
- [x] Retry missed questions
- [x] Score history
- [x] Choice of question count
- [x] Notes/style persistence + `.txt` upload
- [x] Export results
- [ ] Support for quizzing across multiple notes files at once
- [ ] Difficulty levels (easy/medium/hard questions)
- [ ] Export quiz as PDF

---

## 🤝 Contributing

Contributions are welcome! This project is participating in **Hacktoberfest**. Feel free to open issues or submit pull requests.

1. Fork the repo
2. Create a branch (`git checkout -b feat/your-feature`)
3. Commit your changes (`git commit -m "feat: add your feature"`)
4. Push and open a PR
