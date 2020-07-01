#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Output: [5,10]
#

class Solution():
    def kill(self, pid, ppid, kill_id):
        self.result = [kill_id]
        kill_ids = [kill_id]
        children = {}

        for i in range(len(pid)):
            parent = ppid[i]
            keys = children.keys()
            if parent in keys:
                children[parent].append(pid[i])
            else:
                child = pid[i]
                children[parent] = [child]

        keys = children.keys()
        
        for id in kill_ids:
            if id not in keys:
                continue 
            else:
                self.result += children[id]
                kill_ids += children[id]

        return self.result

def main():
    pid = [1, 3, 10, 5, 7, 14]
    ppid = [3, 0, 5, 3, 10, 7]
    kill_id = 5
    
    x = Solution()

    print(x.kill(pid, ppid, kill_id))


main()




























    
