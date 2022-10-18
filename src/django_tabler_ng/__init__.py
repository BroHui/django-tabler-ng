
__all__ = [
    "__version__",
]

PACKAGE_NAME = "django_tabler_ng"

try:
    from importlib.metadata import metadata
except ImportError:
    from importlib_metadata import metadata

# package_metadata = metadata(PACKAGE_NAME)
# __version__ = package_metadata["Version"]