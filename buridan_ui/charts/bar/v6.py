import reflex as rx
from ...wrappers.state import ComponentWrapperState

data = [
    {"month": "Jan", "desktop": 186},
    {"month": "Feb", "desktop": 340},
    {"month": "Mar", "desktop": 237, "active": True},
    {"month": "Apr", "desktop": 73},
    {"month": "May", "desktop": 209},
    {"month": "Jun", "desktop": 214},
]


def barchart_v6():
    modified_data = [
        {
            **item,
            "stroke": (
                rx.color("slate", 11)
                if item.get("active", False)
                else "none"  # No stroke when inactive
            ),
        }
        for item in data
    ]

    return rx.center(
        rx.vstack(
            rx.vstack(
                rx.heading("Bar Chart - Active", size="4", weight="bold"),
                rx.text("January - June 2024", size="1", color=rx.color("slate", 11)),
                spacing="1",
            ),
            rx.divider(height="1rem", opacity="0"),
            rx.recharts.bar_chart(
                rx.recharts.cartesian_grid(horizontal=True, vertical=False),
                rx.recharts.graphing_tooltip(
                    label_style={"fontWeight": "700"},
                    item_style={"padding": "0px"},
                    separator=":",
                ),
                rx.recharts.bar(
                    data_key="desktop",
                    fill=ComponentWrapperState.default_theme[0],
                    stack_id="a",
                    radius=6,
                    stroke="stroke",
                    stroke_width=2,
                ),
                rx.recharts.y_axis(type_="number", hide=True),
                rx.recharts.x_axis(data_key="month", type_="category", axis_line=False),
                data=modified_data,
                width="100%",
                height=250,
                bar_size=50,
                bar_gap="1px",
                bar_category_gap="1px",
                margin={"top": 25},
            ),
            rx.vstack(
                rx.heading("Trending up by 5.2% this month", size="2", weight="bold"),
                rx.text(
                    "Showing total visitors for the last 6 months",
                    size="1",
                    color=rx.color("slate", 11),
                ),
                spacing="1",
            ),
            width="100%",
        ),
        width="100%",
        padding="12px",
    )