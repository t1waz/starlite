from mypyc.build import mypycify


def build(setup_kwargs):
    extensions = [
        "starlite",
    ]
    cmd_args = ["--ignore-missing-imports", "--config-file", "mypy.ini"]
    extensions.extend(cmd_args)
    setup_kwargs.update({"ext_modules": mypycify(extensions, verbose=True)})
