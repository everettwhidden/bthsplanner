import reflex as rx

import bthsplanner.theme as theme

from bthsplanner.backend import PlannerState

required_courses_labels = ["Major Course", "Required Course"]

def nav_link(label: str, href: str) -> rx.Component:
    # active tab comes from the current url, so there's nothing to flash
    is_active = PlannerState.router.page.path == href
    return rx.link(
        rx.box(
            rx.text(
                label,
                size="3",
                color="inherit",
                weight= "medium",
            ),
            color=rx.cond(is_active, theme.text, theme.text_dim),
            padding_x="10px",
            padding_y="8px",
            border_radius="6px",
            transition="background-color 0s ease, color 0s ease",
            _hover={"background_color": "rgba(128, 128, 128, 0.15)", "color": theme.text},
        ),
        href=href,
        text_decoration="none",
        border_bottom=rx.cond(is_active, "2px solid #3b82f6", "2px solid transparent"),
    )
def navigation_layout(content: rx.Component, full_width: bool = False, zero_gap: bool = False, show_border: bool = True) -> rx.Component:
    return rx.vstack(
        # Navigation Bar
        rx.box(
            rx.hstack(
                # Logo & Brand (wrapped with link to home)
                rx.link(
                    rx.hstack(
                        rx.image(
                            src="/header_logo.png",
                            width="40px",
                            height="40px",
                            object_fit="contain",
                            border_radius="4px",
                        ),
                        rx.text(
                            "BTHS Planner", size="6", weight="bold", color=theme.text,
                            transition="opacity 0s ease",
                            _hover={"opacity": "0.7"},
                        ),
                        spacing="3",
                        align_items="center",
                    ),
                    href="/",
                    style={
                        "text_decoration": "none",
                        "_hover": {"text_decoration": "none"},
                    },
                ),
                rx.spacer(),
                # Navigation Links
                rx.hstack(
                    nav_link("Plan", "/plan"),
                    nav_link("Explore", "/explore"),
                    nav_link("How It Works", "/how-it-works"),
                    #nav_link("Settings", "/settings"), temporarily removed
                    spacing="4",
                    margin_right="16px",
                ),
                # Action Buttons
                rx.hstack(
                    # Clickable Theme Toggle Icon Button
                    rx.icon_button(
                        rx.cond(
                            rx.color_mode == "light",
                            rx.icon("moon", size=20),
                            rx.icon("sun", size=20),
                        ),
                        on_click=rx.toggle_color_mode,
                        variant="ghost",
                        color_scheme="gray",
                        size="2",
                        style={
                            "cursor": "pointer",
                            "color": theme.text,
                            "background_color": "transparent",
                            "border": "none",
                            "box_shadow": "none",
                            "outline": "none",
                            "transition": "all 0s ease",
                            "_hover": {"background_color": "rgba(128, 128, 128, 0.25)"},
                        },
                    ),
                    rx.button(
                        "Export to Excel",
                        on_click=PlannerState.export_to_excel,
                        color_scheme="blue",
                        size="2",
                    ),
                    spacing="3",
                    align_items="center",
                ),
                align_items="center",
                width="100%",
            ),
            position="sticky",
            top="0",
            z_index="100",
            background_color=theme.lighter_aa_blue,
            border_bottom=f"1px solid {theme.border}" if show_border else "none",
            padding_x="16px",
            padding_y="8px",
            width="100%",
        ),
        # Page Content Container
        rx.box(
            content,
            padding_x="0px" if full_width else "32px",
            padding_y="0px" if full_width else "25px",
            width="100%",
            max_width="none" if full_width else "1400px",
            margin="0" if full_width else "0 auto",
        ),
        width="100%",
        min_height="100vh",
        background_color=theme.illini_blue,
        spacing="0",
    ),
    