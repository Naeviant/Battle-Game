from typing import Any, Callable, List, Union

from guizero import App, Box, PushButton


class Aligner():
    def __init__(self, parent: Union[App, Box], width: int) -> None:
        self.widget = Box(parent, width=width, height=1)


class Padding():
    def __init__(self,
                 parent: Union[App, Box],
                 height: int,
                 grid: List[Union[int, None]]=None) -> None:
        self.widget = Box(parent, width="fill", height=height, grid=grid)


class HoverablePushButton():
    DEFAULT_COLOUR = '#555555'
    HOVER_COLOUR = '#333333'
    TEXT_COLOUR = '#EEEEEE'

    def __init__(self,
                 parent: Union[App, Box],
                 width: Union[int, None]=None,
                 text: str = "",
                 command: Callable = None,
                 args: List[Any] = None,
                 grid: List[Union[int, None]]=None) -> None:
        self.widget = PushButton(parent,
                                 width=width,
                                 text=text,
                                 command=command,
                                 args=args,
                                 grid=grid)
        self.widget.bg = HoverablePushButton.DEFAULT_COLOUR
        self.widget.text_color = HoverablePushButton.TEXT_COLOUR
        self.widget.tk.bind("<Enter>", self.on_hover)
        self.widget.tk.bind("<Leave>", self.off_hover)

    def on_hover(self, _) -> None:
        """Actions which happen when the starts to hover over the button."""
        if self.widget.enabled:
            self.widget.bg = HoverablePushButton.HOVER_COLOUR

    def off_hover(self, _) -> None:
        """Actions which happen when the stops hovering over the button."""
        if self.widget.enabled:
            self.widget.bg = HoverablePushButton.DEFAULT_COLOUR

    def disable(self) -> None:
        """Disables the button widget."""
        self.widget.disable()
        self.widget.bg = HoverablePushButton.HOVER_COLOUR

    def enable(self) -> None:
        """Enables the button widget."""
        self.widget.enable()
        self.widget.bg = HoverablePushButton.DEFAULT_COLOUR
