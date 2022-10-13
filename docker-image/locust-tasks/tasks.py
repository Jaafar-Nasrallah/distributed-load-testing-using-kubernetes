#!/usr/bin/env python

# Copyright 2022 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import uuid

from datetime import datetime
from locust import FastHttpUser, TaskSet, task


# [START locust_test_task]

class MetricsTaskSet(TaskSet):
    _deviceid = None

    def on_start(self):
        self._deviceid = str(uuid.uuid4())

    @task(200)
    def login(self):
        self.client.get('/recommend?mwv=true&widgetids=5704070618677248&userid=5c7a3dbf-5f0a-4866-83e9-fbbbe08b8776&appdomain=kooora.com&history_postids=1180081&country_code=LB&device_code=desktop&exc_ads=')
        self.client.get('/recommend?mwv=true&widgetids=5743010377629696&userid=5c7a3dbf-5f0a-4866-83e9-fbbbe08b8776&appdomain=kooora.com&history_postids=1180081,1179546&country_code=LB&device_code=desktop&exc_ads=')
        self.client.get('/recommend?mwv=true&widgetids=5749976369987584,5769901083983872&userid=fa8373bb-ccc8-414c-a780-b9e429d50fa8&appdomain=albayan.ae&history_postids=1.4535700&country_code=LB&device_code=desktop&exc_ads=')
        self.client.get('/recommend?mwv=true&widgetids=5653503041077248,5673817028427776&userid=dae5edc6-2e01-43b0-ada9-7792527a8e27&appdomain=emaratalyoum.com&history_postids=1.1677054&country_code=LB&device_code=desktop&exc_ads=')
        self.client.get('/recommend?mwv=true&widgetids=5635919931506688,5714101758066688&userid=9ba27121-63cc-4225-a02f-b71608b22012&appdomain=almayadeen.net&history_postids=1638386&country_code=LB&device_code=desktop&exc_ads=')



class MetricsLocust(FastHttpUser):
    tasks = {MetricsTaskSet}

# [END locust_test_task]
