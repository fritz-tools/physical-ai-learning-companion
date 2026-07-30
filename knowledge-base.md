https://github.com/fritz-tools/physical-ai-learning-companion

# Physical AI Knowledge Base

## OpenUSD Foundations

### Stage

A Stage is the complete scene that OpenUSD presents to you.

A Stage does not have to come from one file. OpenUSD can combine information from multiple USD files/layers to create the Stage.

### Scenegraph
The scenegraph is the hierarchical organization of all Prims in a USD stage.
Each Prim occupies a unique location in the scenegraph, identified by its namespace (Prim path).
Parent-child relationships in the scenegraph are created by Prim paths, not by Prim types.



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


OpenUSD merged the information from multiple files into one scene.

Not copied.

Not duplicated.

Not imported like a Word document.

It **composed** one scene from several sources.

### Variants
Why Variants Exist

Variants allow an asset creator to package multiple approved versions of an asset inside a single asset. Instead of creating separate files for each version, downstream users simply choose from a predefined set of options.

Key Insight

Variants are primarily a collaboration feature, not just a modeling feature.
Variant Sets

A Variant Set is a named collection of choices.

Example:

State
• Open
• Closed
• Damaged

A scene selects one option instead of creating separate assets.

Who Owns Variants

Official Variants are generally created and maintained by the asset team because they represent reusable choices that any downstream project may need.

### Overrides

If I need a customization only for my own scene, I usually author an override instead of modifying the original asset.

Overrides allow me to express my own opinions without changing the shared asset.

Author an override: Create a new opinion in my own layer that changes how an existing asset appears or behaves in my specific context, without modifying the original asset.

#### Overrides vs. Variants

Override

Local to one scene or context.
Authored by a downstream user.
Does not modify the original asset.

Variant

Part of the asset itself.
Created for reuse.
Can be selected by many downstream users.I now understand the difference.

Promotion Path:
a useful override can later become an official Variant.

Workflow:

Override
        ↓
Team adopts it
        ↓
Asset team promotes it
        ↓
Official Variant

### Prims
A prim is a node in a scenegraph.
Think of every Prim as having four big pieces of information:

- Where is it?:
/Geometry/Shelves/Shelf01
- What is it?:
Xform
- What values does it have?:
size, translate, visibility, color... (Attributes)
- What other Prims is it connected to?:
targets, materials, skeletons... (Relationships)

#### Prim Types
A Typed Prim is a Prim that has been assigned a type.
- A Prim: (something that exists in the scenegraph)
- A typed Prim: (a Prim with a specific schema/type like Sphere, Cube, Xform, Camera, etc.)
For example:

/
└── Warehouse

might simply be an organizational Prim.

Whereas:

/
└── Warehouse
    └── Camera01 (Camera)

is a Prim that OpenUSD understands as a camera.
You'll probably have something like:

/
└── Museum
    ├── Geometry
    ├── Lighting
    ├── Cameras
    └── Metadata

Some of those Prims are there just to organize the scene.

Others represent specific things with behavior and properties, like cameras or lights.

That's why OpenUSD separates "there is a Prim here" from "this Prim is a Sphere/Camera/Xform/etc."


Think of it this way:

stage.DefinePrim("/hello")
stage.DefinePrim("/world", "Sphere")


is not saying:

Create a Prim called world, then put a Sphere inside it.

It's saying:

Create a Prim called world whose type is Sphere.
So the scenegraph looks like this:

/
├── hello
└── world (type = Sphere)

not

/
├── hello
└── world
    └── Sphere

* Not every Prim represents visible geometry.

Some Prims are used:

to organize the scene (Xform is a common example),
to group other Prims,
to hold metadata,
or simply to act as containers.

### Scope Vs XForm

Scope vs. Xform
Scope is for organization only.
Xform organizes and provides a transform that affects all of its children.

/ (Pseudoroot) Automatically generated
├── Geometry   (scope) The Purpose of a scope is to organize prims
│   ├── Shelves (XForm)
        ├──Shelf1
        ├──Shelf2
│   ├── Robots
        ├──Robot1
        ├──Robot2
├── Cameras
│   ├── Camera1
│   └── Camera2
└── Lights

A Prim has lots of properties besides its name:

Name: world
Type: Sphere
Transform
Visibility
Attributes
RelationshipsA Prim has lots of properties besides its name:

    Name: world

    Type: Sphere

    Transform

    Visibility

    Attributes

    Relationships

    Metadata







### Hierarchy from Prim paths
Hierarchy is created by a Prim's path, not by its type.
Parent-child relationships come from the namespace.
* Prims can be reorganized after they're created by reparenting them under a new parent.

### NameSpace
A namespace is the hierarchical naming system used to organize and locate Prims within a USD stage.

A Prim's namespace is expressed as its namepath, for example:

/Geometry/Shelves/Crate001


#### Scenegraph Editing
Reparenting changes a Prim's namespace path.
Changing a Prim's path is similar to moving a referenced asset in a DAM or InDesign project—anything using the old path must be updated
Reparenting changes a Prim's namespace path.
Changing a Prim's path is similar to moving a referenced asset in a DAM or InDesign project—anything using the old path must be updated




## USD Composition
### Why Composition Matters

This ability to compose a scene from multiple sources is one of OpenUSD's core strengths.

Different files can contribute different pieces of information while OpenUSD presents the result as one composed Stage.



### Composition Mindset:

One of the fundamental ideas of OpenUSD.

Instead of asking:

"Should I make another copy of this asset?"

 ask:

"Can I express this as another layer of opinions?"

This is one of the reasons OpenUSD enables many teams to collaborate on the same assets without constantly duplicating work.

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
