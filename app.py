from flask import Flask, render_template

app = Flask(__name__)

# بياناتك الشخصية والمهارات والمشاريع الـ 11
USER_INFO = {
    "name": "Mohamad Badran Farhoud",
    "title": "AI Engineer at Homs University",
    "bio": "I am an AI Engineering student at Homs University, specializing in Artificial Intelligence and Natural Language Processing.",
    "email": "mohamad.farhoud@example.com",
    "github": "https://github.com/MohamadFarhoud9"
}

SKILLS = {
    "Languages": ["Python", "C++", "HTML", "CSS"],
    "Frameworks": ["Flask"],
    "Tools": ["Git", "GitHub"]
}

PROJECTS = [
    {
        "title": "Number_Guessing_Game",
        "description": "A simple interactive game: the program picks a secret number from 1 to 100, and the player keeps guessing until they find it with statistics and replay options.",
        "tech": "Python",
        "url": "https://github.com/MohamadFarhoud9/Number_Gussing_Game"
    },
    {
        "title": "Random-Password-Generator-Python",
        "description": "A simple Python command-line program that generates random passwords using uppercase letters, lowercase letters, numbers, and symbols.",
        "tech": "Python",
        "url": "https://github.com/MohamadFarhoud9/-Random-Password-Generator-Python-"
    },
    {
        "title": "drix-file-organizer-main",
        "description": "An automated Python utility that scans directories and intelligently organizes cluttered files into categorized folders based on their file extensions.",
        "tech": "Python",
        "url": "https://github.com/MohamadFarhoud9/drix-file-organizer-main"
    },
    {
        "title": "ytdlp-gui-master-Public",
        "description": "A user-friendly graphical interface built on top of yt-dlp to easily download videos and audio from YouTube and various platforms with simple clicks.",
        "tech": "Python, GUI",
        "url": "https://github.com/MohamadFarhoud9/ytdlp-gui-master-Public"
    },
    {
        "title": "Sales-data-analyziz",
        "description": "A data analysis project utilizing Python to process sales datasets, extract meaningful insights, identify trends, and generate analytical reports.",
        "tech": "Python, Data Analysis",
        "url": "https://github.com/MohamadFarhoud9/Sales-data-analyziz"
    },
    {
        "title": "Stock-tracker",
        "description": "A Python-based application designed to monitor stock prices, track market fluctuations, and help manage investment portfolios efficiently.",
        "tech": "Python",
        "url": "https://github.com/MohamadFarhoud9/Stock-tracker"
    },
    {
        "title": "text-to-speech",
        "description": "A Python application that converts written text into spoken audio output using speech synthesis libraries, providing a seamless text-to-audio experience.",
        "tech": "Python, Speech Synthesis",
        "url": "https://github.com/MohamadFarhoud9/text-to-speech"
    },
    {
        "title": "Taitanic-survival-analyziz",
        "description": "A machine learning and data analysis project utilizing the famous Titanic dataset to explore survival patterns, perform exploratory data analysis (EDA), and predict passenger survival outcomes.",
        "tech": "Python, Machine Learning",
        "url": "https://github.com/MohamadFarhoud9/Taitanic-survival-analyziz"
    },
    {
        "title": "Tinker-calculator",
        "description": "A desktop calculator application built using Python's Tkinter library, featuring a clean graphical user interface to perform standard mathematical calculations smoothly.",
        "tech": "Python, Tkinter",
        "url": "https://github.com/MohamadFarhoud9/Tinker-calculator"
    },
    {
        "title": "Audio-Extractor-master",
        "description": "A Python utility designed to extract audio tracks seamlessly from video files, converting and saving them into popular audio formats with high efficiency.",
        "tech": "Python, Audio Processing",
        "url": "https://github.com/MohamadFarhoud9/Audio-Extractor-master"
    },
    {
        "title": "Web-scraping-data",
        "description": "A Python web scraping tool built to automatically extract, parse, and structure data from websites into clean, usable formats for data analysis and automation.",
        "tech": "Python, Web Scraping",
        "url": "https://github.com/MohamadFarhoud9/Web-scraping-data"
    }
]

@app.route('/')
def home():
    return render_template('index.html', user=USER_INFO, skills=SKILLS, projects=PROJECTS)

if __name__ == '__main__':
    app.run(debug=True)