from pytracking.evaluation.environment import EnvSettings
import os

def local_env_settings():
    settings = EnvSettings()

    base_path = '/home/hexdjx/code/Tracking/'
    dataset_path = '/media/hexdjx/907856427856276E/'

    settings.network_path = dataset_path + 'pretrained_networks'
    # Set your local paths here.
    settings.dataspec_path = base_path + 'OUPT/ltr/data_specs'
    settings.davis_dir = dataset_path + 'DAVIS/2017'
    settings.got10k_path = dataset_path + 'GOT-10k'
    settings.lasot_path = dataset_path + 'LaSOT/LaSOTBenchmark'
    settings.nfs_path = dataset_path + 'NFS'
    settings.otb_path = dataset_path + 'OTB100'
    settings.tpl_path = dataset_path + 'TC128'
    settings.trackingnet_path = dataset_path + 'TrackingNet'
    settings.uav_path = dataset_path + 'UAV123'
    settings.youtubevos_dir = dataset_path + 'YouTubeVOS/2018'
    settings.vot_path = '/home/hexdjx/code/Tracking/OUPT/pytracking/VOT/vot2018-workspace/sequences/'
    # result paths
    settings.result_plot_path = base_path + 'OUPT/pytracking/results/plots/'
    settings.results_path = base_path + 'OUPT/pytracking/results/tracking_results/'    # Where to store tracking results
    settings.segmentation_path = base_path + 'OUPT/pytracking/results/segmentation_results/'
    settings.tn_packed_results_path = base_path + 'OUPT/pytracking/results/packed_results/'

    return settings

