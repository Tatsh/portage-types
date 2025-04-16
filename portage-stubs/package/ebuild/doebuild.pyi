from typing import Literal


def doebuild(
    myebuild: str,
    mydo: Literal['clean', 'cleanrm', 'compile', 'configure', 'depend', 'digest', 'fetch',
                  'fetchall', 'help', 'info', 'install', 'manifest', 'merge', 'nofetch', 'postinst',
                  'postrm', 'preinst', 'prepare', 'prerm', 'pretend', 'qmerge', 'setup', 'test',
                  'unpack'],
    settings: str | None = ...,
    debug: Literal[0, 1] = ...,
    listonly: Literal[0, 1] = ...,
    fetchonly: Literal[0, 1] = ...,
    cleanup: Literal[0, 1] = ...,
    use_cache: Literal[0, 1] = ...,
    fetchall: Literal[0, 1] = ...,
    tree: Literal['vartree', 'porttree', 'bintree'] = ...,
    mydbapi: str | None = ...,
    vartree: str | None = ...,
    prev_mtimes: str | None = ...,
    fd_pipes: str | None = ...,
    returnpid: int | bool = ...,
    returnproc: int | bool = ...,
) -> int | str | list[int]:
    ...
