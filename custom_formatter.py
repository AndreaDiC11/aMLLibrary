"""
Copyright 2019 Marco Lattuada

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import logging


class CustomFormatter(logging.Formatter):

    indentation_level = [0]

    """
    custom formatter used to manage indentation in logging

    Attributes
    ----------
    _indentation_level : integer
        Current level of indentation
    """
    def format(self, record):
        if record.msg.startswith("-->"):
            if record.msg == "-->":
                self.indentation_level[0] = self.indentation_level[0] + 3
                return ""
            record.msg = " " * self.indentation_level[0] + record.msg[3:]
            self.indentation_level[0] = self.indentation_level[0] + 3
        elif record.msg.startswith("---"):
            record.msg = " " * (self.indentation_level[0] + 3) + record.msg[3:]
        elif record.msg == "<--":
            self.indentation_level[0] = self.indentation_level[0] - 3
            return ""
        elif record.msg.startswith("<--"):
            self.indentation_level[0] = self.indentation_level[0] - 3
            record.msg = " " * self.indentation_level[0] + record.msg[3:]
        else:
            record.msg = " " * self.indentation_level[0] + record.msg
        ret = super(CustomFormatter, self).format(record)
        ret = ret.replace("\n", "\n" + " " * self.indentation_level[0])
        ret = ret + "\n"
        return ret
