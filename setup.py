import setuptools
import os

def get_version_and_cmdclass(pkg_path):
    import os
    from importlib.util import module_from_spec, spec_from_file_location

    spec = spec_from_file_location("version", os.path.join(pkg_path, "_version.py"))
    module = module_from_spec(spec)
    spec.loader.exec_module(module)

    data = module.get_data()
    return data["version"], module.get_cmdclass(pkg_path)


if __name__ == "__main__":
    # we define the license string like this to be backwards compatible to setuptools<77
    version, cmdclass = get_version_and_cmdclass(
        os.path.join("octoprint_costestimation")
    )
    setuptools.setup(license="AGPL-3.0-or-later", version=version, cmdclass=cmdclass)
