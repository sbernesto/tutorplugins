from tutor import hooks

hooks.Filters.ENV_PATCHES.add_items([
    (
        "openedx-dockerfile-git-patches-default",
        """
# Fixing this `django-require` package to be from `openedx` org rather than `edx` org.
RUN git config url."https://github.com/openedx/django-require.git".insteadOf "https://github.com/edx/django-require.git"
"""
    ),
    (
        "openedx-dockerfile-post-python-requirements",
        """
# Make sure to install latest version of `openedx/django-require` for the platform to use. Uninstall existing version 1.0.12 first, then reinstall v2.0.0.
RUN pip uninstall -y django-require
RUN pip install -e git+https://github.com/openedx/django-require.git@v2.0.0#egg=openedx-django-require==2.0.0
"""
    )
])
