places_to_visit = ["Vatican City", "Greece", "Paris", "Japan", "Sweden"]

print("Original List")
print(places_to_visit)

print("\nSorted list without changing list")
print(sorted(places_to_visit))

print("\nOriginal List again")
print(places_to_visit)

print("\nSorted list without changing list")
print(sorted(places_to_visit, reverse=True))

print("\nSorted list without changing list in reverse order")
print(places_to_visit)

places_to_visit.reverse()

print("\nList in Reverse Order but modified")
print(places_to_visit)

places_to_visit.reverse()

print("\nList in Reverse Order again. So back to its original order.")
print(places_to_visit)

places_to_visit.sort()

print("\nList sorted in natural order")
print(places_to_visit)

places_to_visit.sort(reverse=True)

print("\nList sorted in reverse natural order")
print(places_to_visit)