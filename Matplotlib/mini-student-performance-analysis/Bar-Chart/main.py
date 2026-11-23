import matplotlib.pyplot as plt
from pathlib import Path

subjects = ["Python", "C++", "SQL", "NumPy", "Matplotlib"]
marks = [85, 75, 90, 80, 95]

plt.figure(figsize=(8, 5))

plt.bar(subjects, marks, color="skyblue", edgecolor="black")

for i in range(len(subjects)):
    plt.text(i, marks[i], str(marks[i]), ha="center", va="bottom")

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Performance Analysis")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
output_path = Path(__file__).with_name("student_performance.png")

plt.savefig(output_path, dpi=300)
plt.show()