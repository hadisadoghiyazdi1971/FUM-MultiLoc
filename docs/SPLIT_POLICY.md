# Split Policy

Random sample-level splitting is discouraged when adjacent observations are highly correlated.

Candidate split tracks include:

- session-independent;
- trajectory-independent;
- day-independent;
- device-independent;
- user/operator-independent where relevant;
- environment-change / temporal-generalization.

The final benchmark must state the grouping unit used to prevent leakage. Test sets should not share near-duplicate visual frames or temporally adjacent sensor windows with training data unless the task explicitly studies that setting.
