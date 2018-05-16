#!/usr/local/bin/python

#  Copyright (c) 2018 Sony Pictures Imageworks Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.





from Manifest import unittest, Cue3


class ProxyTests(unittest.TestCase):
    """proxy converts different types of entities to usable Ice proxies"""

    def testProxyUniqueId(self):
        """convert a string and class name to proxy"""
        id = "A0000000-0000-0000-0000-000000000000"
        self.assertEquals(str(Cue3.proxy(id, "Group")),
                          "manageGroup/A0000000-0000-0000-0000-000000000000 -t:tcp -h cue3test01 -p 9019 -t 5000")

    def testProxyUniqueIdArray(self):
        """convert a list of strings and a class name to a proxy"""
        ids = ["A0000000-0000-0000-0000-000000000000","B0000000-0000-0000-0000-000000000000"]
        self.assertTrue(len(Cue3.proxy(ids, "Group")), 2)

    def testProxyEntity(self):
        """convert an entity to a proxy"""
        job = Cue3.getJobs()[0]
        self.assertEquals(job.proxy, Cue3.proxy(job))

    def testProxyProxy(self):
        """convert a proxy to a proxy"""
        job = Cue3.getJobs()[0]
        proxy = job.proxy
        self.assertEquals(proxy, Cue3.proxy(proxy))

    def testProxyEntityList(self):
        """convert a list of entities to a list of proxies"""
        jobs = Cue3.getJobs()
        self.assertEquals(len(jobs), len(Cue3.proxy(jobs)))
        proxies  = Cue3.proxy(jobs)
        for i in range(0,len(proxies)):
            self.assertEqual(proxies[i], jobs[i].proxy)

    def testProxyProxyList(self):
        """convert a list of proxies to a list of proxies"""
        proxiesA = [job.proxy for job in Cue3.getJobs()]
        proxiesB = Cue3.proxy(proxiesA)
        self.assertEquals(len(proxiesA), len(proxiesB))
        for i in range(0,len(proxiesA)):
            self.assertEqual(proxiesA[i], proxiesB[i])

class IdTests(unittest.TestCase):
    """id() takes a proxy or entity and returns the unique id"""

    def testIdOnEntity(self):
        job = Cue3.getJobs()[0]
        self.assertEquals(job.proxy.ice_getIdentity().name, Cue3.id(job))

    def testIdOnProxy(self):
        proxy = Cue3.getJobs()[0].proxy
        self.assertEquals(proxy.ice_getIdentity().name, Cue3.id(proxy))

    def testIdOnEntityList(self):
        jobs = Cue3.getJobs()
        ids = Cue3.id(jobs)
        self.assertEquals(len(jobs), len(ids))
        for i in range(0,len(jobs)):
            self.assertEquals(jobs[i].proxy.ice_getIdentity().name, ids[i])

    def testIdOnEntityList(self):
        jobs = Cue3.getJobs()
        ids = Cue3.id(jobs)
        self.assertEquals(len(jobs), len(ids))
        for i in range(0,len(jobs)):
            self.assertEquals(jobs[i].proxy.ice_getIdentity().name, ids[i])

if __name__ == '__main__':
    unittest.main()

