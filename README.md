# How certain is a tool leaderboard's top rank?

A compact statistical note on Armature's public [AI-search leaderboard](https://armature.tech/leaderboards/ai-search), updated September 29, 2026. The page reports **639** judged sessions: **92** Exa picks and **89** Brave Search API picks, and itself describes them as tied at about 14%.

Run `python3 experiment.py` (standard library only). Treating sessions as independent draws with a single winner, Exa's lead is **0.469 percentage points**. An illustrative normal 95% interval for Exa minus Brave is **−3.66 to +4.60 points**; a conditional two-sided binomial calculation gives **p = 0.8819** under equal pick probability. These are descriptive computations from the published aggregate counts, not a test of Armature's scoring code or a correction to its stated tie.

The **independence assumption is weak**: sessions share repositories, agents, prompts, and personas. The aggregate counts cannot identify a cluster-aware interval. The sharper question is how much ranking confidence changes when one resamples at the repository or task level instead of the run level. The public per-run board could support that follow-up if its run-level metadata are exported.

Sources: [YC profile and founders](https://www.ycombinator.com/companies/armature), [AI-search leaderboard and method](https://armature.tech/leaderboards/ai-search).
