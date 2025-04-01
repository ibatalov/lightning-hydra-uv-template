from contextlib import AbstractContextManager
import certifi
import ssl
import urllib
from functools import partial

class enforce_certificates(AbstractContextManager):
    """Context manager to enforce SSL certificates."""

    def __enter__(self) -> None:
        """Enter the context."""
        self.urlopen = urllib.request.urlopen
        urllib.request.urlopen = partial(urllib.request.urlopen,
                                         context=ssl.create_default_context(cafile=certifi.where()),
                                        )

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """Exit the context. Restore default functionality/"""
        urllib.request.urlopen = self.urlopen
        if exc_type is not None:
            return False
        return True