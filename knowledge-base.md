https://github.com/fritz-tools/physical-ai-learning-companion

# Physical AI Knowledge Base

## OpenUSD Foundations
### Stage

A Stage is the complete scene that OpenUSD presents to you.

A Stage does not have to come from one file. OpenUSD can combine information from multiple USD files/layers to create the Stage.

### Composing Multiple Layers into One Stage

OpenUSD can use multiple layers to build one Stage.

For example, imagine multiple layers contribute information at the same location:

    World
    └── Geometry

One layer might contribute a Cube:

    World
    └── Geometry
        └── Cube

Another might contribute a Sphere:

    World
    └── Geometry
        └── Sphere

When OpenUSD builds the Stage, it looks at the layers and notices that they refer to the same location:

    World
    └── Geometry

Instead of making separate copies of World and Geometry, OpenUSD understands:

> "They're all talking about the same place."

So it combines their contributions.

The final Stage becomes:

    World
    └── Geometry
        ├── Cube
        └── Sphere

This is the composed result.

### The Big Idea

OpenUSD merged the information from multiple files into one scene.

Not copied.

Not duplicated.

Not imported like a Word document.

It **composed** one scene from several sources.


## USD Composition
### Why Composition Matters

This ability to compose a scene from multiple sources is one of OpenUSD's core strengths.

Different files can contribute different pieces of information while OpenUSD presents the result as one composed Stage.

## Python for OpenUSD
### Programmatically Building a Stage

Elements can be added to a USD Stage through Python instead of placing everything manually in a GUI.

For a small scene, manually placing objects in a GUI may make sense. But if a scene needs hundreds of repeated or systematically placed elements, such as 400 museum crates, doing that manually would be slow and error-prone.

Python can create the prims, add references to existing USD assets, and set their properties and positions according to rules.

This means Python is useful not because every USD scene needs to be built with code, but because code can automate repetitive or rule-based scene assembly.

## Omniverse

## Isaac Sim

## GitHub

## Glossary

## Questions to Revisit
