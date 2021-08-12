class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/media/hexdjx/907856427856276E/'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = self.workspace_dir + '/tensorboard/'    # Directory for tensorboard files.
        self.pretrained_networks = self.workspace_dir + '/pretrained_networks/'
        self.lasot_dir = '/media/hexdjx/907856427856276E/LaSOT/LaSOTBenchmark'
        self.got10k_dir = '/media/hexdjx/907856427856276E/GOT-10k/train'
        self.trackingnet_dir = '/media/hexdjx/907856427856276E/TrackingNet'
        self.coco_dir = '/media/hexdjx/907856427856276E/COCO'
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = ''
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
        self.davis_dir = '/media/hexdjx/907856427856276E/DAVIS'
        self.youtubevos_dir = '/media/hexdjx/907856427856276E/YouTubeVOS'
