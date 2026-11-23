import matplotlib.pyplot as plt
from pathlib import Path

subjects = ["Python", "C++", "SQL", "NumPy", "Matplotlib"]
marks = [85, 75, 90, 80, 95]

study_hours = [3, 2, 2.5, 3.5, 4]

plt.figure(figsize=(8, 5))
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Student Performance Analysis")
plt.axis("equal")
output_path = Path(__file__).with_name("student_performance.png")
plt.savefig(output_path, dpi=300)