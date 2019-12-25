from contextlib import contextmanager


@contextmanager
def atomic_write(file, mode="w", as_file=True, **kwargs):
    """Write a file atomically
    :param file: str or :class:`os.PathLike` target to write
    :param bool as_file:  if True, the yielded object is a :class:File.
        (eg, what you get with `open(...)`).  Otherwise, it will be the
        temporary file path string
    :param kwargs: anything else needed to open the file
    :raises: FileExistsError if target exists
    Example::
        with atomic_write("hello.txt") as f:
            f.write("world!")
    """
    raise NotImplementedError()
