from types import ModuleType

import cloudcoil.models.knative_serving as knative_serving


def test_has_modules():
    modules = list(filter(lambda x: isinstance(x, ModuleType), knative_serving.__dict__.values()))
    assert modules, "No modules found in knative_serving"
