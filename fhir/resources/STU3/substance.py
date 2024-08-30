# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Substance
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class Substance(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A homogeneous material with a definite composition.
    """

    __resource_type__ = "Substance"

    category: typing.List[fhirtypes.CodeableConceptType] = Field(  # type: ignore
        None,
        alias="category",
        title="What class/type of substance this is",
        description=(
            "A code that classifies the general type of substance.  This is used  "
            "for searching, sorting and display purposes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    code: fhirtypes.CodeableConceptType = Field(  # type: ignore
        ...,
        alias="code",
        title="What substance this is",
        description="A code (or set of codes) that identify this substance.",
        json_schema_extra={
            "element_property": True,
        },
    )

    description: fhirtypes.StringType = Field(  # type: ignore
        None,
        alias="description",
        title="Textual description of the substance, comments",
        description=(
            "A description of the substance - its appearance, handling "
            "requirements, and other usage notes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(  # type: ignore
        None,
        alias="identifier",
        title="Unique identifier",
        description="Unique identifier for the substance.",
        json_schema_extra={
            "element_property": True,
        },
    )

    ingredient: typing.List[fhirtypes.SubstanceIngredientType] = Field(  # type: ignore
        None,
        alias="ingredient",
        title="Composition information about the substance",
        description="A substance can be composed of other substances.",
        json_schema_extra={
            "element_property": True,
        },
    )

    instance: typing.List[fhirtypes.SubstanceInstanceType] = Field(  # type: ignore
        None,
        alias="instance",
        title="If this describes a specific package/container of the substance",
        description=(
            "Substance may be used to describe a kind of substance, or a specific "
            "package/container of the substance: an instance."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    status: fhirtypes.CodeType = Field(  # type: ignore
        None,
        alias="status",
        title="active | inactive | entered-in-error",
        description="A code to indicate if the substance is actively used.",
        json_schema_extra={
            "element_property": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["active", "inactive", "entered-in-error"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Substance`` according specification,
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
            "description",
            "instance",
            "ingredient",
        ]


class SubstanceIngredient(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Composition information about the substance.
    A substance can be composed of other substances.
    """

    __resource_type__ = "SubstanceIngredient"

    quantity: fhirtypes.RatioType = Field(  # type: ignore
        None,
        alias="quantity",
        title="Optional amount (concentration)",
        description="The amount of the ingredient in the substance - a concentration ratio.",
        json_schema_extra={
            "element_property": True,
        },
    )

    substanceCodeableConcept: fhirtypes.CodeableConceptType = Field(  # type: ignore
        None,
        alias="substanceCodeableConcept",
        title="A component of the substance",
        description="Another substance that is a component of this substance.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e substance[x]
            "one_of_many": "substance",
            "one_of_many_required": True,
        },
    )

    substanceReference: fhirtypes.ReferenceType = Field(  # type: ignore
        None,
        alias="substanceReference",
        title="A component of the substance",
        description="Another substance that is a component of this substance.",
        json_schema_extra={
            "element_property": True,
            # Choice of Data Types. i.e substance[x]
            "one_of_many": "substance",
            "one_of_many_required": True,
            # note: Listed Resource Type(s) should be allowed as Reference.
            "enum_reference_types": ["Substance"],
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceIngredient`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "quantity",
            "substanceCodeableConcept",
            "substanceReference",
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
            "substance": ["substanceCodeableConcept", "substanceReference"]
        }
        return one_of_many_fields


class SubstanceInstance(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    If this describes a specific package/container of the substance.
    Substance may be used to describe a kind of substance, or a specific
    package/container of the substance: an instance.
    """

    __resource_type__ = "SubstanceInstance"

    expiry: fhirtypes.DateTimeType = Field(  # type: ignore
        None,
        alias="expiry",
        title="When no longer valid to use",
        description=(
            "When the substance is no longer valid to use. For some substances, a "
            "single arbitrary date is used for expiry."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    expiry__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(  # type: ignore
        None, alias="_expiry", title="Extension field for ``expiry``."
    )

    identifier: fhirtypes.IdentifierType = Field(  # type: ignore
        None,
        alias="identifier",
        title="Identifier of the package/container",
        description=(
            "Identifier associated with the package/container (usually a label "
            "affixed directly)."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    quantity: fhirtypes.QuantityType = Field(  # type: ignore
        None,
        alias="quantity",
        title="Amount of substance in the package",
        description="The amount of the substance.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``SubstanceInstance`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "identifier",
            "expiry",
            "quantity",
        ]
