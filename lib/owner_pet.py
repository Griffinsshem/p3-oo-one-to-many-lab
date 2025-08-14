class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner=None):
        # Validate name
        if not isinstance(name, str):
            raise Exception("Pet name must be a string.")
        
        # Validate name
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type: '{pet_type}'. Must be one of {Pet.PET_TYPES}")
        
        # Validate owner if provided
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner or None.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Add pet to the list of all pets
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Owner name must be a string.")
        self.name = name

    def pets(self):
        # Return list of this owner's pets
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        # Check that pet is an instance of Pet
        if not isinstance(pet, Pet):
            raise Exception("Can only add an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        # Return pets sorted by name
        return sorted(self.pets(), key=lambda pet: pet.name)