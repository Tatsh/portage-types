from typing import Any, Literal, Mapping, Sequence, TypedDict

__all__ = ('db', 'root')


class dbapi:
    def aux_get(self,
                mycpv: str,
                mylist: Sequence[Literal['DEFINED_PHASES', 'DEPEND', 'EAPI', 'HDEPEND', 'HOMEPAGE',
                                         'INHERITED', 'IUSE', 'KEYWORDS', 'LICENSE', 'PDEPEND',
                                         'PROPERTIES', 'PROVIDE', 'RDEPEND', 'REQUIRED_USE',
                                         'repository', 'RESTRICT', 'SRC_URI', 'SLOT']],
                mytree: str | None = ...,
                myrepo: str | None = ...) -> Sequence[str]:
        ...

    def xmatch(self, level: Literal['bestmatch-visible', 'match-all-cpv-only', 'match-all',
                                    'match-visible', 'minimum-all', 'minimum-visible',
                                    'minimum-all-ignore-profile'],
               origdep: str) -> Sequence[str] | str:
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

    def match(self, mydep: str, use_cache: Literal[0, 1] = ...) -> Sequence[str] | str:
        ...


class PortageTree:
    dbapi: dbapi


class DBRootDict(TypedDict):
    bintree: Any
    porttree: PortageTree
    virtuals: Any


db: Mapping[str, DBRootDict]
root: str
