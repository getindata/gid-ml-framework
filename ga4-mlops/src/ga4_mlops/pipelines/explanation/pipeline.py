"""
This is a boilerplate pipeline 'explanation'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import calculate_shap, create_explanations, sample_data


def create_pipeline(subset: str, **kwargs) -> Pipeline:
    """Create model explanation pipeline.

    Args:
        subset (str): Data subset to explain model on (train, valid, test). Has to contain ground truth column (target).

    Returns:
        Pipeline: explanation Kedro pipeline
    """
    possible_subsets = ["train", "valid", "test"]
    assert subset in possible_subsets, f"Subset should be one of: {possible_subsets}"

    namespace = subset

    pipeline_template = pipeline(
        [
            node(
                name="sample_data_node",
                func=sample_data,
                inputs=["abt", "params:n_obs", "params:sampling_seed"],
                outputs="abt_sample",
            ),
            node(
                name="calculate_shap_node",
                func=calculate_shap,
                inputs=["abt_sample", "stored.model"],
                outputs="shap_values",
            ),
            node(
                name="create_explanations_node",
                func=create_explanations,
                inputs=[
                    "shap_values",
                    "abt_sample",
                    "stored.model",
                    "params:pdp_top_n",
                ],
                outputs=[
                    "shap_summary_plot",
                    "feature_importance",
                    "partial_dependence_plots",
                ],
            ),
        ]
    )

    main_pipeline = pipeline(
        pipe=pipeline_template,
        inputs={
            "stored.model": "stored.model",
        },
        parameters={
            "n_obs": "n_obs",
            "sampling_seed": "sampling_seed",
            "pdp_top_n": "pdp_top_n",
        },
        outputs={
            "shap_summary_plot": "shap_summary_plot",
            "feature_importance": "feature_importance",
            "partial_dependence_plots": "partial_dependence_plots",
        },
        namespace=namespace,
    )

    return main_pipeline
