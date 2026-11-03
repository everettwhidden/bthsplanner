import reflex as rx

import bthsplanner.theme as theme
from bthsplanner.backend import PlannerState

required_courses_labels = ["Major Course", "Required Course"]

def detail_line(label: str, value) -> rx.Component:
    # bold label followed by a plain value, e.g. "Periods: 1"
    return rx.text(
        rx.text.span(f"{label}: ", weight="bold"),
        value,
        font_size="18px",
        color=theme.text,
    )


def course_detail_modal() -> rx.Component:
    course = PlannerState.active_modal_course
    return rx.dialog.root(
        rx.dialog.content(
            rx.box(
                rx.vstack(
                    # title + close button
                    rx.hstack(
                        rx.text(course["name"], font_size="25px", weight="bold", color=theme.text),
                        rx.spacer(),
                        rx.button(
                            "✕",
                            variant="ghost",
                            color_scheme="gray",
                            on_click=PlannerState.close_course_details,
                            style={"cursor": "pointer", "font_size": "16px"}
                        ),
                        width="100%",
                        align_items="center"
                    ),

                    # course info as plain text lines
                    rx.vstack(
                        detail_line("Periods", course["periods"].to(str)),
                        detail_line("Semesters", course["semesters"].to(str)),
                        detail_line("Credits", course["credits"].to(str)),
                        detail_line("Grades", course["grade_badges"].to(list[str]).join(", ")),
                        detail_line("Elective", rx.cond(course["is_elective"], "Yes", "No")),
                        align_items="start",
                        spacing="1",
                        margin_top="6px",
                        margin_bottom="12px",
                    ),

                    # full description
                    rx.text("Description", font_size = "18px", weight="bold", color=theme.text),
                    rx.text(
                        course["description"],
                        font_size="20px",
                        color=theme.text,
                        line_height="1.6",
                        margin_top="0px"
                    ),

                    align_items="start",
                    spacing="3",
                    width="100%"
                ),
                style={
                    "background_color": theme.lighter_aa_blue,
                    "border": f"1px solid {theme.border}",
                    "border_radius": "12px",
                    "padding": "24px",
                    "width": "100%",
                    "height": "100%"
                }
            ),
            style={
                "max_width": "900px",
                "width": "90vw",
                "height": "auto",
                "max_height": "900px",
                "background": "transparent",
                "padding": "0",
                "border": "none"
            }
        ),
        open=PlannerState.is_detail_open,
        on_open_change=lambda _: PlannerState.close_course_details(),
    )

def render_modal_course_row(course: dict, target_year: str) -> rx.Component:
    is_added = rx.cond(
        target_year == "Freshman",
        PlannerState.freshman_electives.contains(course["name"]),
        rx.cond(
            target_year == "Sophomore",
            PlannerState.sophomore_electives.contains(course["name"]),
            rx.cond(
                target_year == "Junior",
                PlannerState.junior_electives.contains(course["name"]),
                PlannerState.senior_electives.contains(course["name"])
            )
        )
    )
    
    return rx.box(
        rx.hstack(
            rx.box(
                rx.vstack(
                    rx.hstack(
                        rx.text(course["name"], font_weight="700", font_size="16px", color=rx.cond(course["disabled"], "#52525b", theme.text)), 
                        rx.badge(
                            rx.cond(
                                course['periods'] == 1,
                                f"{course['periods']} period",
                                f"{course['periods']} periods"
                            ),
                            color_scheme=rx.cond(course["disabled"], "gray", "orange"), 
                            variant="soft", 
                            radius="full"
                        ),
                        spacing="2"
                    ),
                    rx.text(course["description"], font_size="14px", color=rx.cond(course["disabled"], "#51515c", theme.text), max_lines=1, margin_top="2px"),
                    align_items="start",
                ),
                on_click=lambda: PlannerState.open_course_details(course["name"]),
                style={"cursor": rx.cond(course["disabled"], "not-allowed", "pointer")}, 
                width="100%"
            ),
            rx.spacer(),
            rx.cond(
                course["disabled"],
                rx.button("No room", color_scheme="gray", size="2", variant="soft", style={"cursor": "not-allowed", "opacity": "0.5", "pointer_events": "none"}),
                rx.cond(
                    is_added,
                    rx.button("Delete", on_click=lambda: PlannerState.delete_course(course["name"], target_year), color_scheme="red", variant="soft", size="1", style={"cursor": "pointer"}),
                    rx.button("Add", on_click=lambda: PlannerState.add_course(course["name"], target_year), color_scheme="blue", size="1", style={"cursor": "pointer"})
                )
            ),
            align_items="center", width="100%"
        ),
        border_bottom=f"1px solid {theme.border}", padding_y="10px", width="100%",
        opacity=rx.cond(course["disabled"], "0.5", "1.0")
    )

def course_search_modal(period_count: rx.Var, target_year: str) -> rx.Component:
    active_button = rx.dialog.trigger(
        rx.button(
            "Add Course",
            on_click=lambda: PlannerState.open_search_for_grade(target_year),
            width="100%", margin_top="0px",
            style={
                "background_color": "#2563eb1a", "color": "#60a5fa", 
                "font_weight": "600", "cursor": "pointer",
                "_hover": {"background_color": "#2563eb33"}
            }
        )
    )

    disabled_button = rx.button(
        "Schedule Full (10/10 Pds)",
        width="100%", margin_top="0px",
        style={
            "background_color": theme.illini_blue, "color": theme.text_dim, 
            "font_weight": "600", "cursor": "not-allowed",
            "opacity": "0.6",
            "font_size" : "14px"
        }
    )

    return rx.dialog.root(
        rx.cond(
            period_count >= 10,
            disabled_button,
            active_button
        ),
        rx.dialog.content(
            rx.hstack(rx.dialog.title("Add Course", margin="0"), rx.spacer(), rx.dialog.close(rx.button("✕", variant="ghost", color_scheme="gray", style={"cursor": "pointer"})), width="100%"),
            rx.input(placeholder="Search courses...", on_change=PlannerState.set_search_query, margin_y="16px", width="100%", size="3"),
            rx.scroll_area(
                rx.vstack(
                    rx.foreach(PlannerState.filtered_catalog, lambda course: render_modal_course_row(course, target_year)),
                    width="100%", align_items="stretch"
                ),
                style={"max_height": "400px"}
            ),
            style={"max_width": "750px", "background_color": theme.illini_blue, "border": f"1px solid {theme.border}", "padding": "20px"}
        )
    )