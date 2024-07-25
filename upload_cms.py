##Plugins no sirve
from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    (
        "caddyfile-cms",
        """
handle_path /import/* {
    request_body {
        max_size 500MB
    }
}
"""
    )
)
