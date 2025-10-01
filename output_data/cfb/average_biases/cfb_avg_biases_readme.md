## Output Files in average_biases

### 1. `voter_team_biases.csv`
**Description:** Average bias metrics for each voter-team pair across all seasons.

**Columns:** voter, team, bias1-a, bias1-b, bias1-c, bias2-a, bias2-b, bias2-c, bias3-a, bias3-b, bias3-c

### 2. `season_team_biases.csv`
**Description:** Average bias metrics for each season-team pair across all voters.

**Columns:**
season, conference, bias1-a, bias1-b, bias1-c, bias2-a, bias2-b, bias2-c, bias3-a, bias3-b, bias3-c

### 3. `season_voter_conference_biases.csv`
**Description:** Average bias metrics for each season-voter-conference combination (averaged over all teams in the conference).

**Columns:**
season, voter, conference, bias1-a, bias1-b, bias1-c, bias2-a, bias2-b, bias2-c, bias3-a, bias3-b, bias3-c

### 4. `voter_conference_biases.csv`
**Description:** Average bias metrics for each voter-conference pair across all seasons (same as #3 but also averaged over seasons).

**Columns:**
voter, conference, bias1-a, bias1-b, bias1-c, bias2-a, bias2-b, bias2-c, bias3-a, bias3-b, bias3-c
