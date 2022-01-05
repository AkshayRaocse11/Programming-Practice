import json

REGION_TO_MACHINES_MAP = {
    # (machine_name, capacity, cost_per_hr)
    'New York': [
        ('Large', 10, 120),
        ('XLarge', 20, 230),
        ('2XLarge', 40, 450),
        ('4XLarge', 80, 774),
        ('8XLarge', 160, 1400),
        ('10XLarge', 320, 2820)
    ],
    'India': [
        ('Large', 10, 140),
        # ('XLarge', 20, None),
        ('2XLarge', 40, 413),
        ('4XLarge', 80, 890),
        ('8XLarge', 160, 1300),
        ('10XLarge', 320, 2970)
    ],
    'China': [
        ('Large', 10, 110),
        ('XLarge', 20, 200),
        # ('2XLarge', 40, None),
        ('4XLarge', 80, 670),
        ('8XLarge', 160, 1180),
        # ('10XLarge', 320, None)
    ]
}


class Machine():
    def __init__(self, name, capacity, cost_per_hr=None):
        self.name = name
        self.capacity = capacity
        self.cost_per_hr = cost_per_hr
        self.cost_per_unit = None

        if self.cost_per_hr is not None:
            self.cost_per_unit = self.cost_per_hr / self.capacity


def allocate_machines_regionally(machines, required_capacity):
    # Only allocate machines that have cost_per_hr specified, ignore others
    filtered_machines = []
    for spec_tuple in machines:
        _machine = Machine(*spec_tuple)
        if _machine.cost_per_hr:
            filtered_machines.append(_machine)
    
    # Prioritise machines with least cost_per_unit
    machine_priorities = sorted(
        filtered_machines,
        key=lambda machine: machine.cost_per_unit
    )
    
    # Allocation logic
    allocated_machines = []
    for machine in machine_priorities:
        reqd_no_of_machines = required_capacity // machine.capacity
        if reqd_no_of_machines <= 0:
            continue
        # Subtract maximum counts of machine capacity possible
        required_capacity %= machine.capacity
        allocated_machines.append(
            (machine.name, reqd_no_of_machines, machine.cost_per_hr)
        )
    return allocated_machines


def allocate_machines(required_capacity, total_hrs):
    results = { 'Output': [] }

    for region, machines_in_region in REGION_TO_MACHINES_MAP.items():
        result = {}
        result['region'] = region
        result['machines'] = []
        cost_by_region = 0
        machines_allocated_by_region = allocate_machines_regionally(
            machines_in_region, required_capacity
        )
        for (
            machine_name, reqd_no_of_machines, cost_per_hr
        ) in machines_allocated_by_region:
            result['machines'].append((machine_name, reqd_no_of_machines))
            cost_by_region += (reqd_no_of_machines * cost_per_hr * total_hrs)

        result['total_cost'] = '${}'.format(cost_by_region)
        results['Output'].append(result)

    return results


if __name__ == '__main__':

    required_capacity = int(input("Please Enter a Capacity(integer):"))
    total_hrs = int(input('Please Enter a Hours(integer):'))
    print('Capacity:    {}'.format(required_capacity))
    print('Hours:       {}'.format(total_hrs))

    results = allocate_machines(required_capacity, total_hrs)

    print(json.dumps(results, indent=4))

##################################Sample Inputs#########################################################

#Test case1: Enter total hours: 1
############ Enter total capacity: 1150

#Test case2: Enter total hours: 5
############ Enter total capacity: 230

# Test case3: Enter total hours: 24
############# Enter total capacity: 100

#Test case4: Enter total hours: 12
############ Enter total capacity: 1100