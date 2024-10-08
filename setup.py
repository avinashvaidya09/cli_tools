from setuptools import setup, find_packages

setup(
    name='agent_automation',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    requires=['click'],
    entry_points={
        'console_scripts': [
            'agent_automation = automation.scripts.agent_automation:cli',
        ],
    },
)