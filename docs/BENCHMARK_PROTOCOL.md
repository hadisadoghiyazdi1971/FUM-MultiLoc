# Benchmark Protocol

The first stable release should define fixed inputs, outputs, splits, and metrics for each supported task.

## T1 — Floor classification
Input: one or more supported modalities.
Output: `floor_id`.
Primary metric: accuracy. Secondary metrics may include macro-F1.

## T2 — Room / zone recognition
Output: `room_id` and/or `zone_id` depending on release policy.
Metrics: accuracy and macro-F1.

## T3 — Metric localization
Output: position in the benchmark's local metric coordinate system.
Required metrics should include median error, mean error, RMSE, and selected error percentiles.

## T4 — IMU trajectory estimation
Input: IMU sequence, plus only the initialization information explicitly allowed by the protocol.
Output: trajectory.
Trajectory metrics must be finalized before v1.0.

## T5 — Visual localization
Input: image/frame or allowed image sequence.
Output: metric position and, if supported, orientation.

## T6 — Wi-Fi + IMU fusion
Input: synchronized Wi-Fi and inertial observations.
Output: position/trajectory.

## T7 — Full multimodal localization
Input: the modalities explicitly enabled in the selected benchmark track.
Output: position/trajectory and optional semantic location.

## T8 — Missing-modality robustness
Evaluate a model trained/defined under a declared modality set when one or more modalities are unavailable or degraded.

## General rules to finalize
- exact train/validation/test policy;
- allowed external training data;
- test-label visibility;
- per-sample vs per-trajectory aggregation;
- handling of missing sensor frames;
- confidence/uncertainty outputs;
- deterministic evaluator implementation.
