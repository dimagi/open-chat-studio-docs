"""
Python Node docs
"""
from typing import Any


def get_participant_data() -> dict:
    """
    Returns the current [participant's data](../participant_data.md){:target="_blank"} as a dictionary.
    """


def set_participant_data(data: dict) -> None:
    """
    Updates the current [participant's data](../participant_data.md){:target="_blank"} with the provided dictionary.
    This will overwrite any existing data.
    """

def get_participant_schedules(self) -> list:
    """
    Returns all active scheduled messages for the participant in the current experiment session.
    """


def get_temp_state_key(key_name: str) -> str | None:
    """
    Returns the value of the temporary state key with the given name.
    If the key does not exist, it returns `None`.

    See also: [Temporary State](./#temporary-state)
    """


def set_temp_state_key(key_name: str, data: Any) -> None:
    """
    Sets the value of the temporary state key with the given name to the provided data.
    This will override any existing data for the key.

    See also: [Temporary State](./#temporary-state)
    """
