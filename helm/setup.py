# ============LICENSE_START==========================================
# ===================================================================
# Copyright (c) 2018 AT&T
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============LICENSE_END============================================


from setuptools import setup

# Replace the place holders with values for your project

setup(

    # Do not use underscores in the plugin name.
    name='helm',
    version='5.0.2',
    author='Hong Guan(AT&T)',
    author_email='hg4105@att.com',
    description='This plugin supports Helm3 install/uninstall/upgrade/rollback '
                'charts of ONAP components. ',

    # This must correspond to the actual packages in the plugin.
    packages=['plugin'],

    license='LICENSE',
    zip_safe=False,
    install_requires=[
        # Necessary dependency for developing plugins, do not remove!
        'pyyaml>=3.12',
        "cloudify-plugins-common>=4.1.1"
    ],
    test_requires=[
        "cloudify-dsl-parser>=4.1.1"
        "nose"
    ]
)
