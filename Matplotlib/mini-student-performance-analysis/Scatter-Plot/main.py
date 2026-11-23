import matplotlib.pyplot as plt
from pathlib import Path

study_hours = [3, 2, 2.5, 3.5, 4]
marks = [85, 75, 90, 80, 95]

plt.figure(figsize=(8, 5))
plt.scatter(study_hours, marks, color="blue", alpha=0.7)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.grid(axis="both", linestyle="--", alpha=0.5)
plt.tight_layout()
output_path = Path(__file__).with_name("study_hours_vs_marks.png")
plt.savefig(output_path, dpi=300)
plt.show()          