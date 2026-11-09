# Habit Tracker 📝

A Python-based Habit Tracker designed to help users build consistency, monitor daily routines, and track their personal growth over time.

This project started as a simple console application and is being developed step by step into a more feature-rich habit tracking system.

## ✨ Features

### Implemented
- Add and track multiple daily habits.
- Mark habits as completed or missed.
- Calculate daily completion percentage.
- Display a daily progress summary.
- Save progress automatically using JSON.
- Maintain date-wise records.
- Preserve previous days' progress.

### Planned Features 🚀
- [ ] Habit history viewer
- [ ] Input validation and error handling
- [ ] Daily streak counter
- [ ] Weekly and monthly progress reports
- [ ] Edit and delete existing habits
- [ ] Interactive menu system
- [ ] GUI using Tkinter
- [ ] SQLite database integration

## 🛠️ Tech Stack

- **Language:** Python
- **Data Storage:** JSON (current)
- **Planned Database:** SQLite
- **Planned GUI:** Tkinter

## 📚 Concepts Practised

- Variables and Data Types
- Conditional Statements
- Loops
- Lists and Dictionaries
- String Formatting
- File Handling
- JSON Serialization and Deserialization
- OS Module
- Date and Time Handling

## 📂 Project Structure

```text
Habit-Tracker/
│
├── habit_tracker.py
├── habits.json
├── .gitignore
└── README.md
```

*Note: `habits.json` is generated automatically when the application saves its first entry.*

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd Habit-Tracker
```

### 3. Run the application

```bash
python habit_tracker.py
```

### 4. Start tracking!

Enter your habits and record whether you completed them for the day.

## 💾 Data Storage

The application stores daily progress in a JSON file using dates as keys.

Example:

```json
{
    "2026-11-09": {
        "Python": true,
        "DSA": true,
        "Workout": false
    }
}
```

Each date stores its own habit completion records, allowing progress to be preserved across multiple days.

## 🗺️ Development Roadmap

| Version | Planned Development |
|---|---|
| V1 | Basic Habit Tracking |
| V2 | JSON-based Data Persistence |
| V3 | Habit History Viewer |
| V4 | Input Validation |
| V5 | Streak Counter |
| V6 | Weekly Progress Reports |
| V7 | Edit and Delete Habits |
| V8 | Interactive Menu |
| V9 | GUI with Tkinter |
| V10 | SQLite Integration |

## 📌 Project Status

**Current Version:** V2 – JSON Data Persistence

**Status:** Actively developing 🚧

## 🎯 Goal

To gradually transform a beginner Python project into a complete habit tracking application while learning programming concepts, problem-solving, data persistence, and software development practices.

---

*Built with Python 🐍 | Learning by building, one version at a time.*
