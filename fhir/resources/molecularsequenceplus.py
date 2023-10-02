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


class MolecularSequencePlus(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Representation of a molecular sequence.
    """

    resource_type = Field("MolecularSequencePlus", const=True)

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

    literal: typing.List[fhirtypes.MolecularSequenceLiteralPlusType] = Field(
        None,
        alias="literal",
        title="A literal representation of a Molecular Sequence.",
        description='A literal representation of a Molecular Sequence.',
        # if property is element of this resource.
        element_property=True,
    )
    #TODO:not sure yet what this does need to double check and look into more
    literal__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_literal", title="Extension field for ``literal``."
    )

    formatted: typing.List[fhirtypes.AttachmentType] = Field(
        None,
        alias="formatted",
        title=(
            "Embedded file or a link (URL) which contains content to represent the "
            "sequence"
        ),
        description=(
            "Sequence that was observed as file content. Can be an actual file "
            "contents, or referenced by a URL to an external system."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    relative: typing.List[fhirtypes.MolecularSequenceRelativePlusType] = Field(
        None,
        alias="relative",
        title="A sequence defined relative to another sequence",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    extracted: typing.List[fhirtypes.MolecularSequenceExtractedType] = Field(
        None,
        alias="extracted",
        title="A Molecular Sequence that is represented as an extracted portion of a different Molecular Sequence.",
        description="A Molecular Sequence that is represented as an extracted portion of a different Molecular Sequence.",
        # if property is element of this resource.
        element_property=True,
    )

    repeated: typing.List[fhirtypes.MolecularSequenceRepeatedType] = Field(
        None,
        alias="repeated",
        title="A Molecular Sequence that is represented as a repeated sequence motif.",
        description="A Molecular Sequence that is represented as a repeated sequence motif.",
        # if property is element of this resource.
        element_property=True,
    )

    concatenated: typing.List[fhirtypes.MolecularSequenceConcatenatedType] = Field(
        None,
        alias="concatenated",
        title="A Molecular Sequence that is represented as an ordered concatenation of two or more Molecular Sequences.",
        description="A Molecular Sequence that is represented as an ordered concatenation of two or more Molecular Sequences.",
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
            "literal",
            "formatted",
            "relative",
            "extracted",
            "repeated",
            "concatenated",
        ]

class MolecularSequenceLiteralPlus(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A literal representation of a Molecular Sequence.
    """

    resource_type = Field("MolecularSequenceLiteralPlus", const=True)

    sequenceValue: fhirtypes.String = Field(
        ...,
        alias="sequenceValue",
        title=(
            "Indicates the order in which the sequence should be considered when "
            "putting multiple 'relative' elements together"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    encoding: fhirtypes.CodeableConceptType = Field(
        None,
        alias="encoding",
        title="The encoding used for the expression of the primary sequence",
        description=(
            "The encoding used for the expression of the primary sequence. "
            "This defines the characters that may be used in the primary sequence "
            "and it permits the explicit inclusion/exclusion of IUPAC ambiguity codes."
        ),
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
            "sequenceValue",
            "encoding",
            
        ]

class MolecularSequenceRelativePlus(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A sequence defined relative to another sequence.
    """

    resource_type = Field("MolecularSequenceRelativePlus", const=True)

    startingSequence: fhirtypes.ReferenceType = Field(
        ...,
        alias="startingSequence",
        title="The Molecular Sequence that serves as the starting sequence, on which edits will be applied.",
        description="The method for sequencing, for example, chip information.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MolecularSequencePlus"],
    )
    
    edit: typing.List[fhirtypes.MolecularSequenceRelativeEditPlusType] = Field(
        None,
        alias="edit",
        title="Changes in sequence from the starting sequence",
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
            "startingSequence",
            "edit",
        ]

class MolecularSequenceRelativeEditPlus(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    An edit (change) made to a sequence.
    """

    resource_type = Field("MolecularSequenceRelativeEditPlus", const=True)

    editOrder: fhirtypes.Integer = Field(
        None,
        alias="editOrder",
        title="The order of this edit, relative to other edits on the starting sequence",
        description=(
            "The order of this edit, relative to other edits on the starting sequence."
        ),
        # if property is element of this resource.
        element_property=False,
    )

    coordinateSystem: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="coordinateSystem",
        title="The coordinate system used to define the edited intervals on the starting sequence. Coordinate systems are usually 0- or 1-based",
        description=(
            "The coordinate system used to define the edited intervals on the starting sequence. "
            "Coordinate systems are usually 0- or 1-based.  "
        ),
        # if property is element of this resource.
        element_property=True,
    )

    start: fhirtypes.Integer = Field(
        ...,
        alias="start",
        title="The start coordinate of the interval that will be edited.",
        description=(
            "The start coordinate of the interval that will be edited."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_start", title="Extension field for ``start``."
    )

    end: fhirtypes.Integer = Field(
        ...,
        alias="end",
        title="The end coordinate of the interval that will be edited",
        description=(
            "The end coordinate of the interval that will be edited. "
        ),
        # if property is element of this resource.
        element_property=True,
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_end", title="Extension field for ``end``."
    )    

    replacementSequence: fhirtypes.ReferenceType = Field(
        ...,
        alias="replacementSequence",
        title="The sequence that defines the replacement sequence used in the edit operation",
        description="The sequence that defines the replacement sequence used in the edit operation.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MolecularSequencePlus"],
    )
    #TODO:not sure yet what this does need to double check and look into more
    replacementSequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_replacementSequence",
        title="Extension field for ``replacementSequence``.",
    )

    replacedSequence: fhirtypes.ReferenceType = Field(
        None,
        alias="replacedSequence",
        title="The sequence on the 'starting' sequence for the edit operation, defined by the specified interval, that will be replaced during the edit",
        description=(
            "The sequence on the 'starting' sequence for the edit operation,  "
            "defined by the specified interval, that will be replaced during the edit."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MolecularSequencePlus"],
    )
    #TODO:not sure yet what this does need to double check and look into more
    replacedSequence__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None,
        alias="_replacedSequence",
        title="Extension field for ``replacedSequence``.",
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceRelativeEditPlus`` according specification,
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
            "replacementSequence",
            "replacedSequence",
        ]
    
class MolecularSequenceExtracted(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A Molecular Sequence that is represented as an extracted portion of a different Molecular Sequence.
    """

    resource_type = Field("MolecularSequenceExtracted", const=True)

    startingSequence: fhirtypes.ReferenceType = Field(
        ...,
        alias="startingSequence",
        title="The Molecular Sequence that serves as the parent sequence, from which the intended sequence will be extracted",
        description=("The Molecular Sequence that serves as the parent sequence,"
                     "from which the intended sequence will be extracted."),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MolecularSequencePlus"],
    )

    start: fhirtypes.Integer = Field(
        ...,
        alias="start",
        title="The start coordinate (on the parent sequence) of the interval that defines the subsequence to be extracted",
        description=(
            "The start coordinate (on the parent sequence) of "
            " the interval that defines the subsequence to be extracted."
            ),
        # if property is element of this resource.
        element_property=True,
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_start", title="Extension field for ``start``."
    )
    
    end: fhirtypes.Integer = Field(
        ...,
        alias="end",
        title="The end coordinate (on the parent sequence) of the interval that defines the subsequence to be extracted",
        description=(
            "The end coordinate (on the parent sequence) of the interval that defines"
            "the subsequence to be extracted."
            ),
        # if property is element of this resource.
        element_property=True,
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_end", title="Extension field for ``end``."
    )
    
    coordinateSystem: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="coordinateSystem",
        title="The coordinate system used to define the interval that defines the subsequence to be extracted. Coordinate systems are usually 0- or 1-based",
        description=(
            "The coordinate system used to define the interval"
            "that defines the subsequence to be extracted."
            "Coordinate systems are usually 0- or 1-based."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    reverseComplement: fhirtypes.Boolean = Field(
        None,
        alias="reverseComplement",
        title="A flag that indicates whether the extracted sequence should be reverse complemented",
        description="A flag that indicates whether the extracted sequence should be reverse complemented.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceExtracted`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "startingSequence",
            "start",
            "end",
            "coordinateSystem",
            "reverseComplement",
        ]
    
class MolecularSequenceRepeated(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A Molecular Sequence that is represented as a repeated sequence motif.
    """

    resource_type = Field("MolecularSequenceRepeated", const=True)

    sequenceMotif: fhirtypes.ReferenceType = Field(
        ...,
        alias="sequenceMotif",
        title="The sequence that defines the repeated motif",
        description="The sequence that defines the repeated motif.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MolecularSequencePlus"],
    )

    copyCount: fhirtypes.Integer = Field(
        ...,
        alias="copyCount",
        title="The number of repeats (copies) of the sequence motif",
        description="The number of repeats (copies) of the sequence motif.",
        # if property is element of this resource.
        element_property=True,
    )
    #TODO: check if we need to put this in for copyCount still dont know what this does
    # start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
    #     None, alias="_start", title="Extension field for ``start``."
    # )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceRepeated`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceMotif",
            "copyCount",
        ]
    
class MolecularSequenceConcatenated(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A Molecular Sequence that is represented as an ordered concatenation of two or more Molecular Sequences.
    """

    resource_type = Field("MolecularSequenceConcatenated", const=True)

    sequenceElement: typing.List[fhirtypes.MolecularSequenceConcatenatedSequenceElementType] = Field(
        ...,
        alias="sequenceElement",
        title="One element of a concatenated Molecular Sequence.",
        description="One element of a concatenated Molecular Sequence.",
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceConcatenated`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequenceElement",
        ]

class MolecularSequenceConcatenatedSequenceElement(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    One element of a concatenated Molecular Sequence.
    """

    resource_type = Field("MolecularSequenceConcatenatedSequenceElement", const=True)

    sequence: fhirtypes.ReferenceType = Field(
        ...,
        alias="sequence",
        title="The method for sequencing",
        description="The method for sequencing, for example, chip information.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["MolecularSequencePlus"],
    )

    ordinalIndex: fhirtypes.Integer = Field(
        ...,
        alias="ordinalIndex",
        title="The ordinal position of this sequence element within the concatenated Molecular Sequence",
        description="The ordinal position of this sequence element within the concatenated Molecular Sequence.",
        # if property is element of this resource.
        element_property=True,
    )
    #TODO: check if we need to put this in for ordinalIndex still dont know what this does
    # start__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
    #     None, alias="_start", title="Extension field for ``start``."
    # )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``MolecularSequenceConcatenatedSequenceElement`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "sequence",
            "ordinalIndex",
        ]
