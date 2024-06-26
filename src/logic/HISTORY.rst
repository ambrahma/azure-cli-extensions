.. :changelog:

Release History
===============

1.1.0
++++++
* `az logic integration-account`: Add new command group `assembly` to support managing assembly
* `az logic integration-account`: Add new command group `batch-configuration` to support managing batch configuration
* `az logic integration-account`: Add new command group `partner` to support managing partner
* `az logic integration-account`: Add new command group `session` to support managing session
* `az logic integration-account`: Add new command `list-callback-url` to support listing callback url
* `az logic integration-account workflow`: Add new command `generate-upgraded-definition` to support generating upgraded definition

1.0.1
++++++
* `az logic workflow`: Fix the issue with `parameters` in `--definition` not working

1.0.0
++++++
* Add new command group `az logic workflow identity` to support managing identity
* `az logic workflow identity`: Add new parameters `--mi-system-assigned` `--mi-user-assigned` to support managing identity

0.1.7
++++++
* Add new command group `az logic integration-account map` to support manage integration account map
* Upgrade SDK to fix deserialization errors

0.1.6
++++++
* Add README.md link in help
* Fix a syntax error in README.md

0.1.5
++++++
* Upgrade SDK to fix deserialization errors

0.1.4
++++++
* Add missing help for top level command group

0.1.3
++++++
* Preview logic extension

0.1.2
++++++
* `logic workflow update`: --definition is not to be mandatory while updating

0.1.1
++++++
* Fix parsing argument --integration-service-environment.

0.1.0
++++++
* Initial release.
