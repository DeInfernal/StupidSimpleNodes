class SSN_Seed_INT:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff})
                    }
                }

    RETURN_TYPES = ("INT",)
    FUNCTION = "seed"

    CATEGORY = "StupidSimpleNodes"

    def seed(self, seed):
        return (int(seed), )

class SSN_Math_Add_INT:
    @classmethod
    def INPUT_TYPES(cls):
        return {
                    "required": {
                        "var1": ("INT", {"default": 0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff}),
                        "var2": ("INT", {"default": 0, "min": -0xffffffffffffffff, "max": 0xffffffffffffffff})
                    }
                }

    RETURN_TYPES = ("INT",)
    FUNCTION = "add"

    CATEGORY = "StupidSimpleNodes"

    def add(self, var1, var2):
        return (int(var1)+int(var2), )

NODE_CLASS_MAPPINGS = {
    "Stupid Simple Seed (INT)": SSN_Seed_INT,
    "Stupid Simple Addition (INT)": SSN_Math_Add_INT
}    