# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/RiskAssessment
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class RiskAssessment(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Potential outcomes for a subject with likelihood.
    An assessment of the likely outcome(s) for a patient or other subject as
    well as the likelihood of each outcome.
    """

    __resource_type__ = "RiskAssessment"

    basedOn: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="basedOn",
        title="Request fulfilled by this assessment",
        description="A reference to the request that is fulfilled by this risk assessment.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    basis: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        None,
        alias="basis",
        title="Information used in assessment",
        description=(
            "Indicates the source data considered as part of the assessment (for "
            "example, FamilyHistory, Observations, Procedures, Conditions, etc.)."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="code",
        title="Type of assessment",
        description="The type of the risk assessment performed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    condition: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="condition",
        title="Condition assessed",
        description=(
            "For assessments or prognosis specific to a particular condition, "
            "indicates the condition being assessed."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Condition"],
        },
    )

    encounter: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="encounter",
        title="Where was assessment performed?",
        description="The encounter where the assessment was performed.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(  # type: ignore
        None,
        alias="identifier",
        title="Unique identifier for the assessment",
        description="Business identifier assigned to the risk assessment.",
        json_schema_extra={
            "element_property": True,
        },
    )

    method: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="method",
        title="Evaluation mechanism",
        description="The algorithm, process or mechanism used to evaluate the risk.",
        json_schema_extra={
            "element_property": True,
        },
    )

    mitigation: fhirtypes.StringType = Field(  # type: ignore
        None,
        alias="mitigation",
        title="How to reduce risk",
        description=(
            "A description of the steps that might be taken to reduce the "
            "identified risk(s)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    mitigation__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_mitigation", title="Extension field for ``mitigation``."
    )

    note: typing.List[fhirtypes.AnnotationType] = Field(  # type: ignore
        None,
        alias="note",
        title="Comments on the risk assessment",
        description="Additional comments about the risk assessment.",
        json_schema_extra={
            "element_property": True,
        },
    )

    occurrenceDateTime: fhirtypes.DateTimeType = Field(  # type: ignore
        None,
        alias="occurrenceDateTime",
        title="When was assessment made?",
        description="The date (and possibly time) the risk assessment was performed.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )
    occurrenceDateTime__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None,
        alias="_occurrenceDateTime",
        title="Extension field for ``occurrenceDateTime``.",
    )

    occurrencePeriod: fhirtypes.PeriodType = Field(  # type: ignore
        None,
        alias="occurrencePeriod",
        title="When was assessment made?",
        description="The date (and possibly time) the risk assessment was performed.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e occurrence[x]
            "one_of_many": "occurrence",
            "one_of_many_required": False,
        },
    )

    parent: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="parent",
        title="Part of this occurrence",
        description=(
            "A reference to a resource that this risk assessment is part of, such "
            "as a Procedure."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Resource"],
        },
    )

    performer: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="performer",
        title="Who did assessment?",
        description="The provider or software application that performed the assessment.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Practitioner", "PractitionerRole", "Device"],
        },
    )

    prediction: typing.List[fhirtypes.RiskAssessmentPredictionType] = Field(  # type: ignore
        None,
        alias="prediction",
        title="Outcome predicted",
        description="Describes the expected outcome for the subject.",
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonCode: typing.List[fhirtypes.CodeableConceptType] = Field(  # type: ignore
        None,
        alias="reasonCode",
        title="Why the assessment was necessary?",
        description="The reason the risk assessment was performed.",
        json_schema_extra={
            "element_property": True,
        },
    )

    reasonReference: typing.List[fhirtypes.ReferenceType] = Field(  # type: ignore
        None,
        alias="reasonReference",
        title="Why the assessment was necessary?",
        description="Resources supporting the reason the risk assessment was performed.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Condition",
                "Observation",
                "DiagnosticReport",
                "DocumentReference",
            ],
        },
    )

    status: fhirtypes.CodeType = Field(  # type: ignore
        None,
        alias="status",
        title="registered | preliminary | final | amended +",
        description=(
            "The status of the RiskAssessment, using the same statuses as an "
            "Observation."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["registered", "preliminary", "final", "amended", "+"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Who/what does assessment apply to?",
        description="The patient or group the risk assessment applies to.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Patient", "Group"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RiskAssessment`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "basedOn",
            "parent",
            "status",
            "method",
            "code",
            "subject",
            "encounter",
            "occurrenceDateTime",
            "occurrencePeriod",
            "condition",
            "performer",
            "reasonCode",
            "reasonReference",
            "basis",
            "prediction",
            "mitigation",
            "note",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
        return required_fields

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {"occurrence": ["occurrenceDateTime", "occurrencePeriod"]}
        return one_of_many_fields


class RiskAssessmentPrediction(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Outcome predicted.
    Describes the expected outcome for the subject.
    """

    __resource_type__ = "RiskAssessmentPrediction"

    outcome: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="outcome",
        title="Possible outcome for the subject",
        description=(
            "One of the potential outcomes for the patient (e.g. remission, death,"
            "  a particular condition)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    probabilityDecimal: fhirtypes.DecimalType = Field(  # type: ignore
        None,
        alias="probabilityDecimal",
        title="Likelihood of specified outcome",
        description="Indicates how likely the outcome is (in the specified timeframe).",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e probability[x]
            "one_of_many": "probability",
            "one_of_many_required": False,
        },
    )
    probabilityDecimal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None,
        alias="_probabilityDecimal",
        title="Extension field for ``probabilityDecimal``.",
    )

    probabilityRange: fhirtypes.RangeType = Field(  # type: ignore
        None,
        alias="probabilityRange",
        title="Likelihood of specified outcome",
        description="Indicates how likely the outcome is (in the specified timeframe).",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e probability[x]
            "one_of_many": "probability",
            "one_of_many_required": False,
        },
    )

    qualitativeRisk: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="qualitativeRisk",
        title="Likelihood of specified outcome as a qualitative value",
        description=(
            "Indicates how likely the outcome is (in the specified timeframe), "
            "expressed as a qualitative value (e.g. low, medium, or high)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    rationale: fhirtypes.StringType = Field(  # type: ignore
        None,
        alias="rationale",
        title="Explanation of prediction",
        description="Additional information explaining the basis for the prediction.",
        json_schema_extra={
            "element_property": True,
        },
    )
    rationale__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_rationale", title="Extension field for ``rationale``."
    )

    relativeRisk: fhirtypes.DecimalType = Field(  # type: ignore
        None,
        alias="relativeRisk",
        title="Relative likelihood",
        description=(
            "Indicates the risk for this particular subject (with their specific "
            "characteristics) divided by the risk of the population in general.  "
            "(Numbers greater than 1 = higher risk than the population, numbers "
            "less than 1 = lower risk.)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    relativeRisk__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_relativeRisk", title="Extension field for ``relativeRisk``."
    )

    whenPeriod: fhirtypes.PeriodType = Field(  # type: ignore
        None,
        alias="whenPeriod",
        title="Timeframe or age range",
        description=(
            "Indicates the period of time or age range of the subject to which the "
            "specified probability applies."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e when[x]
            "one_of_many": "when",
            "one_of_many_required": False,
        },
    )

    whenRange: fhirtypes.RangeType = Field(  # type: ignore
        None,
        alias="whenRange",
        title="Timeframe or age range",
        description=(
            "Indicates the period of time or age range of the subject to which the "
            "specified probability applies."
        ),
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e when[x]
            "one_of_many": "when",
            "one_of_many_required": False,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``RiskAssessmentPrediction`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "outcome",
            "probabilityDecimal",
            "probabilityRange",
            "qualitativeRisk",
            "relativeRisk",
            "whenPeriod",
            "whenRange",
            "rationale",
        ]

    def get_one_of_many_fields(self) -> typing.Dict[str, typing.List[str]]:
        """https://www.hl7.org/fhir/formats.html#choice
        A few elements have a choice of more than one data type for their content.
        All such elements have a name that takes the form nnn[x].
        The "nnn" part of the name is constant, and the "[x]" is replaced with
        the title-cased name of the type that is actually used.
        The table view shows each of these names explicitly.

        Elements that have a choice of data type cannot repeat - they must have a
        maximum cardinality of 1. When constructing an instance of an element with a
        choice of types, the authoring system must create a single element with a
        data type chosen from among the list of permitted data types.
        """
        one_of_many_fields = {
            "probability": ["probabilityDecimal", "probabilityRange"],
            "when": ["whenPeriod", "whenRange"],
        }
        return one_of_many_fields
