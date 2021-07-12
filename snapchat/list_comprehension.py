lambda_ds_classes = ["unit1", "unit2", "unit3", "unit4", "cs", "labs"]

core_classes = [c for c in lambda_ds_classes if c[:4] == "unit"]

# Same result as list comprehension above, different code
# core_classes = []
# for c in lambda_ds_classes:
#     if c[:4] == 'unit':
#         core_class.append(c)

core_class_numbers = [
    core_classes[-1]
    for core_classes in [c for c in lambda_ds_classes if c[:4] == "unit"]
]

# Same result as list comprehension above, different code
# core_class_numbers = []
# for c in core_classes:
#     core_class_numbers.append(c[-1])
