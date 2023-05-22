from __future__ import annotations

import sys
import logging
from typing import Literal

from pathlib import Path
import shutil

from urllib.parse import urlparse
import requests

from easyfatt_db_connector.constants import DEFAULT_FIREBIRD_LOCATION

RELEASE_URL = "https://api.github.com/repos/FirebirdSQL/firebird/releases"
PROCESSOR_ARCHITECTURE = 32 << bool(sys.maxsize >> 32)

logger = logging.getLogger(__name__)

__all__ = ["get_available_releases", "download"]

def get_available_releases() -> list[str]:
    """ Retrieves the available releases from the FirebirdSQL repository.

    Returns:
        releases (list[str]): List of available release tags.
    """
    response = requests.get(RELEASE_URL)

    return [
        release["tag_name"]
        for release in response.json()
        if list(
            filter(
                lambda a: "_x64_embed.zip" in a["name"]
                or "_Win32_embed.zip" in a["name"],
                release["assets"],
            )
        )
    ]


def download(
    tag_name: Literal["R2_5_8", "R2_5_9"] | None = None,
    firebird_path: Path = DEFAULT_FIREBIRD_LOCATION,
    architecture: Literal[32, 64] | None = None,
) -> Path:
    """Downloads a local copy for the Firebird Embedded DB.

    Args:
        tag_name ('R2_5_8' | 'R2_5_9', optional): The tag name of the release (see https://github.com/FirebirdSQL/firebird/releases).
        firebird_path (Path, optional): Path where the firebird database will be installed. Defaults to `~/.cache/firebird-embedded/`.
        architecture (Literal[32, 64] | None, optional): Desired processor architecture (32 or 64 bit, None for automatic discovery). Defaults to None.

    Raises:
        Exception: No available releases were found
        Exception: Release '{tag_name}' not found. Available releases are {available_releases}.
        Exception: Unexpected number of downloads found: {download_no}. Expected 1.

    Returns:
        firebird (Path): Path to the Firebase Embedded folder
    """
    available_releases = get_available_releases()

    desired_architecture = (
        architecture if architecture is not None else PROCESSOR_ARCHITECTURE
    )

    if len(available_releases) == 0:
        raise Exception("No available releases were found")
    elif tag_name is not None and tag_name not in available_releases:
        raise Exception(f"Release '{tag_name}' not found. Available releases are {', '.join(available_releases)}.")

    release_name = tag_name if tag_name is not None else available_releases[0]
    release = requests.get(
        f"https://api.github.com/repos/FirebirdSQL/firebird/releases/tags/{release_name}"
    ).json()
    assets = release["assets"]

    # Retrieve the download url for the desired architecture
    remote_package_urls = [
        asset["browser_download_url"]
        for asset in assets
        if ("_x64_embed.zip" if desired_architecture == 64 else "_Win32_embed.zip")
        in asset["name"]
    ]

    if len(remote_package_urls) != 1:
        raise Exception(
            f"Unexpected number of downloads found: {', '.join(remote_package_urls)}. Expected 1."
        )

    zip_file_path: Path = (
        firebird_path / str(urlparse(remote_package_urls[0]).path).split("/")[-1]
    )
    version_file = firebird_path / "version.txt"

    try:
        firebird_path.mkdir(parents=True)
    except FileExistsError:
        # Check if version is the same
        if version_file.exists() and version_file.read_text() == zip_file_path.stem:
            return firebird_path

        # Remove all old files
        for child in firebird_path.glob("*"):
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()

    # Download the archive and extract it
    response = requests.get(remote_package_urls[0], allow_redirects=True)
    with open(zip_file_path, "wb") as zip_file:
        zip_file.write(response.content)

    shutil.unpack_archive(zip_file_path, firebird_path)
    zip_file_path.unlink()

    # Write the version file
    version_file.write_text(zip_file_path.stem)

    return firebird_path


if __name__ == "__main__":
    print(download())
    # print(download("R2_5_8"))
    # print(download("R2_5_9", architecture=32))
