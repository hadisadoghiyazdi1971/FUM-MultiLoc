# Vision Modality

The full visual corpus may be several gigabytes and should not be stored directly in this Git repository.

Recommended future release design:

- lightweight `vision_index` table linking `vision_ref` to session/timestamp/archive/path;
- immutable image shards on the dataset host;
- sanitized public images only;
- a small reviewed example subset in `examples/` if useful.

See `../schemas/vision.schema.json` and `../docs/PRIVACY_AND_ANONYMIZATION.md`.
