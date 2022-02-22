from cookiecutter.main import cookiecutter

from datetime import datetime

cookiecutter(
    "nzoth/template/",
    no_input=True,
    extra_context={
        "app_name": "gods-unchained-card-analyzer",
        "app_version": "0.1.0",
        "app_description": "Classify Gods Unchained cards strategy.",
        "dependencies": {
            "pandas": "1.3.3",
            "scikit-learn": "0.24.2"
        }
    },
    overwrite_if_exists=True
)
