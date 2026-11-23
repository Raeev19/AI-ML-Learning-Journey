
import matplotlib.pyplot as plt
from pathlib import Path

# Dataset
subjects = ["Python", "C++", "SQL", "NumPy", "Matplotlib"]
marks = [85, 75, 90, 80, 95]
study_hours = [3, 2, 2.5, 3.5, 4]

# Create 2x2 dashboard
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# 1. Bar Chart
ax[0, 0].bar(
    subjects, marks,
    color="skyblue",
    edgecolor="black"
)
ax[0, 0].set_title("Subject-wise Marks")
ax[0, 0].set_xlabel("Subjects")
ax[0, 0].set_ylabel("Marks")
ax[0, 0].grid(axis="y", linestyle="--", alpha=0.5)
ax[0, 0].tick_params(axis="x", rotation=20)

# 2. Line Plot
ax[0, 1].plot(
    subjects, study_hours,
    color="green",
    marker="o",
    linestyle="--",
    label="Study Hours"
)
ax[0, 1].set_title("Study Hours by Subject")
ax[0, 1].set_xlabel("Subjects")
ax[0, 1].set_ylabel("Study Hours")
ax[0, 1].legend()
ax[0, 1].grid(axis="y", linestyle="--", alpha=0.5)
ax[0, 1].tick_params(axis="x", rotation=20)

# 3. Pie Chart
ax[1, 0].pie(
    marks,
    labels=subjects,
    autopct="%1.1f%%",
    startangle=90
)
ax[1, 0].set_title("Marks Distribution")

# 4. Scatter Plot
ax[1, 1].scatter(
    study_hours, marks,
    color="purple",
    s=100,
    alpha=0.7,
    edgecolor="black"
)
ax[1, 1].set_title("Study Hours vs Marks")
ax[1, 1].set_xlabel("Study Hours")
ax[1, 1].set_ylabel("Marks")
ax[1, 1].grid(axis="both", linestyle="--", alpha=0.5)

# Main Dashboard Title
fig.suptitle(
    "Student Performance Dashboard",
    fontsize=16,
    fontweight="bold"
)

# Adjust layout
plt.tight_layout()

# Save dashboard
output_path = Path(__file__).with_name("student_dashboard.png")
plt.savefig(output_path, dpi=300, bbox_inches="tight")

print(f"Dashboard saved at: {output_path}")
