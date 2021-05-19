from pprint import pprint
from countapi import (
    create_counter,
    get_info,
    get_value,
    hit_counter,
    update_counter,
    set_value,
    get_stats,
)


ctr = create_counter(
    namespace="py-countapi-example",
    enable_reset=True,
    update_lower_bound=-27,
    update_upper_bound=30,
)

print("The created counter details:")
pprint(vars(ctr))
print()

print("To get started, let's fetch the counter info.")
print("Here's what we've got:")
info = get_info(ctr.key, namespace=ctr.namespace)
pprint(vars(info))
print()

print("Now, let's hit the counter a few times.")
print()

for i in range(7):
    value = hit_counter(ctr.key, namespace=ctr.namespace)
    print(f"After {i+1} hits, the value response is:")
    pprint(vars(value))

print()


print("Now, let's update the counter with a few values.")

for amount in [8, 3, -4, -1, 6, 25]:
    value = update_counter(amount, ctr.key, namespace=ctr.namespace)
    print(f"We added {amount}, the value response is:")
    pprint(vars(value))

print()

print("For sanity, let's hit the get endpoint.")
value = get_value(ctr.key, namespace=ctr.namespace)
pprint(vars(value))
print()

print("Next, let's simply set the counter to a value of 302.")
print("The result:")
result = set_value(302, ctr.key, namespace=ctr.namespace)
pprint(vars(result))
print()

print("Lastly, let us now fetch the information for this counter again.")
print("Here's what we've got:")
info = get_info(ctr.key, namespace=ctr.namespace)
pprint(vars(info))
print()

print("One last thing, if you want some general stats about CountAPI.")
print("Here are the stats we received:")
stats = get_stats()
pprint(vars(stats))
print()

print("That's all, folks!")
print()
