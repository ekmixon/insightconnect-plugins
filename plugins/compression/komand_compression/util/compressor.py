import io
import glob
from zipfile import ZipFile
import zipfile
import os
import tarfile
import lzma
import gzip
import bz2
from .algorithm import Algorithm


def dispatch_compress(algorithm, file_bytes, tmpdir=""):

    if algorithm == Algorithm.GZIP:
        return gzip_compress(file_bytes)

    elif algorithm == Algorithm.BZIP:
        return bzip_compress(file_bytes)

    elif algorithm == Algorithm.LZ:
        return lz_compress(file_bytes)

    elif algorithm == Algorithm.XZ:
        return xz_compress(file_bytes)

    elif algorithm == Algorithm.ZIP:
        return zip_compress(file_bytes, tmpdir)

    elif algorithm == Algorithm.TARBALL:
        return tarball_compress(file_bytes, tmpdir)

    else:
        raise Exception("Dispatch Compress: Invalid enum passed.")


def tarball_compress(file_bytes, tmpdir):
    with tarfile.open(f"{tmpdir}test.tar.gz", "w:gz") as tar:
        tar.add(tmpdir, recursive=True)
    fbytes = []
    with open(f"{tmpdir}test.tar.gz", "rb") as f:
        fbytes = f.read()
    os.remove(f"{tmpdir}test.tar.gz")
    return fbytes


def gzip_compress(file_bytes):
    return gzip.compress(file_bytes)


def bzip_compress(file_bytes):
    return bz2.compress(file_bytes)


def xz_compress(file_bytes):
    return lzma.compress(data=file_bytes)


def lz_compress(file_bytes):
    return lzma.compress(data=file_bytes, format=lzma.FORMAT_ALONE)


def zip_compress(file_bytes, tmpdir=""):
    if file_bytes is None:
        zipf = f"{tmpdir}compressed.zip"
        with zipfile.ZipFile(zipf, "w", zipfile.ZIP_DEFLATED) as zippy:
            for x in glob.glob(f"{tmpdir}*"):
                zippy.write(x, os.path.basename(x))
        with open(zipf, "rb") as f:
            fbytes = f.read()
        os.remove(zipf)
        return fbytes

    else:
        algorithm = zipfile.ZIP_DEFLATED  # sets compression type to deflated (standard for .zip)
        # zip archive created in temp
        zip_object = ZipFile("/tmp/compressed.zip", "w", algorithm)  # noqa: B108
        zip_object.writestr("compressed", file_bytes)  # TODO use magic to correctly name files in archive
        zip_object.close()
        with open("/tmp/compressed.zip", "rb") as in_file:
            compressed = in_file.read()
        # clean up
        os.remove("/tmp/compressed.zip")  # noqa: B108
        return compressed
