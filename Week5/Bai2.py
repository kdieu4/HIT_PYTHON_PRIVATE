students = [{"id": 1, "name": "An", "score": 8.5},
            {"id": 2, "name": "Bình", "score": 7.2},
            {"id": 3, "name": "Chi", "score": 9.0}
            ]


def find_by_id(data: list[dict], id: int) -> dict:
    for item in data:
        if item["id"] == id:
            return item


def filter_by_score(data: list[dict], min_score: float) -> list[dict]:
    filtered_data = []
    for item in data:
        if item["score"] >= min_score:
            filtered_data.append(item)
    return filtered_data


def sort_by_score(data: list[dict], reverse=False) -> list[dict]:
    sorted_data = sorted(data, key=lambda x: x["score"], reverse=reverse)
    return sorted_data

def add_student(data: list[dict], student_dict: dict) -> list[dict]:
    found = find_by_id(data, student_dict["id"])
    if not found:
        data.append(student_dict)
    return data


def remove_student(data: list[dict], id: int) -> list[dict]:
    found = find_by_id(data, id)
    if found:
        data.remove(found)
    return data

def statistics(data: list[dict]) -> tuple:
   mean_score = sum(list(map(lambda x: x["score"], data))) / len(data)
   highest_score_student = max(data, key=lambda x: x["score"])
   lowest_score_student = min(data, key=lambda x: x["score"])
   return mean_score, highest_score_student, lowest_score_student


print(find_by_id(students, 5))

print(filter_by_score(students, 8.0))

print(sort_by_score(students))

new_student = {"id": 4, "name": "Dung", "score": 6.8}
print(add_student(students, new_student))

print(remove_student(students, 1))

print(statistics(students))
