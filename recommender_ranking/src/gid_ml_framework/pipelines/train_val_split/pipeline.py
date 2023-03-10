from kedro.pipeline import Pipeline, node
from kedro.pipeline.modular_pipeline import pipeline

from .nodes import train_val_split


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=train_val_split,
                inputs=[
                    "transactions",
                    "params:candidate_selection.date_column",
                    "params:candidate_selection.no_train_week",
                    "params:candidate_selection.no_val_week",
                ],
                outputs=["train_transactions", "val_transactions"],
                name="train_val_split_node",
            ),
        ],
        namespace="train_val_split",
        inputs=["transactions"],
        outputs=["train_transactions", "val_transactions"],
    )
