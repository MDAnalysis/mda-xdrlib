from setuptools import setup
import versioneer


setup(name="mda-xdrlib",
      include_package_data=True,
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
)
