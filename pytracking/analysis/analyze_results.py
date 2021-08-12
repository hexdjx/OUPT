# Generating Results on Datasets

import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [7, 4]  # 14，8

from pytracking.analysis.plot_results import plot_results, print_results, print_per_sequence_results
from pytracking.evaluation import Tracker, get_dataset, trackerlist

trackers = []
#######################################################
# origin paper results
# otb:100, uav:123, tpl:129, nfs:100, lasot:280
# trackers.extend(trackerlist('CCOT', 'default', None, 'CCOT'))  # otb uav nfs tpl
# trackers.extend(trackerlist('ECO', 'default_hc', None, 'ECO-HC'))  # otb uav tpl
# trackers.extend(trackerlist('UPDT', 'default', range(0, 10), 'UPDT'))  # otb uav nfs tpl
# trackers.extend(trackerlist('MDNet', 'default', None, 'MDNet'))  # otb lasot(all data 1400) nfs
# trackers.extend(trackerlist('ECO', 'default_deep', None, 'ECO'))  # otb uav nfs tpl
# trackers.extend(trackerlist('DaSiamRPN', 'default', None, 'DaSiamRPN'))  # otb uav
# trackers.extend(trackerlist('SiamRPN++', 'default', None, 'SiamRPN++'))  # otb uav lasot
# trackers.extend(trackerlist('KYS', 'default', range(0, 1), 'KYS'))  # otb nfs # 5
# trackers.extend(trackerlist('ATOM', 'default', range(0, 5), 'ATOM'))  # otb uav nfs lasot # 5

# trackers.extend(trackerlist('DiMP', 'dimp18', range(0, 1), 'DiMP18'))  # otb uav nfs lasot # 5
# trackers.extend(trackerlist('DiMP', 'dimp50', range(0, 1), 'DiMP50'))  # otb uav nfs lasot # 5
# trackers.extend(trackerlist('DiMP', 'prdimp18', range(0, 1), 'PrDiMP18'))  # otb uav nfs lasot # 5
# trackers.extend(trackerlist('DiMP', 'prdimp50', range(0, 1), 'PrDiMP50'))  # otb uav nfs lasot # 5
# trackers.extend(trackerlist('DiMP', 'super_dimp', range(0, 1), 'SuperDiMP'))  # otb # 1

#################################################################################

# --my add--#####################################################################
# Object Uncertainty Policy

# OTB datasets results
# oupt target set num test
# trackers.extend(trackerlist('oupt', 'dimp18_10', range(0, 1), 'DiMP18_oup_10'))  # otb
# trackers.extend(trackerlist('oupt', 'dimp18_11', range(0, 1), 'DiMP18_oup_11'))  # otb
# trackers.extend(trackerlist('oupt', 'dimp18_12', range(0, 1), 'DiMP18_oup_12'))  # otb
# trackers.extend(trackerlist('oupt', 'dimp18_13', range(0, 1), 'DiMP18_oup_13'))  # otb
# trackers.extend(trackerlist('oupt', 'dimp18_14', range(0, 1), 'DiMP18_oup_14'))  # otb
# trackers.extend(trackerlist('oupt', 'dimp18_15', range(0, 1), 'DiMP18_oup_15'))  # otb
# trackers.extend(trackerlist('oupt', 'dimp18_16', range(0, 1), 'DiMP18_oup_16'))  # otb
# trackers.extend(trackerlist('oupt', 'dimp18_17', range(0, 1), 'DiMP18_oup_17'))  # otb this is better!
# trackers.extend(trackerlist('oupt', 'dimp18_18', range(0, 1), 'DiMP18_oup_18'))  # otb
# trackers.extend(trackerlist('oupt', 'dimp18_19', range(0, 1), 'DiMP18_oup_19'))  # otb
# trackers.extend(trackerlist('oupt', 'dimp18_20', range(0, 1), 'DiMP18_oup_20'))  # otb

# feature fusion
trackers.extend(trackerlist('oupt', 'oupt18', range(0, 1), 'DiMP18_oup_l0'))  # otb
trackers.extend(trackerlist('oupt', 'dimp18_l1', range(0, 1), 'DiMP18_oup_l1'))  # otb
trackers.extend(trackerlist('oupt', 'dimp18_l2', range(0, 1), 'DiMP18_oup_l2'))  # otb
trackers.extend(trackerlist('oupt', 'dimp18_l3', range(0, 1), 'DiMP18_oup_l3'))  # otb
trackers.extend(trackerlist('oupt', 'dimp18_l4', range(0, 1), 'DiMP18_oup_l4'))  # otb
trackers.extend(trackerlist('oupt', 'dimp18_l5', range(0, 1), 'DiMP18_oup_l5'))  # otb
trackers.extend(trackerlist('oupt', 'dimp18_l6', range(0, 1), 'DiMP18_oup_l6'))  # otb
trackers.extend(trackerlist('oupt', 'dimp18_l7', range(0, 1), 'DiMP18_oup_l7'))  # otb
trackers.extend(trackerlist('oupt', 'dimp18_l8', range(0, 1), 'DiMP18_oup_l8'))  # otb
trackers.extend(trackerlist('oupt', 'dimp18_l9', range(0, 1), 'DiMP18_oup_l9'))  # otb
trackers.extend(trackerlist('oupt', 'dimp18_l10', range(0, 1), 'DiMP18_oup_l10'))  # otb
trackers.extend(trackerlist('oupt', 'dimp18_l11', range(0, 1), 'DiMP18_oup_l11'))  # otb
trackers.extend(trackerlist('oupt', 'dimp18_l12', range(0, 1), 'DiMP18_oup_l12'))  # otb
trackers.extend(trackerlist('oupt', 'dimp18_l13', range(0, 1), 'DiMP18_oup_l13'))  # otb
trackers.extend(trackerlist('oupt', 'dimp18_l14', range(0, 1), 'DiMP18_oup_l14'))  # otb


# whether consider the initial state
# trackers.extend(trackerlist('oupt', 'oupt18_0', range(0, 1), 'ours(DiMP18_oup0)'))  # otb
# trackers.extend(trackerlist('oupt', 'oupt18_1', range(0, 1), 'ours(DiMP18_oup1)'))  # otb

# DiMP and PrDiMP based OTB results
# trackers.extend(trackerlist('oupt', 'oupt18', range(0, 1), 'ours(DiMP18_oup)'))
# trackers.extend(trackerlist('oupt', 'oupt50', range(0, 1), 'ours(DiMP50_oup)'))
# trackers.extend(trackerlist('oupt', 'proupt18', range(0, 1), 'ours(PrDiMP18_oup)'))
# trackers.extend(trackerlist('oupt', 'proupt50', range(0, 1), 'ours(PrDiMP50_oup)'))

# DiMP and PrDiMP based OTB, UAV, NFS, LaSOT and TPL results
# trackers.extend(trackerlist('dimp', 'prdimp50', range(0, 1), 'PrDiMP50'))  # tpl rerun
# trackers.extend(trackerlist('oupt', 'proupt50', range(0, 1), 'OUPT'))

#################################################################################################

# --plot results--##############################################################################
dataset = get_dataset('otb')
plot_results(trackers, dataset, 'OTB', merge_results=True, plot_types=('success', 'prec'),
             skip_missing_seq=False, force_evaluation=True, plot_bin_gap=0.05, exclude_invalid_frames=False)
#
# dataset = get_dataset('nfs')
# plot_results(trackers, dataset, 'NFS', merge_results=True, plot_types=('success', 'prec'),
#              skip_missing_seq=False, force_evaluation=True, plot_bin_gap=0.05, exclude_invalid_frames=False)
#
# dataset = get_dataset('uav')
# plot_results(trackers, dataset, 'UAV', merge_results=True, plot_types=('success', 'prec'),
#              skip_missing_seq=False, force_evaluation=True, plot_bin_gap=0.05, exclude_invalid_frames=False)

# dataset = get_dataset('lasot')
# plot_results(trackers, dataset, 'LaSOT', merge_results=True, plot_types=('success', 'prec'),
#              skip_missing_seq=False, force_evaluation=True, plot_bin_gap=0.05, exclude_invalid_frames=False)

# dataset = get_dataset('tpl')  # tpl tpl_nootb
# plot_results(trackers, dataset, 'TPL', merge_results=True, plot_types=('success', 'prec'),
#              skip_missing_seq=False, force_evaluation=True, plot_bin_gap=0.05, exclude_invalid_frames=False)

##################################################################################

# --print tables--##############################################################################
# dataset = get_dataset('otb')
# print_results(trackers, dataset, 'OTB', merge_results=True, plot_types=('success', 'prec', 'norm_prec'))

# dataset = get_dataset('nfs')
# print_results(trackers, dataset, 'NFS', merge_results=True, plot_types=('success', 'prec', 'norm_prec'))

# dataset = get_dataset('uav')
# print_results(trackers, dataset, 'UAV', merge_results=True, plot_types=('success', 'prec', 'norm_prec'))

# dataset = get_dataset('otb', 'nfs', 'uav')
# print_results(trackers, dataset, 'OTB+NFS+UAV', merge_results=True, plot_types=('success', 'prec', 'norm_prec'))

# dataset = get_dataset('lasot')
# print_results(trackers, dataset, 'LaSOT', merge_results=True, plot_types=('success', 'prec', 'norm_prec'))
##################################################################################################

# --Filtered per-sequence results--##############################################################
# Print per sequence results for sequences where all trackers fail, i.e. all trackers have average overlap in percentage of less than 10.0
# filter_criteria = {'mode': 'ao_max', 'threshold': 10.0}
# dataset = get_dataset('otb', 'nfs', 'uav')
# print_per_sequence_results(trackers, dataset, 'OTB+NFS+UAV', merge_results=True, filter_criteria=filter_criteria,
#                            force_evaluation=False)

# Print per sequence results for sequences where at least one tracker fails, i.e. a tracker has average overlap in percentage of less than 10.0
# filter_criteria = {'mode': 'ao_min', 'threshold': 10.0}
# dataset = get_dataset('otb', 'nfs', 'uav')
# print_per_sequence_results(trackers, dataset, 'OTB+NFS+UAV', merge_results=True, filter_criteria=filter_criteria,
#                            force_evaluation=False)

# Print per sequence results for sequences where the trackers have differing behavior.
# i.e. average overlap in percentage for different trackers on a sequence differ by at least 40.0
# filter_criteria = {'mode': 'delta_ao', 'threshold': 40.0}
# dataset = get_dataset('otb', 'nfs', 'uav')
# print_per_sequence_results(trackers, dataset, 'OTB+NFS+UAV', merge_results=True, filter_criteria=filter_criteria,
#                            force_evaluation=False)

# Print per sequence results for all sequences
# filter_criteria = None
# dataset = get_dataset('otb', 'nfs', 'uav')
# print_per_sequence_results(trackers, dataset, 'OTB+NFS+UAV', merge_results=True, filter_criteria=filter_criteria,
#                            force_evaluation=False)
######################################################################################
