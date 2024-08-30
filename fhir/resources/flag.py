# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Flag
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field

from . import domainresource, fhirtypes


class Flag(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Key information to flag to healthcare providers.
    Prospective warnings of potential issues when providing care to the
    patient.
    """

    __resource_type__ = "Flag"

    author: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="author",
        title="Flag creator",
        description="The person, organization or device that created the flag.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Device",
                "Organization",
                "Patient",
                "RelatedPerson",
                "Practitioner",
                "PractitionerRole",
            ],
        },
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(  # type: ignore
        None,
        alias="category",
        title="Clinical, administrative, etc",
        description=(
            "Allows a flag to be divided into different categories like clinical, "
            "administrative etc. Intended to be used as a means of filtering which "
            "flags are displayed to particular user or in a given context."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="Coded or textual message to display to user",
        description=(
            "The coded value or textual component of the flag to display to the "
            "user."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    encounter: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="encounter",
        title="Alert relevant during encounter",
        description="This alert is only relevant during the encounter.",
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Encounter"],
        },
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(  # type: ignore
        None,
        alias="identifier",
        title="Business identifier",
        description=(
            "Business identifiers assigned to this flag by the performer or other "
            "systems which remain constant as the resource is updated and "
            "propagates from server to server."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    period: fhirtypes.PeriodType = Field(  # type: ignore
        None,
        alias="period",
        title="Time period when flag is active",
        description=(
            "The period of time from the activation of the flag to inactivation of "
            "the flag. If the flag is active, the end of the period should be "
            "unspecified."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType = Field(  # type: ignore
        None,
        alias="status",
        title="active | inactive | entered-in-error",
        description="Supports basic workflow.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "inactive", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    subject: fhirtypes.ReferenceType = Field(  # type: ignore
        ...,
        alias="subject",
        title="Who/What is flag about?",
        description=(
            "The patient, related person, location, group, organization, or "
            "practitioner etc. this is about record this flag is associated with."
        ),
        json_schema_extra={
            "element_property": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": [
                "Patient",
                "RelatedPerson",
                "Location",
                "Group",
                "Organization",
                "Practitioner",
                "PractitionerRole",
                "PlanDefinition",
                "Medication",
                "Procedure",
            ],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Flag`` according specification,
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
            "status",
            "category",
            "code",
            "subject",
            "period",
            "encounter",
            "author",
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
