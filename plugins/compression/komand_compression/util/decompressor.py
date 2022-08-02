import os
import gzip
import bz2
import lzma
import lzma
from zipfile import ZipFile
import base64
import binascii
import io
from .algorithm import Algorithm


def dispatch_decompress(algorithm, file_bytes):

    if algorithm == Algorithm.GZIP:
        return gzip_decompress(file_bytes)

    elif algorithm == Algorithm.BZIP:
        return bzip_decompress(file_bytes)

    elif algorithm == Algorithm.LZ:
        return lz_decompress(file_bytes)

    elif algorithm == Algorithm.XZ:
        return xz_decompress(file_bytes)

    elif algorithm == Algorithm.ZIP:
        return zip_decompress(file_bytes)
    else:
        raise Exception("Dispatch Decompress: Invalid enum passed.")


def gzip_decompress(file_bytes):
    return gzip.decompress(file_bytes)


def bzip_decompress(file_bytes):
    return bz2.decompress(file_bytes)


def xz_decompress(file_bytes):
    return lzma.decompress(file_bytes)


def lz_decompress(file_bytes):
    return lzma.decompress(file_bytes, format=lzma.FORMAT_ALONE)


def zip_decompress(file_bytes):
    file_b64 = base64.b64encode(file_bytes)
    decode_data = binascii.a2b_base64(file_b64)  # read base64 into ascii array
    byte_array = bytes(decode_data)  # transform ascii to bytes

    zip_file = io.BytesIO(byte_array)  # transform byte array into a file like object

    zip_object = ZipFile(zip_file, "r")
    decompressed = {name: zip_object.read(name) for name in zip_object.namelist()}
    file_list = list(map(lambda file: {"filename": file[0], "content": file[1]}, decompressed.items()))
    files = {
        fil["filename"]: gzip_decompress(fil["content"])
        if ".gz" in fil["filename"]
        else fil["content"]
        for fil in file_list
        if os.path.basename(fil["filename"]) != ""
        and os.path.basename(fil["filename"])[0] != "."
    }

    return files if len(files) != 1 else files[list(files.keys())[0]]
