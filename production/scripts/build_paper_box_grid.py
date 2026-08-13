from pxr import Usd, UsdGeom

warehouse_path = "/home/fritz/Documents/physical_ai/production/worlds/paper_warehouse/warehouse.usda"

box_asset_path = "../../3d_assets/warehouse_assets/paper_box_mint/box_paper_mint.usd"

stage = Usd.Stage.Open(warehouse_path)

x_positions = [0.33, 0.11, -0.11, -0.33]
y_positions = [0.32, 0.00, -0.32]

z = 0.617

box_number = 25

for y in y_positions:
    for x in x_positions:

        prim_path = f"/World/PaperBoxes/PaperBox_{box_number:02d}"

        box = UsdGeom.Xform.Define(stage, prim_path)

        box.GetPrim().GetReferences().AddReference(box_asset_path)

        box.AddTranslateOp().Set((x, y, z))

        box_number += 1

stage.Save()

print("Added Boxes 25 through 36.")