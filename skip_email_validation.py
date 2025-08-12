from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    ("openedx-common-settings", "FEATURES['SKIP_EMAIL_VALIDATION'] = True",)
)
