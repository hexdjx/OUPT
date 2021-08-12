from pytracking.evaluation import Tracker, get_dataset, trackerlist

# my add oupt
# Learning Object-Uncertainty Policy for Visual Tracking
def oupt_otb():
    # Run OUPT on OTB dataset
    # target memory size parameter test (10~20)

    # trackers = trackerlist('oupt', 'oupt18_10', range(1)) + \
    #            trackerlist('oupt', 'oupt18_12', range(1)) + \
    #            trackerlist('oupt', 'oupt18_13', range(1)) + \
    #            trackerlist('oupt', 'oupt18_14', range(1)) + \
    #            trackerlist('oupt', 'oupt18_15', range(1)) + \
    #            trackerlist('oupt', 'oupt18_16', range(1)) + \
    #            trackerlist('oupt', 'oupt18_17', range(1)) + \
    #            trackerlist('oupt', 'oupt18_18', range(1)) + \
    #            trackerlist('oupt', 'oupt18_19', range(1)) + \
    #            trackerlist('oupt', 'oupt18_20', range(1))

    # target layer choice [layer1~layer4]
    # trackers = trackerlist('oupt', 'dimp18_l1', range(1)) + \
    #           trackerlist('oupt', 'dimp18_l2', range(1)) + \
    #           trackerlist('oupt', 'dimp18_l3', range(1)) + \
    #           trackerlist('oupt', 'dimp18_l4', range(1)) + \
    #           trackerlist('oupt', 'dimp18_l5', range(1)) + \
    #           trackerlist('oupt', 'dimp18_l6', range(1)) + \
    #           trackerlist('oupt', 'dimp18_l7', range(1)) + \
    #           trackerlist('oupt', 'dimp18_l8', range(1)) + \
    #           trackerlist('oupt', 'dimp18_l9', range(1)) + \
    #           trackerlist('oupt', 'dimp18_l10', range(1)) + \
    #           trackerlist('oupt', 'dimp18_l11', range(1)) + \
    #           trackerlist('oupt', 'dimp18_l12', range(1)) + \
    #           trackerlist('oupt', 'dimp18_l13', range(1)) + \
    #           trackerlist('oupt', 'dimp18_l14', range(1))

    # whether consider the initial state
    # trackers = trackerlist('oupt', 'oupt18_0', range(1)) + \
    #            trackerlist('oupt', 'oupt18_1', range(1))

    # final test based on DiMP and PrDiMP
    trackers = trackerlist('oupt', 'oupt18', range(1)) + \
               trackerlist('oupt', 'oupt50', range(1)) + \
               trackerlist('oupt', 'proupt18', range(1)) + \
               trackerlist('oupt', 'proupt50', range(1))

    dataset = get_dataset('otb')
    return trackers, dataset


def oupt_tpl():
    # Run OUPT on Temple Color datasets
    trackers = trackerlist('oupt', 'proupt50', range(1)) + \
               trackerlist('dimp', 'prdimp50', range(1))

    dataset = get_dataset('tpl')
    return trackers, dataset


def oupt_nfs_uav():
    # Run OUPT on NFS and UAV datasets
    trackers = trackerlist('oupt', 'proupt50', range(1))

    dataset = get_dataset('nfs', 'uav')
    return trackers, dataset


def oupt_lasot():
    # Run OUPT on LaSOT dataset
    trackers = trackerlist('oupt', 'proupt50', range(1))

    dataset = get_dataset('lasot')
    return trackers, dataset


def oupt_trackingnet():
    # Run OUPT on TrackingNet dataset
    trackers = trackerlist('oupt', 'proupt50', range(1))

    dataset = get_dataset('trackingnet')
    return trackers, dataset

