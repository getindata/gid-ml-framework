"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from .pipelines import data_preprocessing


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_preprocessing_pipeline = data_preprocessing.create_pipeline()

    return {
        "__default__": data_preprocessing_pipeline,
        "data_preprocessing": data_preprocessing_pipeline,
    }
