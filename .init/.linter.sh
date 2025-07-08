#!/bin/bash
cd /home/kavia/workspace/code-generation/nettwin-vision-10-783d060f/Main_Container_for_NetTwin_Vision
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

