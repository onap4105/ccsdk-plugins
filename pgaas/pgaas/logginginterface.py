# org.onap.ccsdk
# ============LICENSE_START====================================================
# =============================================================================
# Copyright (c) 2018 AT&T Intellectual Property. All rights reserved.
# =============================================================================
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============LICENSE_END======================================================

from cloudify import ctx

def debug(msg):
  """
  Print a debugging message.
  This is a handy endpoint to add other extended debugging calls.
  """
  ctx.logger.debug(msg)
  with open("/var/tmp/pgaas.log", "a") as fd:
    fd.write("DEBUG: " + msg + "\n")

def warn(msg):
  """
  Print a warning message.
  This is a handy endpoint to add other extended warning calls.
  """
  ctx.logger.warn(msg)
  with open("/var/tmp/pgaas.log", "a") as fd:
    fd.write("WARN: " + msg + "\n")

def error(msg):
  """
  Print an error message.
  This is a handy endpoint to add other extended error calls.
  """
  ctx.logger.error(msg)
  with open("/var/tmp/pgaas.log", "a") as fd:
    fd.write("ERROR: " + msg + "\n")

def info(msg):
  """
  Print a info message.
  This is a handy endpoint to add other extended info calls.
  """
  ctx.logger.info(msg)
  with open("/var/tmp/pgaas.log", "a") as fd:
    fd.write("INFO: " + msg + "\n")