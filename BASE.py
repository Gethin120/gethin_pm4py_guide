# 进程树对齐
from pm4py.algo.conformance.alignments.process_tree import algorithm as align_approx
# 打印出对齐
from pm4py.objects.petri_net.utils.align_utils import pretty_print_alignments
# token重演
from pm4py.algo.conformance.tokenreplay import algorithm as tr
# 反对齐
from pm4py.algo.conformance.antialignments.variants.discounted_a_star import apply as antii
# 打印批量执行的每个活动资源组合的摘要信息（大小）
from pm4py.algo.discovery.batches import algorithm
# 获取指定维度中事件的分布，月、日、时间
from pm4py.statistics.attributes.pandas.get import get_events_distribution
# 特征提取（不是很懂）
from pm4py.algo.transformation.log_to_features import algorithm as feature_extraction
# 从csv读日志
# dataframe = pd.read_csv(os.path.join("..", "tests", "input_data", "receipt.csv"))
# dataframe = pm4py.format_dataframe(dataframe)

# discovery
import pm4py_examples.im_example
import pm4py_examples.heu_miner_test
import pm4py_examples.heuminer_plusplus
import pm4py_examples.alpha_miner
import pm4py_examples.footprints_petri_net
import pm4py_examples.data_petri_nets
import pm4py_examples.inductive_miner
import pm4py_examples.network_analysis
import pm4py_examples.trans_system_stochastic_vis

# alignment
import pm4py_examples.multialignments
import pm4py_examples.token_replay_imdf
import pm4py_examples.token_replay_alpha
import pm4py_examples.backwards_token_replay
import pm4py_examples
# 日志有多少条迹、多少种事件、多少种变体
# len(pm4py.get_variants_as_tuples(log))
#性能谱的形式展示日志日期分布
import pm4py_examples.perf_spectrum_visualization

# 资源处理相关新包新文章
# from pm4py.algo.organizational_mining
import pm4py_examples.resource_profiles_log
import pm4py_examples.rework
import pm4py_examples.roles_detection

#计时
import time

aa = time.time()
bb = time.time()
cc = time.time()
print("playout time", bb - aa)
print("alignments time", cc - bb)
print("TOTAL", cc - aa)

# 手工生成日志
import pm4py_examples.manual_log_generation
# 手工生成Petri网
import pm4py_examples.petri_manual_generation
import pm4py_examples.tree_manual_generation
# 手工生成进程树
import pm4py_examples.tree_manual_generation


# 分析日志
import pm4py_examples.memory_profilation_alignments
import memory_profiler

# 模拟日志，使用蒙特卡罗算法，例子里介绍了参数的设置方式
import pm4py_examples.montecarlo_petri_net
# 模拟日志，使用dfg
import pm4py_examples.performance_dfg_simulation
# 模拟日志，使用进程树
import pm4py_examples.tree_playout

#事件流
import pm4py_examples.pandas_iterable_to_trace_stream
import pm4py_examples.streaming_xes_reader_event_stream
import pm4py_examples.streaming_xes_reader_event_stream
import pm4py_examples.streaming_xes_reader_trace_stream
import pm4py_examples.streaming_discovery_dfg
import pm4py_examples.streaming_conformance_footprints
import pm4py_examples.streaming_conformance_tbr
import pm4py_examples.streaming_conformance_temporal_profile
# 导入xes文件

from pm4py.objects.log.importer.xes.importer import apply as xes_importer
log = xes_importer('trace_.xes')

# 使用alpha算法挖掘Petri网
from pm4py.algo.discovery.alpha.algorithm import apply as alpha_miner
net, initial_marking, final_marking = alpha_miner(log)
net, im, fm=alpha_miner(log)
# Petri网可视化
from pm4py.visualization.petri_net import visualizer as pn_vis
petri_net_alpha = pn_vis.apply(net,initial_marking,final_marking)
pn_vis.view(petri_net_alpha)

#导入pnml格式的Petri网
from pm4py.objects.petri_net.importer.importer import apply as pnml_importer
from pm4py.objects.petri_net.importer.importer import Variants
net, initial_marking, final_marking = pnml_importer('model/lj_final.pnml', variant=Variants.PNML)

# 检查Petri网的稳健性
from pm4py.algo.analysis.woflan.algorithm import apply as soudness
soudness(net,initial_marking,final_marking)

# 评估Petri网
from pm4py.evaluation import evaluator
result = evaluator.apply(log, net, initial_marking, final_marking)
result_fitness=result['fitness']['log_fitness']
result_precision=result['precision']
result_f=result['fscore']
# Petri网通过matplotlib可视化
