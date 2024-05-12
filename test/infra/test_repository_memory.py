from domain.entities.plc_factory import PlcFactory
from infra.plc_repository_memory import PlcRepositoryMemory


def test_should_create_empty_repository_memory() -> None:
    repository = PlcRepositoryMemory()
    assert repository is not None
    assert len(repository.get_all_plcs()) == 0


def test_should_add_plc() -> None:
    repository = PlcRepositoryMemory()
    plc = PlcFactory.default()

    repository.add_plc(plc)

    assert len(repository.get_all_plcs()) == 1
    assert repository.get_all_plcs()[0] == plc


def test_should_remove_plc() -> None:
    repository = PlcRepositoryMemory()
    plc = PlcFactory.default()
    plc_2 = PlcFactory.default()

    repository.add_plc(plc)
    repository.add_plc(plc_2)

    assert len(repository.get_all_plcs()) == 2

    repository.remove_plc(plc.id)

    assert len(repository.get_all_plcs()) == 1
    assert repository.get_all_plcs()[0] == plc_2
