import logging
import pathlib

from mkdocs.config import Config, config_options
from mkdocs.plugins import BasePlugin
from .openapi_to_docs import convert_openapi_to_markdown
import requests

from mkdocs.plugins import get_plugin_logger

log = get_plugin_logger(__name__)


class ApiDocsBuildPluginConfig(Config):
    openapi_schema_url = config_options.Type(str)
    output_schema_path = config_options.Type(str, default="schema.yml")
    output_dir = config_options.Type(str, default="api")


class ApiDocsBuildPlugin(BasePlugin[ApiDocsBuildPluginConfig]):
    """Plugin for converting the OpenAPI schema in a simplified set of documentation for LLMs"""

    def on_post_build(self, config):
        try:
            response = requests.get(self.config.openapi_schema_url)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
            api_content = response.content
        except requests.exceptions.RequestException as e:
            logging.error(e)
            return

        output = pathlib.Path(self.config.output_schema_path)
        existing_content = None
        if output.exists():
            existing_content = output.read_bytes()

        if api_content != existing_content:
            output.write_bytes(api_content)
            log.info("API Schema downloaded to %s", output)
            api_docs_dir = pathlib.Path(config.docs_dir) / self.config.output_dir
            convert_openapi_to_markdown(output, api_docs_dir)
        else:
            log.info("API Schema unchanged - ignoring")
