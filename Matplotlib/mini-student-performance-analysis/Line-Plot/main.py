import matplotlib.pyplot as plt
from pathlib import Path

subjects = ["Python", "C++", "SQL", "NumPy", "Matplotlib"]
marks = [85, 75, 90, 80, 95]

study_hours = [3, 2, 2.5, 3.5, 4]

plt.figure(figsize=(8, 5))

plt.plot(subjects, study_hours, color="green",
         marker="o", linestyle="--", label="Study Hours")

plt.xlabel("Subjects")
plt.ylabel("Study Hours")
plt.title("Study Hours Analysis")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
output_path = Path(__file__).with_name("study_hours.png")

plt.savefig(output_path, dpi=300)
plt.show()