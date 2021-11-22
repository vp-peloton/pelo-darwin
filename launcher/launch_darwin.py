#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 12:19:36 2017

@author: vijaypappu
"""

import argparse
# import pelo_darwin
from pelo_darwin.backend.common_utils import CommonUtils
from pelo_darwin.ga_orchestrator import GAOrchestrator
from pelo_darwin.constrained_ga_runner import ConstrainedGARunner

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)

    args = parser.parse_args()
    task_config_path = args.config

    task_config = CommonUtils.load_json(task_config_path)
    ga_orchestrator = GAOrchestrator(task_config)
    # ga_runner = GARunner(ga_orchestrator)
    constrained_ga_runner = ConstrainedGARunner(ga_orchestrator)
    constrained_ga_runner.run()
