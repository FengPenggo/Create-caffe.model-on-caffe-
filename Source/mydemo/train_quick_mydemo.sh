#!/usr/bin/env sh
set -e

TOOLS=./build/tools

$TOOLS/caffe train \
  --solver=./mydemo/c2f1_quick_solver_mydemo.prototxt $@

# reduce learning rate by factor of 10 after 8 epochs
$TOOLS/caffe train \
  --solver=./mydemo/c2f1_quick_solver_lr1_mydemo.prototxt \
  --snapshot=./mydemo/c2f1_quick_mydemo_iter_4000.solverstate.h5 $@
