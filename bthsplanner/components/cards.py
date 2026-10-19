import reflex as rx
import bthsplanner.theme as theme
from data.courses import alternates_with_gym, elective_color
from bthsplanner.backend import DropdownOptions, MAJOR_COURSE_COLOR, PlannerState

required_courses_labels = ["Major", "Required"]

def course_card(label: str, course_name: str) -> rx.Component:
    color = MAJOR_COURSE_COLOR if label in required_courses_labels else PlannerState.dropdown_colors[course_name]
    return rx.box(
        rx.box(
            rx.text(label, class_name="card-label", color = theme.text),
            rx.text(course_name, class_name="card-title"),
            class_name="course-card",
            style={
                "background_color": theme.lighter_aa_blue,
                "border": f"2px solid color-mix(in srgb, {color} 85%, {theme.border} 15%)"
            }
        ),
        on_click=PlannerState.open_course_details(course_name),
        style={"cursor": "pointer"}, class_name="card-spacing-wrapper",
    )
def elective_card(label: str, year: str) -> rx.Component:
    color = elective_color
    return rx.box(
        rx.box(
            rx.text("Elective", class_name="card-label", color = theme.text), 
            rx.text(label, class_name="card-title"),
            class_name="course-card", 
            on_click=PlannerState.open_course_details(label), 
            style={"cursor": "pointer", "background_color" : theme.lighter_aa_blue, "border": f"2px solid color-mix(in srgb, {color} 85%, {theme.border} 15%)"}, 
        ),
        rx.button(
            "✕", 
            on_click=[rx.stop_propagation, PlannerState.delete_course(label, year)],
            variant="ghost", 
            size="1", 
            color_scheme="red",
            style={
                "position": "absolute", "top": "50%", "transform": "translateY(-50%)", 
                "right": "20px", "font_size": "20px", "cursor": "pointer", 
                "padding": "4px", "height": "auto", "z_index": "10"
            }
            ),
        class_name="card-spacing-wrapper", 
        style={"position": "relative", "width": "100%"}
    )    
def dropdown_card(label: str, options: list[str], value: rx.Var, on_change: any) -> rx.Component:
    color = MAJOR_COURSE_COLOR if label in required_courses_labels else PlannerState.dropdown_colors[value]
    return rx.box(
        rx.box(
            rx.text(label, class_name="card-label", font_size="13px",color = theme.text),
            rx.select(options, value=value, on_change=on_change, variant="ghost", class_name="reflex-dropdown-select", on_click=[rx.stop_propagation], font_size = "15px" ),
            class_name="dropdown-card-wrapper",
            style={
                "background_color": theme.lighter_aa_blue,
                "border": f"2px solid color-mix(in srgb, {color} 85%, {theme.border} 15%)"
            }
        ),
        on_click=PlannerState.open_course_details(value),
        style={"cursor": "pointer"}, class_name="card-spacing-wrapper",
    )

def toggle_card(
    body: rx.Component,
    selected: rx.Var,
    on_toggle: any,
    disabled: rx.Var | bool = False,
    tooltip: str | None = None,
    margin_bottom: str = "0px",
) -> rx.Component:
    # wraps any card with a +/x button, fades when not selected
    wrapped = rx.box(
        body,
        rx.button(
            rx.cond(selected, "✕", "＋"),
            on_click=on_toggle,
            variant="ghost",
            size="1",
            color_scheme=rx.cond(selected, "red", "green"),
            disabled=disabled,
            style={
                "position": "absolute", "top": "40px", "transform": "translateY(-50%)",
                "right": "20px", "font_size": "20px", "cursor": "pointer",
                "padding": "4px", "height": "auto", "z_index": "10",
            },
        ),
        style={
            "position": "relative",
            "margin_bottom": margin_bottom,
            "width": "100%",
            "opacity": rx.cond(selected, "1.0", "0.4"),
        },
    )
    # tooltip is a normal python str, so a plain if works here
    if tooltip:
        return rx.tooltip(wrapped, content=tooltip)
    return wrapped


def toggle_dropdown_card(
    label: str,
    options: list[str],
    value: rx.Var,
    on_change: any,
    **toggle_args,
) -> rx.Component:
    return toggle_card(dropdown_card(label, options, value, on_change), **toggle_args)


def physics_toggle_args(course) -> dict:
    # course can be a str or a Var
    selected = PlannerState.selected_senior_physics.contains(course)
    only_one_left = PlannerState.selected_senior_physics.length() == 1
    return dict(
        selected=selected,
        on_toggle=PlannerState.toggle_senior_physics(course),
        disabled=only_one_left & selected,
        tooltip="You must keep at least one AP Physics",
    
    )


def senior_physics_cards() -> rx.Component:
    ap_ii = "AP Physics II"
    return rx.vstack(
        toggle_card(course_card("Major", ap_ii), **physics_toggle_args(ap_ii)),
        # always show the dropdown so they can pick mechanics or E&M
        toggle_dropdown_card(
            "Major",
            DropdownOptions.sn_phys_c_opts,
            PlannerState.sn_phys_c,
            PlannerState.change_sn_phys_c,
            **physics_toggle_args(PlannerState.sn_phys_c),
        ),
        course_card("Major", "Modern Physics"),
        width="100%", spacing="3", margin_top="0px",
    )

digital_e_alt_w_gym_majors = ["Electrical Engineering"]

def _has_partner_map(course: rx.Var[str]) -> rx.Var[bool]:
    is_gym_alt_major = rx.Var.create(digital_e_alt_w_gym_majors).contains(PlannerState.major)
    return PlannerState.partner_map.contains(course) & ~is_gym_alt_major

def render_major_course(course: rx.Var[str]) -> rx.Component:
    
    return rx.cond(
        _has_partner_map(course),
        rx.tooltip(
            course_card("Major", course),
            content=f"Double period, alternates daily with {PlannerState.partner_map[course]}",
        ),
        rx.cond(
            rx.Var.create(alternates_with_gym).contains(course),
            rx.tooltip(
                course_card("Major", course),
                content = "Double period, alternates daily with Phys Ed"
            ),
        
        course_card("Major", course),
        ),
    )
