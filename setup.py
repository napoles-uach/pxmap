import setuptools

setuptools.setup(
    name="pxmap",
    version="0.0.2",
    author="Jose Manuel Napoles Duarte",
    author_email="jnapoles@uach.mx",
    description="Streamlit component for Plotly express",
    long_description="Streamlit component for creating maps with Plotly express",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63","plotly >=4.14.3"
    ],
)
