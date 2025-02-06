# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        outimg = []
        row = len(img)
        col = len(img[0])
        
        for i in range(row):
            o = []
            for j in range(col):
                sum, count = 0, 0
                rowup = max(0, i - 1)
                rowdown = min(i + 1, row)
                colleft = max(0, j - 1)
                colright = min(j + 1, col)
                for k in range(rowup, min(rowdown + 1, row)):
                    for l in range(colleft, min(colright + 1, col)):
                        sum += img[k][l]
                        count += 1
                o.append(sum // count)
            outimg.append(o)
        
        return outimg

                