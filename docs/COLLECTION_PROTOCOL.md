# Collection Protocol

For every acquisition campaign/session, record enough metadata to reproduce the acquisition context without revealing unnecessary personal information.

Minimum planned session metadata:

- anonymous `session_id`;
- date/time or privacy-preserving temporal representation;
- device ID/model;
- enabled sensors;
- building/floor coverage;
- acquisition mode (stationary fingerprint, walking trajectory, etc.);
- operator/participant anonymous ID if scientifically required;
- notable environmental conditions;
- known interruptions or sensor failures.

The final protocol must describe device placement/orientation, walking instructions, reference-point procedure, camera configuration, IMU rates, Wi-Fi scan behavior, cellular sampling behavior, and ground-truth acquisition.
