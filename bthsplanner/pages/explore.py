import reflex as rx

import bthsplanner.theme as theme
from bthsplanner.backend import ExploreState, PlannerState
from bthsplanner.components import (
    navigation_layout,
    course_detail_modal,
    explore_sidebar
)
def meta_badge(content) -> rx.Component:
    # all card badges share one gray style
    return rx.badge(content, color_scheme="gray", variant="soft", radius="full")

@rx.page(route="/explore", title="BTHS Planner - Explore Courses", description="Explore all of the course offerings at Brooklyn Technical High School.", on_load=PlannerState.change_tab("Explore")) 
def explore_page() -> rx.Component:
    explore_main = rx.vstack(
        rx.heading("Explore Courses", font_size="30px", margin_bottom="8px", color=theme.text),
        rx.input(
            placeholder="Search titles, descriptions or keywords...",
            on_change=ExploreState.set_explore_search_query,
            value=ExploreState.explore_search_query,
            width="100%",
            max_width="800px",
            margin_top="12px",
            margin_bottom="10px",
            size="3",
            background_color=theme.lighter_aa_blue,
        ),

        rx.text(
            "Showing " + ExploreState.explore_catalog_count.to_string()
            + " of " + ExploreState.explore_total_count.to_string() + " courses",
            color=theme.text,
            size="3",
        ),

        
        # Fixed Grid layout setup to ensure single search results maintain standard sizing instead of stretching
        rx.box(
            rx.foreach(
                ExploreState.explore_catalog,
                lambda course: rx.box(
                    rx.vstack(
                        rx.text(course["name"], size="5", weight="bold", color=theme.text, ),
                        rx.hstack(
                            meta_badge(
                                rx.cond(course["semesters"] == 1, "1 semester", "2 semesters"),
                            ),
                            meta_badge(
                                rx.cond(
                                    course["periods"] == 1,
                                    f"{course['periods']} period",
                                    f"{course['periods']} periods",
                                ),
                            ),
                            meta_badge(f"{course['credits']} credits"),
                            rx.cond(
                                course["is_elective"],
                                meta_badge("Elective"),
                            ),
                            rx.foreach(
                                course["grade_badges"].to(list[str]),
                                lambda grade: meta_badge(grade),
                            ),
                            width="100%",
                            align_items="start",
                            spacing="1",
                            wrap="wrap",
                        ),
                        rx.cond(
                            course["summary"] != "",
                            rx.text(
                                course["summary"],
                                size="2",
                                color=theme.text,
                                # clamp to 2 lines so a long summary can't push the card taller
                                style={
                                    "display": "-webkit-box",
                                    "WebkitLineClamp": "2",
                                    "WebkitBoxOrient": "vertical",
                                    "overflow": "hidden",
                                },
                            ),
                        ),
                        align_items="start",
                        spacing="2",
                    ),
                    on_click=PlannerState.open_course_details(course["name"]),
                    class_name="explore-card",
                    border=f"1px solid {theme.border}",
                    border_radius="12px",
                    padding="24px",
                    padding_top = "15px",
                    height="130px",
                    width="100%",
                    overflow="hidden",
                )
            
            ),
            # Standardized layout settings for the responsive grid

            style={
                "display": "grid",
                "grid_template_columns": "repeat(auto-fill, minmax(400px, 1fr))",
                "gap": "24px",
            },
            width="100%",
        
        ),
        rx.text(
            "All course information and data is found through online sources or from personal knowledge. Please contact your guidance counselor if you are unsure about any course data. Additionally, AI was used to summarize each course and create it's description. Because AI can make mistakes, some descriptions may be incorrect or inaccurate. If you notice any mistakes, please contact us directly.",
            color=theme.text_dim,
            size="1",
            text_align="left",
            width="100%",
            max_width="600px",
            margin_x="0px",
            margin_top="16px",
        ),
        course_detail_modal(),
        
        align_items="start",
        width="100%"
    )
    explore_content = rx.hstack(
        explore_sidebar(),
        rx.box(
            explore_main,
            flex="1",
            min_width="0",
            padding_x="32px",
            padding_y="25px",
        ),
        align="start",
        spacing="0",
        width="100%",
        margin="0",
    )
    return navigation_layout(explore_content, full_width = True)

