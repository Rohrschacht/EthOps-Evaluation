#!/usr/bin/env python3

import os
import pm4py
from pm4py.objects.log.obj import EventLog
from pm4py.objects.log.obj import Trace
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.algo.evaluation.replay_fitness import algorithm as replay_fitness_evaluator
from pm4py.algo.evaluation.precision import algorithm as precision_evaluator
from pm4py.algo.evaluation.generalization import algorithm as generalization_evaluator
from pm4py.algo.evaluation.simplicity import algorithm as simplicity_evaluator
from pm4py.objects.conversion.bpmn import converter as bpmn_converter

from pm4py.util import constants

event_log = pm4py.read_xes("test_output/log_DevOpsRegistry_all.xes")
print(event_log)

event_log.rename(columns={"case:ident:piid": "case_id"}, inplace=True)
print(event_log)

num_events = len(event_log)
num_cases = len(event_log.case_id.unique())
print("Number of events: {}\nNumber of cases: {}".format(num_events, num_cases))

event_log.rename(columns={"case_id": "case:concept:name"}, inplace=True)

manual_bpmn_graph = pm4py.read_bpmn("simple_smart_contract_v2.bpmn")
manual_net, man_im, man_fm = bpmn_converter.apply(manual_bpmn_graph)

manual_fitness = replay_fitness_evaluator.apply(event_log, manual_net, man_im, man_fm, variant=replay_fitness_evaluator.Variants.TOKEN_BASED)
print("Manual fitness: ", manual_fitness)

replayed_traces = pm4py.conformance_diagnostics_token_based_replay(event_log, manual_net, man_im, man_fm)
replayed_traces = [trace for trace in replayed_traces if not trace["trace_is_fit"]]
for trace in replayed_traces:
    print(trace)
    print()
