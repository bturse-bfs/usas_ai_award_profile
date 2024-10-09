import requests
from time import sleep
from zipfile import ZipFile
from io import BytesIO
import logging

logger = logging.getLogger(__name__)

# update award_id
award_id = "ASST_NON_1905CA5MAP_7530"


def initiate_award_profile_download(award_id: str) -> dict:
    """Initiates an award profile download on the USAspending server.

    params
        award_id: ID of an award summary on USAspending.

    return
        response from POST request to one of these endpoints:
        https://api.usaspending.gov/api/v2/download/assistance
        https://api.usaspending.gov/api/v2/download/contract
        https://api.usaspending.gov/api/v2/download/idv
        depending on award type indicated by first segment of award_id
    """
    award_id_type = award_id.split("_")[0]
    if award_id_type not in ("ASST", "CONT", "IDV"):
        raise ValueError("award_id must begin with 'ASST_' 'CONT_' or 'IDV_'")
    award_id_ep_type_map = {
        "ASST": "assistance",
        "CONT": "contract",
        "IDV": "idv",
    }
    url_base = "https://api.usaspending.gov/api/v2/download/"
    award_id_ep = f"{url_base}{award_id_ep_type_map.get(award_id_type)}/"
    r = requests.post(award_id_ep, json={"award_id": award_id})
    return r.json()


def wait_and_download_file(download_initiation_response: dict) -> None:
    """Wait for a download to complete on USAspending, then download the zip package.

    params:
        download_initiation_response: response from api/v2/download resource.
        Can be generated by initiate_award_profile_download

    returns None
    """
    status_url = download_initiation_response["status_url"]
    status_response = requests.get(status_url).json()
    logger.info(status_url)

    while status_response["status"] in ("ready", "running"):
        status_response = requests.get(status_url).json()
    sleep(30)

    if status_response["status"] == "finished":
        r = requests.get(status_response["file_url"])
        z = ZipFile(BytesIO(r.content))
        z.extractall(status_response["file_name"])


if __name__ == "__main__":
    wait_and_download_file(initiate_award_profile_download(award_id))
