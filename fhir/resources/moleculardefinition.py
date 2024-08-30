# -*- coding: utf-8 -*-
"""
Profile: https://build.fhir.org/branches/cg-im-molseq-work_in_progress_2/molecularsequence.html
Release: R5P
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic import Field, root_validator


from . import backboneelement, domainresource, fhirtypes


class MolecularDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Representation of a molecular sequence.
    """

    resource_type = Field("MolecularDefinition", const=True)

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Unique ID for this particular sequence",
        description="A unique identifier for this particular sequence instance.",
        # if property is element of this resource.
        element_property=True,
    )

    type: fhirtypes.Code = Field(
        None,
        alias="type",
        title="aa | dna | rna",
        description="Amino Acid Sequence/ DNA Sequence / RNA Sequence.",
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["aa", "dna", "rna"],
    )
    type__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_type", title="Extension field for ``type``."
    )

    location: typing.List[fhirtypes.MolecularDefinitionLocationType] = Field(
        None,
        alias="location",
        title="Location of this molecule",
        description="The molecular location of this molecule.",
        # if property is element of this resource.
        element_property=True,
    )

    memberState: fhirtypes.ReferenceType = Field(
        None,
        alias="memberState",
        title="A member or part of this molecule.",
        description="A member or part of this molecule.",
        # if property is element of this resource.
        element_property=True,
         # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MolecularDefinition"],
    )

    representation: typing.List[fhirtypes.MolecularDefinitionRepresentationType] = Field(
        None,
        alias="representation",
        title="...",
        description="The representation of this molecular definition, e.g., as a literal or repeated elements.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequencePlus`` according specification,
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
            "type",
            "location",
            "memberState",
            "representation",
        ]

class MolecularDefinitionLocation(backboneelement.BackboneElement):

    resource_type = Field("MolecularDefinitionLocation", const=True)
    #TODO: double check if this is correct: removed list: typing.List[]
    sequenceLocation: fhirtypes.MolecularDefinitionLocationSequenceLocationType = Field(
        None,
        alias="sequenceLocation",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    featureLocation: typing.List[fhirtypes.MolecularDefinitionLocationFeatureLocationType] = Field(
        None,
        alias="featureLocation",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceRelativePlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceLocation",
            "featureLocation",
        ]

class MolecularDefinitionLocationSequenceLocation(backboneelement.BackboneElement):

    resource_type = Field("MolecularDefinitionLocationSequenceLocation", const=True)

    sequenceContext: fhirtypes.ReferenceType= Field(
        ...,
        alias="sequenceContext",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MolecularDefinition"],
    )

    coordinateInterval: typing.List[fhirtypes.MolecularDefinitionLocationSequenceLocationCoordinateIntervalType] = Field(
        None,
        alias="coordinateInterval",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    strand: fhirtypes.CodeableConceptType = Field(
        None,
        alias="strand",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["Forward", "Reverse"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceContext",
            "coordinateInterval",
            "strand",
        ]

class MolecularDefinitionLocationSequenceLocationCoordinateInterval(backboneelement.BackboneElement):

    resource_type = Field("MolecularDefinitionLocationSequenceLocationCoordinateInterval", const=True)

    numberingSystem: fhirtypes.CodeableConceptType = Field(
        None,
        alias= "numberingSystem",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    startQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="startQuantity",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e sequence[x]
        one_of_many="start",
        one_of_many_required=False,
    )

    startRange: fhirtypes.RangeType = Field(
        None,
        alias="startRange",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e sequence[x]
        one_of_many="start",
        one_of_many_required=False,
        
    )
    
    endQuantity: fhirtypes.QuantityType = Field(
        None,
        alias="endQuantity",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e sequence[x]
        one_of_many="end",
        one_of_many_required=False,
    )

    endRange: fhirtypes.RangeType = Field(
        None,
        alias="endRange",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e sequence[x]
        one_of_many="end",
        one_of_many_required=False,
        
    )

    @root_validator(pre=True, allow_reuse=True)
    def validate_one_of_many_4432(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
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
            "start": [
                "startQuantity",
                "startRange",
            ],
            "end": [
                "endQuantity",
                "endRange"
            ]
        }
        for prefix, fields in one_of_many_fields.items():
            assert cls.__fields__[fields[0]].field_info.extra["one_of_many"] == prefix
            required = (
                cls.__fields__[fields[0]].field_info.extra["one_of_many_required"]
                is True
            )
            found = False
            for field in fields:
                if field in values and values[field] is not None:
                    if found is True:
                        raise ValueError(
                            "Any of one field value is expected from "
                            f"this list {fields}, but got multiple!"
                        )
                    else:
                        found = True
            if required is True and found is False:
                raise ValueError(f"Expect any of field value from this list {fields}.")

        return values
    
class MolecularDefinitionLocationFeatureLocation(backboneelement.BackboneElement):

    resource_type = Field("MolecularDefinitionLocationFeatureLocation", const=True)

    geneId: fhirtypes.CodeableConceptType =  Field(
        None,
        alias="geneId",
        title="...",
        description=(None),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "geneId",
        ]

class MolecularDefinitionRepresentation(backboneelement.BackboneElement):

    resource_type = Field("MolecularDefinitionRepresentation", const=True)


    focus: fhirtypes.CodeableConceptType = Field(
        None,
        alias="focus",
        title="...",
        description=(None),
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        None,
        alias="code",
        title="...",
        description=(None),
        # if property is element of this resource.
        element_property=True,
    )
    # getting rid of list:typing.List[]
    literal: fhirtypes.MolecularDefinitionRepresentationLiteralType= Field(
        None,
        alias="literal",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    # getting rid of list:typing.List[]
    resolvable: fhirtypes.AttachmentType= Field(
        None,
        alias="resolvable",
        title="...",
        description=(None),
        # if property is element of this resource.
        element_property=True,
    )
    # getting rid of list:typing.List[]
    extracted: fhirtypes.MolecularDefinitionRepresentationExtractedType = Field(
        None,
        alias="extracted",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    # getting rid of list:typing.List[]
    repeated: fhirtypes.MolecularDefinitionRepresentationRepeatedType = Field(
        None,
        alias="repeated",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    # getting rid of list:typing.List[]
    concatenated: fhirtypes.MolecularDefinitionRepresentationConcatenatedType = Field(
        None,
        alias="concatenated",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    # getting rid of list:typing.List[]
    relative: fhirtypes.MolecularDefinitionRepresentationRelativeType = Field(
        None,
        alias="relative",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "focus",
            "code",
            "literal",
            "resolvable",
            "extracted",
            "repeated",
            "concatenated",
            "relative",
        ]

class MolecularDefinitionRepresentationLiteral(backboneelement.BackboneElement):

    resource_type = Field("MolecularDefinitionRepresentationLiteral", const=True)

    encoding: fhirtypes.CodeableConceptType = Field(
        None,
        alias="encoding",
        title="...",
        description=(None),
        # if property is element of this resource.
        element_property=True,
    )

    value: fhirtypes.String = Field(
        ...,
        alias="value",
        title="...",
        description=(None),
        # if property is element of this resource.
        element_property=True,
    )


    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "encoding",
            "value",
        ]

class MolecularDefinitionRepresentationExtracted(backboneelement.BackboneElement):

    resource_type = Field("MolecularDefinitionRepresentationExtracted", const=True)
    # getting rid of list:typing.List[]
    startingMolecule: fhirtypes.ReferenceType = Field(
        ...,
        alias="startingMolecule",
        title="...",
        description=(None),
        # if property is element of this resource.
        element_property=True,
        enum_reference_types=["MolecularDefinition"],
    )

    start: fhirtypes.Integer = Field(
        ...,
        alias="start",
        title="...",
        description=(None),
        # if property is element of this resource.
        element_property=True,
  
    )

    end: fhirtypes.Integer = Field(
        ...,
        alias="end",
        title="...",
        description=(None),
        # if property is element of this resource.
        element_property=True,
    )

    coordinateSystem: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="coordinateSystem",
        title="...",
        description=(None),
        # if property is element of this resource.
        element_property=True,
    )
    
    reverseComplement: fhirtypes.Boolean = Field(
        None,
        alias="reverseComplement",
        title="...",
        description=(None),
        # if property is element of this resource.
        element_property=True,
    )


    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "startingMolecule",
            "start",
            "end",
            "coordinateSystem",
            "reverseComplement",
        ]

class MolecularDefinitionRepresentationRepeated(backboneelement.BackboneElement):

    resource_type = Field("MolecularDefinitionRepresentationRepeated", const=True)

    sequenceMotif: typing.List[fhirtypes.ReferenceType] = Field(
        ...,
        alias="sequenceMotif	",
        title="...",
        description=(None),
        # if property is element of this resource.
        element_property=True,
        enum_reference_type = ["MolecularDefinition"]
    )

    copyCount: fhirtypes.Integer = Field(
        ...,
        alias="copyCount",
        title="...",
        description=(None),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceMotif",
            "copyCount",
        ]

class MolecularDefinitionRepresentationConcatenated(backboneelement.BackboneElement):

    resource_type = Field("MolecularDefinitionRepresentationConcatenated", const=True)

    sequenceElement: typing.List[fhirtypes.MolecularDefinitionRepresentationConcatenatedSequenceElementType] = Field(
        None,
        alias="sequenceElement",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceElement",
        ]

class MolecularDefinitionRepresentationConcatenatedSequenceElement(backboneelement.BackboneElement):

    resource_type = Field("MolecularDefinitionRepresentationConcatenatedSequenceElement", const=True)
    # removed typing.List[]
    sequence: fhirtypes.ReferenceType = Field(
        ...,
        alias="sequence",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MolecularDefinition"],
    )

    ordinalIndex: fhirtypes.Integer = Field(
        ...,
        alias="ordinalIndex",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "ordinalIndex",
        ]

class MolecularDefinitionRepresentationRelative(backboneelement.BackboneElement):

    resource_type = Field("MolecularDefinitionRepresentationRelative", const=True)
    # removed typing.List[]
    startingMolecule: fhirtypes.ReferenceType = Field(
        ...,
        alias="startingMolecule",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MolecularDefinition"],
    )

    edit: typing.List[fhirtypes.MolecularDefinitionRepresentationRelativeEditType] = Field(
        None,
        alias="edit",
        title="...",
        description=None,
        # if property is element of this resource.
        elements_sequence= True)

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "startingMolecule",
            "edit",
        ]

class MolecularDefinitionRepresentationRelativeEdit(backboneelement.BackboneElement):

    resource_type = Field("MolecularDefinitionRepresentationRelativeEdit", const=True)

    editOrder: fhirtypes.Integer = Field(
        None,
        alias="editOrder",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    coordinateSystem: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="coordinateSystem",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    start: fhirtypes.Integer = Field(
        ...,
        alias="start",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    end: fhirtypes.Integer = Field(
        ...,
        alias="end",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )
    #removed typing.List[]
    replacementMolecule: fhirtypes.ReferenceType = Field(
        ...,
        alias="replacementMolecule",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MolecularDefinition"],
    )
    #removed typing.List[]
    replacedMolecule: fhirtypes.ReferenceType = Field(
        None,
        alias="replacedMolecule",
        title="...",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MolecularDefinition"],
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceLiteralPlus`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "editOrder",
            "coordinateSystem",
            "start",
            "end",
            "replacementMolecule",
            "replacedMolecule",
        ]
























