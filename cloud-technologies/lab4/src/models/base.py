import typing as t

ModelType = t.TypeVar('ModelType')


def load_model(cls: t.Type[ModelType], data: t.Mapping) -> ModelType:
    required = cls.__dict__.get('__required_keys__', frozenset())
    optional = cls.__dict__.get('__optional_keys__', frozenset())

    model = cls(
        **{key: data[key] for key in required},
        **{key: data[key] for key in optional if key in data},
    )

    return model
