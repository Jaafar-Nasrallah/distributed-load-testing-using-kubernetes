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

    @task(1000)
    def login(self):
        self.client.post(
            '/recommend?mwv=true&widgetids=5634837222260736&userid=5e589e7b-7fc9-4858-9a7a-931ff70eeafa&appdomain=dev-blog.cognativex.com&history_postids=124,125&history_adids=-1722605703,137263211,1696517043,-1555703880,-644877927&exc_ads=', {"deviceid": self._deviceid})



class MetricsLocust(FastHttpUser):
    tasks = {MetricsTaskSet}

# [END locust_test_task]
