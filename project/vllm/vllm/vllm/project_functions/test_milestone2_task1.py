from collections import defaultdict
from typing import List

class PrefixStatsCollector:
    def __init__(self):
        self.total_requests = 0
        self.requests_with_hit = 0
        self.block_hit_counts = defaultdict(int)
        self.block_last_use_time = {}
        self.reuse_gaps = []

    def record_request(self, prompt: str, used_blocks: List[str], now: float):
        self.total_requests += 1
        if used_blocks:
            self.requests_with_hit += 1

        for block in used_blocks:
            self.block_hit_counts[block] += 1
            if block in self.block_last_use_time:
                gap = now - self.block_last_use_time[block]
                self.reuse_gaps.append(gap)
            self.block_last_use_time[block] = now

    def report(self):
        total_blocks = len(self.block_hit_counts)
        total_hits = sum(self.block_hit_counts.values())
        avg_reuse_count = total_hits / total_blocks if total_blocks > 0 else 0.0
        avg_reuse_gap = sum(self.reuse_gaps) / len(self.reuse_gaps) if self.reuse_gaps else 0.0
        hit_rate = self.requests_with_hit / self.total_requests if self.total_requests > 0 else 0.0

        summary = {
            "total_requests": self.total_requests,
            "requests_with_hit": self.requests_with_hit,
            "hit_rate": hit_rate,
            "average_block_reuse_count": avg_reuse_count,
            "average_reuse_time_gap": avg_reuse_gap,
        }

        print("PrefixStatsCollector Report:")
        for k, v in summary.items():
            print(f"{k}: {v}")

        return summary