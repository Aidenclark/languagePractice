advanced_hashmap = AdvancedHashMap()
# Add enough keys to trigger a resize
for name in ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"]:
    advanced_hashmap.add(name, f'Data for {name}')

print(advanced_hashmap.map)
print(advanced_hashmap.size)  # Should reflect the increased size after resizing
