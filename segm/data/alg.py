from pathlib import Path

from segm.data.base import BaseMMSeg
from segm.data import utils
from segm.config import dataset_dir
import os


ALG_CONFIG_PATH = Path(__file__).parent / "config" / "alg.py"
ALG_CATS_PATH = Path(__file__).parent / "config" / "alg.yml"


class ALG(BaseMMSeg):
    def __init__(self, image_size, crop_size, split, **kwargs):
        super().__init__(
            image_size,
            crop_size,
            split,
            ALG_CONFIG_PATH,
            **kwargs,
        )
        self.names, self.colors = utils.dataset_cat_description(ALG_CATS_PATH)
        self.n_cls = 2
        self.ignore_label = 0
        self.reduce_zero_label = True

    def update_default_config(self, config):
        root_dir = "/project01/cvrl/jhuang24/australia-backup/data/"
        path = root_dir
        config.data_root = path

        if self.split == "train":
            config.data.train.data_root = os.path.join(path, "test")
        # elif self.split == "trainval":
        #     config.data.trainval.data_root = os.path.join(path, "test")
        # elif self.split == "val":
        #     config.data.val.data_root = os.path.join(path, "test")
        elif self.split == "test":
            config.data.test.data_root = root_dir

        config = super().update_default_config(config)
        return config

    def test_post_process(self, labels):
        return labels + 1
