<div align = right>

&ensp;[<kbd> <br> EN <br> </kbd>](./README.md)&ensp;
&ensp;[<kbd> <br> RU <br> </kbd>](./README_RU.md)&ensp;

</div>

---

# Salt.Box Bridge Messages

## Содержание

- **[Описание](#описание)**
- **[Модули сообщений](#модули-сообщений)**
- **[Соглашение об именовании](#соглашение-об-именовании)**
- **[Настройка окружения разработки](#настройка-окружения-разработки)**


## Описание

**Salt.Box Bridge Messages** – общая библиотека моделей сообщений на
[pydantic](https://docs.pydantic.dev/), которую используют Salt.Box Core и
Salt.Box Bridge для общения друг с другом. Оба компонента зависят от этого
пакета, чтобы формат сообщений, передаваемых между ними, был определён один
раз и оставался синхронным, а не поддерживался каждой стороной отдельно.

Каждый класс сообщения наследуется либо от `CoreMessageBase`, либо от
`BridgeMessageBase` из [`base.py`](./saltbox_bridge_messages/base.py), в
зависимости от того, какой компонент его отправляет, оба несут поле
`master`, идентифицирующее Salt master, к которому относится сообщение.

## Модули сообщений

- [`base`](./saltbox_bridge_messages/base.py) – общие классы
  `CoreMessageBase` и `BridgeMessageBase`, от которых наследуется каждое
  сообщение, а также `CoreEmptyMessage` для запросов без payload
- [`master`](./saltbox_bridge_messages/master.py) – сообщения про кэш
  pillar: запрос на обновление кэша pillar для цели и ответ Bridge с
  отрендеренными данными pillar
- [`minion`](./saltbox_bridge_messages/minion.py) – сообщения про сбор
  миньонов: запрос списка миньонов, подходящих под цель, и ответ Bridge с
  найденными minion ID и их master
- [`salt_keys`](./saltbox_bridge_messages/salt_keys.py) – сообщения про
  управление ключами Salt: принятие или получение списка ключей миньонов по
  статусу, `accepted`, `unaccepted`, `rejected` или `denied`
- [`system`](./saltbox_bridge_messages/system.py) – сообщения жизненного
  цикла master: авторизация нового master по его публичным ключам GitFS и
  SSHFS, отчёт о статусе синхронизации master и сообщения для
  нагрузочного тестирования, которыми Bridge засыпает поток поддельных
  событий `job/{jid}/new`
- [`utils`](./saltbox_bridge_messages/utils.py) – общие вспомогательные
  элементы: литерал `SaltTgtType` с типами целей Salt и `Iso8601ZDatetime`,
  aware datetime, сериализующийся с суффиксом `Z`

## Соглашение об именовании

Предпочтительное именование классов сообщений:

```python
class CoreSomeDataRequest(CoreMessageBase): ...
class BridgeSomeDataResponse(BridgeMessageBase): ...
class BridgeOtherDataMessage(BridgeMessageBase): ...
```

Где:

- `[ Core | Bridge ]...` – компонент, который **отправляет** сообщение
- `...SomeData...` – содержательное описание сообщения
- `...[ Message | Request | Response ]` – тип сообщения, `Message`
  используется, когда сообщение отправляется не в ответ на какое-то
  полученное сообщение

## Настройка окружения разработки

Mypy [может не распознавать editable-установленные библиотеки](https://github.com/python/mypy/issues/13392),
в таком случае используйте обычную установку.

Чтобы добавить путь к этому пакету для автодополнения и импортов в
редакторе без его установки:

**PyCharm**, через настройку Sources Root:

1. Откройте структуру проекта, вид Project
2. Найдите папку, которую нужно добавить в `PYTHONPATH`, обычно это корневая
   папка этого пакета
3. Кликните по папке правой кнопкой и выберите **Mark Directory as → Sources Root**

**VSCode**, в `settings.json`:

```json
{
  "python.analysis.extraPaths": [
    "../saltbox-bridge-messages"
  ]
}
```
