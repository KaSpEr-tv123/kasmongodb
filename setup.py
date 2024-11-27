from setuptools import setup, find_packages

setup(
    name="kasmongodb",  # Название вашей библиотеки
    version="0.1.0",  # Версия
    description="KasMongoDB library for easier MongoDB operations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KaSpEr-tv123/kasmongodb",  # Ссылка на ваш репозиторий
    author="kasperenok",  # Автор
    license="MIT",  # Лицензия
    packages=find_packages(),
    install_requires=[
        "pymongo>=4.0.0"  # Зависимости
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
