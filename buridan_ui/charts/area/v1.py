import reflex as rx

from ..style import info, tooltip_styles


def areachart_v1():

    data = [
        {"month": "Jan", "desktop": 186},
        {"month": "Feb", "desktop": 305},
        {"month": "Mar", "desktop": 237},
        {"month": "Apr", "desktop": 73},
        {"month": "May", "desktop": 209},
        {"month": "Jun", "desktop": 214},
    ]

    return rx.box(
        rx.vstack(
            info(
                "Area Chart",
                "3",
                "Showing total visitors for the last 6 months",
                "start",
            ),
            rx.recharts.area_chart(
                rx.recharts.graphing_tooltip(**vars(tooltip_styles)),
                rx.recharts.cartesian_grid(
                    horizontal=True, vertical=False, class_name="opacity-25"
                ),
                rx.recharts.area(
                    data_key="desktop",
                    fill=rx.color("accent"),
                    stroke=rx.color("accent", 8),
                ),
                rx.recharts.x_axis(
                    data_key="month",
                    axis_line=False,
                    tick_size=10,
                    tick_line=False,
                    custom_attrs={"fontSize": "12px"},
                    interval="preserveStartEnd",
                ),
                data=data,
                width="100%",
                height=250,
            ),
            info(
                "Trending up by 5.2% this month",
                "2",
                "January - June 2024",
                "start",
            ),
            width="100%",
            class_name=tooltip_styles.general_style,
        ),
        width="100%",
        padding="0.5em",
    )
