# -*- coding: utf-8 -*-
"""
Profile: https://build.fhir.org/branches/cg-im-molseq-work_in_progress_2/molecularsequence.html
Release: R5P
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""

# from .. import molecularsequenceplus
import sys
sys.path.append('../fhir.resources')
from fhir.resources.molecularsequenceplus import MolecularSequencePlus


def impl_molecularsequenceplus_1(inst):
    """No. 1 tests collection for MolecularSequencePlus.
    Test File: Simple sequence example
    Citation: https://build.fhir.org/branches/cg-im-molseq-work_in_progress_2/molecularsequence-examples.html
    """
    
    assert inst.id == "example"
    assert inst.text['status'] == "generated"
    assert inst.text['div'] ==  "<div xmlns=\"http://www.w3.org/1999/xhtml\"><p><b>Generated Narrative: MolecularSequence</b><a name=\"example\"> </a></p><div style=\"display: inline-block; background-color: #d9e0e7; padding: 6px; margin: 4px; border: 1px solid #8da1b4; border-radius: 5px; line-height: 60%\"><p style=\"margin-bottom: 0px\">Resource MolecularSequence &quot;example&quot; </p></div><p><b>type</b>: dna</p><h3>Literals</h3><table class=\"grid\"><tr><td style=\"display: none\">-</td><td><b>SequenceValue</b></td></tr><tr><td style=\"display: none\">*</td><td>ATGAACAGACAAGTAAAAGACATGACAGYGATACTTTCCCAGAGCTGAAGTTAACAAATGCACCTGGTTC TTTTACTAAGTGTTCAAATACCAGTGAACTTAAAGAATTTGTCAATCCTAGCCTTCCAAGAGAAGAAAAA GAAGAGAAACTAGAAACAGTTAAAGTGTCTAATAATGCTGAAGACCCCAAAGATCTCATGTTAAGTGGAG AAAGGGTTTTGCAAACTGAAAGATCTGTAGAGAGTAGCAGTATTTCAYTGGTACCTGGTACTGATTATGG CACTCAGGAAAGTATCTCGTTACTGGAAGTTAGCACTCTAGGGAAGGCAAAAACAGAACCAAATAAATGT GTGAGTCAGTGTGCAGCATTTGAAAACCCCAAGGGACTAATTCATGGTTGTTCCAAAGATAATAGAAATG ACACAGAAGGCTTTAAGTATCCATTGGGACATGAAGTTAACCACAGTCGGGAAACAAGCATAGAAATGGA AGAAAGTGAACTTGATGCTCAGTATTTGCAGAATACATTCAAGGTTTCAAAGCGCCAGTCATTTGCTCYG TTTTCAAATCCAGGAAATGCAGAAGAGGAATGTGCAACATTCTCTGCCCACTCTGGGTCCTTAAAGAAAC AAAGTCCAAAAGTCACTTTTGAATGTGAACAAAAGGAAGAAAATCAAGGAAAGAATGAGTCTAATATCAA GCCTGTACAGACAGTTAATATCACTGCAGGCTTTCCTGTGGTTGGTCAGAAAGA</td></tr></table><h3>Formatteds</h3><table class=\"grid\"><tr><td style=\"display: none\">-</td><td><b>ContentType</b></td><td><b>Url</b></td></tr><tr><td style=\"display: none\">*</td><td>text/html</td><td><a href=\"https://www.ncbi.nlm.nih.gov/nuccore/MW716256.1?report=fasta\">https://www.ncbi.nlm.nih.gov/nuccore/MW716256.1?report=fasta</a></td></tr></table><blockquote><p><b>relative</b></p><p><b>startingSequence</b>: <a href=\"broken-link.html\">MolecularSequence/StartingSequenceExample: Starting Sequence Resource</a></p><h3>Edits</h3><table class=\"grid\"><tr><td style=\"display: none\">-</td><td><b>CoordinateSystem</b></td><td><b>Start</b></td><td><b>End</b></td><td><b>ReplacementSequence</b></td><td><b>ReplacedSequence</b></td></tr><tr><td style=\"display: none\">*</td><td>0-based interval counting <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"https://loinc.org/\">LOINC</a>#LA30100-4)</span></td><td>0</td><td>725</td><td><a href=\"broken-link.html\">MolecularSequence/ReplacementSequenceExample: Replacement Sequence Resource</a></td><td><a href=\"broken-link.html\">MolecularSequence/ReplacedSequenceExample: Replaced Sequence Resource</a></td></tr></table></blockquote><h3>Extracteds</h3><table class=\"grid\"><tr><td style=\"display: none\">-</td><td><b>StartingSequence</b></td><td><b>Start</b></td><td><b>End</b></td><td><b>CoordinateSystem</b></td><td><b>ReverseComplement</b></td></tr><tr><td style=\"display: none\">*</td><td><a href=\"broken-link.html\">MolecularSequence/StartingSequenceExample: Starting Sequence Resource</a></td><td>0</td><td>745</td><td>0-based interval counting <span style=\"background: LightGoldenRodYellow; margin: 4px; border: 1px solid khaki\"> (<a href=\"https://loinc.org/\">LOINC</a>#LA30100-4)</span></td><td>false</td></tr></table><blockquote><p><b>concatenated</b></p><blockquote><p><b>sequenceElement</b></p><p><b>sequence</b>: <a href=\"broken-link.html\">MolecularSequence/Sequence0ConcatenatedExample: Sequence-of index 0-Resource for concatenated sequence example</a></p><p><b>ordinalIndex</b>: 0</p></blockquote><blockquote><p><b>sequenceElement</b></p><p><b>sequence</b>: <a href=\"broken-link.html\">MolecularSequence/Sequence1ConcatenatedExample: Sequence-of index 1-Resource for concatenated sequence example</a></p><p><b>ordinalIndex</b>: 1</p></blockquote><blockquote><p><b>sequenceElement</b></p><p><b>sequence</b>: <a href=\"broken-link.html\">MolecularSequence/Sequence2ConcatenatedExample: Sequence-of index 2-Resource for concatenated sequence example</a></p><p><b>ordinalIndex</b>: 2</p></blockquote></blockquote></div>"
    assert inst.type == "dna"
    assert inst.literal[0].sequenceValue == "ATGAACAGACAAGTAAAAGACATGACAGYGATACTTTCCCAGAGCTGAAGTTAACAAATGCACCTGGTTC TTTTACTAAGTGTTCAAATACCAGTGAACTTAAAGAATTTGTCAATCCTAGCCTTCCAAGAGAAGAAAAA GAAGAGAAACTAGAAACAGTTAAAGTGTCTAATAATGCTGAAGACCCCAAAGATCTCATGTTAAGTGGAG AAAGGGTTTTGCAAACTGAAAGATCTGTAGAGAGTAGCAGTATTTCAYTGGTACCTGGTACTGATTATGG CACTCAGGAAAGTATCTCGTTACTGGAAGTTAGCACTCTAGGGAAGGCAAAAACAGAACCAAATAAATGT GTGAGTCAGTGTGCAGCATTTGAAAACCCCAAGGGACTAATTCATGGTTGTTCCAAAGATAATAGAAATG ACACAGAAGGCTTTAAGTATCCATTGGGACATGAAGTTAACCACAGTCGGGAAACAAGCATAGAAATGGA AGAAAGTGAACTTGATGCTCAGTATTTGCAGAATACATTCAAGGTTTCAAAGCGCCAGTCATTTGCTCYG TTTTCAAATCCAGGAAATGCAGAAGAGGAATGTGCAACATTCTCTGCCCACTCTGGGTCCTTAAAGAAAC AAAGTCCAAAAGTCACTTTTGAATGTGAACAAAAGGAAGAAAATCAAGGAAAGAATGAGTCTAATATCAA GCCTGTACAGACAGTTAATATCACTGCAGGCTTTCCTGTGGTTGGTCAGAAAGA"
    
    assert inst.formatted[0].contentType == "text/html"
    assert inst.formatted[0].url == "https://www.ncbi.nlm.nih.gov/nuccore/MW716256.1?report=fasta"
    
    assert inst.relative[0].startingSequence.reference == "MolecularSequence/StartingSequenceExample"
    assert inst.relative[0].startingSequence.type == "MolecularSequence"
    assert inst.relative[0].startingSequence.display == "Starting Sequence Resource"
    assert inst.relative[0].edit[0].coordinateSystem.coding[0].system == "http://loinc.org"
    assert inst.relative[0].edit[0].coordinateSystem.coding[0].code == "LA30100-4"
    assert inst.relative[0].edit[0].coordinateSystem.coding[0].display ==  "0-based interval counting"
    assert inst.relative[0].edit[0].start == 0
    assert inst.relative[0].edit[0].end == 725
    assert inst.relative[0].edit[0].replacementSequence.reference == "MolecularSequence/ReplacementSequenceExample"
    assert inst.relative[0].edit[0].replacementSequence.type == "MolecularSequence"
    assert inst.relative[0].edit[0].replacementSequence.display == "Replacement Sequence Resource"
    
    assert inst.extracted[0].startingSequence.reference == "MolecularSequence/StartingSequenceExample"
    assert inst.extracted[0].startingSequence.type == "MolecularSequence"
    assert inst.extracted[0].startingSequence.display == "Starting Sequence Resource"
    assert inst.extracted[0].edit[0].start == 0
    assert inst.extracted[0].edit[0].end == 745
    assert inst.extracted[0].coordinateSystem.coding[0].system == "http://loinc.org"
    assert inst.extracted[0].coordinateSystem.coding[0].code == "LA30100-4"
    assert inst.extracted[0].coordinateSystem.coding[0].display == "0-based interval counting"
    assert inst.extracted[0].coordinateSystem.text == "0-based interval counting"
    assert inst.extracted[0].reverseComplement == False

    assert inst.concatenated[0].sequenceElement[0].sequence.reference == "MolecularSequence/Sequence0ConcatenatedExample"
    assert inst.concatenated[0].sequenceElement[0].sequence.type == "MolecularSequence"
    assert inst.concatenated[0].sequenceElement[0].sequence.display == "Sequence-of index 0-Resource for concatenated sequence example"
    assert inst.concatenated[0].sequenceElement[0].ordinalIndex== 0

    assert inst.concatenated[0].sequenceElement[1].sequence.reference == "MolecularSequence/Sequence1ConcatenatedExample"
    assert inst.concatenated[0].sequenceElement[1].sequence.type == "MolecularSequence"
    assert inst.concatenated[0].sequenceElement[1].sequence.display == "Sequence-of index 1-Resource for concatenated sequence example"
    assert inst.concatenated[0].sequenceElement[1].ordinalIndex== 1

    assert inst.concatenated[0].sequenceElement[2].sequence.reference == "MolecularSequence/Sequence2ConcatenatedExample"
    assert inst.concatenated[0].sequenceElement[2].sequence.type == "MolecularSequence"
    assert inst.concatenated[0].sequenceElement[2].sequence.display == "Sequence-of index 2-Resource for concatenated sequence example"
    assert inst.concatenated[0].sequenceElement[2].ordinalIndex== 2

def test_molecularsequence_1(base_settings):
    """No. 1 tests collection for MolecularSequencePlus.
    Test File: simple_sequence_example.json
    """
    filename = '../simple_sequence_example.json'
    inst = molecularsequenceplus.MolecularSequencePlus.parse_file(
        filename, content_type="application/json", encoding="utf-8"
    )

    assert "MolecularSequencePlus" == inst.resourceType

    impl_molecularsequenceplus_1(inst)

    # testing reverse by generating data from itself and create again.
    data = inst.dict()
    assert "MolecularSequence" == data["resourceType"]

    inst2 = impl_molecularsequenceplus_1.MolecularSequencePlus(**data)
    impl_molecularsequenceplus_1(inst2)