# pylint: disable=too-few-public-methods,unused-argument
from collections.abc import Sequence
from typing import Any, Literal, Mapping, TypedDict, Union, Optional

__all__ = ('db', 'root', 'settings')


class dbapi:
    def aux_get(self,
                mycpv: str,
                mylist: list[Literal['DEFINED_PHASES', 'DEPEND', 'EAPI', 'HDEPEND', 'HOMEPAGE',
                                     'INHERITED', 'IUSE', 'KEYWORDS', 'LICENSE', 'PDEPEND',
                                     'PROPERTIES', 'PROVIDE', 'RDEPEND', 'REQUIRED_USE',
                                     'repository', 'RESTRICT', 'SRC_URI', 'SLOT']],
                mytree: str | None = ...,
                myrepo: str | None = ...) -> list[str]:
        ...

    def xmatch(self, level: Literal['bestmatch-visible', 'match-all-cpv-only', 'match-all',
                                    'match-visible', 'minimum-all', 'minimum-visible',
                                    'minimum-all-ignore-profile'],
                origdep: str) -> Union[Sequence[str], str]:
        ...

    def findname(self, mycpv: str, mytree: str | None = ..., myrepo: str | None = ...) -> str:
        ...

    def findname2(
            self,
            mycpv: str,
            mytree: str | None = ...,
            myrepo: str | None = ...
    ) -> tuple[None, Literal[0]] | tuple[str, str] | tuple[str, None]:
        ...

    def match(self, mydep: str, use_cache: Literal[0, 1] = 1) -> list[str] | str:
        ...


class PortageTree:
    dbapi: dbapi


class DBRootDict(TypedDict):
    bintree: Any
    porttree: PortageTree
    virtuals: Any


class config:
    def __init__(
        self,
        clone: Optional["config"] = None,
        mycpv: Optional[str] = None,
        config_profile_path: Optional[str] = None,
        config_incrementals: Optional[dict[str, str]] = None,
        config_root: Optional[str] = None,
        target_root: Optional[str] = None,
        sysroot: Optional[str] = None,
        eprefix: Optional[str] = None,
        local_config: bool = True,
        env: Optional[dict[str, str]] = None,
        _unmatched_removal: bool = False,
        repositories: Optional[list[str]] = None,
    ) -> None: ...
    def __getitem__(self, key: str) -> str: ...
    def __setitem__(self, key: str, value: str) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self) -> str: ...
    def get(self, k: str, x: Any = ...) -> Any: ...
    def __len__(self) -> int: ...


def doebuild(
    myebuild:str,
    mydo:Literal['info', 'nofetch', 'pretend', 'configure', 'compile', 'merge',
                 'test','install','prepare','clean','cleanrm','depend', 'digest',
                 'fetch','fetchall','help','manifest','qmerge','postinst','postrm',
                 'preinst','prepare','prerm','setup']= ...,
    settings: str | None = ...,
    debug:Literal[0, 1] = 0,
    listonly:Literal[0, 1] = 0,
    fetchonly:Literal[0, 1] = 0,
    cleanup:Literal[0, 1] = 0,
    use_cache:Literal[0, 1] = 1,
    fetchall:Literal[0, 1] = 0,
    tree:Literal['vartree','porttree','bintree'] = 'porttree',
    mydbapi:Optional[str] = None,
    vartree:Optional[str] = None,
    prev_mtimes:Optional[str] = None,
    fd_pipes:Optional[str] = None,
    returnpid:Optional[int] = False,
    returnproc:Optional[int] = False,
) -> Union[int, str, list[int]]: ...


db: Mapping[str, DBRootDict]
root: str
settings: config
