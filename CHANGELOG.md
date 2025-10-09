# CHANGELOG

<!-- version list -->

## v1.8.0 (2025-10-09)

### Features

- Add Bistro Šindelář and K2
  ([`84fc677`](https://github.com/jdobes/lunch/commit/84fc677cd5668621fcd81c73a48bdaee38d9f5e0))


## v1.7.7 (2025-10-02)

### Bug Fixes

- Branding update
  ([`54c712f`](https://github.com/jdobes/lunch/commit/54c712f9935fd3562fa454fdf8a16e6b9a845595))


## v1.7.6 (2025-06-17)

### Bug Fixes

- Tag detection on last commit
  ([`891ed4a`](https://github.com/jdobes/lunch/commit/891ed4a39f976246cc61713c3e97ae294aedac39))


## v1.7.5 (2025-06-17)

### Bug Fixes

- Connexion 3
  ([`9cdd197`](https://github.com/jdobes/lunch/commit/9cdd197060ca964fcb73b36e0890ea345bfad30f))


## v1.7.4 (2025-06-17)

### Bug Fixes

- Update semantic-release
  ([`aa90e89`](https://github.com/jdobes/lunch/commit/aa90e89a966cc0f098783fc568ad0b7d85a3793e))

### Continuous Integration

- Rebuild only latest if tag not on the last commit
  ([`1b7405d`](https://github.com/jdobes/lunch/commit/1b7405d3a2b81538119269f063d1ccb342c52202))


## v1.7.3 (2025-06-16)

### Bug Fixes

- Restaurant naming
  ([`69a47f8`](https://github.com/jdobes/lunch/commit/69a47f859eab0df2eada024fc76e730f61371708))

- Use shorter day names on small displays
  ([`09ad9aa`](https://github.com/jdobes/lunch/commit/09ad9aabfdb9fba79e43b5ef07fdf688106cbbfb))

### Chores

- Ubi10 and nodejs 22
  ([`5e92f87`](https://github.com/jdobes/lunch/commit/5e92f87c4cd74a19b431f076052912c08fa7f091))

- Update frontend deps
  ([`dda725d`](https://github.com/jdobes/lunch/commit/dda725d0d6be47ca7b0cbdc05b46245a6efc5a3e))

- Update readme
  ([`69176b9`](https://github.com/jdobes/lunch/commit/69176b97f09fb880a5e804d12e024642add1a032))

### Continuous Integration

- Need tags
  ([`7b42f39`](https://github.com/jdobes/lunch/commit/7b42f39056f6a1072b81ca823769e6a75ec7f82d))

- Rebuild last tag if needed
  ([`f1fd165`](https://github.com/jdobes/lunch/commit/f1fd165ea92d729ef8f1882e60461f2a2952d137))

### Refactoring

- Remove docker-compose with single service
  ([`3379714`](https://github.com/jdobes/lunch/commit/3379714b0b8f1f5f3a07077773564e93e2595ee2))


## v1.7.2 (2025-06-15)

### Bug Fixes

- Get sesamo from menicka
  ([`96f7df6`](https://github.com/jdobes/lunch/commit/96f7df65423b50a17fa06661ec302dcb1dca74e9))

- Nepal has new page
  ([`6bc8360`](https://github.com/jdobes/lunch/commit/6bc8360d4cb6e66ceba103bca75a044da9f00191))

- Spravne misto doesn't exist anymore
  ([`18e9667`](https://github.com/jdobes/lunch/commit/18e9667fa9baed96d24a0e1aa475110a9ca39c43))

### Chores

- Publish image to ghcr.io
  ([`611d682`](https://github.com/jdobes/lunch/commit/611d682f6a5839a3dd8da63e5b09a5b7d8349150))

- Ubi10, python312, remove playwright
  ([`d333425`](https://github.com/jdobes/lunch/commit/d333425e9155c0501477b6c964dca42ecf9a33e3))

### Refactoring

- Remove nginx
  ([`ef71f9c`](https://github.com/jdobes/lunch/commit/ef71f9c44ebcbc183a2106c527a2d980291db5b1))


## v1.7.1 (2025-05-26)

### Bug Fixes

- Python-semantic-release v10 contains various breaking changes, lock for now
  ([`1e2d30d`](https://github.com/jdobes/lunch/commit/1e2d30d319da0bcb76a0dd3853a54e7696460be4))


## v1.7.0 (2025-05-26)

### Features

- **api**: Calculate first day of the week for menu deletion
  ([`62915f0`](https://github.com/jdobes/lunch/commit/62915f0b99de703ef2bec45b1f2157dcc4aac116))

- **web**: Add day selection for restaurant menus
  ([`30f5e30`](https://github.com/jdobes/lunch/commit/30f5e306639c2510e9e3426ff17cb647955ae858))

- **web**: Set default selected day to monday if it's saturday/sunday
  ([`c3ab59c`](https://github.com/jdobes/lunch/commit/c3ab59c62cff50022b5cfde59ad827050b2bd045))


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
