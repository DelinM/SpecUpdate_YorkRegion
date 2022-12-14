Spec_dic = {1: "General Requirements",
            2: "Site Works",
            3: "Concrete",
            4: "Masonry",
            5: "Metals",
            6: "Wood and Plastics",
            7: "Thermal and Moisture Protection",
            8: "Doors and Windows",
            9: "Finishes",
            10: "Specialties",
            11: "Equipment",
            12: "Furnishings",
            13: "SCADA and Instrumentation",
            14: "Conveying Systems",
            15: "Mechanical",
            16: "Electrical"}



"""
spec container: hashmap <String, list>

key: spec number -> String

values:
value 0: Div Number -> integer
value 1: Div Name -> string
value 2: Name (full name of the spec) -> string
value 3: OriginalYorkRegion (if this is an original york region spec) -> boolean
value 4: ETOSpec (if ETO folder has this spec) -> boolean
value 5: should it included in Bid form -> boolean
"""