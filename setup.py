from setuptools import setup, find_packages

setup(
    name="SchoolManagementSystemAI",
    version="1.0.0",
    description="AI-Powered School Management System",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "Flask",
        "SQLAlchemy",
        "numpy",
        "opencv-python",
        "pytest",
    ],
)
