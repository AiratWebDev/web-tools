import tinify
from static.tiny_key import key

tinify.key = key


def compressor(file_name):
    source = tinify.from_file(f"downloads/unoptimized/{file_name}")
    source.to_file(f"downloads/optimized/{file_name}")
    return f"downloads/optimized/{file_name}"
