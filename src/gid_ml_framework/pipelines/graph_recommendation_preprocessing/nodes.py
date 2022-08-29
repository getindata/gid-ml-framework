from typing import Iterator, Union, Tuple, List
from datetime import datetime
import logging
from xmlrpc.client import Boolean

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from kedro.extras.datasets.pandas import CSVDataSet

from gid_ml_framework.extras.datasets.chunks_dataset import (
 _load,
 _concat_chunks,
)


pd.options.mode.chained_assignment = None
log = logging.getLogger(__name__)
# Overwriting load method because of chunksize bug in Kedro < 0.18
CSVDataSet._load = _load


def concat_train_val(train_df: pd.DataFrame, val_df: pd.DataFrame, date_column: str) -> pd.DataFrame:
    """Concatenate train and val subsets for preprocessing purposes. Also converts date column to timestamp and
    renames columns.

    Args:
        train_df (pd.DataFrame): transactions train dataframe
        val_df (pd.DataFrame): transaction val datafreame

    Returns:
        pd.DataFrame: concatenated transactions dataframe
    """
    concat_df = pd.concat([train_df, val_df]).reset_index(drop=True)
    concat_df.loc[:, 'time'] = concat_df.loc[:, date_column].values.astype(np.int64) // 10 ** 9
    concat_df.drop(date_column, axis=1, inplace=True)
    concat_df.rename(columns={'articles_id': 'item_id', 'customer_id': 'user_id'}, inplace=True)
    return concat_df


def map_users_and_items(train_df: pd.DataFrame, val_df: pd.DataFrame) -> Tuple:
    """Map users and items ids to consecutive integers.

    """
