"""Module for getting configuration values (often from env). Based on
config-variables.ts."""

import os

UPLOAD_CHUNK_SIZE = 8 * 1024**2  # 8 MB.
UPLOAD_FILE_CONCURRENCY = 2


def get_runtime_url():
  """Returns the value of the ACTIONS_RUNTIME_URL var in the environment. Raises
  an exception if not set."""
  if url := os.environ.get('ACTIONS_RUNTIME_URL'):
    return url
  else:
    raise Exception('Unable to get ACTIONS_RUNTIME_URL env variable')


def get_runtime_token():
  """Returns the value of the ACTIONS_RUNTIME_TOKEN var in the environment.
  Raises an exception if not set."""
  if token := os.environ.get('ACTIONS_RUNTIME_TOKEN'):
    return token
  else:
    raise Exception('Unable to get ACTIONS_RUNTIME_TOKEN env variable')


def get_work_flow_run_id():
  """Returns the value of the GITHUB_RUN_ID var in the environment. Raises an
  exception if not set."""
  if work_flow_run_id := os.environ.get('GITHUB_RUN_ID'):
    return work_flow_run_id
  else:
    raise Exception('Unable to get GITHUB_RUN_ID env variable.')


def get_retention_days():
  """Returns the value of the GITHUB_RETENTION_DAYS or None if it wasn't
  specified."""
  return os.environ.get('GITHUB_RETENTION_DAYS')
