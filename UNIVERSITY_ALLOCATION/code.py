# Simple University Allocation

students = [
    {"name": "Ravi", "rank": 150},
    {"name": "Sita", "rank": 200},
    {"name": "Arjun", "rank": 50},
]

# Sort by rank
students.sort(key=lambda x: x["rank"])

# Allocate universities
universities = ["JNTU", "OU", "AU"]

for i, student in enumerate(students):
    # Simple logic: best rank gets first university
    alloc = universities[i % len(universities)]
    print(f"{student['name']} (Rank {student['rank']}) -> {alloc}")
