from os import environ

from Cython.Build import cythonize
from Cython.Distutils.build_ext import new_build_ext
from setuptools import Distribution

environ["CFLAGS"] = "-O3"

distribution = Distribution(
    {
        "ext_modules": cythonize(
            [
                "starlite/app.py",
                "starlite/asgi.py",
                "starlite/controller.py",
                "starlite/kwargs.py",
                "starlite/response.py",
                "starlite/routing.py",
                "starlite/handlers/*.py",
            ],
            nthreads=0,
            language_level=3,
            annotate=False,
            force=True,
        ),
        "cmdclass": {
            "build_ext": new_build_ext,
        },
    }
)

# Grab the build_ext command and copy all files back to source dir.
# Done so Poetry grabs the files during the next step in its build.
distribution.run_command("build_ext")
build_ext_cmd = distribution.get_command_obj("build_ext")
build_ext_cmd.copy_extensions_to_source()
