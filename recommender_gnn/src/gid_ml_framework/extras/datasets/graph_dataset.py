import logging
import os
from pathlib import Path
from typing import Any, Dict, List

from kedro.io import AbstractDataSet
from kedro.io.core import get_protocol_and_path
from pathy import Pathy

from gid_ml_framework.extras.graph_utils.dgsr_utils import (
    SubGraphsDataset,
    load_graphs_python,
    save_graphs_python,
)

logger = logging.getLogger(__name__)


class DGSRSubGraphsDataSet(AbstractDataSet):
    """``DGSRSubGraphsDataSet`` loads/saves dgl graphs structures from/to a given directory using dgl loaders.

    Examples:
    ::
        >>> DGSRSubGraphsDataSet(dir='path/to/graphs/')
    """

    def __init__(
        self,
        dir: str,
        save_args: Dict[str, Any] = None,
        load_args: Dict[str, Any] = None,
    ):
        """Creates a new instance of DGSRSubGraphsDataSet to loads/saves dgl graphs structures from/to a given directory
        using dgl loaders.

        Args:
            dir: The directory location to load/save data.
            save_args: Additional arguments to kedro AbstractDataSet saving function
            load_args: Additional arguments to kedro AbstractDataSet loading function
        """
        self._dir = Pathy(dir) if dir[0:5] == "gs://" else Path(dir)
        protocol, _ = get_protocol_and_path(dir)
        self._protocol = protocol

        self._load_args = dict()
        if load_args is not None:
            self._load_args.update(load_args)

        self._save_args = dict()
        if save_args is not None:
            self._save_args.update(save_args)

    def _load(self) -> SubGraphsDataset:
        load_path = self._dir
        dataset = SubGraphsDataset(load_path, load_graphs_python)
        return dataset

    def _save(self, data: List) -> None:
        file_extension = self._save_args.get("file_extension")

        save_path = self._dir
        if save_path.exists():
            logger.warning("Directory already exists, it may be not empty!")
        else:
            logger.info(f"Creating new directory: {save_path}")
            save_path.mkdir(parents=True, exist_ok=True)
        if data:
            for row in data:
                if row:
                    user, item_number, graph, graph_dict = row
                    save_dir = os.path.join(save_path, str(user))
                    file_name = "_".join([str(user), str(item_number)])
                    save_filepath = os.path.join(
                        save_dir, f"{file_name}.{file_extension}"
                    )
                    _create_parent_dir(save_filepath)
                    logger.info(f"Saving graph here: {save_filepath}")
                    save_graphs_python(save_filepath, graph, graph_dict)

    def _describe(self) -> Dict[str, Any]:
        """Returns a dict that describes the attributes of the dataset."""
        return dict(filepath=self._dir, protocol=self._protocol)


def _create_parent_dir(path: str) -> None:
    path_object = Pathy(path) if path[0:5] == "gs://" else Path(path)
    path_object.parent.mkdir(parents=True, exist_ok=True)