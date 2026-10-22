import reflex as rx

# importing the pages package is what registers every @rx.page route
from bthsplanner.pages import hide_watermark_style

app = rx.App(
    stylesheets=["/style.css"],
    style=hide_watermark_style,
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.meta(property="og:image", content="https://bthsplanner.com/preview.png"),
        rx.el.meta(name="twitter:card", content="summary_large_image"),
        rx.el.meta(name="twitter:image", content="https://bthsplanner.com/preview.png"),
        rx.el.link(rel="icon", type="image/png", href="/favicon.ico"),
        rx.el.script(
            src="https://umami-production-07b7.up.railway.app/script.js",
            defer=True,
            custom_attrs={"data-website-id": "779aee42-e79c-4289-b881-65d70df59e21"},
        ),
    ],
)