"""
This is a boilerplate pipeline 'prediction'
generated using Kedro 0.18.4
"""
import logging

import pandas as pd
import xgboost as xgb

from ..data_preparation_utils import extract_column_names

logger = logging.getLogger(__name__)


def predict(abt_predict: pd.DataFrame, model) -> pd.DataFrame:
    """Make predictions on a given data frame.

    Args:
        abt_predict (pd.DataFrame): data frame to predict on
        model: XGBoost model

    Returns:
        pd.DataFrame: data frame with predicted scores
    """
    logger.info("Applying model to get predictions...")

    info_cols, num_cols, cat_cols, _ = extract_column_names(abt_predict)
    dpredict = xgb.DMatrix(abt_predict[num_cols + cat_cols])

    scores = model.predict(dpredict)

    predictions = abt_predict.loc[:, info_cols]
    predictions["y_score"] = scores

    return predictions
