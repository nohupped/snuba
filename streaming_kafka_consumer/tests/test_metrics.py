import pytest
from streaming_kafka_consumer.metrics import Gauge, configure_metrics, get_metrics
from streaming_kafka_consumer.tests.metrics import Gauge as GaugeCall
from streaming_kafka_consumer.tests.metrics import TestingMetricsBackend


def test_gauge_simple() -> None:
    backend = TestingMetricsBackend

    name = "name"
    tags = {"tag": "value"}
    gauge = Gauge(backend, name, tags)

    with gauge:
        pass

    assert backend.calls == [
        GaugeCall(name, 0.0, tags),
        GaugeCall(name, 1.0, tags),
        GaugeCall(name, 0.0, tags),
    ]


def test_configure_metrics() -> None:
    assert get_metrics() == TestingMetricsBackend

    with pytest.raises(AssertionError):
        configure_metrics(TestingMetricsBackend)
