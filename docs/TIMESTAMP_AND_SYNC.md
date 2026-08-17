# Timestamp and Synchronization Specification

Multimodal benchmarking requires an explicit time model.

The final release must specify for every modality:

- timestamp source;
- unit (recommended canonical unit: integer nanoseconds);
- epoch/reference;
- monotonic vs wall-clock behavior;
- device clock domain;
- known offsets;
- clock drift correction;
- synchronization method;
- maximum/typical residual alignment error.

The master sample index should never rely on file ordering alone for synchronization.
