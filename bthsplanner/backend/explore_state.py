import reflex as rx

from .explore_helpers import filter_explore_catalog


def _toggle(items: list[str], item: str):
    if item in items:
        items.remove(item)
    else:
        items.append(item)


class ExploreState(rx.State):
    explore_search_query: str = ""
    order: str = "A-Z"
    selected_grades: list[str] = []
    selected_majors: list[str] = []
    selected_filters: list[str] = []
    selected_period_length: list[str] = []
    selected_semesters: list[str] = []

    def clear_filters(self):
        self.order = "A-Z"
        self.selected_grades = []
        self.selected_majors = []
        self.selected_filters = []
        self.selected_period_length = []
        self.selected_semesters = []

    def set_explore_search_query(self, val: str):
        self.explore_search_query = val

    def set_order(self, val: str):
        self.order = val

    def toggle_grade(self, grade: str):
        _toggle(self.selected_grades, grade)

    def toggle_filter(self, filter_name: str):
        _toggle(self.selected_filters, filter_name)

    def toggle_major(self, major: str):
        _toggle(self.selected_majors, major)

    def toggle_period_length(self, period_length: str):
        _toggle(self.selected_period_length, period_length)

    def toggle_semester(self, semester: str):
        _toggle(self.selected_semesters, semester)

    @rx.var
    def explore_catalog(self) -> list[dict]:
        return filter_explore_catalog(
            query=self.explore_search_query,
            order=self.order,
            grades=self.selected_grades,
            majors=self.selected_majors,
            filters=self.selected_filters,
            period_lengths=self.selected_period_length,
            semesters=self.selected_semesters,
        )

    @rx.var
    def explore_catalog_count(self) -> int:
        return len(self.explore_catalog)

    @rx.var
    def explore_total_count(self) -> int:
        # total with no filters applied
        return len(filter_explore_catalog(
            query="",
            order="A-Z",
            grades=[],
            majors=[],
            filters=[],
            period_lengths=[],
            semesters=[],
        ))