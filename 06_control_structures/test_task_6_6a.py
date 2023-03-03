import sys
import pytest


@pytest.mark.parametrize(
    "ip_add,ip_type",
    [
        ("10.1.1.1", "unicast"),
        ("28.1.1.1", "unicast"),
        ("230.1.1.1", "multicast"),
        ("255.255.255.255", "local broadcast"),
        ("0.0.0.0", "unassigned"),
        ("250.1.1.1", "unused"),
    ],
)
def test_task_correct_ip(capsys, monkeypatch, ip_add, ip_type):
    """
    Проверка работы задания при вводе multicast адреса
    """
    monkeypatch.setattr("builtins.input", lambda x=None: ip_add)
    if sys.modules.get("task_6_6a"):
        del sys.modules["task_6_6a"]
    import task_6_6a

    out, err = capsys.readouterr()
    correct_stdout = ip_type
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout == out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"


@pytest.mark.parametrize(
    "ip_add,ip_type",
    [
        ("10.1.1", "неправильный ip-адрес"),
        ("10.a.2.a", "неправильный ip-адрес"),
        ("10.1.1.1.1", "неправильный ip-адрес"),
        ("10.1.1.1.a", "неправильный ip-адрес"),
        ("10.1.1.", "неправильный ip-адрес"),
        ("300.1.1.1", "неправильный ip-адрес"),
        ("30,1.1.1.1", "неправильный ip-адрес"),
    ],
)
def test_task_wrong_ip(capsys, monkeypatch, ip_add, ip_type):
    """
    Проверка работы задания при вводе multicast адреса
    """
    monkeypatch.setattr("builtins.input", lambda x=None: ip_add)
    if sys.modules.get("task_6_6a"):
        del sys.modules["task_6_6a"]
    import task_6_6a

    out, err = capsys.readouterr()
    correct_stdout = ip_type
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout == out.strip().lower()
    ), "На стандартный поток вывода выводится неправильный вывод"