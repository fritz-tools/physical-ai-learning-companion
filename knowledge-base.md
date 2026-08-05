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

* The scenegraph should reflect how the object will be used, not just how it was modeled.


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

Prim
│
├── Namespace
├── Type
└── Properties
      ├── Attributes
      └── Relationships

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
Metadata

* mental model:

Prim
├── Namespace
├── Type
└── Properties
      ├── Attributes
      │      size = 100
      │      color = brown
      │      visibility = inherited
      │
      └── Relationships
             (links to other Prims)

### Attributes
An attribute is a named value, with a defined data type, stored on a Prim.

Examples include visibility, display color, extent, radius, size, mass, and transform values. Attributes can also have different values over time, which is how USD supports animation.

### Retrieving Properties of a Prim

OpenUSD documentation states "Properties are the other kind of namespace object"
The important part is simply:

Every Prim can have properties.

And there are only two kinds of properties:

Properties
├── Attributes
└── Relationships

What does it mean that it's "another kind of namespace object"? 
We already know a Prim has a namespace.

For example:

/Geometry/Crates/Crate001

That path exists because the Prim lives in the namespace.

If we imagine the crate has an attribute called size.
That attribute also has a path.

It isn't just called size.

It actually lives under the Prim.

Conceptually, its full path is:

/Geometry/Crates/Crate001.size

And another attribute would be:

/Geometry/Crates/Crate001.color 

* more notes in retrieving properties under # Python for OpenUSD section below 






### Fallback values

Imagine we create a brand-new sphere and never write:

double radius = 10

we just create the sphere.

Then we ask:

sphere.GetRadiusAttr().Get()

We might expect:

"There is no radius."

Instead, USD says:

"The Sphere schema defines a default radius."

So it returns that default value.
The Sphere schema says:

"If nobody specifies a radius, assume this default."

When you ask for an attribute's value, USD figures out the correct answer.
Sometimes that answer comes from:

a value you authored

Sometimes it comes from:

a fallback defined by the schema

there are many places USD can get a value from. "Value resolution" is the process of deciding which one wins.


### Hierarchy from Prim paths
Hierarchy is created by a Prim's path, not by its type.
Parent-child relationships come from the namespace.
* Prims can be reorganized after they're created by reparenting them under a new parent.

### NameSpace
A namespace is the hierarchical naming system used to organize and locate Prims within a USD stage.

A Prim's namespace is expressed as its namepath, for example:

/Geometry/Shelves/Crate001

* To retrieve the properties of a prim read below under
### Scenegraph Editing
Reparenting changes a Prim's namespace path.
Changing a Prim's path is similar to moving a referenced asset in a DAM or InDesign project—anything using the old path must be updated
Reparenting changes a Prim's namespace path.
Changing a Prim's path is similar to moving a referenced asset in a DAM or InDesign project—anything using the old path must be updated


### Relationships

- A relationship is a property that creates a connection between one Prim and one or more other Prims.
- Relationships answer the question: "What is this Prim connected to?"
- Unlike attributes, relationships do not store values. They store target Prim paths.
- Relationships are used to express associations, such as a material bound to a mesh or a camera targeting an object.
- Relationships are properties, just like attributes, and are namespace objects that belong to a Prim.
- Relationships can be queried and modified through the USD API.

## OpenUSD Asset Pipeline

OpenUSD Asset Workflow

1. Source Asset
   • DCC applications
   • Native file formats (.blend, .ma, .hip)

2. Asset Preparation
   • Naming
   • Scale
   • Pivot
   • Materials

3. Asset Publishing
   • Export to USD
   • Validation
   • Published asset

4. Asset Library
   • Organization
   • Canonical assets
   • Versioning (later)

5. Asset Reuse
   • References
   • Instances
   • Assemblies

### Asset Preparation

Purpose: Prepare a 3D model so it becomes a predictable, reliable, reusable OpenUSD asset. Not enough to simply have the model look correct.

- Asset boundary: Decide what the reusable asset is (e.g., one crate, not an entire warehouse).
- Scale: Use correct real-world dimensions. Later physics, robots, collisions, navigation all assume objects have realistic dimensions
- Pivot (origin): Place the local origin appropriately for movement and placement. Pivot determines how an object moves and rotates when placed into a world
- Naming: Use clear, consistent object names.
- Transforms: Apply/clean transforms before publishing.e.g. if the model has a rotation transform it will always be placed rotated. 
- Materials: Assign default materials.
- Hierarchy: Organize the model logically for reuse. Assess whether you need to leave room for growth in your streucture
- Reusability: Ask "Could someone else place this asset into another project without editing it?




### From 3D Model to Reusable OpenUSD Asset

1. Create the source asset

Model the object in a DCC (Digital Content Creation) application such as Blender.

Example:

crate.blend

The native project file (.blend) is the artist's editable working file. It contains Blender-specific information such as modifiers, collections, cameras, lights, and other editing data.

2. Prepare the asset

Before exporting:

Apply the correct scale.
Set the object's origin (pivot).
Organize and name objects clearly.
Assign materials.
Remove unnecessary objects.
Ensure the asset is ready for reuse.

3. Export to USD

Export the asset from Blender as a USD file.

Example:

assets/
    crate/
        crate.usda

The exported crate.usda becomes the reusable OpenUSD asset used by the rest of the pipeline.

4. Validate the exported asset

Open the USD asset in a USD-native application such as:

usdview
Omniverse USD Composer
Isaac Sim

Verify:

hierarchy
transforms
geometry
materials
naming
default prim
overall asset organization

5. Publish the asset

Once validated, crate.usda becomes the canonical crate asset.

Other scenes should reference this file instead of creating new crate geometry.

6. Build worlds using references

Later, a warehouse scene can reference the asset many times:

crate.usda
        │
        ├──► Crate_001
        ├──► Crate_002
        ├──► Crate_003
        └──► ...

Each occurrence has its own position, orientation, and metadata while sharing the same underlying asset.



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

### The main idea behind USD composition

Imagine the example warehouse warehouse.usda. It is not a 3D model in the traditional sense.

It's much closer to an assembly recipe.

It says things like:

Place a shelf here.
Place another shelf over there.
Place a crate on this shelf.
Place another crate here.
Rotate this one.
Translate that one.

Most of the actual geometry lives somewhere else, in the reusable assets.

That's a very different way of thinking than a traditional monolithic 3D scene, and it's one of the reasons OpenUSD scales so well.

### Minimum Reusable Asset

Imagine you might eventually have 1,000 crates spread across many museum warehouses.

Which of these would you make into a reusable asset?

A single crate
A shelf that permanently includes several crates
An entire warehouse
Some combination of the above?

The answer should be based on what needs to be independently manipulated in the future

### Asset Composition

Atomic assets: crate, shelf, wall, floor, pallet, camera mount, etc.
Assemblies: loaded shelf, warehouse aisle, entire warehouse.
Top-level world: the museum warehouse digital twin

### From Canonical Asset to Occurrence 

crate.usda in this example is the reusable asset definition or canonical asset

crate.usda
└── /Crate
    └── Geometry

Crate_001 is a prim inside another stage, such as the warehouse stage.

Warehouse.usda
└── /World
    └── /Warehouse
        └── /Crates
            └── /Crate_001


Crate_001 gets its crate contents by referencing crate.usda.

Step 1: Author crate.usda

A simplified asset file could look like this:

#usda 1.0
(
    defaultPrim = "Crate"
)

def Xform "Crate"
{
    def Cube "Geometry"
    {
        double size = 1
    }
}

This file defines a reusable prim named:

/Crate

It contains the crate's shared information, currently just its geometry.

The defaultPrim = "Crate" line tells OpenUSD:

When another file references this asset without specifying a prim path, use /Crate.

Step 2: Create a prim called Crate_001

Inside Warehouse.usda, we author a new prim:

def Xform "Crate_001"
{
}

At this point, Crate_001 is only an empty Xform. It has a name and a location in the scenegraph, but no crate geometry.

Step 3: Add the reference

We add a reference from Crate_001 to crate.usda:

def Xform "Crate_001" (
    prepend references = @../../assets/crate/crate.usda@
)
{
}

OpenUSD then composes the referenced asset beneath that prim.

Conceptually:

crate.usda
/Crate
└── Geometry

          referenced by

Warehouse.usda
/World/Warehouse/Crates/Crate_001
└── Geometry

The source prim was named /Crate, but it appears in the warehouse under the name and location of the referencing prim:

/World/Warehouse/Crates/Crate_001

That is how we go from the generic asset name Crate to the world-specific identity Crate_001.

#### What is actually stored where?

In crate.usda:

The reusable definition

geometry
dimensions
shared materials
internal prim organization

In Warehouse.usda:

The occurrence in this particular world

name: Crate_001
position
rotation
warehouse location
inventory identity
instance-specific metadataWhat is actually stored where?

In crate.usda:

The reusable definition

geometry
dimensions
shared materials
internal prim organization

In Warehouse.usda:

The occurrence in this particular world

name: Crate_001
position
rotation
warehouse location
inventory identity
instance-specific metadata

## Python for OpenUSD
### Programmatically Building a Stage

Elements can be added to a USD Stage through Python instead of placing everything manually in a GUI.

For a small scene, manually placing objects in a GUI may make sense. But if a scene needs hundreds of repeated or systematically placed elements, such as 400 museum crates, doing that manually would be slow and error-prone.

Python can create the prims, add references to existing USD assets, and set their properties and positions according to rules.

This means Python is useful not because every USD scene needs to be built with code, but because code can automate repetitive or rule-based scene assembly.

* The distinction between generic vs. typed APIs is fundamentally a USD API design concept, but I'm learning it through Python, so I'll put it here.
Why Use Typed APIs?
Use typed APIs when you already know what kind of Prim you are creating.

### Typed APIs 
They provide schema-specific methods and make your code clearer and safer.

- Usd provides generic APIs that work with any Prim.
- UsdGeom provides type-specific APIs for geometry and transforms.
- stage.DefinePrim() returns a generic Usd.Prim.
- UsdGeom.Cube.Define() returns a typed UsdGeom.Cube.

### Attributes & Python

The OpenUSD tutorial page introduces the basic Python pattern:

sphere.GetRadiusAttr().Get()

I'm breaking it down in two parts:

sphere.GetRadiusAttr()

means:
Give me the sphere’s radius attribute object.

Then:

.Get()

means:
Give me the current value stored in that attribute.

Similarly:

sphere.GetRadiusAttr().Set(100.0)

means:
Find the radius attribute and set its value to 100.0.

### From OpenUSD Tutorial: Working With Python

"To work with attributes in OpenUSD, we will generally use schema-specific APIs. Each schema-specific API has a function to grab its own attributes. Review the following examples to learn more."

"While there's also a dedicated UsdAttribute API..."
For example:
prim.GetAttribute("size")
You're saying:

"Find the attribute named size."

This works with any attribute.
Then the tutorial says:

"...it's preferred to use the schema-specific methods..."

This means if you're working with a known schema like Cube, use the methods that Cube provides.

Instead of:

prim.GetAttribute("size")

write:

cube.GetSizeAttr()

The difference is

The first one uses a string:

"size"
The second one uses a dedicated method:

GetSizeAttr()

Why is it more clear?

Imagine you open this code six months from now.

Which tells you more?

prim.GetAttribute("size")

or

cube.GetSizeAttr()

The second one immediately tells you:

this object is a Cube
we're accessing its size attribute


* For Prims, we use /:

/Geometry/Crates/Crate001

For properties, USD uses a dot (.) after the Prim path:

/Geometry/Crates/Crate001.size
/Geometry/Crates/Crate001.color
/Geometry/Crates/Crate001.visibility

### Retrieving Properties of a Prim

If you ask:

prim.GetPropertyNames()

you're asking:

"Tell me the labels on the folders."

Result:

size
color
visibility

You only get the names.

If you ask:

prim.GetProperties()

you're asking:

"Give me the actual folders."

Now you receive the property objects themselves.

Those property objects let you inspect attributes or relationships.

* We interact with attributes through the UsdAttribute API.

sphere_prim.GetRadiusAttr().Get()

We can use the Get() method for the radius, displayColor, and extent attributes.

### Getting Attribute Values
We interact with attributes through the UsdAttribute API.

GetRadiusAttr() will return a UsdAttribute object that can be used to modify the attribute. Which means it will not retrieve the value of the attribute. To get the value of an attribute, use the Get() method.

For example, to get the value of the radius attribute, we would use the following snippet.

sphere_prim.GetRadiusAttr().Get()

* Since we have not explicitly authored any attribute values, Get() will return the fallback value that was defined in the schema.

### Setting Attribute Values

Here is an example of setting a value to the radius attribute.

sphere_prim.GetRadiusAttr().Set(100.0)

When getting attribute values, USD will apply value resolution since we authored a default value. The Get() method will retrieve the value of the attribute. To set the values, we use the Set() method. This will resolve to the authored value rather than the fallback value from the sphere schema.

### Working with Relationships in Python

Get the target paths of a relationship
UsdRelationship.GetTargets()

Set the target paths for a relationship
UsdRelationship.SetTargets()

Add a new target path to a relationship
UsdRelationship.AddTarget()

Remove a target path from a relationship
UsdRelationship.RemoveTarget()

* Relationships are properties that store one or more target paths. You can author a relationship with CreateRelationship, then later retrieve it with GetRelationship and inspect the targets with GetTargets.




## Omniverse

## Isaac Sim


