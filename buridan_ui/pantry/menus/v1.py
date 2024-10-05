import reflex as rx


class Content(rx.State):
    links: list[dict[str, str]] = [
        {"label": "Usage", "link": "#usage", "color": "hsl(160.1 84.1% 39.4%)"},
        {"label": "Position and placement", "link": "#position", "color": "gray"},
        {"label": "With other overlays", "link": "#overlays", "color": "gray"},
        {"label": "Manage focus", "link": "#focus", "color": "gray"},
        {"label": "Examples", "link": "#1", "color": "gray"},
        {"label": "Show on focus", "link": "#2", "color": "gray"},
        {"label": "Show on hover", "link": "#3", "color": "gray"},
        {"label": "With form", "link": "#4", "color": "gray"},
    ]

    index: int = 0
    position_y: str = "10px"

    async def toggle_table_content(self, index: int, item: dict[str, str]):
        self.links = [
            (
                {**data, "color": "gray"}
                if data["label"] != item["label"]
                else {**data, "color": "hsl(160.1 84.1% 39.4%)"}
            )
            for data in self.links
        ]
        self.position_y = f"{10 + (index * 30)}px"


def items(index: int, data: dict[str, str]):
    return rx.hstack(
        rx.link(
            rx.text(
                data["label"],
                font_size="12px",
                color=data["color"],
                weight="medium",
                on_click=Content.toggle_table_content(index, data),
            ),
            href=data["link"],
            text_decoration="none",
        ),
        border_left="1px solid hsl(0, 0%, 20%)",
        width="200px",
        height="30px",
        align="center",
        justify="start",
        padding_left="15px",
        _hover={"bg": "hsl(0, 0%, 25%)"},
        border_radius="0px 5px 5px 0px",
    )


def item_header():
    return rx.hstack(
        rx.icon(tag="puzzle", size=12),
        rx.text("Menu Items", font_size="11px", color_scheme="gray", weight="medium"),
        width="100%",
        justify="start",
        align="center",
        border_left="1px solid hsl(0, 0%, 20%)",
        border_radius="0px 5px 5px 0px",
        padding_left="15px",
        height="30px",
        bg="hsl(0 0% 16%)",
    )


def menus_v1():
    return rx.vstack(
        item_header(),
        rx.vstack(
            rx.box(
                width="10px",
                height="10px",
                border_radius="10px",
                border="1px solid hsl(160.1 84.1% 39.4%)",
                bg="hsl(0, 0%, 15%)",
                position="absolute",
                left="-4.5px",
                top=Content.position_y,
                transition="all 200ms ease-out",
            ),
            rx.foreach(
                Content.links,
                lambda data, index: items(index, data),
            ),
            spacing="0",
            position="relative",
        ),
        spacing="0",
    )
