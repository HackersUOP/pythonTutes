'''
* Copyright 2016 Hackers' Club, University Of Peradeniya
* Author : Irunika Weeraratne E/11/431
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
* http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*
'''

#If condition example
temperature = 130

if temperature>100:
    print "Hot"
    if temperature>120:
        print "too hot"
elif temperature > 25:
    print "mid"
else:
    print "cold"