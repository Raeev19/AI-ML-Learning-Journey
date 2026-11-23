import matplotlib.pyplot as plt
from pathlib import Path    

marks = [85, 75, 90, 80, 95]

plt.figure(figsize=(8, 5))
plt.hist(marks, bins=5, color="orange", edgecolor="black", alpha
=0.7)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Student Performance Analysis")
plt.grid(axis="y", linestyle="--", alpha=0.5)           
plt.tight_layout()
output_path = Path(__file__).with_name("student_performance.png")
plt.savefig(output_path, dpi=300)
plt.show()            

