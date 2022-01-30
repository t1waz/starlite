import os

try:
    from mypyc.build import mypycify
except ImportError:
    def build(setup_kwargs):
        pass
else:
    def build(setup_kwargs):
        extensions = ["starlite/asgi.py"]
        cmd_args = ['--ignore-missing-imports', '--config-file', "mypy.ini"]
        extensions.extend(cmd_args)
        setup_kwargs.update({
            'ext_modules': mypycify(extensions, verbose=True)
        })