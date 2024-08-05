students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

for student, subjects in students.items():
  print("-" * 50)
  print(f"-- Student Name => {student}")
  print("-" * 50)
  total_rank = 0
  for subject, rank in subjects.items():
    if rank == 'A': value = 100
    elif rank == 'B': value = 80
    elif rank == 'C': value = 40
    elif rank == 'D': value = 20
    total_rank += value
    print(f"- {subject} => {value} Points")
  else:
    print(f"Total Points For {student} Is {total_rank}")
