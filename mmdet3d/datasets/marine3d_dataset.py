import mmengine

from mmdet3d.registry import DATASETS
from .det3d_dataset import Det3DDataset
from .kitti_dataset import KittiDataset


@DATASETS.register_module()
class Marine3dDataset(KittiDataset):

    # replace with all the classes in customized pkl info file
    METAINFO = {
        'classes': ('ship', 'buoy', 'others'),
        'palette': [(165, 42, 42), (106, 0, 228), (119, 11, 32)]
    }
