class Solution:
    def safe_reports(self, reports: List[List[int]]):
        ans = 0
        
        for report in reports:
            m = len(report)
            increasing = True
            for i in range(1, m):
                diff = report[i] - report[i - 1]
                if diff <= 0 or diff > 3:
                    increasing = False
                    break

            decreasing = True
            for i in range(1, m):
                diff = report[i - 1] - report[i]
                if diff <= 0 or diff > 3:
                    decreasing = False
                    break
            
            if decreasing or increasing:
                ans += 1
        
        return ans
      
    def is_damp(self, report: List[int]):
        m = len(report)
        increasing = True
        for i in range(1, m):
            diff = report[i] - report[i - 1]
            if diff <= 0 or diff > 3:
                increasing = False
                break

        decreasing = True
        for i in range(1, m):
            diff = report[i - 1] - report[i]
            if diff <= 0 or diff > 3:
                decreasing = False
                break
        
        if decreasing or increasing:
            return True
        return False

    def safe_reports_dampener(self, reports: List[List[int]]):
        ans = 0
        
        for report in reports:
            if self.is_damp(report):
                ans += 1
            else:
                m = len(report)
                for i in range(0, m):
                    d_report = report[:i]+report[i+1:]
                    if self.is_damp(d_report):
                        ans += 1
                        break
        return ans
