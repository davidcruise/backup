#!/bin/bash
open 'https://colab.research.google.com/drive/1ZvxMtYMo8nFwOWmZsQvcx-DgAvNYCdHd'
jupyter notebook --no-browser\
  --NotebookApp.allow_origin='https://colab.research.google.com' \
  --port=8888 \
  --NotebookApp.port_retries=0
