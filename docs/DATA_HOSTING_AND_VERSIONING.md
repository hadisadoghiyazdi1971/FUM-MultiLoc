# Data Hosting and Versioning

## GitHub
Use GitHub for:

- benchmark specifications;
- schemas;
- loaders;
- evaluator;
- baseline source code;
- small sanitized examples;
- release manifests and checksums.

Do not use Git history as the primary store for multi-gigabyte image/sensor archives.

## Large data release
Large immutable releases should be stored using a suitable archival/dataset platform. The selected host should provide stable URLs, versioning, sufficient storage, and preferably a DOI or other persistent identifier.

## Git LFS
Git LFS is intentionally not enabled in v0.1.0. It may later be used for a small number of versioned binary artifacts, but it should not become the primary distribution mechanism for the full vision corpus.

## Release immutability
Each public benchmark release should have:

- semantic version;
- manifest listing all distributed files;
- file sizes;
- cryptographic checksums;
- schema/protocol version;
- archive/DOI reference.
