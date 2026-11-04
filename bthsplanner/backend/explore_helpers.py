from data.courses import COURSE_CATALOG, MAJORS, AP_COURSES, SUMMARIES

from .helpers import grade_badges, majors_for_course


def filter_explore_catalog(
    query: str,
    order: str,
    grades: list[str],
    majors: list[str],
    filters: list[str],
    period_lengths: list[str],
    semesters: list[str],
) -> list[dict]:
    query = query.lower().strip()
    results = []

    GRADE_RANK = {"Freshman": 0, "Sophomore": 1, "Junior": 2, "Senior": 3}

    for name, data in COURSE_CATALOG.items():
        if query not in name.lower() and query not in data.get("description", "").lower():
            continue

        badges = grade_badges(
            data.get("is_elective", False),
            data.get("grades", []),
            data.get("available_grades", []),
        )

        if filters:
            
            if "Elective" in filters and "Non-elective" in filters:
                pass    
            elif "Non-elective" in filters and data.get("is_elective"):
                continue
            elif "Elective" in filters and not data.get("is_elective"):
                continue

            if "AP" in filters and name not in AP_COURSES:
                continue

        if grades and not any(g in badges for g in grades):
            continue

        if majors:
            course_majors = majors_for_course(name)
            if not any(m in course_majors for m in majors):
                continue

        if period_lengths:
            periods = data.get("periods", 1)
            label = "1 period" if periods == 1 else f"{periods} periods"
            if label not in period_lengths:
                continue

        if semesters:
            sems = data.get("semesters", 2)
            label = "1 semester" if sems == 1 else f"{sems} semesters"
            if label not in semesters:
                continue

        results.append({
            "name": name,
            "summary": SUMMARIES.get(name, ""),
            "description": data.get("description", ""),
            "periods": data.get("periods", 1),
            "semesters": data.get("semesters", 2),
            "credits": f"{float(data.get('credits', 1.0)):.1f}",
            "is_elective": data.get("is_elective", False),
            "disabled": False,
            "grade_badges": badges,
        })

    if order == "A-Z":
        results.sort(key=lambda c: c["name"].lower())
    elif order == "Z-A":
        results.sort(key=lambda c: c["name"].lower(), reverse=True)
    elif order == "Grade level":
        results.sort(key=lambda c: (min((GRADE_RANK[g] for g in c["grade_badges"]), default=99), c["name"].lower() ))
    
    return results