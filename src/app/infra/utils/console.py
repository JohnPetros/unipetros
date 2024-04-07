from typing import Any
from inspect import currentframe
from cowsay import func


class Console:
    def log(self, data: Any) -> None:
        current_frame = currentframe()
        caller_frame = current_frame.f_back
        filename = caller_frame.f_code.co_filename
        line = caller_frame.f_lineno

        func(f"FILE: {filename}\nLINE: {line}\nLOG: {data}")
