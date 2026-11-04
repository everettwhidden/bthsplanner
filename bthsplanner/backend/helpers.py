import math

from data.courses import COURSE_CATALOG, alternate_list, alternates_with_gym, MAJORS


def next_lang_level(lang: str) -> str:
    if lang.endswith(" I"):
        return lang[:-1] + "II"
    return lang  # already at level II, nothing higher to bump to


def grade_badges(is_elective: bool, grades: list, available_grades: list) -> list[str]:
    if grades:
        return grades
    if available_grades:
        return available_grades
    if is_elective:
        return ["Junior", "Senior"]
    return []


def build_partner_map(pairs) -> dict[str, str]:
    m = {}
    for a, b in pairs:
        m[a] = b
        m[b] = a
    return m


def calculate_total_periods(courses: set[str]) -> int:
    full_year_periods = 0
    semester_1pd = 0
    semester_2pd = 0

    for c in courses:
        data = COURSE_CATALOG.get(c, {})
        pds = data.get("periods", 1)

        if data.get("semesters") == 1:
            if pds == 2:
                semester_2pd += 1
            else:
                semester_1pd += 1
        elif c in alternates_with_gym:
            full_year_periods += pds - 1
        elif pds == 2 and c in alternate_list:
            # double periods that alternate daily only cost one slot
            full_year_periods += 1
        else:
            full_year_periods += pds

    # two one-semester classes share a slot, so each pair costs one period
    # (or two periods for a pair of double-period classes)
    semester_room = math.ceil(semester_1pd / 2) + math.ceil(semester_2pd / 2) * 2
    return full_year_periods + semester_room


def majors_for_course(name: str) -> list[str]:
    # majors that list this course as a junior or senior requirement
    return [
        major for major, info in MAJORS.items()
        if name in info.get("Junior", []) or name in info.get("Senior", [])
    ]