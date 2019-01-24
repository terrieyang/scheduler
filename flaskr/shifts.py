import numpy as np
import random
import copy
import datetime

def naive_assignment(names, tasks, weeks):
  assignments = []
  for i in range(weeks):
    assignments.append(rotate(names, i % len(tasks)))
  return assignments

def rotate(l, n):
    return l[n:] + l[:n]

def count(schedule, tasks, names):
  result = []
  for task in tasks:
    result.append([0] * len(names))
  for week in schedule:
    for i in range(len(week)):
      result[i][names.index(week[i])] += 1  
  return result

def score(count):
  score = 0.00
  for i in range(len(count)):
    score += np.std(list(zip(*count))[i])
  return score


def satisfied(schedule, constraints, tasks):
  for name, items in constraints.items():
    for week in schedule:
      for task in items:
        if week[tasks.index(task)] == name:
          return False
  return True

def constrain(schedule, constraints, tasks):
  print(constraints)
  t = datetime.datetime.now()
  print(t)
  while not satisfied(schedule, constraints, tasks):
    if datetime.datetime.now() > t + datetime.timedelta(0,1):
      return None
    for name, items in constraints.items():
      for week in schedule:
        for task in items:
          #task = task.decode('utf-8')
          while week[tasks.index(task)] == name:
            if datetime.datetime.now() > t + datetime.timedelta(0,1):
              return None
            n = random.randint(0, len(week) - 1)
            week[tasks.index(task)] = week[n]
            week[n] = name
  return schedule


def optimize(schedule, constraints, tasks, names):
  old_schedule = copy.deepcopy(schedule)
  week_num = random.randint(0, len(schedule) - 1)
  week = schedule[week_num]
  counts = count(schedule, tasks, names)
  curr_score = score(counts)


  num1 = random.randint(0, len(week) - 1)
  num2 = random.randint(0, len(week) - 1)

  while num2 == num1 or (week[num1] in constraints and tasks[num2] in constraints[week[num1]]) or (week[num2] in constraints and tasks[num1] in constraints[week[num2]]):
    num2 = random.randint(0, len(week) - 1)

  temp = week[num1]
  week[num1] = week[num2]
  week[num2] = temp

  counts = count(schedule, tasks, names)
  new_score = score(counts)

  if new_score > curr_score:
    schedule = old_schedule
  return schedule

