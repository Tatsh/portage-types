<!-- markdownlint-configure-file {"MD024": { "siblings_only": true } } -->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `portage.dbapi` exported from correct location `portage.dbapi.dbapi`.
- `portage.doebuild` exported from correct location `portage.package.ebuild.doebuild`.
- `portage.config` exported from correct location `portage.package.ebuild.config.config`.
- `'unpack'` as a valid `mydo` argument to `doebuild`.
- `portage.dbapi.portagetree.dbapi`
- `portage.dbapi.portdbapi.getFetchMap`
- `portage.versions._pkg_str`

### Fixed

- Corrected return value of `portage.versions.catpkgsplit`.
- Corrected argument names of `portage.versions.vercmp`.
- Corrected argument names of `portage.versions.catpkgsplit`.

### Removed

- Removed fake class `Config`. Use `config` instead.

[unreleased]: https://github.com/Tatsh/portage-stubs/-/compare/v0.0.4...HEAD
