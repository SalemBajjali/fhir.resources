# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceMetric
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
from pydantic.validators import bytes_validator  # noqa: F401

from .. import fhirtypes  # noqa: F401
from .. import devicemetric


def impl_devicemetric_1(inst):
    assert inst.calibration[0].state == "calibrated"
    assert inst.calibration[0].time == fhirtypes.Instant.validate(
        "2016-12-28T09:03:04-05:00"
    )
    assert inst.calibration[0].type == "two-point"
    assert inst.category == "measurement"
    assert inst.color == "blue"
    assert inst.device.reference == "Device/dev1"
    assert inst.id == "example"
    assert inst.identifier[0].system == "http://goodcare.org/devicemetric/id"
    assert inst.identifier[0].value == "345675"
    assert inst.measurementFrequency.code == "Hz"
    assert inst.measurementFrequency.system == "http://unitsofmeasure.org"
    assert inst.measurementFrequency.unit == "Hertz"
    assert float(inst.measurementFrequency.value) == float(1)
    assert inst.meta.tag[0].code == "HTEST"
    assert inst.meta.tag[0].display == "test health data"
    assert (
        inst.meta.tag[0].system == "http://terminology.hl7.org/CodeSystem/v3-ActReason"
    )
    assert inst.operationalStatus == "on"
    assert inst.text.status == "generated"
    assert inst.type.coding[0].code == "150456"
    assert inst.type.coding[0].display == "MDC_PULS_OXIM_SAT_O2"
    assert inst.type.coding[0].system == "urn:iso:std:iso:11073:10101"
    assert inst.unit.coding[0].code == "262688"
    assert inst.unit.coding[0].display == "MDC_DIM_PERCENT"
    assert inst.unit.coding[0].system == "urn:iso:std:iso:11073:10101"


def test_devicemetric_1(base_settings):
    """No. 1 tests collection for DeviceMetric.
    Test File: devicemetric-example.json
    """
    filename = base_settings["unittest_data_dir"] / "devicemetric-example.json"
    inst = devicemetric.DeviceMetric.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )
    assert "DeviceMetric" == inst.resource_type

    impl_devicemetric_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "DeviceMetric" == data["resourceType"]

    inst2 = devicemetric.DeviceMetric(**data)
    impl_devicemetric_1(inst2)
