from cookiecutter.main import cookiecutter

class Template:

    @staticmethod
    def render(project_params: dict) -> None:
        cookiecutter(
            "https://github.com/ericvenarusso/nzoth-template.git",
            no_input=True,
            extra_context=project_params,
            overwrite_if_exists=True
        )