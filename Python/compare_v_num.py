__author__ = 'ZHIXU'

# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.


class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        if not isinstance(version1, str) or not isinstance(version2, str):
            return
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        flag = 0
        if len(v1_list) >= len(v2_list):
            for i in xrange(len(v2_list)):
                num1 = int(v1_list[i])
                num2 = int(v2_list[i])
                if num1 > num2:
                    flag = 1
                    break
                elif num1 < num2:
                    flag = -1
                    break
                if i == len(v2_list)-1 and len(v1_list)>len(v2_list):
                    for j in xrange(i+1, len(v1_list)):
                        num = int(v1_list[j])
                        if num != 0:
                            flag = 1
                            break
        else:
            for i in xrange(len(v1_list)):
                num1 = int(v1_list[i])
                num2 = int(v2_list[i])
                if num1 > num2:
                    flag = 1
                    break
                elif num1 < num2:
                    flag = -1
                    break
                if i == len(v1_list)-1 and len(v2_list)>len(v1_list):
                    for j in xrange(i+1, len(v2_list)):
                        num = int(v2_list[j])
                        if num != 0:
                            flag = -1
                            break
        return flag


if __name__ == '__main__':
    version1 = '1'
    version2 = '1.0'
    sol = Solution()
    print(sol.compareVersion(version1, version2))