from contextlib import contextmanager
import os
import tempfile


@contextmanager
def atomic_write(file, mode="w", as_file=True, **kwargs):
    """Write a file atomically

    :param file: str or :class:`os.PathLike` target to write
    :param bool as_file:  if True, the yielded object is a :class:File.
        (eg, what you get with `open(...)`).  Otherwise, it will be the
        temporary file path string
    :param kwargs: anything else needed to open the file
    :raises: FileExistsError if target exists
    :return: yields temp file if as_file flag is True, else yields path to temp file

    Example::
        with atomic_write("hello.txt") as f:
            f.write("world!")
    """
    # if file already exists, raise an error
    if os.path.exists(file):
        raise FileExistsError(f"The file {file} already exists.")

    # retrieve file extension from path; used to ensure temp file has same extension as file
    file_extension = os.path.splitext(file)[-1]

    hasFailed = False  # flag used to verify if failure occurred

    # generate temporary file with random filename in the same directory
    # this ensures temp file resides on the same filesystem
    with tempfile.NamedTemporaryFile(
        mode=mode,
        suffix=file_extension,
        dir=os.path.dirname(file),
        delete=False,
        **kwargs,
    ) as tf:
        try:
            # if as_file flag is True, yield the temporary file
            if as_file:
                yield tf
            else:  # otherwise return the temporary file path string
                yield tf.name
        except:
            # intercept any error, set failure flag to True, and re-throw error
            hasFailed = True
            raise
        finally:
            # if failure occurred, then remove potentially incomplete file
            if hasFailed:
                # remove incomplete file
                if os.path.exists(file):
                    os.remove(file)
            else:
                # otherwise rename temp file to target destination name
                os.rename(tf.name, file)

            # remove temporary file
            if os.path.exists(tf.name):
                os.remove(tf.name)
