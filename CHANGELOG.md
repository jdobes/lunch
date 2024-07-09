# CHANGELOG

## v1.0.1 (2024-07-09)

### Fix

* fix(qwerty, sesamo): Facebook changed generated HTML ([`6f8abb9`](https://github.com/jdobes/lunch/commit/6f8abb90cb842f37108a752635e52bf26b0e0609))

## v1.0.0 (2024-07-09)

### Feature

* feat: Enable python-semantic-release ([`6d1cf89`](https://github.com/jdobes/lunch/commit/6d1cf8997f3be3503585af6e7664d0fb7e209499))

* feat: add Rubin ([`24295b3`](https://github.com/jdobes/lunch/commit/24295b36dea6391a8bdf9e53c569aad4167cb663))

### Fix

* fix(restaurants): Rubin from their site ([`de46d69`](https://github.com/jdobes/lunch/commit/de46d698b7721b15765e0e6918509437374b5de5))

### Unknown

* hostname has to resolvable, and some real value is only needed in local env ([`1317faa`](https://github.com/jdobes/lunch/commit/1317faa059424fe26fbadeb2f1911146f6e16a1e))

* add Moravia

closes #52 ([`d8ee915`](https://github.com/jdobes/lunch/commit/d8ee91576bbe82e957790e4396fe2203dd7ee0fe))

* add more empty states ([`4481768`](https://github.com/jdobes/lunch/commit/4481768c8cb32e7be0f57bcefbf576815b898c41))

* parse jeanpauls from pdf ([`7ade9c1`](https://github.com/jdobes/lunch/commit/7ade9c12ef2f699b23e1ae83034060a485e85074))

* filter out empty responses from menicka ([`c29a48b`](https://github.com/jdobes/lunch/commit/c29a48b8be6bb946db0261aa17765c08210b2a81))

* sesamo stopped publishing to website, use facebook to get latest menu

unfortunately the format is different every week ([`689cd75`](https://github.com/jdobes/lunch/commit/689cd752495304341267ea758f23fb3f53dd2ae5))

* don&#39;t clear the menu when it&#39;s removed from the page on the same day

remove it the next day ([`1f2208a`](https://github.com/jdobes/lunch/commit/1f2208a3e451318ea744eef5ed5f37b093158486))

* add http proxy support ([`98f7165`](https://github.com/jdobes/lunch/commit/98f71650b22333b4bed870b3569f9dbd35277c72))

* switch to firefox for playwright

chromium doesn&#39;t seem to run in k3s on arm64, this is easiest workaround

can&#39;t use distro firefox because playwright works only with custom firefox build ([`da0c35e`](https://github.com/jdobes/lunch/commit/da0c35e52bda71e91824cfaeef7a6e5a82c1aa48))

* add qwerty ([`4166d65`](https://github.com/jdobes/lunch/commit/4166d65863e6c247a5005922f4c6e4d016ae3a4b))

* simplify multi-arch build - build react app assets once

build final image without node bloat ([`881c5bc`](https://github.com/jdobes/lunch/commit/881c5bc59be92f36929802959906056f016491ff))

* diacritics ([`5935026`](https://github.com/jdobes/lunch/commit/593502604ea96feb11c9fc3171a4dc360d1fc6e9))

* build and push images ([`b9cb94f`](https://github.com/jdobes/lunch/commit/b9cb94f6eaffc5438a2aec74f3028df7b5d27697))

* add restaurants near tpb ([`8c29828`](https://github.com/jdobes/lunch/commit/8c298286336004ee16df60600b9fa93218749571))

* tzdata need to now explicitly required otherwise apscheduler initialization fails ([`47ab2df`](https://github.com/jdobes/lunch/commit/47ab2df2d4362697801bb800471a2731202cd40f))

* fix roayal nepal ([`a617895`](https://github.com/jdobes/lunch/commit/a617895c5fe48110e698a92ce877be7b728cf98b))

* fix nepal ([`98e4fc2`](https://github.com/jdobes/lunch/commit/98e4fc21ec09d8c0f09f455adf91c689f60ebabb))

* fix portoriko and padthai ([`bd12915`](https://github.com/jdobes/lunch/commit/bd129153a2dc8d91043ac847bfa5dc04488e073b))

* Drop u Hrebicku as it got closed ([`b74dc46`](https://github.com/jdobes/lunch/commit/b74dc469c7c1acde16b1b49186f4ff039a092474))

* fix sesamo ([`d07cf44`](https://github.com/jdobes/lunch/commit/d07cf4498194b468f595446cbb6b998c3092dfb1))

* remove zomato ([`eb13202`](https://github.com/jdobes/lunch/commit/eb132026a3dce7ab0ea8fab8aa5e540068cf5154))

* change to cron scheduler ([`9b22bb6`](https://github.com/jdobes/lunch/commit/9b22bb6c333c7fbbf454b36a9534d872eac77eb6))

* upgrade to MUI 5 ([`84b4920`](https://github.com/jdobes/lunch/commit/84b492000c2403be0ebe6a367954f355517c0760))

* Fix nepalese restaurant namings ([`0f0e661`](https://github.com/jdobes/lunch/commit/0f0e66108a3d8197621426418da0ff5e38a047ff))

* add royal nepal ([`cfbe4e5`](https://github.com/jdobes/lunch/commit/cfbe4e51d74f3f6a1f9400ab5503b189431bafce))

* add jeanpauls and sesamo ([`923c7d2`](https://github.com/jdobes/lunch/commit/923c7d2051f53aa4628dccce5479aa49f441dfed))

* remove alergens ([`5759b30`](https://github.com/jdobes/lunch/commit/5759b306355e3a6cc8261186ada04527e5cb6cd5))

* add uhrebicku ([`5f94d83`](https://github.com/jdobes/lunch/commit/5f94d830cf029a61df1c1693d1067124d05dd2b6))

* add podman build instructions ([`caad4f5`](https://github.com/jdobes/lunch/commit/caad4f5a489e404cbf228a83186b551a2157d570))

* update velorex name ([`e575b78`](https://github.com/jdobes/lunch/commit/e575b78ed5d32289fc27e11c7290fde1ebf9076a))

* Update velorex.py ([`f7e8ccc`](https://github.com/jdobes/lunch/commit/f7e8ccc8dbafebdeb4addc7a90766f85d739b268))

* delete taste of india ([`286c6cd`](https://github.com/jdobes/lunch/commit/286c6cd8e7cbd550479ec96d5507f2e7818efeb0))

* add docker-compose ([`f0c9d20`](https://github.com/jdobes/lunch/commit/f0c9d207eac41e56f6bff749df03a06ea05392c6))

* fix nepal ([`62540c8`](https://github.com/jdobes/lunch/commit/62540c895922d0fdbe8567dfa193771ff5974d8d))

* migrate many restaurants to menicka ([`1d60fc4`](https://github.com/jdobes/lunch/commit/1d60fc4c6b605fa282886d4e00129b1e273620d0))

* delete liquid bread ([`d16aefa`](https://github.com/jdobes/lunch/commit/d16aefa5bd3baf9e3ac957962275e591642006b0))

* fix timestamp ([`d7f1859`](https://github.com/jdobes/lunch/commit/d7f185977143687a55435c5ed33bfb5a27a999e4))

* update deps ([`10a287d`](https://github.com/jdobes/lunch/commit/10a287d7fbf0de777b0298aa947bca7708b01218))

* release ([`f11da9a`](https://github.com/jdobes/lunch/commit/f11da9aea34880c6806705f97eb3e784b8e995bf))

* better fix ([`672d3d9`](https://github.com/jdobes/lunch/commit/672d3d92ead6ea25f05a84cbe5144d74faea63d5))

* fix nepal ([`75c4bd8`](https://github.com/jdobes/lunch/commit/75c4bd878e3bf7b8c9241eca7cda65acdc2b8a33))

* fix missing function in python 3.6 ([`fb8061c`](https://github.com/jdobes/lunch/commit/fb8061c1dcf96356d4c315b83cbd6ceac0623b21))

* no need to do in this svc ([`3eccfcd`](https://github.com/jdobes/lunch/commit/3eccfcd454add3122b82a88dc4f182a3fd6cb37b))

* setup nginx proxy and podman pod to make routing to web and api container work ([`ffa314b`](https://github.com/jdobes/lunch/commit/ffa314b3f34b04e8bc93a52bbb2553ff9e41321b))

* show warning in dev env ([`a861f3a`](https://github.com/jdobes/lunch/commit/a861f3a49967644df35ef508402f4e1ba9a95def))

* free some space ([`31da642`](https://github.com/jdobes/lunch/commit/31da642acd98d00766198f49523407435bdf55d1))

* fix build errors ([`6ceeacd`](https://github.com/jdobes/lunch/commit/6ceeacd0df9ddf63306b401d5d1a28ceabb18ccd))

* run with -it until permissions are fixed

https://bugzilla.redhat.com/show_bug.cgi?id=1786449 ([`d6f5a7a`](https://github.com/jdobes/lunch/commit/d6f5a7a92618a34458731348c6239866b4181f3e))

* reduce size using ubi-minimal ([`d58df79`](https://github.com/jdobes/lunch/commit/d58df79f8bd772e5e37c34bc85b6c3897a36ee08))

* fix readme ([`c34a560`](https://github.com/jdobes/lunch/commit/c34a5605c203edb21fae92380203deb6f1b35c19))

* split services (need to resolve nginx logging yet) ([`ac2d926`](https://github.com/jdobes/lunch/commit/ac2d9269ffb3634b18254183ea9d12e2f3b6e12a))

* update deps ([`4f38fc6`](https://github.com/jdobes/lunch/commit/4f38fc6ced1605364532340bca73a7a6214ced4c))

* switch to centos 8 and reduce image size ([`c2996bb`](https://github.com/jdobes/lunch/commit/c2996bb65156e71ac6ae43543e83b2f905bc3151))

* fix velorex ([`b3956e1`](https://github.com/jdobes/lunch/commit/b3956e1eccab70ea5c718182cb35dfde16f916d2))

* fix parsers ([`808c174`](https://github.com/jdobes/lunch/commit/808c174795103c6d2f812fcd1c529e17a970f324))

* add timestamp ([`5dc66b5`](https://github.com/jdobes/lunch/commit/5dc66b5a7c908f6baa19f69dd53d0b5047655d23))

* continue parsing other modules in case of exception ([`32e1aa2`](https://github.com/jdobes/lunch/commit/32e1aa2cd84a69f00bac2122d7e0acd105c60a9b))

* Bump eslint-utils from 1.4.0 to 1.4.3 in /web

Bumps [eslint-utils](https://github.com/mysticatea/eslint-utils) from 1.4.0 to 1.4.3.
- [Release notes](https://github.com/mysticatea/eslint-utils/releases)
- [Commits](https://github.com/mysticatea/eslint-utils/compare/v1.4.0...v1.4.3)

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`8f150eb`](https://github.com/jdobes/lunch/commit/8f150eb18f1ef1c362168f5960b8845972b624ec))

* fix liquid bread ([`6741846`](https://github.com/jdobes/lunch/commit/6741846ac9c5f9569bfe79060934d692fd2833a1))

* fix purkynka ([`27401e2`](https://github.com/jdobes/lunch/commit/27401e2ac30011cc5a4002fff8bb8a3f87ce038e))

* use a more precise name ([`788c5b6`](https://github.com/jdobes/lunch/commit/788c5b6fca62f7f28aad83a13ef09bdbf5f7e3ed))

* add taste of india ([`508df65`](https://github.com/jdobes/lunch/commit/508df65932500d47d4c1587f5c69167bcb708fd2))

* add liquid bread ([`940e2df`](https://github.com/jdobes/lunch/commit/940e2dfde675939452ddf0f78e4261037d902163))

* add comment ([`2fd2c0a`](https://github.com/jdobes/lunch/commit/2fd2c0a1279b69ef84af3dd026b39123e0dc9060))

* add purkynka ([`febf9ec`](https://github.com/jdobes/lunch/commit/febf9ec0721448a7d555140e0a6dc23adc67f29a))

* add nepal ([`6496706`](https://github.com/jdobes/lunch/commit/6496706b29797d2af659d5f79346bb5a6a450b2d))

* skip earlier days while syncing and remove empty lines ([`e26abb8`](https://github.com/jdobes/lunch/commit/e26abb8ef92511dd1ff0bd2f0984f81f65afac91))

* parse zomato restaurants ([`f442bb6`](https://github.com/jdobes/lunch/commit/f442bb6a77129c46cc051773ba64304b32b4fa76))

* replace newlines with &lt;br/&gt; ([`2e3f672`](https://github.com/jdobes/lunch/commit/2e3f67298ac3e269b2cb3b18f2fc7e36fe37bfe5))

* set utf-8 encoding, it&#39;s not set by default ([`8e8d46f`](https://github.com/jdobes/lunch/commit/8e8d46fbacd04834c9b57d914dbdfbd11834ce45))

* define API url if running UI using npm start ([`4f81fd8`](https://github.com/jdobes/lunch/commit/4f81fd8d95a8a83f4997221b0cf18d0d610722fa))

* fetch both APIs at once, combine results, display ([`453292f`](https://github.com/jdobes/lunch/commit/453292fa53a0cb8b21195f9efe9d5ef37da55bb1))

* change footer ([`9d9caa9`](https://github.com/jdobes/lunch/commit/9d9caa93c60908d12c9e17a8f3eb9b5d64e674dc))

* allow CORS ([`26f6909`](https://github.com/jdobes/lunch/commit/26f6909d7ac9f4dceabaf4c19e32eea6618b9e78))

* split to more components ([`2a80f34`](https://github.com/jdobes/lunch/commit/2a80f34735fd52c9da0689f168f5cd82729d4d90))

* run sync every 6 hours by default ([`226f99d`](https://github.com/jdobes/lunch/commit/226f99dbb71415c1d8af106fd096edc08ea50b4d))

* add favicon ([`819ebf4`](https://github.com/jdobes/lunch/commit/819ebf4e5877f692d8d9cd30e14a2e3ec01161ff))

* add simple web draft and remove unused stuff ([`61b3c6f`](https://github.com/jdobes/lunch/commit/61b3c6fe06ee8d68fdbb9aae1783bf47f6536754))

* update dependencies ([`b770d11`](https://github.com/jdobes/lunch/commit/b770d1144428c2184c4e77a714536e6fce38cc13))

* add material-ui to dependencies ([`29775fc`](https://github.com/jdobes/lunch/commit/29775fcd6e2b1a3ef637f8c5c5222831933d629a))

* rename app ([`3547085`](https://github.com/jdobes/lunch/commit/35470856354e9df37b18c723baad8059db270e1e))

* move python gitignore to api dir ([`50eb195`](https://github.com/jdobes/lunch/commit/50eb195fc4468b5cbf8aa4cf02434275d4ebfc8c))

* rename git structure ([`adbf584`](https://github.com/jdobes/lunch/commit/adbf584f1ab01b20ba0c52809dd1c3261b1d6abf))

* serve react app from connexion app ([`74f65b4`](https://github.com/jdobes/lunch/commit/74f65b428561d76e3899d22210c53c06623326f2))

* add react template ([`65a66e7`](https://github.com/jdobes/lunch/commit/65a66e70be9b3145bebc2ed995a07ce7dc27e4fe))

* rename api directory ([`a59ee26`](https://github.com/jdobes/lunch/commit/a59ee268722ba9e4c8cf0b6359e90c9e2316b320))

* fix select ([`1957203`](https://github.com/jdobes/lunch/commit/195720377f6b8c9b43cf92d84e5cbc74b157865c))

* add more restaurants ([`8f43cd4`](https://github.com/jdobes/lunch/commit/8f43cd4bfd4e402a9a55ed27b0cb99830069faa4))

* support getting menus ([`e56af7d`](https://github.com/jdobes/lunch/commit/e56af7d68cff7a964dabe644934e461df31816ae))

* add url to response ([`0ab0527`](https://github.com/jdobes/lunch/commit/0ab0527617923cca187084b20532751ec9668cff))

* improve date parsing and deleting old menus ([`62ab90b`](https://github.com/jdobes/lunch/commit/62ab90b2ea98e08bd40823172769c13da236370d))

* upsert to avoid unique constraint violation ([`8dea613`](https://github.com/jdobes/lunch/commit/8dea6131799dc6260b68c599800b4d97240c3f9e))

* add unique constraint ([`355777e`](https://github.com/jdobes/lunch/commit/355777e416fc6a56f9bbfb87caf180346ec9e096))

* parse and store draft ([`589c18b`](https://github.com/jdobes/lunch/commit/589c18bdc6ecb58be9f1af8034ff226a95015d12))

* download page with menu ([`b3cc05c`](https://github.com/jdobes/lunch/commit/b3cc05ca2cfc2db4379638c28f66d56f448eecec))

* include restaurant name ([`db90656`](https://github.com/jdobes/lunch/commit/db906569871d820ed8353ddcc7eb552072446888))

* save imported module ([`fcfedcc`](https://github.com/jdobes/lunch/commit/fcfedcc11f545f106ba86cd21c884d1b66a1b1a1))

* config using env, populate data, unable to use in memory DB ([`7319e1a`](https://github.com/jdobes/lunch/commit/7319e1a36301dbe8db262ff284f48a3ab651b8e4))

* continue with prototyping ([`183f105`](https://github.com/jdobes/lunch/commit/183f1059cc0c939b139cd88889b65948300d8bae))

* add draft service ([`425a3ec`](https://github.com/jdobes/lunch/commit/425a3eccd0478901a0b1cdbfea760afee20d3170))

* Initial commit ([`5aaff71`](https://github.com/jdobes/lunch/commit/5aaff71eb0b1c7b99e990a394f2f2262032d1729))
