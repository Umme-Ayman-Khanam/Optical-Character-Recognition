from setuptools import setup

setup(
    name='OCR',
    version='1.0.0',
    description='Optical Character Recognition',
    author='Umme Ayman Khanam',
    packages=['word_detector'],
    url="https://github.com/Umme-Ayman-Khanam/Optical-Character-Recognition",
    install_requires=['numpy', 'sklearn', 'opencv-python'],
    python_requires='>=3.7'
)
