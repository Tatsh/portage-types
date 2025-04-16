<!-- markdownlint-configure-file {"MD024": { "siblings_only": true } } -->

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.6]

### Fixed

- Return value of `portage.dbapi.portdbapi.getFetchMap`

## [0.0.5]

### Fixed

- Fixed `dbapi`, `fd_types`, `mydo`, `prev_mtimes`, `settings`, `vartree` argument types in
  `portage.package.ebuild.doebuild.doebuild`

### Removed

- Removed deprecated `returnpid` argument from `portage.package.ebuild.doebuild.doebuild`

## [0.0.4]

### Added

- `portage.dbapi` exported from correct location `portage.dbapi`.
- `portage.doebuild` exported from correct location `portage.package.ebuild.doebuild.doebuild`.
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

[unreleased]: https://github.com/Tatsh/portage-stubs/-/compare/v0.0.5...HEAD
