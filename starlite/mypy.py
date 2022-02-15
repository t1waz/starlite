from typing import Callable, Optional, Union

from mypy.nodes import SymbolTableNode
from mypy.types import FunctionLike, Type
from typing_extensions import Type as TypingType

from starlite import MissingDependencyException

try:
    from mypy.plugin import (
        ClassDefContext,
        DynamicClassDefContext,
        FunctionContext,
        FunctionSigContext,
        MethodContext,
        Plugin,
    )
except ImportError as exc:
    raise MissingDependencyException("mypy is not installed") from exc


def plugin(version: str) -> TypingType[Plugin]:
    """
    this is the entry point for mypy
    """
    return StarliteMyPyPlugin


class StarliteMyPyPlugin(Plugin):
    def get_dynamic_class_hook(self, fullname: str) -> Optional[Callable[[DynamicClassDefContext], None]]:
        if "dto_test" in fullname:
            return _dynamic_class_hook
        return None

    def get_function_hook(self, fullname: str) -> Optional[Callable[[FunctionContext], Type]]:
        if "dto_test" in fullname:
            return _dynamic_class_hook
        return None

    def get_function_signature_hook(self, fullname: str) -> Optional[Callable[[FunctionSigContext], FunctionLike]]:
        if "dto_test" in fullname:
            return _dynamic_class_hook
        return None

    # def get_function_signature_hook(self, fullname: str):
    #     if fullname == "starlite.dto.DTO":
    #         return _dynamic_class_hook
    #     return None
    #
    # def get_method_signature_hook(self, fullname: str):
    #     if fullname == "starlite.dto.DTO":
    #         return _dynamic_class_hook
    #     return None


def _dynamic_class_hook(ctx: Union[FunctionContext, MethodContext]) -> Type:
    """ """

    global_modules = ctx.api.modules[ctx.api.cur_mod_id].names
    if "starlite" not in global_modules:
        lookup_sym: SymbolTableNode = ctx.api.modules["starlite.dto.DTO"].names["Mapped"]
        global_modules["starlite"] = lookup_sym
