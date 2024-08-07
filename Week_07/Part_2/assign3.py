my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
for subject, rank in my_ranks.items():
  print(f"My Rank in {subject} Is {rank} And This Equal {100 if rank == 'A' else 80 if rank == 'B' else 60} Points")

total_rank = 0
for rank in my_ranks.values():
  if rank == 'A': value = 100
  elif rank == 'B': value = 80
  elif rank == 'C': value = 60
  total_rank += value

print(f"Total Points Is {total_rank}")