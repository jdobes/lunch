# CHANGELOG


## v1.6.0 (2025-05-06)

### Features

- **api**: Send day and url when requesting menus
  ([`5d36fcf`](https://github.com/jdobes/lunch/commit/5d36fcf7ae82c823eaf9e5432c67eb73da847e51))

This change is later used on the frontend, where we display metadata about menu

Signed-off-by: Filip Mudry <fmudry@redhat.com>

- **web**: Display metadata (date and url) of a menu details
  ([`4366ea5`](https://github.com/jdobes/lunch/commit/4366ea58bda123735bb68c3d8f0d245924d5a4c4))

This should offer an easy way to verify that a menu is valid

Signed-off-by: Filip Mudry <fmudry@redhat.com>


## v1.5.4 (2025-05-06)

### Bug Fixes

- Non-root user in container permissions
  ([`69a928a`](https://github.com/jdobes/lunch/commit/69a928aecdac51312d85bc2f3cfd554434d91188))


## v1.5.3 (2025-02-04)

### Bug Fixes

- Switch rubin to menicka
  ([`b696124`](https://github.com/jdobes/lunch/commit/b6961243ecf2931ac0c20cb9728b5f93deced745))


## v1.5.2 (2025-01-27)

### Bug Fixes

- Parse Qwerty restaurant from their website
  ([`e8e0a11`](https://github.com/jdobes/lunch/commit/e8e0a11270a7b82dccf6939a7c8e54664c6ba658))


## v1.5.1 (2025-01-07)

### Bug Fixes

- Seems that pytz now needs to be explicitly required
  ([`e900222`](https://github.com/jdobes/lunch/commit/e90022218a7f9da062e18459c8f1c144d2b5706f))


## v1.5.0 (2024-11-10)

### Features

- **web**: Support user location
  ([`f42f1e3`](https://github.com/jdobes/lunch/commit/f42f1e363ace18d463d9be50df41b7d7cda27776))


## v1.4.0 (2024-11-06)

### Features

- **web**: Sort by distance
  ([`c6c30d7`](https://github.com/jdobes/lunch/commit/c6c30d71cb2fa75d8d3b3cdce7cf2c9e4aafc4e0))


## v1.3.0 (2024-11-04)

### Chores

- Bump npm to match dev env
  ([`1337919`](https://github.com/jdobes/lunch/commit/1337919ef5787dad702d613b1e8fa6fd365b3b85))

- **web**: Update libs
  ([`d3f6e8d`](https://github.com/jdobes/lunch/commit/d3f6e8d5eb1ec4814aea34c05957d48e100fd148))

### Features

- **web**: Implement dark mode
  ([`951ad93`](https://github.com/jdobes/lunch/commit/951ad93fe5f8f49f68f5923143435a9143acf62d))


## v1.2.1 (2024-11-03)

### Bug Fixes

- **web**: Scaling on mobile
  ([`979b69b`](https://github.com/jdobes/lunch/commit/979b69b4135517b62c668d63f55f45424dbcd0be))


## v1.2.0 (2024-11-03)

### Bug Fixes

- Google maps say vitalite is closed
  ([`f267b89`](https://github.com/jdobes/lunch/commit/f267b896134d1957b345bf347b80347b1ee277f4))

### Features

- **api**: Return location of restaurants and the office
  ([`0cc3d5c`](https://github.com/jdobes/lunch/commit/0cc3d5c3e1bbedf5772cfac80e65b31320c21bc8))

- **web**: Add distance chips
  ([`9743412`](https://github.com/jdobes/lunch/commit/9743412280a74dc4523c8391b295a06b20a5f6e6))


## v1.1.0 (2024-11-03)

### Features

- Add alvin
  ([`cd003cf`](https://github.com/jdobes/lunch/commit/cd003cf5294c5c2490b64e11fdd1c3c5fd4ec578))

- **qwerty**: Include weekly menu
  ([`0d20a29`](https://github.com/jdobes/lunch/commit/0d20a299b93004b9a45b57abb8712d2900d60928))


## v1.0.1 (2024-07-09)

### Bug Fixes

- **qwerty, sesamo**: Facebook changed generated HTML
  ([`6f8abb9`](https://github.com/jdobes/lunch/commit/6f8abb90cb842f37108a752635e52bf26b0e0609))


## v1.0.0 (2024-07-09)

### Bug Fixes

- **restaurants**: Rubin from their site
  ([`de46d69`](https://github.com/jdobes/lunch/commit/de46d698b7721b15765e0e6918509437374b5de5))

### Features

- Add Rubin
  ([`24295b3`](https://github.com/jdobes/lunch/commit/24295b36dea6391a8bdf9e53c569aad4167cb663))

- Enable python-semantic-release
  ([`6d1cf89`](https://github.com/jdobes/lunch/commit/6d1cf8997f3be3503585af6e7664d0fb7e209499))
