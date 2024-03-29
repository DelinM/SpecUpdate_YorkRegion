div_dic = {'01': "General Requirements",
           '02': "Site Works",
           '03': "Concrete",
           '04': "Masonry",
           '05': "Metals",
           '06': "Wood and Plastics",
           '07': "Thermal and Moisture Protection",
           '08': "Doors and Windows",
           '09': "Finishes",
           '10': "Specialties",
           '11': "Equipment",
           '12': "Furnishings",
           '13': "SCADA and Instrumentation",
           '14': "Conveying Systems",
           '15': "Mechanical",
           '16': "Electrical"}

yorkspec_dic = {'01000': ['01', 'General Requirements', 'General Requirements', True, False, False],
                '01010': ['01', 'General Requirements', 'Summary of Work', True, False, False],
                '01025': ['01', 'General Requirements', 'Measurement and Payment', True, False, False],
                '01035': ['01', 'General Requirements', 'Amending and Supplementing Contract Documents', True, False,
                          False], '01040': ['01', 'General Requirements', 'Coordination', True, False, False],
                '01060': ['01', 'General Requirements', 'Regulatory Requirements', True, False, False],
                '01080': ['01', 'General Requirements', 'Process Equipment Location Tagging', True, False, False],
                '01080A': ['01', 'General Requirements', 'PELT Labelling Schedule', True, False, False],
                '01092': ['01', 'General Requirements', 'Abbreviations', True, False, False],
                '01200': ['01', 'General Requirements', 'Project Meetings', True, False, False],
                '01200A': ['01', 'General Requirements', 'Pre-Construction Meeting Agenda Template', True, False,
                           False], '01250': ['01', 'General Requirements', 'Substitutions', True, False, False],
                '01300': ['01', 'General Requirements', 'Submittals', True, False, False],
                '01310': ['01', 'General Requirements', 'Construction Schedules', True, False, False],
                '01310A': ['01', 'General Requirements', 'Facility Schedule Template', True, False, False],
                '01310B': ['01', 'General Requirements', 'Linear Schedule Template', True, False, False],
                '01351': ['01', 'General Requirements', 'Health and Safety', True, False, False],
                '01400': ['01', 'General Requirements', 'Quality Control', True, False, False],
                '01420': ['01', 'General Requirements', 'References', True, False, False],
                '01425': ['01', 'General Requirements', 'Computerized Maintenance Management System Data Requirements',
                          True, False, False],
                '01430': ['01', 'General Requirements', 'Operation and Maintenance Data', True, False, False],
                '01450': ['01', 'General Requirements', 'As-Built Drawings', True, False, False],
                '01450A': ['01', 'General Requirements', 'Declaration of Complete and Accurate As-Built Documentation',
                           True, False, False],
                '01501': ['01', 'General Requirements', 'Construction Sequencing', True, False, False],
                '01505': ['01', 'General Requirements', 'Mobilization and Demobilization', True, False, False],
                '01520': ['01', 'General Requirements', 'Field Office', True, False, False],
                '01550': ['01', 'General Requirements', 'Traffic Control', True, False, False],
                '01551': ['01', 'General Requirements', 'Portable Variable Message Signs', True, False, False],
                '01561': ['01', 'General Requirements', 'Environmental Protection', True, False, False],
                '01600': ['01', 'General Requirements', 'Material and Equipment', True, False, False],
                '01640': ['01', 'General Requirements', 'Manufacturers Services', True, False, False],
                '01710': ['01', 'General Requirements', 'Pre-Construction Structural Survey', True, False, False],
                '01720': ['01', 'General Requirements', 'Preparation', True, False, False],
                '01740': ['01', 'General Requirements', 'Cleaning', True, False, False],
                '01741': ['01', 'General Requirements', 'Site Maintenance', True, False, False],
                '01750': ['01', 'General Requirements',
                          'Disinfection and Testing of Water Retaining Structures and Process Piping', True, False,
                          False], '01760': ['01', 'General Requirements', 'Warranty Work', True, False, False],
                '01770': ['01', 'General Requirements', 'Closeout Procedures', True, False, False],
                '01780': ['01', 'General Requirements', 'Contract Closeout', True, False, False],
                '01810': ['01', 'General Requirements', 'Equipment Testing and Facility Commissioning', True, False,
                          False],
                '01810A': ['01', 'General Requirements', 'Equipment Testing and Commissioning Forms', True, False,
                           False],
                '01820': ['01', 'General Requirements', 'Demonstration and Training', True, False, False],
                '01820A': ['01', 'General Requirements', 'Summary of Training Requirements', True, False, False],
                '01820B': ['01', 'General Requirements', 'Training Schedule', True, False, False],
                '01820C': ['01', 'General Requirements', 'OJT Form (On the Job Training Form)', True, False, False],
                '01820D': ['01', 'General Requirements', 'Training Evaluation Form', True, False, False],
                '02230': ['02', 'Site Works', 'Site Preparation For Pipelines Utilities And Associated Structures',
                          True, False, False], '02232': ['02', 'Site Works', 'Tree Pruning', True, False, False],
                '02240': ['02', 'Site Works', 'Dewatering-General', True, False, False],
                '02241': ['02', 'Site Works', 'Provide Water Control Plan Dewatering and Discharge Plan', True, False,
                          False],
                '02242': ['02', 'Site Works', 'Supply Install and Subsequently Remove Dewatering System', True, False,
                          False],
                '02243': ['02', 'Site Works', 'Operate and Maintain Dewatering System', True, False, False],
                '02244': ['02', 'Site Works', 'Retain Specialty Contractor to Monitor Dewatering', True, False, False],
                '02245': ['02', 'Site Works', 'Restoration Works Associated With Dewatering Activities', True, False,
                          False],
                '02246': ['02', 'Site Works', 'Bypass Pumping Or Fluming And Unwatering', True, False, False],
                '02260': ['02', 'Site Works', 'Excavation Support Systems', True, False, False],
                '02261': ['02', 'Site Works', 'Excavation Temporary Support Systems', True, False, False],
                '02300': ['02', 'Site Works', 'Excavating and Backfilling - Structures', True, False, False],
                '02314': ['02', 'Site Works', 'Tunnelling', True, False, False],
                '02315': ['02', 'Site Works', 'Trenching, Backfilling and Compacting', True, False, False],
                '02316': ['02', 'Site Works', 'Rock Removal', True, False, False],
                '02317': ['02', 'Site Works', 'Roadway Excavation Embankment and Compaction', True, False, False],
                '02362': ['02', 'Site Works', 'Dust Control', True, False, False],
                '02389': ['02', 'Site Works', 'Preservation of Water Courses', True, False, False],
                '02511': ['02', 'Site Works', 'Watermains', True, False, False],
                '02511A': ['02', 'Site Works', '- Record of Watermain Installation and Connection', True, False, False],
                '02530': ['02', 'Site Works', 'Sewerage', True, False, False],
                '02531': ['02', 'Site Works', 'Sewage Forcemains', True, False, False],
                '02555': ['02', 'Site Works', 'Cathodic Protection', True, False, False],
                '02631': ['02', 'Site Works', 'Maintenance Holes, Catch Basins, Ditch Inlets and Valve Chambers', True,
                          False, False], '02701': ['02', 'Site Works', 'Aggregates - General', True, False, False],
                '02720': ['02', 'Site Works', 'Untreated Granular Subbase Base Surface And Shoulder', True, False,
                          False], '02725': ['02', 'Site Works', 'Hot Mix Asphalt', True, False, False],
                '02821': ['02', 'Site Works', 'Chain Link Fences and Gates', True, False, False],
                '02822': ['02', 'Site Works', 'Wire Fences and Gates', True, False, False],
                '02911': ['02', 'Site Works', 'Topsoil and Finish Grading', True, False, False],
                '02922': ['02', 'Site Works', 'Hydraulic Seeding', True, False, False],
                '02933': ['02', 'Site Works', 'Sodding', True, False, False],
                '02934': ['02', 'Site Works', 'Compost Seeding', True, False, False],
                '02935': ['02', 'Site Works', 'Planting of Trees Shrubs and Ground Covers', True, False, False],
                '02936': ['02', 'Site Works', 'Landscape Maintenance', True, False, False],
                '02959': ['02', 'Site Works', 'CCTV Inspection of Gravity Sewers', True, False, False],
                '03100': ['03', 'Concrete', 'Concrete Forms and Accessories', True, False, False],
                '03200': ['03', 'Concrete', 'Concrete Reinforcement', True, False, False],
                '03300': ['03', 'Concrete', 'Cast in Place Concrete', True, False, False],
                '03345': ['03', 'Concrete', 'Concrete Curing and Finishing', True, False, False],
                '03410': ['03', 'Concrete', 'Plant Precast Structural Concrete', True, False, False],
                '04051': ['04', 'Masonry', 'Masonry Procedures', True, False, False],
                '04060': ['04', 'Masonry', 'Mortar and Masonry Grout', True, False, False],
                '04080': ['04', 'Masonry', 'Masonry Reinforcement and Connectors', True, False, False],
                '04090': ['04', 'Masonry', 'Masonry Accessories', True, False, False],
                '04211': ['04', 'Masonry', 'Brick Masonry', True, False, False],
                '04220': ['04', 'Masonry', 'Concrete Masonry Units', True, False, False],
                '05050': ['05', 'Metals', 'Welding', True, False, False],
                '05120': ['05', 'Metals', 'Structural Steel', True, False, False],
                '05500': ['05', 'Metals', '_Metal_Fabrications_-_General', True, False, False],
                '05501': ['05', 'Metals', 'Metal Fabrications - Architectural', True, False, False],
                '05502': ['05', 'Metals', 'Metal Fabrications - Structural', True, False, False],
                '05503': ['05', 'Metals', 'Metal Fabrications - Mechanical', True, False, False],
                '05510': ['05', 'Metals', 'Metal Stairs', True, False, False],
                '05512': ['05', 'Metals', 'Aluminum Handrails', True, False, False],
                '05810': ['05', 'Metals', 'Expansion Joint Cover Assemblies', True, False, False],
                '06100': ['06', 'Wood and Plastics', 'Rough Carpentry', True, False, False],
                '06200': ['06', 'Wood and Plastics', 'Finish Carpentry', True, False, False],
                '07140': ['07', 'Thermal and Moisture Protection', 'Hot-Applied Rubberized Asphalt Waterproofing', True,
                          False, False],
                '07160': ['07', 'Thermal and Moisture Protection', 'Capillary Waterproofing', True, False, False],
                '07200': ['07', 'Thermal and Moisture Protection', 'Insulation', True, False, False],
                '07520': ['07', 'Thermal and Moisture Protection', 'Modified Bituminous Membrane Roofing', True, False,
                          False],
                '07570': ['07', 'Thermal and Moisture Protection', 'Traffic Topping', True, False, False],
                '07610': ['07', 'Thermal and Moisture Protection', 'Sheet Metal Roofing', True, False, False],
                '07620': ['07', 'Thermal and Moisture Protection', 'Sheet Metal Flashing', True, False, False],
                '07700': ['07', 'Thermal and Moisture Protection', 'Roof Specialities and Accessories', True, False,
                          False],
                '07840': ['07', 'Thermal and Moisture Protection', 'Firestopping', True, False, False],
                '07900': ['07', 'Thermal and Moisture Protection', 'Joint Sealers', True, False, False],
                '08110': ['08', 'Doors and Windows', 'Steel Doors and Frames', True, False, False],
                '08331': ['08', 'Doors and Windows', 'Overhead Coiling Doors', True, False, False],
                '08410': ['08', 'Doors and Windows', 'Aluminum Doors and Frames', True, False, False],
                '08520': ['08', 'Doors and Windows', 'Windows', True, False, False],
                '08710': ['08', 'Doors and Windows', 'Door Hardware', True, False, False],
                '08800': ['08', 'Doors and Windows', 'Glazing', True, False, False],
                '09250': ['09', 'Finishes', 'Gypsum Board', True, False, False],
                '09300': ['09', 'Finishes', 'Ceramic Tiling', True, False, False],
                '09510': ['09', 'Finishes', 'Acoustical Ceiling', True, False, False],
                '09522': ['09', 'Finishes', 'Acoustical Treatment (Metal)', True, False, False],
                '09650': ['09', 'Finishes', 'Resilient Tile Flooring', True, False, False],
                '09850': ['09', 'Finishes', 'Chemical Resistant Coatings', True, False, False],
                '09900': ['09', 'Finishes', 'Painting And Protective Coatings', True, False, False],
                '09960': ['09', 'Finishes', 'Painting of Steel Tanks and Appurtenances', True, False, False],
                '10200': ['10', 'Specialties', 'Louvres and Vents', True, False, False],
                '10420': ['10', 'Specialties', 'Fire Extinguishers and Safety Blankets', True, False, False],
                '10800': ['10', 'Specialties', 'Toilet Accessories', True, False, False],
                '10999': ['10', 'Specialties', 'Manufactured Specialties', True, False, False],
                '11010': ['11', 'Equipment', 'Equipment General Requirements', True, False, False],
                '11240': ['11', 'Equipment', 'Chemical Metering Pumps', True, False, False],
                '11280': ['11', 'Equipment', 'Fabricated Sluice Gates', True, False, False],
                '11282': ['11', 'Equipment', 'Fabricated Slide Gates and Stop Logs', True, False, False],
                '11300': ['11', 'Equipment', 'Submersible Mixers', True, False, False],
                '11374': ['11', 'Equipment', 'Aeration Centrifugal Blowers', True, False, False],
                '11376': ['11', 'Equipment', 'Rotary Positive Displacement Blowers', True, False, False],
                '11377': ['11', 'Equipment', 'Coarse Bubble Air Diffusers', True, False, False],
                '11378': ['11', 'Equipment', 'Fine Bubble Air Diffusers', True, False, False],
                '11410': ['11', 'Equipment', 'Submersible Well Pumps', True, False, False],
                '11421': ['11', 'Equipment', 'Horizontal Split Case Pumps', True, False, False],
                '11422': ['11', 'Equipment', 'Vertical Turbine Pumps', True, False, False],
                '11441': ['11', 'Equipment', 'Submersible Sewage Pumps', True, False, False],
                '11530': ['11', 'Equipment', 'Chemical Storage Tanks', True, False, False],
                '11540': ['11', 'Equipment', 'Liquid Chemical Feed Systems', True, False, False],
                '11580': ['11', 'Equipment', 'Activated Carbon Odour Control Systems', True, False, False],
                '11590': ['11', 'Equipment', 'Automatic Composite Samplers', True, False, False],
                '11601': ['11', 'Equipment', 'Tank Lining Systems', True, False, False],
                '11700': ['11', 'Equipment', 'Elevated Water Storage Tank', True, False, False],
                '11710': ['11', 'Equipment', 'Fiberglass Reinforced Plastic Tanks', True, False, False],
                '11900': ['11', 'Equipment', 'Aboveground Fuel Oil Storage Tanks', True, False, False],
                '11905': ['11', 'Equipment', 'Fuel Oil System', True, False, False],
                '12345': ['12', 'Furnishings', 'Laboratory Casework and Equipment', True, False, False],
                '13010': ['13', 'SCADA and Instrumentation', 'Process Control General Requirements', True, False,
                          False],
                '13050': ['13', 'SCADA and Instrumentation', 'SCADA Instrumentation and Control Documentation', True,
                          False, False],
                '13105': ['13', 'SCADA and Instrumentation', 'General Instrumentation Requirements', True, False,
                          False],
                '13110': ['13', 'SCADA and Instrumentation', 'Ultrasonic Level Transmitter', True, False, False],
                '13120': ['13', 'SCADA and Instrumentation', 'Magnetic Flow Meters', True, False, False],
                '13130': ['13', 'SCADA and Instrumentation', 'Float Switch', True, False, False],
                '13140': ['13', 'SCADA and Instrumentation', 'Differential Pressure Transmitter', True, False, False],
                '13150': ['13', 'SCADA and Instrumentation', 'Pressure Switch', True, False, False],
                '13160': ['13', 'SCADA and Instrumentation', 'Temperature Transmitter', True, False, False],
                '13170': ['13', 'SCADA and Instrumentation', 'Sludge Blanket Level', True, False, False],
                '13180': ['13', 'SCADA and Instrumentation', 'Turbidity Analyzer', True, False, False],
                '13185': ['13', 'SCADA and Instrumentation', 'pH and ORP Analyzer', True, False, False],
                '13190': ['13', 'SCADA and Instrumentation', 'Gas Detector', True, False, False],
                '13195': ['13', 'SCADA and Instrumentation', 'Chlorine Residual Analyzer', True, False, False],
                '13200': ['13', 'SCADA and Instrumentation', 'Gauge Pressure Transmitter', True, False, False],
                '13210': ['13', 'SCADA and Instrumentation', 'Fluoride Analyzer', True, False, False],
                '13215': ['13', 'SCADA and Instrumentation', 'Chlorine Gas Detectors', True, False, False],
                '13220': ['13', 'SCADA and Instrumentation', 'Dissolved Oxygen Analyzer', True, False, False],
                '13230': ['13', 'SCADA and Instrumentation', 'Thermal Mass Flow Meters', True, False, False],
                '13240': ['13', 'SCADA and Instrumentation', 'Ultrasonic Flow Meter', True, False, False],
                '13250': ['13', 'SCADA and Instrumentation', 'Capacitance Level', True, False, False],
                '13260': ['13', 'SCADA and Instrumentation', 'Bubbler Level Analyzer', True, False, False],
                '13280': ['13', 'SCADA and Instrumentation', 'Weigh Scale', True, False, False],
                '13285': ['13', 'SCADA and Instrumentation', 'Depth and Level Pressure Transmitter', True, False,
                          False], '13290': ['13', 'SCADA and Instrumentation', 'Conductive Level', True, False, False],
                '13295': ['13', 'SCADA and Instrumentation', 'Suspended Solids', True, False, False],
                '13305': ['13', 'SCADA and Instrumentation', 'Field Wiring', True, False, False],
                '13310': ['13', 'SCADA and Instrumentation', 'Panel Specifications', True, False, False],
                '13311': ['13', 'SCADA and Instrumentation', 'Panel - FAT Plan - Template', True, False, False],
                '13390': ['13', 'SCADA and Instrumentation', 'Package Control Systems', True, False, False],
                '13400': ['13', 'SCADA and Instrumentation', 'Programmable Automation Controllers', True, False, False],
                '13510': ['13', 'SCADA and Instrumentation', 'PCS SCADA Local Area Network', True, False, False],
                '13520A': ['13', 'SCADA and Instrumentation', 'SCADA 900MHz Wide Area Radio Network', True, False,
                           False],
                '13520B': ['13', 'SCADA and Instrumentation', 'SCADA 5 8GHz Wide Area Radio Network', True, False,
                           False],
                '13930': ['13', 'SCADA and Instrumentation', 'Instrument and Equipment Testing', True, False, False],
                '28 00 00': ['13', 'SCADA and Instrumentation', 'Security System Specification', True, False, False],
                '14620': ['14', 'Conveying Systems', 'Hoist Monorail and Lifting Davit Systems', True, False, False],
                '14620-01': ['14', 'Conveying Systems',
                             'Hoist Monorail Data Sheet Hoist Monorail and Lifting Davit System', True, False, False],
                '14630': ['14', 'Conveying Systems', 'Overhead Traveling Cranes', True, False, False],
                '14630-01': ['14', 'Conveying Systems', 'Crane Data Sheet 96 Overhead Traveling Cranes', True, False,
                             False],
                '15010': ['15', 'Mechanical', 'Mechanical General Requirements', True, False, False],
                '15075': ['15', 'Mechanical', 'Facilities Piping Identification', True, False, False],
                '15080': ['15', 'Mechanical', 'Process Piping Insulation', True, False, False],
                '15100': ['15', 'Mechanical', 'Plumbing Piping', True, False, False],
                '15100-01': ['15', 'Mechanical', 'Polyvinyl Chloride Drain Waste and Vent', True, False, False],
                '15100-02': ['15', 'Mechanical', 'Cast Iron Soil Pipe (CISP) and Fittings', True, False, False],
                '15100-03': ['15', 'Mechanical', 'Acid-Resistant Cast Iron Pipe and Fittings', True, False, False],
                '15100-05': ['15', 'Mechanical', 'Acid-Resistant Polypropylene Waste and Vent Pipe and Fittings', True,
                             False, False],
                '15100-06': ['15', 'Mechanical', 'Perforated Polyvinyl Chloride (Pvc) Pipe And Fittings', True, False,
                             False],
                '15100-07': ['15', 'Mechanical', 'High-Density Polyethylene (HDPE) Pipe And Fittings-Gas Service', True,
                             False, False],
                '15100-08': ['15', 'Mechanical', 'High Purity Polypropylene (Hp-Pp) Pipe And Fittings', True, False,
                             False],
                '15100-09': ['15', 'Mechanical', 'Carbon Steel Tubing And Fittings', True, False, False],
                '15100-10': ['15', 'Mechanical', 'Galvanized Steel Drain And Vent Pipe And Fittings', True, False,
                             False], '15200': ['15', 'Mechanical', 'Process Piping and Fittings', True, False, False],
                '15200-01': ['15', 'Mechanical', 'Cement-Mortar, Glass And Asphaltic-Lined Ductile Iron', True, False,
                             False],
                '15200-02': ['15', 'Mechanical', 'Carbon Steel Pipe And Fittings-Special Service', True, False, False],
                '15200-03': ['15', 'Mechanical', 'Carbon Steel Pipe And Fittings-General Service', True, False, False],
                '15200-04': ['15', 'Mechanical', 'Welded Steel Pipe And Fittings', True, False, False],
                '15200-05': ['15', 'Mechanical', 'Glass Rubber And PP-Lined Pipe, Carbon Steel Pipe and Fittings', True,
                             False, False],
                '15200-06': ['15', 'Mechanical', 'PVFD-Lined Steel Pipe And Ductile Iron Fittings', True, False, False],
                '15200-07': ['15', 'Mechanical', 'Galvanized Steel Pipe And Malleable Iron Fittings', True, False,
                             False],
                '15200-08': ['15', 'Mechanical', 'Stainless Steel Pipe And Fittings-General Service', True, False,
                             False],
                '15200-09': ['15', 'Mechanical', 'Stainless Steel Pipe And Fittings-Digester Gas Service', True, False,
                             False],
                '15200-10': ['15', 'Mechanical', 'Stainless Steel Pipe And Fittings-Special Service', True, False,
                             False],
                '15200-11': ['15', 'Mechanical', 'Polyvinyl Chloride (PVC) Pipe And Fittings', True, False, False],
                '15200-12': ['15', 'Mechanical', 'Chlorinated Polyvinyl Chloride (CPVC) Pipe And Fittings', True, False,
                             False],
                '15200-13': ['15', 'Mechanical', 'Fiberglass Reinforced Plastic (Frp) Pipe And Fittings', True, False,
                             False],
                '15200-14': ['15', 'Mechanical', 'Copper And Copper Alloy Pipe Tubing And Fittings', True, False,
                             False],
                '15200-15': ['15', 'Mechanical', 'High Density Polyethylene (HDPE) Pipe And Fittings', True, False,
                             False],
                '15200-16': ['15', 'Mechanical', 'Double Wall Containment Piping', True, False, False],
                '15200-17': ['15', 'Mechanical', 'PTFE-Lined Steel Pipe And Fittings', True, False, False],
                '15200-18': ['15', 'Mechanical', 'Alloy 20 Pipe And Fittings', True, False, False],
                '15200-19': ['15', 'Mechanical', 'Polyvinylidene Fluoride (PVDF) Pipe And Fittings', True, False,
                             False], '15201': ['15', 'Mechanical', 'Piping Support Systems', True, False, False],
                '15204': ['15', 'Mechanical', 'Process Piping Specialties', True, False, False],
                '15205': ['15', 'Mechanical', 'Process Valves and Operators', True, False, False],
                '15208': ['15', 'Mechanical', 'Surge Control Systems (Water)', True, False, False],
                '15410': ['15', 'Mechanical', 'Plumbing Fixtures', True, False, False],
                '15440': ['15', 'Mechanical', 'Plumbing Equipment', True, False, False],
                '15500': ['15', 'Mechanical', 'Heat Generation', True, False, False],
                '15500-01': ['15', 'Mechanical', 'Air Handling Unit', True, False, False],
                '15730': ['15', 'Mechanical', 'Unitary Air-Conditioning Equipment =', True, False, False],
                '15730-01': ['15', 'Mechanical', 'Split System DX Indoor Units =', True, False, False],
                '15730-02': ['15', 'Mechanical', 'Ductless Split System DX Indoor Units', True, False, False],
                '15730-03': ['15', 'Mechanical', 'Ductless Split System DX Outdoor Units', True, False, False],
                '15730-04': ['15', 'Mechanical', 'Packaged Indoor Water Source Heat Pump Units', True, False, False],
                '15730-05': ['15', 'Mechanical', 'Packaged Roofing Gas Unit DX AC Units', True, False, False],
                '15730-06': ['15', 'Mechanical', 'Packaged DX Air Conditioning Units', True, False, False],
                '15730-07': ['15', 'Mechanical', 'Room Air Conditioner', True, False, False],
                '15730-08': ['15', 'Mechanical', 'Wall Mount Air Conditioner', True, False, False],
                '15730-09': ['15', 'Mechanical', 'Packaged Terminal Air Conditioner', True, False, False],
                '15760': ['15', 'Mechanical', 'Terminal Heat Transfer Units', True, False, False],
                '15760-01': ['15', 'Mechanical', 'Hot Water Unit Heater', True, False, False],
                '15760-02': ['15', 'Mechanical', 'Finned Tube Radiators', True, False, False],
                '15760-03': ['15', 'Mechanical', 'Cabinet Unit Heater Schedule', True, False, False],
                '15760-04': ['15', 'Mechanical', 'Electric Unit Heater', True, False, False],
                '15810': ['15', 'Mechanical', 'Metal Ductwork and Accessories', True, False, False],
                '15810-01': ['15', 'Mechanical', 'Ductwork Schedule', True, False, False],
                '15810-02': ['15', 'Mechanical', 'Sound Attenuator Schedule', True, False, False],
                '15830': ['15', 'Mechanical', 'Fans', True, False, False],
                '15830-01': ['15', 'Mechanical', 'Fans', True, False, False],
                '15830-02': ['15', 'Mechanical', 'Ceiling Fans', True, False, False],
                '15950': ['15', 'Mechanical', 'HVAC Systems Testing Adjusting and Balancing', True, False, False],
                '15955': ['15', 'Mechanical', 'Piping Leakage Testing', True, False, False],
                '16010': ['16', 'Electrical', 'Electrical General Requirements', True, False, False],
                '16015': ['16', 'Electrical', 'Electrical Systems Analysis', True, False, False],
                '16031': ['16', 'Electrical', 'Inspection and Testing', True, False, False],
                '16032': ['16', 'Electrical', 'Motor Control Centre Testing and Commissioning', True, False, False],
                '16050': ['16', 'Electrical', 'Basic Materials and Methods', True, False, False],
                '16051': ['16', 'Electrical', 'Installation of Cables in Trenches and Ducts', True, False, False],
                '16120': ['16', 'Electrical', 'Wiring Systems', True, False, False],
                '16122': ['16', 'Electrical', 'Wires and Cables 0-1000V', True, False, False],
                '16131': ['16', 'Electrical', 'Splitters Junction Pull Boxes and Cabinets', True, False, False],
                '16132': ['16', 'Electrical', 'Outlet Boxes Conduit Boxes and Fittings', True, False, False],
                '16133': ['16', 'Electrical', 'Conduits Conduit Fastenings and Conduit Fittings', True, False, False],
                '16141': ['16', 'Electrical', 'Wiring Devices', True, False, False],
                '16145': ['16', 'Electrical', 'Modular Wiring System', True, False, False],
                '16221': ['16', 'Electrical', 'Three Phase Induction Motors', True, False, False],
                '16222': ['16', 'Electrical', 'Motors - 1 to 200kW 575V', True, False, False],
                '16223': ['16', 'Electrical', 'Motor Starters Up To 600V', True, False, False],
                '16224': ['16', 'Electrical', 'Variable Frequency Drives Up To 600V', True, False, False],
                '16225': ['16', 'Electrical', 'Motor Control Centres', True, False, False],
                '16226': ['16', 'Electrical', 'Reduced Voltage Soft Starters Up To 600V', True, False, False],
                '16231': ['16', 'Electrical', 'Diesel Electric Generating Units (Liquid Cooled)', True, False, False],
                '16233': ['16', 'Electrical', 'Diesel Electric Generating Units Factory Test Results', True, False,
                          False],
                '16234': ['16', 'Electrical', 'Diesel Electronic Generating Units Information Form', True, False,
                          False],
                '16261': ['16', 'Electrical', 'Medium Voltage Reduced Voltage Soft Starters', True, False, False],
                '16262': ['16', 'Electrical', 'Medium Voltage Variable Frequency Drives', True, False, False],
                '16271': ['16', 'Electrical', 'Dry Type Tranformers up to 600 V Primary', True, False, False],
                '16276': ['16', 'Electrical', 'Pad Mounted Distribution Tranformers', True, False, False],
                '16289': ['16', 'Electrical', 'Transient Voltage Surge Suppression (TVSS)', True, False, False],
                '16402': ['16', 'Electrical', 'Service Entrance Board', True, False, False],
                '16411': ['16', 'Electrical', 'Air Circuit Breakers', True, False, False],
                '16412': ['16', 'Electrical', 'Molded Case Circuit Breakers', True, False, False],
                '16414': ['16', 'Electrical', 'Disconnect Switches - Fused and Unfused', True, False, False],
                '16441': ['16', 'Electrical', 'Panelboard Breaker Type', True, False, False],
                '16450': ['16', 'Electrical', 'Grounding - Secondary', True, False, False],
                '16480': ['16', 'Electrical', 'Grounding', True, False, False],
                '16496': ['16', 'Electrical', 'Automatic Transfer Switches - Low Voltage', True, False, False],
                '16505': ['16', 'Electrical', 'Lighting Equipment', True, False, False],
                '16670': ['16', 'Electrical', 'Lightning Protection System', True, False, False]}
