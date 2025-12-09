students = {}

print("Вводьте ім'я студента та оцінку. Щоб завершити — введіть 'stop'.")

while True:
    name = input("Ім'я студента: ")

    if name.lower() == "stop":
        break

    try:
        grade = int(input("Оцінка (1-12): "))
    except ValueError:
        print("Оцінка має бути числом!")
        continue

    if grade < 1 or grade > 12:
        print("Оцінка має бути від 1 до 12.")
        continue

    students[name] = grade

print("\n--- РЕЗУЛЬТАТИ ---")

print("\nСписок студентів і їхні оцінки:")
for name, grade in students.items():
    print(f"{name}: {grade}")

grades = list(students.values())

if grades:  
    avg_grade = sum(grades) / len(grades)
else:
    avg_grade = 0

excellent = [name for name, g in students.items() if 10 <= g <= 12]
good = [name for name, g in students.items() if 7 <= g <= 9]
middle = [name for name, g in students.items() if 4 <= g <= 6]
bad = [name for name, g in students.items() if 1 <= g <= 3]

print(f"\nСередній бал по групі: {avg_grade:.2f}")

print(f"\nВідмінники (10–12): {len(excellent)} — {', '.join(excellent) if excellent else 'немає'}")
print(f"Хорошисти (7–9): {len(good)} — {', '.join(good) if good else 'немає'}")
print(f"Відстаючі (4–6): {len(middle)} — {', '.join(middle) if middle else 'немає'}")
print(f"Не здали (1–3): {len(bad)} — {', '.join(bad) if bad else 'немає'}")
