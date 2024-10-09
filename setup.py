from setuptools import setup, find_packages

setup(
    name="agent_automation",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    requires=["click"],
    entry_points={
        "console_scripts": [
            "agent_automation = automation.scripts.agent_automation:cli",
        ],
    },
    author="Avinash Vaidya",
    author_email="avinash.vaidya@example.com",
    description="A command-line tool to process JSON files",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)
