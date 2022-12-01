class Dataset:
    def __init__(self, labels):
        self.labels = {}
        self.mapping = {}
        for label_id, label in labels.items():
            if type(label) is tuple:
                self.labels[label_id] = (label[0], label[1], label_id) if len(label) > 1 else (label[0], (0, 0, 0))
            else:
                self.labels[label_id] = (label, (0, 0, 0))
            if len(label) > 2:
                for source_id in label[2]:
                    self.mapping[source_id] = label_id
        if len(self.mapping) == 0:
            self.mapping = {label: label for label in labels}

    def get_label_color(self, label_id, bgr=False):
        if bgr:
            return self.labels[label_id][1][::-1] if label_id in self.labels else None
        else:
            return self.labels[label_id][1] if label_id in self.labels else None

    def get_label_ids(self):
        return self.labels.keys()

    def get_label_name(self, label_id):
        return self.labels[label_id][0] if label_id in self.labels else None

    def get_mapped_id(self, source_id):
        return self.mapping[source_id] if source_id in self.mapping else None


DATASETS = dict()

DATASETS['ApronFine'] = Dataset({
    0: ('Airside Safety Vehicle', (125, 56, 44)),
    1: ('Ambulance Vehicle', (246, 240, 81)),
    2: ('Business Jet', (122, 146, 225)),
    3: ('Cargo Airplane', (76, 230, 79)),
    4: ('Cleaning Vehicle', (237, 182, 53)),
    5: ('Common Aircraft', (111, 67, 234)),
    6: ('Container Trolley', (244, 179, 82)),
    7: ('Container Trolley Type A', (169, 126, 215)),
    8: ('Container Trolley Type B', (31, 78, 249)),
    9: ('Container Trolley Type C', (85, 129, 34)),
    10: ('Conveyer Vehicle', (202, 194, 83)),
    11: ('Fire Truck', (68, 19, 164)),
    12: ('Forklift', (168, 72, 72)),
    13: ('Helicopter', (163, 20, 245)),
    14: ('Loading Ramp', (53, 37, 141)),
    15: ('Loading Vehicle', (94, 187, 247)),
    16: ('Other Objects', (120, 213, 83)),
    17: ('Other Vehicles', (234, 52, 134)),
    18: ('Passenger Bus', (82, 10, 214)),
    19: ('Passenger Jet', (218, 171, 114)),
    20: ('Passenger Stairway', (181, 139, 3)),
    21: ('Pedestrian Crossing', (70, 126, 231)),
    22: ('Person Wearing Reflective Vests', (165, 155, 31)),
    23: ('Rescue Helicopter', (28, 102, 155)),
    24: ('Sanitary Truck', (213, 20, 245)),
    25: ('Snowplow', (71, 189, 79)),
    26: ('Speed Limit 30', (117, 96, 235)),
    27: ('Standard Car', (49, 181, 201)),
    28: ('Standard Truck', (153, 56, 89)),
    29: ('Tank Truck', (158, 89, 61)),
    30: ('Taxiing Vehicle', (109, 9, 109)),
    31: ('Tow Vehicle', (216, 100, 121)),
    32: ('Tractor', (113, 186, 229)),
    33: ('Traffic Barrier', (61, 99, 225)),
    34: ('Traffic Cone', (177, 119, 37)),
    35: ('Traffic Cone - Off', (81, 111, 230)),
    36: ('Traffic Cone - On', (35, 175, 70)),
    37: ('Traffic Cone - Standard', (14, 19, 154)),
    38: ('Traffic Sign', (214, 140, 113)),
    39: ('Transport Container', (243, 13, 13)),
    40: ('Transport Vehicle', (76, 184, 101)),
    41: ('Warning Sign', (244, 108, 208)),
    42: ('Person', (161, 140, 67))})

DATASETS['ApronTop'] = Dataset({
    0: ('Airside Safety Vehicle', (125, 56, 44), [0]),
    1: ('Business Jet', (122, 146, 225), [2]),
    2: ('Cargo Airplane', (76, 230, 79), [3]),
    3: ('Common Aircraft', (111, 67, 234), [5]),
    4: ('Container Trolley', (244, 179, 82), [6]),
    5: ('Container Trolley Type A', (169, 126, 215), [7]),
    6: ('Container Trolley Type B', (31, 78, 249), [8]),
    7: ('Fire Truck', (68, 19, 164), [11]),
    8: ('Loading Ramp', (53, 37, 141), [14]),
    9: ('Loading Vehicle', (94, 187, 247), [15]),
    10: ('Other Vehicles', (234, 52, 134), [17]),
    11: ('Passenger Bus', (82, 10, 214), [18]),
    12: ('Passenger Jet', (218, 171, 114), [19]),
    13: ('Passenger Stairway', (181, 139, 3), [20]),
    14: ('Person Wearing Reflective Vests', (165, 155, 31), [22]),
    15: ('Sanitary Truck', (213, 20, 245), [24]),
    16: ('Standard Car', (49, 181, 201), [27]),
    17: ('Conveyor Vehicle', (202, 194, 83), [10]),
    18: ('Tank Truck', (158, 89, 61), [29]),
    19: ('Taxiing Vehicle', (109, 9, 109), [30]),
    20: ('Traffic Cone - Off', (81, 111, 230), [35]),
    21: ('Traffic Cone - On', (35, 175, 70), [36]),
    22: ('Traffic Cone - Standard', (14, 19, 154), [37]),
    23: ('Transport Container', (243, 13, 13), [39]),
    24: ('Transport Vehicle', (76, 184, 101), [40])})

DATASETS['ApronCoarse'] = Dataset({
    0: ('Safety Vehicle', (125, 56, 44), [0]),
    1: ('Business Aircraft', (122, 146, 225), [2]),
    2: ('Cargo Aircraft', (76, 230, 79), [3]),
    3: ('Common Aircraft', (111, 67, 234), [5, 19]),
    4: ('Container Trolley', (244, 179, 82), [6, 7, 8, 9]),
    5: ('Conveyer Vehicle', (202, 194, 83), [10]),
    6: ('Helicopter', (163, 20, 245), [13, 23]),
    7: ('Loading Ramp', (53, 37, 141), [14]),
    8: ('Loading Vehicle', (94, 187, 247), [15]),
    9: ('Other Objects', (120, 213, 83), [16]),
    10: ('Other Vehicles', (234, 52, 134), [1, 4, 11, 12, 17, 24, 25, 28, 31, 32]),
    11: ('Passenger Bus', (82, 10, 214), [18]),
    12: ('Passenger Stairway', (181, 139, 3), [20]),
    13: ('Person', (165, 155, 31), [22, 42]),
    14: ('Standard Car', (49, 181, 201), [27]),
    15: ('Tank Truck', (158, 89, 61), [29]),
    16: ('Taxiing Vehicle', (109, 9, 109), [30]),
    17: ('Traffic Barrier', (61, 99, 225), [33]),
    18: ('Traffic Cone', (177, 119, 37), [34, 37]),
    19: ('Traffic Cone Light', (81, 111, 230), [35, 36]),
    20: ('Traffic Sign', (214, 140, 113), [21, 26, 38, 41]),
    21: ('Transport Container', (243, 13, 13), [39]),
    22: ('Transport Vehicle', (76, 184, 101), [40])})
