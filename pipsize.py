# Size in MB of installed packages
import pkg_resources
import os
from pathlib import Path

installed_packages = pkg_resources.working_set
i=0
for package in installed_packages:
    if i < len(package.key) : i = len(package.key)

for package in installed_packages:
    location = os.path.join(package.location, package.key)
    root_directory = Path(location)
    size = sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())
    size = size / 1024 / 1024
    size = round(size, 2)
    print((f'{package.key}:\t {size} MB').expandtabs(i+3))
