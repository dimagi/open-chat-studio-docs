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


def set_participant_data_key(key_name: str, data: any) -> None:
    """
    Updates the current [participant's data](../participant_data.md){:target="_blank"} with the provided value at the specified key.
    """

def append_to_participant_data_key(key_name: str, data: any) -> None:
    """
    Appends the provided value to the [participant's data](../participant_data.md){:target="_blank"} at the specified key.
    If the value at the key is not a list, it will be converted to a list containing the provided value.
    """

def get_participant_schedules() -> list:
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


def get_session_state_key(key_name: str) -> str | None:
    """
    Returns the value of the session state key with the given name.
    If the key does not exist, it returns `None`.

    See also: [Session State](./#session-state)
    """


def set_session_state_key(key_name: str, data: Any) -> None:
    """
    Sets the value of the session state key with the given name to the provided data.
    This will override any existing data for the key.

    See also: [Session State](./#session-state)
    """


def get_selected_route(router_node_name: str) -> str | None:
    """
    Returns the route selected by a specific router node with the given name.
    If the node does not exist or has no route defined, it returns `None`.
    """


def get_node_path(node_name: str) -> list | None:
    """
    Returns a list containing the sequence of nodes leading to the target node.
    If the node is not found in the pipeline path, returns a list containing
    only the specified node name.
    """


def get_all_routes() -> dict:
    """
    Returns a dictionary containing all routing decisions in the pipeline.
    The keys are the node names and the values are the routes chosen by each node.
    """


def add_message_tag(tag_name: str):
    """Adds a tag to the output message. To add multiple tags, call this function multiple times."""


def add_session_tag(tag_name: str):
    """Adds a tag to the chat session. To add multiple tags, call this function multiple times."""


def get_node_output(node_name: str) -> Any:
    """Returns the output of the specified node if it has been executed.
    If the node has not been executed, it returns `None`.
    """


def abort_with_message(message, tag_name: str = None) -> None:
    """Calling this will terminate the pipeline execution. No further nodes will get executed in
    any branch of the pipeline graph.

    The message provided will be used to notify the user about the reason for the termination.
    If a tag name is provided, it will be used to tag the output message.

    ```python
    # Abort pipeline with custom message
    if safety_violation_detected:
        abort_with_message("Content policy violation detected")
    ```
    """


def require_node_outputs(*node_names):
    """This function is used to ensure that the specified nodes have been executed and their outputs
    are available in the pipeline's state. If any of the specified nodes have not been executed,
    the node will not execute and the pipeline will wait for the required nodes to complete.

    This should be called at the start of the main function.

    ```python
    def main(input, **kwargs):
        require_node_outputs("nodeA", "nodeB")
        return get_node_output("nodeA") + get_node_output("nodeB")
    ```
    """
