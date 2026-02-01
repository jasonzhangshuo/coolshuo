print("Hello Codex")

# Skills Section
skills = {
    "Programming Languages": [
        "Python",
        "JavaScript",
        "TypeScript",
        "Java",
        "C++"
    ],
    "Web Development": [
        "HTML/CSS",
        "React",
        "Vue.js",
        "Node.js",
        "Django"
    ],
    "Data Science": [
        "Pandas",
        "NumPy",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch"
    ],
    "Tools & Platforms": [
        "Git",
        "Docker",
        "AWS",
        "Linux",
        "PostgreSQL"
    ]
}

def display_skills():
    print("\n" + "=" * 50)
    print("           MY SKILLS")
    print("=" * 50)

    for category, skill_list in skills.items():
        print(f"\n{category}:")
        print("-" * len(category))
        for skill in skill_list:
            print(f"  - {skill}")

    print("\n" + "=" * 50)

if __name__ == "__main__":
    display_skills()
