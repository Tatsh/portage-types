# pylint: disable=too-few-public-methods,unused-argument
from typing import Any, Literal, Mapping, TypedDict
from collections.abc import Sequence

__all__ = ('db', 'root')


class dbapi:
    def aux_get(self,
                mycpv: str,
                mylist: list[Literal['DEFINED_PHASES', 'DEPEND', 'EAPI', 'HDEPEND', 'HOMEPAGE',
                                     'INHERITED', 'IUSE', 'KEYWORDS', 'LICENSE', 'PDEPEND',
                                     'PROPERTIES', 'PROVIDE', 'RDEPEND', 'REQUIRED_USE',
                                     'repository', 'RESTRICT', 'SRC_URI', 'SLOT']],
                mytree: str | None = None,
                myrepo: str | None = None) -> list[str]:
        ...

    def xmatch(self,
                level: Literal['bestmatch-visible', 'match-all-cpv-only', 'match-all',
                               'match-visible', 'minimum-all', 'minimum-visible',
                               'minimum-all-ignore-profile'], origdep: str,
                mydep: type[DeprecationWarning] = ...,
                mykey: type[DeprecationWarning] = ...,
                mylist: type[DeprecationWarning] = ...) -> Sequence[str] | str:
        ...

    def findname(self, mycpv: str, mytree: str | None = None, myrepo: str | None = None) -> str:
        ...

    def findname2(
            self,
            mycpv: str,
            mytree: str | None = None,
            myrepo: str | None = None
    ) -> tuple[None, int] | tuple[str, str] | tuple[str, None]:
        ...

    def match(self, mydep: str, use_cache: int = 1) -> Sequence[str] | str: ...


class PortageTree:
    dbapi: dbapi


class DBRootDict(TypedDict):
    bintree: Any
    porttree: PortageTree
    virtuals: Any


def doebuild(myebuild, mydo, _unused=...,
        settings: Incomplete | None = None,
        debug: int = 0,
        listonly: int = 0,
        fetchonly: int = 0,
        cleanup: int = 0,
        use_cache: int = 1,
        fetchall: int = 0,
        tree: Incomplete | None = None,
        mydbapi: Incomplete | None = None,
        vartree: Incomplete | None = None,
        prev_mtimes: Incomplete | None = None,
        fd_pipes: Incomplete | None = None,
        returnpid: bool = False,
        returnproc: bool = False) -> int | portage.process.MultiprocessingProcess | list[int]:
    ...


db: Mapping[str, DBRootDict]
root: str
