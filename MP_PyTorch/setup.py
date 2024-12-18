from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
readme = (this_directory/"README.md").read_text()

setup(
    name='mp_pytorch',
    version='0.1.4',
    packages=['mp_pytorch', 'mp_pytorch.mp', 'mp_pytorch.util',
              'mp_pytorch.basis_gn', 'mp_pytorch.phase_gn', 'mp_pytorch.demo'],
    license='MIT',
    install_requires=[],

    # README.md
    description='The Movement Primitives Package in PyTorch',
    long_description=readme,
    long_description_content_type='text/markdown',
    classifiers=[
                "Intended Audience :: Science/Research",
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: POSIX :: Linux",
                ],
    )
