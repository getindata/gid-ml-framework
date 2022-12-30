"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline

from .pipelines import data_preprocessing, feature_engineering


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_preprocessing_train_pipeline = data_preprocessing.create_pipeline(train=True)
    data_preprocessing_predict_pipeline = data_preprocessing.create_pipeline(
        train=False
    )
    feature_engineering_train_pipeline = feature_engineering.create_pipeline(train=True)
    feature_engineering_predict_pipeline = feature_engineering.create_pipeline(
        train=False
    )

    return {
        "__default__": data_preprocessing_train_pipeline,
        "data_preprocessing_train": data_preprocessing_train_pipeline,
        "data_preprocessing_predict": data_preprocessing_predict_pipeline,
        "feature_engineering_train": feature_engineering_train_pipeline,
        "feature_engineering_predict": feature_engineering_predict_pipeline,
    }
