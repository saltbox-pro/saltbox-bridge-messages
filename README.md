# Salt.Box Bridge Messages

Common lib of message models to communicate between Salt.Box Core and Salt.Box
Bridge.

Mypy [may not recognise editable installed libs](https://github.com/python/mypy/issues/13392),
so use normal install in such case.

Preferred message classes naming:

```python
class CoreSomeDataRequest(CoreMessageBase): ...
class BridgeSomeDataResponse(BridgeMessageBase): ...
class BridgeOtherDataMessage(BridgeMessageBase): ...
```

Where:

- `[ Core | Bridge ]...` is a component which is __sending__ the message
- `...SomeData...` is a meaningful descriptor for the message
- `...[ Message | Request | Response ]` is a type of the message. Use `Message`
  when message assumed to be sent not as a response for some received message.

In PyCharm, to add additional search paths for Python packages (for example, those installed via pip install -e .), use the Sources Root setting:

Open the project structure (Project view).
Find the folder you want to add to PYTHONPATH (usually the root folder of your package).
Right-click on the folder and select Mark Directory as → Sources Root.
After this, PyCharm will treat this path as a source root, and autocompletion/imports will work correctly.

For VSCode in `settings.json`:
```json
{
  "python.analysis.extraPaths": [
    "../saltbox-bridge-messages"
  ]
}
```
