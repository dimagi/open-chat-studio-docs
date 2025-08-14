from mkdocs.plugins import BasePlugin
from .openapi_to_docs import convert_openapi_to_markdown
import requests


class ApiDocsBuildPlugin(BasePlugin):
    def on_post_build(self, config):
        print("Running post-build script...")
        # Your custom post-build logic goes here
        # For example, you could run a shell command:
        # import subprocess
        # subprocess.run(["your_script.sh", "arg1"])
        print("Post-build script finished.")
