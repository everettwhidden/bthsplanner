import reflex as rx

from bthsplanner.theme import lighter_aa_blue, gradient, text, border
from bthsplanner.backend import PlannerState
from bthsplanner.components import (
    navigation_layout,
)



@rx.page(route="/", title="BTHS Planner", description="Brooklyn Tech's Course Planner", on_load=PlannerState.change_tab("Home"))
def home_page() -> rx.Component:
    home_page_content = rx.box(
        # --- HERO SECTION ---
        rx.box(
            # text takes whatever width the image leaves, so it wraps instead of overlapping
            rx.vstack(
                rx.heading(
                    "Planning at scale for the nation's largest high school",
                    font_size="45px",
                    color="white",
                    weight="bold",
                    line_height="1.1",
                    text_wrap="balance",
                ),
                align_items="start",
                flex="1",
                min_width="0",
                padding_left="3rem",
                padding_bottom="3rem",
            ),
            rx.image(
                src="building.png",
                height="120%",          # same size the old scale(1.2) gave
                width="auto",
                max_width="55%",        # image never takes more than 55% so the text always has room
                flex_shrink="0",
                object_fit="contain",
                object_position="bottom right",
            ),
            display="flex",
            align_items="flex-end",     # both sit at the bottom
            justify_content="space-between",
            background=rx.color_mode_cond(
                f"linear-gradient(180deg in oklch, {lighter_aa_blue} 0%, {gradient} 70%, {gradient} 100%)",
                f"linear-gradient(180deg in oklch, {lighter_aa_blue} 0%, {gradient} 70%, {gradient} 100%)",
            ),
            width="100vw",
            height="calc(100vh - 55px)",
            position="relative",
            overflow="hidden",
        ),

        # --- ABOUT SECTION ---
        rx.box(
            rx.container(
                rx.vstack(
                    rx.heading("About", font_size = "40px", margin_bottom="1rem",),
                    rx.text(
                        "BTHS Planner is built specifically for Brooklyn Technical High School students to map out their high school career. Whether you are navigating your major courses, electives, AP requirements, this platform makes planning seamless and intuitive."
                        ,
                        font_size = "20px",
                        line_height="1.7",
                        margin_bottom="1rem",
                        text_align="center"
                    ),
                    rx.text(
                        "BTHS Planner is currently in Beta, which means it is still developing, may contain bugs, and is provided 'as is' without warranties of any kind.", 
                        font_size = "20px",         
                        line_height="1.7",
                        margin_bottom="1rem",
                        text_align="center"),
                    rx.divider(border_color= border),
                    rx.spacer(),
                    rx.heading("Contact", font_size = "15px", margin_bottom = "5px",),
                    rx.link(
                        rx.button(
                            "Feedback",
                            color=text,
                            border=f"2px solid {text}",
                            border_radius="9999px",
                            background="transparent",
                            height="36px",
                            padding_x="20px",
                            font_size="14px",
                            font_weight="medium",
                            transition="all 0.2s ease",
                            _hover={
                                "color": gradient,
                                "border_color": gradient,
                                "background": "transparent",
                            },
                        ),
                        href="https://docs.google.com/forms/d/e/1FAIpQLSebmbV4Ce9doWAPPl86DheyuMYkaYKGf_dxDp0k2z1sfz0BSQ/viewform?usp=header",
                        is_external=True,
                        text_decoration="none",
                    ),
                    rx.link(
                        rx.hstack(
                            
                            rx.text(
                                "Everett Whidden", 
                                color="inherit", 
                                weight="medium", 
                                font_size="14px"
                            ),
                            # Standalone LinkedIn Logo (No background tile, color customizable via 'fill')
                            rx.html(
                                f"""
                                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="currentColor" style="display: block;">
                                    <path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z"/>
                                </svg>
                                """
                            ),
                            spacing="2",
                            align="center",
                        ),
                        href="https://www.linkedin.com/in/everettwhidden",
                        is_external=True,
                        color = text,
                        text_decoration="none",                   
                        transition="color 0.1s ease",
                        _hover={"color": gradient},
                    ),
                    spacing="5",
                    align="center",
                    align_items="center",
                    max_width="800px",
                    margin_x="auto"
                ),
                padding_y="6rem",
            ),
            width="100%",
        ),
        width="100%",
        overflow_x="hidden",
    )
    return navigation_layout(home_page_content, full_width = True, show_border = False)