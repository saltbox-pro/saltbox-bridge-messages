<div align = right>

&ensp;[<kbd> <br> EN <br> </kbd>](./README.md)&ensp;
&ensp;[<kbd> <br> RU <br> </kbd>](./README_RU.md)&ensp;

</div>

---

# Salt.Box Bridge Messages

## Table of Contents

- **[About](#about)**
- **[Message modules](#message-modules)**
- **[Naming convention](#naming-convention)**
- **[Development setup](#development-setup)**


## About

**Salt.Box Bridge Messages** is a shared library of [pydantic](https://docs.pydantic.dev/)
message models used by Salt.Box Core and Salt.Box Bridge to talk to each
other. Both components depend on this package so that the message shapes
sent over the wire are defined once and stay in sync, instead of each side
keeping its own copy.

Every message class extends either `CoreMessageBase` or `BridgeMessageBase`
from [`base.py`](./saltbox_bridge_messages/base.py), depending on which
component sends it, both carry a `master` field identifying the Salt master
the message belongs to.

## Message modules

- [`base`](./saltbox_bridge_messages/base.py) – the common `CoreMessageBase`
  and `BridgeMessageBase` classes every message inherits from, plus
  `CoreEmptyMessage` for requests that need no payload
- [`master`](./saltbox_bridge_messages/master.py) – pillar cache messages:
  requesting a pillar cache update for a target, and the Bridge response
  carrying the rendered pillar data
- [`minion`](./saltbox_bridge_messages/minion.py) – minion-gathering
  messages: requesting a list of minions matching a target, and the Bridge
  response with the matched minion IDs and their master
- [`salt_keys`](./saltbox_bridge_messages/salt_keys.py) – Salt key
  management messages: accepting or listing minion keys by status,
  `accepted`, `unaccepted`, `rejected` or `denied`
- [`system`](./saltbox_bridge_messages/system.py) – master lifecycle
  messages: authorizing a new master with its GitFS and SSHFS public keys,
  reporting master sync status, and load-testing messages used to burst
  fake `job/{jid}/new` events through Bridge
- [`utils`](./saltbox_bridge_messages/utils.py) – shared building blocks:
  the `SaltTgtType` literal of Salt target types, and `Iso8601ZDatetime`,
  an aware datetime that serializes with a `Z` suffix

## Naming convention

Preferred message classes naming:

```python
class CoreSomeDataRequest(CoreMessageBase): ...
class BridgeSomeDataResponse(BridgeMessageBase): ...
class BridgeOtherDataMessage(BridgeMessageBase): ...
```

Where:

- `[ Core | Bridge ]...` is a component which is **sending** the message
- `...SomeData...` is a meaningful descriptor for the message
- `...[ Message | Request | Response ]` is a type of the message, use
  `Message` when the message is not sent as a response to some received
  message

## Development setup

Mypy [may not recognise editable installed libs](https://github.com/python/mypy/issues/13392),
so use a normal install in such a case.

To add this package's path for autocompletion and imports in an editor
without installing it:

**PyCharm**, using the Sources Root setting:

1. Open the project structure, Project view
2. Find the folder to add to `PYTHONPATH`, usually the root folder of this package
3. Right-click the folder and select **Mark Directory as → Sources Root**

**VSCode**, in `settings.json`:

```json
{
  "python.analysis.extraPaths": [
    "../saltbox-bridge-messages"
  ]
}
```
