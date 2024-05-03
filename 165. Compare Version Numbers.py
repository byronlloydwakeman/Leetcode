class Solution:    
    def compareVersion(self, version1: str, version2: str) -> int:
        def fill_with_zeros(array, length):
            # Iterate over the range from 0 to the given length
            for _ in range(length - len(array)):
                # Append 0 to the array
                array.append(0)

        version1_versions = version1.split(".")
        version2_versions = version2.split(".")

        if len(version1_versions) < len(version2_versions):
            fill_with_zeros(version1_versions, len(version2_versions))
        elif len(version1_versions) > len(version2_versions):
            fill_with_zeros(version2_versions,len(version1_versions))

        print(version1_versions)
        print(version2_versions)

        for index in range(min(len(version1_versions), len(version2_versions))):
            if int(version1_versions[index]) > int(version2_versions[index]):
                return 1
            elif int(version1_versions[index]) < int(version2_versions[index]):
                return -1
            
        return 0
