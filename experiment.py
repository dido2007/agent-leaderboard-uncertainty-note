#!/usr/bin/env python3
"""Recompute a descriptive uncertainty bound from Armature's public AI-search counts."""
import json
import math

# Frozen public leaderboard snapshot, updated 2026-09-29.
SOURCE = 'https://armature.tech/leaderboards/ai-search'
n, exa, brave = 639, 92, 89
p_exa, p_brave = exa/n, brave/n
diff = p_exa-p_brave
# Each run has one winner. X=1 for Exa, -1 for Brave, 0 otherwise.
se = math.sqrt((p_exa+p_brave-diff*diff)/n)
ci = [diff-1.96*se, diff+1.96*se]
# Under equal chance among the two, condition on 181 runs choosing either.
m = exa+brave
k = min(exa, brave)
p_two_sided = min(1.0, 2*sum(math.comb(m, i) for i in range(k+1))/2**m)
report = {'source': SOURCE, 'source_snapshot_date': '2026-09-29',
          'total_runs': n, 'exa_wins': exa, 'brave_wins': brave,
          'exa_minus_brave_percentage_points': round(100*diff, 3),
          'iid_normal_95pct_interval_percentage_points': [round(100*x, 2) for x in ci],
          'conditional_two_sided_binomial_p': round(p_two_sided, 4),
          'caveat': 'Descriptive iid calculation only; sessions share codebases, agents and personas. Aggregates cannot identify a cluster-aware interval.'}
assert sum(ci)/2 == diff
assert ci[0] < 0 < ci[1]
print(json.dumps(report, indent=2))
