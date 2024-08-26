from tutor import hooks

hooks.Filters.ENV_PATCHES.add_items([
    (
        "openedx-dockerfile-minimal",
        """
# Install vim
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt update && \
    apt install -y neovim
"""
    )
])
